# 🔍 LLMRec Replication – Augmenting Recommender Systems with LLMs

This repository contains the academic replication of **LLMRec**, a method combining **graph-based recommender systems** with **Large Language Models (LLMs)** to improve performance on sparse datasets.

> 🧠 **Goal**: Demonstrate the methodological steps of LLMRec, even without full-scale computational resources or paid APIs.

---

## 📚 Project Overview

- **Original paper**: _LLMRec: Large Language Models with Graph Augmentation for Recommendation_ (Wei et al., 2024)
- **Focus**: Enrich a user–item graph using simulated LLM outputs (e.g. GPT-3.5) to improve recommendations
- **Scope**: Methodological replication using simplified data and simulated augmentations
- **Dataset**: MovieLens 100k (small-scale for reproducibility)

---
---

## 🗃️ Script Reference

This section documents all the main scripts used in the project, including their purpose, inputs, outputs, and execution order.

### 📌 `scripts/preprocess.py`
**Purpose:**  
Loads the raw MovieLens 100k dataset and filters ratings ≥ 4.0 to generate implicit feedback.

**Inputs:**  
- `data/movielens_100k/ratings.csv`

**Outputs:**  
- Filtered DataFrame (used internally or saved manually if needed)

**Run order:**  
Run **first** to understand or preview the data structure before augmentation.

---

### 📌 `scripts/simulate_llm_augmentations.py`
**Purpose:**  
Simulates GPT-generated augmentations such as user profiles, new interactions, and item attributes.

**Inputs:**  
- `data/synthetic/fake_profiles.json`  
- `data/synthetic/fake_interactions.csv`

**Outputs:**  
- Augmented records used to expand the user–item graph (e.g., in notebooks)

**Run order:**  
Run **after preprocessing** and before encoding.

---

### 📌 `scripts/encode_features.py`
**Purpose:**  
Encodes textual item descriptions or attributes using basic feature extraction (e.g. TF-IDF).

**Inputs:**  
- Simulated item descriptions (hardcoded or loaded)
- Optionally: generated attributes from LLM simulation

**Outputs:**  
- A matrix of item embeddings (for potential graph input)

**Run order:**  
Run **after augmentation** (if encoded item profiles are needed).

---

### 📌 `scripts/evaluate.py`
**Purpose:**  
Simulates evaluation metrics (Recall@5, NDCG@5) for baseline vs augmented recommendations.

**Inputs:**  
- None (outputs are hardcoded or symbolic)

**Outputs:**  
- Printed results to console

**Run order:**  
Can be run **after graph augmentation** or from `03_simulated_results.ipynb` for visualization.

---
---
## 📓 Jupyter Notebooks

In addition to the core scripts, the following notebooks are provided to explore and demonstrate the workflow:

### 🧪 `01_visualize_dataset.ipynb`
**Purpose:**  
Explores the MovieLens dataset with plots and statistics.

**Inputs:**  
- `ratings.csv`, `movies.csv`

**Outputs:**  
- Visuals of rating distributions and most rated movies

**Order:**  
Can be run **at the beginning** to understand the dataset.

---

### 🧪 `02_augmented_graph_demo.ipynb`
**Purpose:**  
Builds and visualizes a user–item graph from synthetic interactions.

**Inputs:**  
- `fake_interactions.csv`, `fake_profiles.json`

**Outputs:**  
- Graph object, visualization of the node-link structure

**Order:**  
Run **after augmentation simulation** (`simulate_llm_augmentations.py`)

---

### 🧪 `03_simulated_results.ipynb`
**Purpose:**  
Loads pre-filled metrics and generates bar plots comparing baseline and augmented recommendation performance.

**Inputs:**  
- `metrics_baseline.csv`, `metrics_augmented.csv`

**Outputs:**  
- Performance comparison chart (Recall@5, NDCG@5)

**Order:**  
Final step in the workflow; can be run to illustrate improvement.

---
---

## ⚙️ Installation

In your terminal, from the root folder `llmrec-replication/`, run:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
