#!/usr/bin/env python3
"""
Notebook Fixer Script
Applies all fixes from REMEDIATION_PLAN.md to the notebook
"""

import json
import sys
from pathlib import Path

INPUT_FILE = 'Medical_Assistant_RAG_Solution_v3_With_Partial_Execution_Output.ipynb.backup'
OUTPUT_FILE = 'Medical_Assistant_RAG_Solution_v3_FIXED.ipynb'

def load_notebook(filename):
    """Load notebook from file"""
    with open(filename, 'r') as f:
        return json.load(f)

def save_notebook(notebook, filename):
    """Save notebook to file"""
    with open(filename, 'w') as f:
        json.dump(notebook, f, indent=1)

def fix_cell_62(notebook):
    """
    FIX #1, #2, #3: Cell 62
    - Remove duplicate start_time
    - Remove duplicate print
    - Fix separators
    """
    print("Fixing Cell 62...")
    cell = notebook['cells'][62]
    source = ''.join(cell['source'])

    # Fix 1: Remove duplicate start_time (keep only first occurrence)
    lines = source.split('\n')
    if lines[0] == lines[1] == 'start_time = time.time()':
        lines.pop(1)  # Remove second occurrence
        print("  ✓ Removed duplicate start_time")

    # Fix 2: Fix separators
    for i, line in enumerate(lines):
        if 'separators = separators or' in line and '["", "", ". "' in line:
            lines[i] = line.replace('["", "", ". ", " ", ""]', '["\\n\\n", "\\n", ". ", " ", ""]')
            print("  ✓ Fixed separators list")

    # Fix 3: Remove duplicate print statement
    # Find and remove the first occurrence of the print-store-print pattern
    for i in range(len(lines) - 2):
        if (lines[i].strip().startswith("print(f'[chunking] stage completed") and
            lines[i+1].strip().startswith("stage_durations['chunking']") and
            lines[i+2].strip().startswith("print(f'[chunking] stage completed")):
            # Remove first print
            lines.pop(i)
            print("  ✓ Removed duplicate print statement")
            break

    # Update cell source
    cell['source'] = [l + '\n' if i < len(lines) - 1 else l for i, l in enumerate(lines)]
    return notebook

def fix_cell_64_delete(notebook):
    """
    FIX #5: Delete Cell 64 (pip install)
    """
    print("Deleting Cell 64 (pip install)...")
    cell = notebook['cells'][64]
    source = ''.join(cell['source'])

    if '!pip install' in source and 'langchain-huggingface' in source:
        # Replace with comment
        cell['source'] = ['# Note: langchain-huggingface should be installed at the beginning of the notebook\n']
        print("  ✓ Replaced Cell 64 with comment")

    return notebook

def fix_cell_65(notebook):
    """
    FIX #4: Replace Cell 65 with embedding-only code
    """
    print("Fixing Cell 65 (split/replace)...")
    cell = notebook['cells'][65]

    # Replace entire cell with embedding-only code
    new_code = '''# Load embedding model
start_time = time.time()

print("Loading embedding model...")
embedding_model_name = 'sentence-transformers/all-MiniLM-L6-v2'

from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name=embedding_model_name,
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)

print(f"✓ Embedding model loaded: {embedding_model_name}")

# Test embedding
sample_vector = embedding_model.embed_documents([chunks[0].page_content[:1000]])[0]
print(f"✓ Sample embedding dimension: {len(sample_vector)}")

stage_durations['embedding'] = time.time() - start_time
print(f'[embedding] stage completed in {stage_durations["embedding"]:.2f} seconds')
'''

    cell['source'] = new_code.split('\n')
    cell['source'] = [l + '\n' if i < len(cell['source']) - 1 else l
                      for i, l in enumerate(cell['source'])]
    print("  ✓ Replaced Cell 65 with embedding-only code")

    return notebook

def fix_cell_67(notebook):
    """
    FIX #6, #7: Cell 67
    - Remove duplicate start_time
    - Remove duplicate print
    """
    print("Fixing Cell 67...")
    cell = notebook['cells'][67]
    source = ''.join(cell['source'])

    lines = source.split('\n')

    # Fix 1: Remove duplicate start_time
    if lines[0] == lines[1] == 'start_time = time.time()':
        lines.pop(1)
        print("  ✓ Removed duplicate start_time")

    # Fix 2: Remove duplicate print statement
    for i in range(len(lines) - 2):
        if (lines[i].strip().startswith("print(f'[vector_db] stage completed") and
            lines[i+1].strip().startswith("stage_durations['vector_db']") and
            lines[i+2].strip().startswith("print(f'[vector_db] stage completed")):
            lines.pop(i)
            print("  ✓ Removed duplicate print statement")
            break

    cell['source'] = [l + '\n' if i < len(lines) - 1 else l for i, l in enumerate(lines)]
    return notebook

def fix_cell_60_delete(notebook):
    """
    FIX #9: Delete Cell 60 (redundant)
    """
    print("Fixing Cell 60 (mark as redundant)...")
    cell = notebook['cells'][60]

    # Replace with comment instead of deleting (safer)
    cell['source'] = ['# Redundant: page count already shown in Cell 58\n',
                     '# print(f"Total number of pages: {len(documents)}")\n']
    print("  ✓ Commented out Cell 60")

    return notebook

