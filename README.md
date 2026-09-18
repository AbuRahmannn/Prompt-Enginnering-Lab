```markdown
# Prompt Engineering Lab (Skill Enhancement Course)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-LCEL-brightgreen.svg)](https://www.langchain.com/)
[![Curriculum](https://img.shields.io/badge/JNTUK-R23%20B.Tech%20IT-orange.svg)](https://jntuk.edu.in)

A structured implementation of the **Prompt Engineering (SEC)** syllabus for JNTUK R23 B.Tech IT IV Year. This repository contains end-to-end Jupyter notebooks, clean modular scripts, sample datasets, and benchmark prompts covering iterative refinement, structured generation, RAG, tool-augmented agents, and red-teaming.

---

## Course Scheme & Credits

| Category | L | T | P | Credits |
|---|---|---|---|---|
| **Skill Enhancement Course (SEC)** | 0 | 1 | 2 | **2** |

### Course Objectives
- Apply iterative prompting techniques for precision, context-grounding, and clarity.
- Steer foundation model outputs using zero-shot, few-shot, and role-based patterns.
- Force structured machine-readable formats (JSON, YAML, Markdown) and trigger chain-of-thought (CoT) reasoning.
- Construct Retrieval-Augmented Generation (RAG) pipelines using LangChain Expression Language (LCEL) and vector embeddings.
- Implement tool-using autonomous agents, test multimodal flows, and evaluate outputs using LLM-as-a-Judge and prompt injection tests.

---

## Repository Structure

```text
.
├── unit-1-foundations/
│   ├── exp1_env_connectivity.py
│   ├── exp2_baseline_vs_enhanced.ipynb
│   ├── exp3_iterative_refinement.ipynb
│   └── exp4_diagnosing_failures.ipynb
├── unit-2-advanced-patterns/
│   ├── exp1_few_shot_vs_zero_shot.ipynb
│   ├── exp2_role_and_negative_prompting.ipynb
│   └── exp3_constraint_enforcement.ipynb
├── unit-3-structured-outputs/
│   ├── exp1_markdown_tables.ipynb
│   ├── exp2_json_yaml_validation.py
│   └── exp3_cot_task_decomposition.ipynb
├── unit-4-rag-langchain/
│   ├── data/
│   │   └── sample_kb.txt
│   ├── exp1_simple_lcel_chain.py
│   ├── exp2_indexing_pipeline.py
│   └── exp3_rag_pipeline_runner.py
├── unit-5-agents-multimodal-eval/
│   ├── exp1_calculator_agent.py
│   ├── exp2_multimodal_vision.py
│   └── exp3_eval_and_redteaming.ipynb
├── requirements.txt
├── .env.example
└── README.md

```

---

## Syllabus & Lab Experiments

### Unit I: Foundations of Prompt Engineering

* **Theory:** Anatomy of a prompt, Prompting vs. Fine-tuning, Iterative prompting lifecycle, Common failure modes.
* **Labs:**
* `exp1_env_connectivity.py`: Secure API setup and basic inference validation.
* `exp2_baseline_vs_enhanced.ipynb`: Baseline naive bio vs. context/role-enhanced bio of Ada Lovelace.
* `exp3_iterative_refinement.ipynb`: Three-stage refinement cycle (Romeo & Juliet 2-sentence summary).
* `exp4_diagnosing_failures.ipynb`: Debugging ambiguous/contradictory prompts and edge-case fixing.



### Unit II: Advanced Prompt Patterns & Techniques

* **Theory:** Exemplar curation, Persona framing, Output constraints, Negative suppression tokens.
* **Labs:**
* `exp1_few_shot_vs_zero_shot.ipynb`: Comparing zero-shot vs. 3-shot exemplar prompts on sentiment/translation.
* `exp2_role_and_negative_prompting.ipynb`: Financial advisor persona with negative brand constraints.
* `exp3_constraint_enforcement.ipynb`: Multi-cycle length, formatting, and density constraints on technical text.



### Unit III: Structured Output & Reasoning Techniques

* **Theory:** Machine-parseable schemas, CoT reasoning mechanisms, Task decomposition.
* **Labs:**
* `exp1_markdown_tables.ipynb`: Generating consistent Markdown tables and itemized lists.
* `exp2_json_yaml_validation.py`: Pydantic/JSON schema validation on structured LLM outputs.
* `exp3_cot_task_decomposition.ipynb`: Zero-shot "Let's think step by step" vs. explicit modular sub-questions.



### Unit IV: Retrieval-Augmented Generation (RAG) & LangChain

* **Theory:** Context limits, Vector indexing, Embeddings, Top-k similarity, LCEL architecture.
* **Labs:**
* `exp1_simple_lcel_chain.py`: Minimal LCEL pipeline (`PromptTemplate | ChatModel | StrOutputParser`).
* `exp2_indexing_pipeline.py`: Document loading, RecursiveCharacter splitting, and vector ingestion (Chroma/FAISS).
* `exp3_rag_pipeline_runner.py`: Top-k contextual injection vs. baseline hallucination benchmarking.



### Unit V: Agents, Multimodal AI & Ethical Evaluation

* **Theory:** Tool calling, ReAct pattern, Vision-Language Models (VLMs), Red-teaming, LLM-as-a-Judge.
* **Labs:**
* `exp1_calculator_agent.py`: LangChain tool-augmented agent invoking programmatic math functions.
* `exp2_multimodal_vision.py`: Image generation prompt -> VLM reverse-captioning alignment check.
* `exp3_eval_and_redteaming.ipynb`: Heuristic evaluation rubric, LLM-as-a-Judge scoring, and prompt injection defense.



---

## Quickstart Setup

### 1. Clone & Create Environment

```bash
git clone [https://github.com/](https://github.com/)<your-username>/prompt-engineering-lab.git
cd prompt-engineering-lab

python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

```

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

### 3. Configure API Credentials

Copy the `.env.example` file to `.env` and supply your API key:

```bash
cp .env.example .env

```

Edit `.env`:

```env
OPENAI_API_KEY=your_actual_api_key_here
# Optional (if using alternative providers):
# ANTHROPIC_API_KEY=your_key_here
# GOOGLE_API_KEY=your_key_here

```

---

## Sample Code Reference

### LCEL RAG Implementation (`unit-4-rag-langchain/exp3_rag_pipeline_runner.py`)

```python
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# 1. Initialize retriever & model
vectorstore = FAISS.load_local("local_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 2. Define prompt template
template = """Answer the question based only on the following context:
{context}

Question: {question}
Answer:"""
prompt = ChatPromptTemplate.from_template(template)

# 3. Build LCEL chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 4. Execute query
response = rag_chain.invoke("What are the core benefits of iterative prompt refinement?")
print(response)

```

---

## Suggested `requirements.txt`

```text
openai>=1.40.0
langchain>=0.2.14
langchain-community>=0.2.12
langchain-openai>=0.1.22
chromadb>=0.5.5
faiss-cpu>=1.8.0
tiktoken>=0.7.0
pydantic>=2.8.2
python-dotenv>=1.0.1
jupyter>=1.0.0
ipywidgets>=8.1.3
streamlit>=1.37.1

```

```

<FollowUp label="Want starter code for any of the 15 lab experiment files?" query="Provide the Python starter code and prompts for the lab experiments in Unit 1 and Unit 2."/>

```
