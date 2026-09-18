🤖 Prompt Engineering — Skill Enhancement Course
<p align="center"> <img src="https://img.shields.io/badge/AI-Prompt%20Engineering-blueviolet?style=for-the-badge" /> <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" /> <img src="https://img.shields.io/badge/LLMs-Generative%20AI-orange?style=for-the-badge" /> <img src="https://img.shields.io/badge/RAG-LangChain-green?style=for-the-badge" /> </p> <p align="center"> <b>A practical journey through Prompt Engineering, LLMs, RAG, Agents, Multimodal AI, and Responsible AI.</b> </p>
📚 About the Course

This repository contains the theory notes, laboratory experiments, implementations, prompts, examples, and evaluation exercises for the Prompt Engineering Skill Enhancement Course.

The course focuses on developing practical skills for interacting with Large Language Models (LLMs), designing effective prompts, building retrieval-augmented applications, creating tool-using agents, experimenting with multimodal AI, and evaluating AI systems for reliability, security, and ethical considerations.

🎯 Course Objectives

By completing this course, students will be able to:

✨ Apply iterative prompting to improve clarity and context.

🎯 Design prompts that effectively steer LLM outputs.

🧩 Use few-shot, role-based, constraint-based, and structured prompting.

🧠 Decompose complex tasks into manageable subtasks.

🔎 Build basic Retrieval-Augmented Generation (RAG) pipelines.

🔗 Develop LLM applications using LangChain and LCEL.

🤖 Build simple tool-using LLM agents.

🖼️ Experiment with multimodal AI and vision-language models.

📊 Evaluate LLM outputs using manual and automated techniques.

🛡️ Understand prompt injection, privacy, bias, misinformation, and AI safety.

🚀 Deploy simple prompt-driven applications using frameworks such as Streamlit or Gradio.

🗂️ Course Structure
Unit	Topic	Major Concepts
I	Foundations of Prompt Engineering	Prompt design, Python, APIs, iteration
II	Advanced Prompt Patterns & Techniques	Few-shot, roles, constraints, refinement
III	Structured Output & Reasoning	JSON, YAML, CoT, task decomposition
IV	RAG & LangChain Workflows	Embeddings, vector stores, LCEL, RAG
V	Agents, Multimodal AI & Ethics	Agents, VLMs, evaluation, security
🧠 Unit I — Foundations of Prompt Engineering
Topics

Definition of Prompt Engineering

Prompt Engineering vs. Model Fine-Tuning

Motivation and benefits

Core principles of effective prompt design

Anatomy of a prompt

Python environment for LLM interaction

Iterative prompting lifecycle

Common prompt failures and remediation

🧪 Lab Experiments
1. Environment & Connectivity

Install required Python packages.

Configure API credentials securely.

Connect to an LLM.

Execute a basic "Hello, World!" prompt.

2. Baseline vs. Enhanced Prompts

Compare:

Write a one-paragraph bio of Ada Lovelace.


with an enhanced prompt containing:

Role/context

Specific instructions

Output requirements

Style constraints

Evaluate both outputs for:

Relevance

Completeness

Style

Instruction following

3. Iterative Prompt Refinement

Summarize Romeo and Juliet through three iterations:

Round 1 → Minimal instruction
Round 2 → Length + style constraints
Round 3 → Setting + theme requirements


Document how each modification changes the generated response.

4. Prompt Failure Diagnosis

Create intentionally problematic prompts involving:

Ambiguity

Missing context

Contradictory instructions

Incorrect output formats

Then refine the prompts and document the improvements.

🎯 Unit II — Advanced Prompt Patterns & Techniques
Topics

Enhanced prompt anatomy

Contextual prompting

Few-shot prompting

Zero-shot prompting

Prompt templates

Role-based prompting

Negative prompting

Constraint specification

Instruction enforcement

Iterative optimization

🧪 Lab Experiments
1. Few-Shot vs. Zero-Shot

Create:

Zero-Shot Prompt
        ↓
LLM
        ↓
Output


and compare it with:

Examples
   ↓
Few-Shot Prompt
   ↓
LLM
   ↓
Output


Possible tasks:

Sentiment classification

Translation

Text classification

Question answering

Evaluate:

Accuracy

Consistency

Example adherence

2. Role-Based & Negative Prompting

Example:

You are a financial education assistant.
Explain the concept in simple language for a beginner.


Experiment with negative constraints such as:

Do not mention brand names.


Observe how role and constraint instructions affect the output.

3. Constraint Specification & Refinement

Start with a basic prompt:

Summarize this technical article.


Then progressively introduce:

• Word-count limit
• Bullet-point format
• Required topics
• Target audience
• Output structure


Compare the outputs after each refinement.

🧩 Unit III — Structured Output & Reasoning Techniques
Topics

Structured LLM outputs

Markdown

Lists and tables

JSON generation

YAML generation

Reasoning-oriented prompting

Task decomposition

Multi-step problem solving