def add_query_code(query_num, query_key):
    """Generate code for a query cell"""
    code = f'''start_time = time.time()

result = generate_rag_response(
    business_queries['{query_key}'],
    retriever,
    k=BEST_CONFIG['retriever_k'],
    max_tokens=BEST_CONFIG['max_tokens'],
    temperature=BEST_CONFIG['temperature']
)

print("=" * 80)
print("ANSWER:")
print(result['answer'])
print("\\nCITATIONS:")
for i, citation in enumerate(result['citations'][:5], 1):
    print(f"  {{i}}. {{citation}}")
print(f"\\nQuery Time: {{time.time() - start_time:.2f}}s")
print("=" * 80)
'''
    return code

def fix_empty_query_cells(notebook):
    """
    FIX #8: Add code to empty cells 84, 86, 88, 90
    """
    print("Fixing empty query cells...")

    # Cell 84: Query 2
    cell_84 = notebook['cells'][84]
    if not ''.join(cell_84['source']).strip():
        cell_84['source'] = add_query_code(2, 'Query 2').split('\n')
        cell_84['source'] = [l + '\n' if i < len(cell_84['source']) - 1 else l
                            for i, l in enumerate(cell_84['source'])]
        print("  ✓ Added code to Cell 84 (Query 2)")

    # Cell 86: Query 3
    cell_86 = notebook['cells'][86]
    if not ''.join(cell_86['source']).strip():
        cell_86['source'] = add_query_code(3, 'Query 3').split('\n')
        cell_86['source'] = [l + '\n' if i < len(cell_86['source']) - 1 else l
                            for i, l in enumerate(cell_86['source'])]
        print("  ✓ Added code to Cell 86 (Query 3)")

    # Cell 88: Query 4
    cell_88 = notebook['cells'][88]
    if not ''.join(cell_88['source']).strip():
        cell_88['source'] = add_query_code(4, 'Query 4').split('\n')
        cell_88['source'] = [l + '\n' if i < len(cell_88['source']) - 1 else l
                            for i, l in enumerate(cell_88['source'])]
        print("  ✓ Added code to Cell 88 (Query 4)")

    # Cell 90: Query 5
    cell_90 = notebook['cells'][90]
    if not ''.join(cell_90['source']).strip():
        cell_90['source'] = add_query_code(5, 'Query 5').split('\n')
        cell_90['source'] = [l + '\n' if i < len(cell_90['source']) - 1 else l
                            for i, l in enumerate(cell_90['source'])]
        print("  ✓ Added code to Cell 90 (Query 5)")

    return notebook

def validate_fixes(notebook):
    """Validate that all fixes were applied"""
    print("\n" + "=" * 80)
    print("VALIDATING FIXES")
    print("=" * 80)

    issues = []

    # Check Cell 62
    cell_62_source = ''.join(notebook['cells'][62]['source'])
    if cell_62_source.count('start_time = time.time()') > 1:
        issues.append("Cell 62: Still has duplicate start_time")
    if '["", "", ". "' in cell_62_source:
        issues.append("Cell 62: Separators not fixed")

    # Check Cell 65
    cell_65_source = ''.join(notebook['cells'][65]['source'])
    if 'PyMuPDFLoader' in cell_65_source:
        issues.append("Cell 65: Still contains PDF loading code")
    if 'HuggingFaceEmbeddings' not in cell_65_source:
        issues.append("Cell 65: Missing embedding code")

    # Check Cell 67
    cell_67_source = ''.join(notebook['cells'][67]['source'])
    if cell_67_source.count('start_time = time.time()') > 1:
        issues.append("Cell 67: Still has duplicate start_time")

    # Check empty cells
    for cell_num, query_name in [(84, 'Query 2'), (86, 'Query 3'),
                                   (88, 'Query 4'), (90, 'Query 5')]:
        cell_source = ''.join(notebook['cells'][cell_num]['source'])
        if not cell_source.strip() or len(cell_source) < 100:
            issues.append(f"Cell {cell_num}: Still empty or too short ({query_name})")
        if 'generate_rag_response' not in cell_source:
            issues.append(f"Cell {cell_num}: Missing generate_rag_response call")

    if issues:
        print("\n❌ VALIDATION FAILED:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print("\n✅ ALL VALIDATIONS PASSED")
        return True

def main():
    print("=" * 80)
    print("NOTEBOOK FIXER - Starting...")
    print("=" * 80)
    print()

    # Load notebook
    print(f"Loading: {INPUT_FILE}")
    notebook = load_notebook(INPUT_FILE)
    print(f"  ✓ Loaded {len(notebook['cells'])} cells")
    print()

    # Apply fixes in order
    print("Applying fixes...")
    print()

    notebook = fix_cell_62(notebook)
    notebook = fix_cell_60_delete(notebook)
    notebook = fix_cell_64_delete(notebook)
    notebook = fix_cell_65(notebook)
    notebook = fix_cell_67(notebook)
    notebook = fix_empty_query_cells(notebook)

    print()

    # Validate
    validation_passed = validate_fixes(notebook)

    if validation_passed:
        # Save
        print()
        print(f"Saving: {OUTPUT_FILE}")
        save_notebook(notebook, OUTPUT_FILE)
        print(f"  ✓ Saved successfully")
        print()
        print("=" * 80)
        print("✅ NOTEBOOK FIXING COMPLETE")
        print("=" * 80)
        print()
        print(f"Fixed notebook: {OUTPUT_FILE}")
        print("Next steps:")
        print("  1. Review the fixed notebook")
        print("  2. Test execution in Google Colab")
        print("  3. Commit and push changes")
        return 0
    else:
        print()
        print("=" * 80)
        print("❌ FIXES NOT SAVED - Validation failed")
        print("=" * 80)
        return 1

if __name__ == '__main__':
    sys.exit(main())
