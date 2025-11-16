# Frequently Asked Questions (FAQ)

## 1. How should one approach the project?

- Before starting the project, please read the problem statement carefully and go through the criteria and descriptions mentioned in the rubric.
- Once you understand the task, download the dataset and import it into a Python notebook to get started with the project.
- Kindly use Google Colab for this project.
- To work on the project, you should start with a quick overview of the data
- Then, you can use the data to build a model.
- It is important to close the analysis with key findings and recommendations to the business.

## 2. I am getting the below error. How do I resolve it?

![colab.PNG](colab.PNG)

Please make sure that Google Colab is set to use the T4 GPU. Without a GPU, you will get CUDA errors. Also, the model might not work optimally even after it is loaded if GPU is not used.

Kindly note that once you run the code in the screenshot above, you will see the following output:

```
Building wheel for llama-cpp-python (pyproject.toml) ... done
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
lida 0.0.10 requires fastapi, which is not installed.
lida 0.0.10 requires kaleido, which is not installed.
lida 0.0.10 requires python-multipart, which is not installed.
lida 0.0.10 requires uvicorn, which is not installed.
llmx 0.0.15a0 requires cohere, which is not installed.
llmx 0.0.15a0 requires openai, which is not installed.
llmx 0.0.15a0 requires tiktoken, which is not installed.
tensorflow-probability 0.22.0 requires typing-extensions<4.6.0, but you have typing-extensions 4.9.0 which is incompatible.
```

As long as the message:

```
Building wheel for llama-cpp-python (pyproject.toml) ... done
```

is displayed, and the required library is installed correctly. The rest of the error messages can be ignored as they will not affect the code execution. Also, kindly restart the session afterwards.

## 3. How to convert the file into HTML for submission?

The notebook can be downloaded to the system in .ipynb format and then converted to an HTML (.html) file using this link.