🧪 Lab Experiments
1. Structured Format Prompting

Generate information using:

Bullet lists

Markdown tables

Numbered lists

Structured sections

Example:

List three benefits of daily exercise
in a Markdown table with columns:
Benefit | Description


Validate whether the generated response follows the requested structure.

2. JSON / YAML Generation

Given:

Book 1:
Title: 1984
Author: George Orwell
Year: 1949

Book 2:
Title: The Hobbit
Author: J.R.R. Tolkien
Year: 1937


Generate machine-readable JSON/YAML and validate it using Python parsers.

Example JSON structure:

{
  "books": [
    {
      "title": "1984",
      "author": "George Orwell",
      "year": 1949
    }
  ]
}

3. Reasoning & Task Decomposition

Compare:

Direct Question
      ↓
     LLM
      ↓
    Answer


against:

Complex Problem
      ↓
Sub-problem 1
      ↓
Sub-problem 2
      ↓
Sub-problem 3
      ↓
Combined Answer


Measure differences in accuracy, consistency, and task completion.

Note: When implementing reasoning experiments, evaluate the final answer and observable intermediate artifacts rather than assuming that hidden/internal reasoning is reliably exposed by a model.

🔎 Unit IV — Retrieval-Augmented Generation & LangChain
Topics

Limitations of LLM internal knowledge

External knowledge sources

Retrieval-Augmented Generation

RAG architecture

Document indexing

Text splitting

Embeddings

Vector stores

LangChain

LangChain Expression Language (LCEL)

Retrieval-generation pipelines

🧪 Lab Experiments
1. Basic LCEL Chain

Build a minimal chain:

Input
  ↓
Prompt Template
  ↓
LLM
  ↓
Output Parser
  ↓
Response


Example task:

Summarize the following text:
{input_text}

2. Data Indexing for RAG

Build an indexing pipeline:

Documents
    ↓
Document Loader
    ↓
Text Splitter
    ↓
Chunks
    ↓
Embeddings
    ↓
Vector Store


Experiment with a small document collection and inspect generated chunks and embeddings.

3. Basic RAG Chain

Implement:

                 ┌──────────────┐
                 │  User Query  │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │   Retriever  │
                 └──────┬───────┘
                        ↓
                Relevant Chunks
                        ↓
              ┌──────────────────┐
              │ Context + Query  │
              └────────┬─────────┘
                       ↓
                 ┌──────────────┐
                 │     LLM      │
                 └──────┬───────┘
                        ↓
                     Answer


Compare:

LLM + Prompt


with:

Retriever + Context + Prompt + LLM


and analyze factual accuracy.

🤖 Unit V — Agents, Multimodal AI & Ethical Evaluation
Topics

LLM agents

Tool calling

Agent architecture

Multimodal AI

Vision-Language Models

Text-to-image prompting

Image understanding

Prompt evaluation

LLM-as-a-Judge

Prompt injection

Privacy and security

Bias and misinformation

Responsible AI

Streamlit / Gradio deployment

🧪 Lab Experiments
1. Simple LLM Agent

Create an agent capable of using a tool such as:

def calculator(expression):
    return eval(expression)


The agent should determine when a calculator tool is required and use it to answer numerical questions.

Example architecture:

User Query
     ↓
   Agent
     ↓
 ┌───┴────┐
 ↓        ↓
LLM     Tool
 ↓        ↓
 └───┬────┘
     ↓
 Final Answer

2. Multimodal Prompting

Experiment with:

Text Prompt
     ↓
Image Generation
     ↓
Generated Image
     ↓
Vision Model
     ↓
Image Description


Compare the generated image and its description against the original prompt to evaluate alignment.

3. Prompt Evaluation & Ethics Workshop

Evaluate multiple model outputs using:

Manual Evaluation

Accuracy

Relevance

Clarity

Format compliance

Completeness

Safety

LLM-as-a-Judge

Use a structured evaluation prompt such as:

Evaluate the following response for:
1. Clarity
2. Correctness
3. Relevance
4. Instruction adherence

Return a structured evaluation.

Prompt Injection Testing

Experiment with adversarial instructions such as:

Ignore previous instructions...


Then investigate mitigation techniques including:

Clear instruction hierarchy

Input validation

Separation of trusted and untrusted content

Output validation

Tool permission boundaries

Retrieval-context isolation

🛠️ Technology Stack
Technology	Purpose
🐍 Python	Core programming language
🤗 Transformers	Working with open-source LLMs
🔗 LangChain	LLM application development
🧬 LCEL	Chain composition
🔎 RAG	Retrieval-grounded generation
📐 Embeddings	Semantic representation
🗄️ Vector Stores	Similarity search
🤖 LLM APIs	Model interaction
🎨 Streamlit	Web application deployment
🖥️ Gradio	Interactive AI interfaces
📊 JSON/YAML	Structured data
🧪 Python Parsers	Output validation
📁 Recommended Repository Structure
prompt-engineering/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── unit-01-foundations/
│   ├
