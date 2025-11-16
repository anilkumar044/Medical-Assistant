# Medical Assistant - Natural Language Processing with Generative AI

![medical-1.png](medical-1.png)

## Business Context

The healthcare industry is rapidly evolving, and professionals face increasing challenges in managing vast volumes of medical data while delivering accurate and timely diagnoses. Quick access to comprehensive, reliable, and up-to-date medical knowledge is critical for improving patient outcomes and ensuring informed decision-making in a fast-paced environment.

Healthcare professionals often encounter information overload, struggling to sift through extensive research and data to create accurate diagnoses and treatment plans. This challenge is amplified by the need for efficiency, particularly in emergencies, where time-sensitive decisions are vital. Furthermore, access to trusted, current medical information from renowned manuals and research papers is essential for maintaining high standards of care.

To address these challenges, healthcare centers can focus on integrating systems that streamline access to medical knowledge, provide tools to support quick decision-making and enhance efficiency. Leveraging centralized knowledge platforms and ensuring healthcare providers have continuous access to reliable resources can significantly improve patient care and operational effectiveness.

## Objective

As an AI specialist, your task is to develop a RAG-based AI solution using renowned medical manuals to address healthcare challenges. The objective is to understand information overload, apply AI techniques to streamline decision-making, analyze its impact on diagnostics and patient outcomes, evaluate its potential to standardize care practices, and create a functional prototype demonstrating its feasibility and effectiveness.

## Questions to Answer

1. What is the protocol for managing sepsis in a critical care unit?
2. What are the common symptoms of appendicitis, and can it be cured via medicine? If not, what surgical procedure should be followed to treat it?
3. What are the effective treatments or solutions for addressing sudden patchy hair loss, commonly seen as localized bald spots on the scalp, and what could be the possible causes behind it?
4. What treatments are recommended for a person who has sustained a physical injury to brain tissue, resulting in temporary or permanent impairment of brain function?
5. What are the necessary precautions and treatment steps for a person who has fractured their leg during a hiking trip, and what should be considered for their care and recovery?

## Data Dictionary

The Merck Manuals are medical references published by the American pharmaceutical company Merck & Co., that cover a wide range of medical topics, including disorders, tests, diagnoses, and drugs. The manuals have been published since 1899 when Merck & Co. was still a subsidiary of the German company Merck.

The manual is a PDF with over 4,000 pages divided into 23 sections.

## Important Note

Please set the runtime to T4-GPU in Google Colab. Please follow the below instructions to the runtime to T4-GPU:
- Click on "Runtime" in the menu bar
- Select "Change runtime type" from the dropdown menu
- In the "Hardware accelerator" section, choose "GPU"
- You may see multiple GPU options; choose "GPU" if you specifically want a T4 GPU
- After selecting the GPU option, click on the "Save" button

## Submission Guidelines

There are two ways to work on this project:

### i. Full-code way
The full code way is to write the solution code from scratch and only submit a final Python notebook with all the insights and observations.

### ii. Low-code way
The low-code way is to use an existing solution notebook template to build the solution and then submit a business presentation with insights and recommendations.

The primary purpose of providing these two options is to allow learners to opt for the approach that aligns with their learning aspirations and outcomes.

| Submission type | Who should choose | What is the same across the two | What is different between the two | Final submission file | Submission Format |
|----------------|-------------------|--------------------------------|----------------------------------|---------------------|-------------------|
| **Full-code** | Learners who aspire to be in hands-on coding roles in the future focussed on building solution codes from scratch | Perform exploratory data analysis to identify insights and recommendations for the problem | Focus on code writing: 10 - 20% grading on the quality of the final code submitted | Solution Python notebook from the full-code template submitted in .html format | .html |
| **Low-code** | Learners who aspire to be in managerial roles in the future - focus on solution review, interpretation, recommendations, and communicating with business | Perform exploratory data analysis to identify insights and recommendations for the problem | Focus on business presentation: 10 - 20% grading on the quality of the final business presentation submitted | Business presentation in .pdf format with problem definition, insights, and recommendations | .pdf |

