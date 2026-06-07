# Understanding Transformers and Hugging Face

## Overview

This repository contains the implementation and analysis of Transformer models using the Hugging Face Transformers library.

The project covers:

* Transformer Architecture
* Self-Attention Mechanism
* Encoder-Decoder Architecture
* Hugging Face Model Card Analysis
* Text Summarization using AutoClasses
* Language Translation using AutoClasses

This project was completed as part of the curriculum tasks assigned by Innomatics Research Labs.

---

# Repository Structure

```text
transformers-huggingface-blog-assignment/
│
├── README.md
├── summarization.py
├── translation.py
├── requirements.txt
├── screenshots/
│   ├── summarization_output.png
│   └── translation_output.png

```

---

# Transformer Architecture

The Transformer architecture was introduced in the paper:

**Attention Is All You Need (Vaswani et al., 2017)**

Unlike RNNs and LSTMs, Transformers use self-attention mechanisms to process sequences in parallel, resulting in:

* Faster training
* Better long-range dependency handling
* Improved scalability

Main Components:

* Input Embeddings
* Positional Encoding
* Self-Attention
* Multi-Head Attention
* Feed Forward Networks
* Residual Connections
* Layer Normalization
* Encoder
* Decoder

---

# Hugging Face Model Card Analysis

## Model Selected

facebook/bart-large-cnn

### Architecture

BART (Bidirectional and Auto-Regressive Transformer)

### Intended Use Cases

* Text Summarization
* News Summarization
* Document Summarization

### Training Dataset

CNN/DailyMail

### Evaluation Metrics

* ROUGE-1
* ROUGE-2
* ROUGE-L

### Limitations

* May hallucinate information
* Depends on input quality

### License

MIT License

---

# Task 1: Text Summarization

## Model Used

facebook/bart-large-cnn

## Sample Input

```text
Transformers have revolutionized NLP by introducing self-attention mechanisms and eliminating recurrence.
```

## Sample Output

```text
Transformers revolutionized NLP using self-attention mechanisms.
```

---

# Task 2: Language Translation

## Model Used

Helsinki-NLP/opus-mt-en-fr

## Sample Input

```text
Machine learning is transforming industries.
```

## Sample Output

```text
L'apprentissage automatique transforme les industries.
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/transformers-huggingface-blog-assignment.git
```

Navigate to project folder:

```bash
cd transformers-huggingface-blog-assignment
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Code

## Summarization

```bash
python summarization.py
```

## Translation

```bash
python translation.py
```

---

# Results and Observations

## Summarization

Strengths:

* Produces concise summaries
* Retains key information
* Fast inference

Limitations:

* Can omit details
* May generate hallucinations

---

## Translation

Strengths:

* Accurate translations
* Preserves context
* Supports multiple languages

Limitations:

* Struggles with idiomatic expressions
* Domain-specific terminology can be challenging

---

# LinkedIn Blog

LinkedIn Article Link:

```text
https://www.linkedin.com/posts/mrutyunjaya3806debata_artificialintelligence-machinelearning-deeplearning-ugcPost-7468779069623492609-p2Ji/?utm_source=share&utm_medium=member_desktop&rcm=ACoAADjkUzAB8nBBvsHkPHtnR3d9jX7z3Mi-xXc
```

---

# References

1. Vaswani et al. (2017) – Attention Is All You Need
2. Hugging Face Documentation
3. BART Model Card
4. Helsinki-NLP Translation Model Card

---

# Author

Mrutyunjaya Debata

## Assignment

This work was completed as part of the curriculum tasks assigned by Innomatics Research Labs.
