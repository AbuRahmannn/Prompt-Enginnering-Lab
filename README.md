```markdown
<div align="center">

# 🧠 Applied Prompt Engineering & LLM Systems

### *From Heuristic Prompt Design to Production-Grade Autonomous Chains*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-LCEL-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![VectorDB](https://img.shields.io/badge/FAISS%20%2F%20Chroma-Vector_Store-FF6F00?style=for-the-badge)](https://github.com/facebookresearch/faiss)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<p align="center">
  <b>A comprehensive laboratory portfolio implementing zero-shot optimization, structured schemas, RAG knowledge grounding, tool-using agents, and automated LLM evaluation.</b>
</p>

---

</div>

## 📌 Executive Summary

Modern AI engineering requires shifting from **conversational guessing** to **deterministic system design**. This repository houses production-grade experiments, pipelines, and evaluation harnesses designed to control, ground, and scale Large Language Model (LLM) applications.

Instead of treating models as black boxes, this portfolio treats them as programmable reasoning runtimes.


```

```
   [Raw User Query] 
          │
          ▼

```

┌─────────────────────┐
│ Prompt Conditioning │ ◄── Few-Shot Exemplars & Constraints
└──────────┬──────────┘
│
▼
┌─────────────────────┐
│ Dynamic Retrieval   │ ◄── Vector Embeddings (RAG)
└──────────┬──────────┘
│
▼
┌─────────────────────┐
│  Execution & Tools  │ ◄── ReAct Loop / Calculator / APIs
└──────────┬──────────┘
│
▼
┌─────────────────────┐
│ Schema Validation   │ ◄── Strict JSON / Pydantic Enforcement
└──────────┬──────────┘
│
▼
[Reliable Output]

```

---

## 🎯 What You Master

### 🧩 1. Precision Prompt Anatomy & Steering
- **Contextual In-Context Learning (ICL):** Move beyond naive zero-shot tasks by utilizing curated few-shot exemplars that enforce deterministic behavior.
- **Negative Token Suppression:** Program strict boundaries (e.g., negative prompting, regulatory constraints, brand-omission filters) to silence hallucinations.
- **System Role Personas:** Exploit latent model spaces by conditioning system instructions with targeted professional roles and style guidelines.

### 📐 2. Deterministic & Structured Schema Parsing
- **Zero-Breakage JSON/YAML Extraction:** Guarantee downstream machine-readability using constrained prompting and Pydantic validation.
- **Structured Markdown Formats:** Force dynamic tabular outputs, nested key-value pairs, and syntax-compliant matrices directly from unstructured text.

### 🧠 3. Advanced Reasoning & Decomposition
- **Chain-of-Thought (CoT):** Elicit hidden reasoning traces using zero-shot ("*Let's think step by step*") and manual few-shot decomposition to solve mathematical and logical paradoxes.
- **Task Decoupling:** Break compound enterprise tasks into asynchronous, single-responsibility sub-prompts to maximize output accuracy.

### ⚡ 4. Retrieval-Augmented Generation (RAG)
- **Knowledge Grounding:** Eliminate model hallucination and token-cutoff issues by interfacing external vector memory directly into the context window.
- **Modern LCEL Pipelines:** Build modular retrieval-generation architectures using LangChain Expression Language (`RunnablePassthrough | Prompt | LLM | Parser`).
- **Vector Ingestion & Chunking:** Design balanced chunking strategies (Recursive Token Splitters) matched with dense embedding indexes (FAISS / ChromaDB).

### 🤖 5. Tool-Augmented Agents & Multimodal AI
- **ReAct & Tool Calling:** Grant models programmatic agency by binding native Python functions (calculators, web extractors, APIs) to autonomous decision loops.
- **Multimodal Visual Alignment:** Round-trip textual image generation with Vision-Language Models (VLMs) to benchmark visual-semantic preservation.

### 🛡️ 6. Red-Teaming, Safety & LLM-as-a-Judge
- **Adversarial Hardening:** Stress-test system prompts against jailbreaks, direct prompt injections ("*Ignore previous instructions*"), and delimiter collision attacks.
- **Automated Meta-Evaluation:** Replace subjective human testing with automated **LLM-as-a-Judge** scoring matrices using standardized rubrics for accuracy, relevance, and compliance.

---

## 🛠️ Repository Architecture

```text
├── 01-prompt-foundations/
│   ├── baseline_vs_enhanced.ipynb        # Naive vs. Context-Engineered Prompts
│   ├── iterative_refinement.ipynb        # 3-Stage Parameter Optimization Loop
│   └── failure_diagnostics.ipynb         # Ambiguity & Edge-Case Remediation
│
├── 02-advanced-patterns/
│   ├── few_shot_benchmarks.ipynb         # N-Shot In-Context Classification
│   ├── role_and_negative_steering.ipynb  # Persona & Negative Token Filters
│   └── constraint_enforcement.ipynb      # Token Density & Format Enforcement
│
├── 03-structured-reasoning/
│   ├── schema_validation.py              # Pydantic-Validated JSON/YAML Extractor
│   ├── markdown_matrix_gen.ipynb         # Tabular Synthesis Engines
│   └── chain_of_thought_logic.ipynb      # Step-by-Step Task Decomposition
│
├── 04-rag-pipelines/
│   ├── document_indexer.py               # Chunking & FAISS Vector Ingestion
│   ├── lcel_rag_chain.py                 # End-to-End Grounded Retrieval Pipeline
│   └── data/                             # Knowledge Base Documents
│
└── 05-agents-eval-redteam/
    ├── calculator_agent.py               # Function-Calling Autonomous Agent
    ├── multimodal_vlm_eval.py            # Cross-Modal Alignment Verification
    └── red_team_judge.ipynb              # Injection Attacks & Evaluation Rubrics

```

---

## 💻 Code Showcase

### Grounded Retrieval Pipeline (LCEL)

```python
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# 1. Connect Vector Store
vectorstore = FAISS.load_local("indexes/kb_store", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 2. Build Grounded Prompt Template
prompt = ChatPromptTemplate.from_template("""
Context Information:
{context}

Based strictly on the context above, answer the question. If unknown, say "I don't know".
Question: {question}
Answer:
""")

# 3. Assemble LCEL Execution Graph
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | ChatOpenAI(model="gpt-4o-mini", temperature=0)
    | StrOutputParser()
)

# 4. Run Grounded Inference
response = rag_chain.invoke("What are the primary failure modes of zero-shot prompts?")
print(response)

```

---

## 🚀 Quickstart Guide

### 1. Clone & Prepare Environment

```bash
git clone [https://github.com/](https://github.com/)<your-username>/applied-prompt-engineering.git
cd applied-prompt-engineering

# Create virtual environment
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

```

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

### 3. Environment Configuration

Create a `.env` file in the root directory:

```bash
cp .env.example .env

```

Supply your API keys inside `.env`:

```env
OPENAI_API_KEY="your-openai-api-key"
# Optional:
# ANTHROPIC_API_KEY="your-anthropic-key"
# TAVILY_API_KEY="your-search-api-key"

```

---

## 📦 Dependencies

```text
openai>=1.40.0
langchain>=0.2.14
langchain-community>=0.2.12
langchain-openai>=0.1.22
faiss-cpu>=1.8.0
chromadb>=0.5.5
pydantic>=2.8.2
python-dotenv>=1.0.1
jupyterlab>=4.2.0
tiktoken>=0.7.0

```

---