### Steps to Complete the Assessment

**Note:** If you submit a presentation, ONLY the presentation will be evaluated. Please make sure that all the sections mentioned in the rubric have been covered in your submission.

#### i. Full-code version
1. Download the full-code version of the learner notebook.
2. Follow the instructions provided in the notebook to complete the project.
3. Write down insights and recommendations for the business problems in the comments.
4. Submit only the solution notebook prepared from the learner notebook [format: .html]

#### ii. Low-code version
1. Download the low-code version of the learner notebook.
2. Follow the instructions provided in the notebook to complete the project.
3. Prepare a business presentation with insights and recommendations for the business problem.
4. Submit only the presentation [format: .pdf]

### Important Submission Rules
- Any assignment found copied/plagiarized with other submissions will not be graded and awarded zero marks.
- Please ensure timely submission as any submission post-deadline will not be accepted for evaluation.
- Submission will not be evaluated if:
  - it is submitted post-deadline, or
  - if more than 1 file is submitted.

## Best Practices for Full-code Submissions

- The final Python notebook should be well-documented, with inline comments explaining the functionality of code and markdown cells containing comments on the observations and insights.
- The notebook should be run from start to finish sequentially before submission.
- It is important to remove all warnings and errors before submission.
- The notebook should be submitted as an HTML file (.html) and NOT as a notebook file (.ipynb).
- Please refer to the FAQ page for common project-related queries.

## Best Practices for Low-code Submissions

- The presentation should be made keeping in mind that the audience will be the Data Science lead of a company.
- The key points in the presentation should be the following:
  - Business Overview of the problem and solution approach
  - Key findings and insights that can drive business decisions
  - Business recommendations
- Focus on explaining the key takeaways in an easy-to-understand manner.
- The inclusion of the potential benefits of implementing the solution will give you the edge.
- Copying and pasting from the notebook is not a good idea, and it is better to avoid showing codes unless they are the focal point of your presentation.
- The presentation should be submitted as a PDF file (.pdf) and NOT as a .pptx file.
- Please refer to the FAQ page for common project-related queries.

## Rubric

| Criteria | Points |
|----------|--------|
| **Question Answering using LLM** <br> - Load the large language model from Hugging Face <br> - Create a function to define the model parameters and generate a response <br> - Apply the response generation function to get answers to the questions provided in the problem statement <br> - Provide comments/observations for the answers received | 8 |
| **Question Answering using LLM with Prompt Engineering** <br> - Apply prompt engineering and LLM parameter tuning (at least 5 combinations) and get answers to the questions provided in the problem statement <br> - Provide comments/observations for the answers received | 11 |
| **Data Preparation for RAG** <br> - Load the data file provided <br> - Split the data using a text splitter with necessary attributes <br> - Load the embedding model <br> - Load the vector database <br> - Define the retriever with appropriate search method and k value | 8 |
| **Question Answering using RAG** <br> - Get answers to the questions provided in the problem statement <br> - Fine-tune the chunking, retriever, and LLM parameters (at least 5 combinations) to check different results <br> - Provide comments/observations for the answers received | 12 |
| **Output Evaluation** <br> - Define the evaluation prompt for groundedness <br> - Define the evaluation prompt for relevance <br> - Evaluate all the responses for the questions provided in the problem statement | 9 |
| **Actionable Insights and Recommendations** <br> - Key takeaways for the business | 4 |
| **Presentation/Notebook - Overall quality** <br> - Structure and flow <br> - Crispness <br> - Visual appeal <br> - Conclusion and Business Recommendations <br><br> OR <br><br> - Structure and flow <br> - Well commented code <br> - Conclusion and Business Recommendations | 8 |

**Total Points: 60**
