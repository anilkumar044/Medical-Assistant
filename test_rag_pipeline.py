#!/usr/bin/env python3
"""
Medical Assistant RAG Pipeline - Data Preparation Demo
This demonstrates the RAG setup without requiring LLM model downloads
"""

import os
import time
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma

print("=" * 80)
print("MEDICAL ASSISTANT RAG PIPELINE - DATA PREPARATION")
print("=" * 80)
print()

# Configuration
CONFIG = {
    'DATA_PATH': './medical_diagnosis_manual.pdf',
    'EMBEDDING_MODEL': 'all-MiniLM-L6-v2',
    'CHUNK_SIZE': 1000,
    'CHUNK_OVERLAP': 200,
    'RETRIEVAL_K': 5,
    'VECTOR_DB_PATH': './chroma_db',
}

# Medical questions to answer
MEDICAL_QUESTIONS = [
    "What is the protocol for managing sepsis in a critical care unit?",
    "What are the common symptoms of appendicitis, and can it be cured via medicine?",
    "What are the effective treatments for sudden patchy hair loss?",
    "What treatments are recommended for traumatic brain injury?",
    "What are the precautions for a person who has fractured their leg?"
]

print("Configuration:")
print(f"  - PDF: {CONFIG['DATA_PATH']}")
print(f"  - Embedding Model: {CONFIG['EMBEDDING_MODEL']}")
print(f"  - Chunk Size: {CONFIG['CHUNK_SIZE']}")
print(f"  - Chunk Overlap: {CONFIG['CHUNK_OVERLAP']}")
print(f"  - Questions: {len(MEDICAL_QUESTIONS)}")
print()

# Step 1: Load PDF
print("[1/5] Loading PDF document...")
start_time = time.time()

if not os.path.exists(CONFIG['DATA_PATH']):
    print(f"✗ Error: PDF file not found at {CONFIG['DATA_PATH']}")
    print("  Please ensure medical_diagnosis_manual.pdf is in the current directory")
    exit(1)

loader = PyMuPDFLoader(CONFIG['DATA_PATH'])
documents = loader.load()

load_time = time.time() - start_time
print(f"✓ PDF loaded successfully!")
print(f"  - Pages: {len(documents)}")
print(f"  - Load time: {load_time:.2f}s")
print()

# Step 2: Analyze document
print("[2/5] Analyzing document content...")
total_chars = sum(len(doc.page_content) for doc in documents)
avg_chars_per_page = total_chars / len(documents) if documents else 0
print(f"  - Total characters: {total_chars:,}")
print(f"  - Avg chars/page: {avg_chars_per_page:.0f}")
print()

# Step 3: Create text chunks
print("[3/5] Creating text chunks...")
start_time = time.time()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CONFIG['CHUNK_SIZE'],
    chunk_overlap=CONFIG['CHUNK_OVERLAP'],
    length_function=len,
    separators=["\n\n", "\n", " ", ""]
)

chunks = text_splitter.split_documents(documents)
chunk_time = time.time() - start_time

print(f"✓ Chunking complete!")
print(f"  - Total chunks: {len(chunks)}")
print(f"  - Chunk time: {chunk_time:.2f}s")
print(f"  - Avg chunk size: {sum(len(c.page_content) for c in chunks) / len(chunks):.0f} chars")
print()

# Step 4: Load embedding model
print("[4/5] Loading embedding model...")
print(f"  Model: {CONFIG['EMBEDDING_MODEL']}")
start_time = time.time()

embeddings = SentenceTransformerEmbeddings(model_name=CONFIG['EMBEDDING_MODEL'])

# Test embedding
test_embedding = embeddings.embed_query("test")
embed_time = time.time() - start_time

print(f"✓ Embedding model loaded!")
print(f"  - Embedding dimension: {len(test_embedding)}")
print(f"  - Load time: {embed_time:.2f}s")
print()

# Step 5: Create vector database
print("[5/5] Creating vector database...")
print(f"  Processing {len(chunks)} chunks...")
start_time = time.time()

# Use a smaller subset for demo if too many chunks
max_chunks = min(len(chunks), 500)  # Limit for demo
if len(chunks) > max_chunks:
    print(f"  Using first {max_chunks} chunks for demo (out of {len(chunks)} total)")
    chunks_to_process = chunks[:max_chunks]
else:
    chunks_to_process = chunks

vector_db = Chroma.from_documents(
    documents=chunks_to_process,
    embedding=embeddings,
    persist_directory=CONFIG['VECTOR_DB_PATH']
)

db_time = time.time() - start_time
print(f"✓ Vector database created!")
print(f"  - Chunks indexed: {len(chunks_to_process)}")
print(f"  - Database path: {CONFIG['VECTOR_DB_PATH']}")
print(f"  - Creation time: {db_time:.2f}s")
print()

# Step 6: Test retrieval
print("=" * 80)
print("TESTING RETRIEVAL")
print("=" * 80)
print()

retriever = vector_db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": CONFIG['RETRIEVAL_K']}
)

for i, question in enumerate(MEDICAL_QUESTIONS, 1):
    print(f"[Question {i}] {question}")

    start_time = time.time()
    retrieved_docs = retriever.get_relevant_documents(question)
    retrieval_time = time.time() - start_time

    print(f"  ✓ Retrieved {len(retrieved_docs)} relevant chunks in {retrieval_time:.3f}s")

    if retrieved_docs:
        # Show first retrieved chunk snippet
        first_chunk = retrieved_docs[0].page_content[:200].replace('\n', ' ')
        print(f"  Preview: {first_chunk}...")
    print()

print("=" * 80)
print("SUMMARY")
print("=" * 80)
print()
print("✅ RAG Pipeline Data Preparation: COMPLETE")
print()
print("Successfully completed:")
print("  ✓ PDF loading and parsing")
print("  ✓ Text chunking with overlap")
print("  ✓ Embedding model loading")
print("  ✓ Vector database creation")
print("  ✓ Similarity search retrieval")
print()
print("Next steps (requires LLM model):")
print("  - Download and load Mistral-7B or similar model")
print("  - Implement response generation with retrieved context")
print("  - Evaluate groundedness and relevance")
print()
print("Total processing time: {:.2f}s".format(
    load_time + chunk_time + embed_time + db_time
))
print("=" * 80)
