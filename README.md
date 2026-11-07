# Linguistic Markers of Professional Burnout in Employees' Self-Descriptive Texts

A comparative corpus analysis that evaluates linguistic markers of occupational burnout using statistical methods (Fisher's Exact Test, Dunning's Log-Likelihood) and exposes the limitations of standard dictionary-based AI tools.

## 📊 Project Overview
This project presents an R&D framework analyzing 37 English-language self-descriptive texts written by employees (~7,000 tokens). The goal was to test popular AI-generated hypotheses about burnout using mathematical statistics.

* **Group A (Burnout):** n = 20
* **Group B (Engagement/Satisfaction):** n = 17

## 🔬 Key Scientific Findings
Contrary to popular AI/HR claims, common text features are often misleading, while subtle syntactic and lexical shifts carry statistical significance (p < 0.05).

### ❌ Debunked AI Myths (No Statistical Difference)
* **ALL CAPS / Exclamation Marks:** Burnout is characterized by depressive silence, not loud orthographic indicators.
* **Negative Emojis (🙁/😢):** Extremely rare in actual corporate and professional self-descriptions.
* **First-Person Pronouns ("I", "Me", "My"):** Density remains identical across both healthy and burned-out groups (~93-95‰).

### ✅ Proven Burnout Markers
* **Obligation Modality:** Words like *must, have to, obliged* are heavily elevated in the burnout group (3.9‰ vs 0.4‰).
* **Absolute Negative Constraints:** The use of `can't / cannot` was an absolute differentiator (2.2‰ vs 0‰).
* **Absolutist Words:** Cognitive distortion markers (*always, never, completely*) are 2.5x more frequent in the burnout group (10.4‰ vs 4.1‰).
* **Positive Affect Collapse:** Severe depletion of positive-emotional vocabulary (5.2‰ vs 16.8‰).

## ⚠️ The Irony & Sarcasm Paradox (AI Limitations)
Standard dictionary-based NLP tools fail to recognize context. In manual analysis, highly burned-out individuals frequently utilized heavy irony and scare quotes (e.g., *I am "thrilled" to work 14-hour days*), causing naive AI models to misclassify negative text as highly positive.

## 🛠️ Tech Stack & Methodology
* **Language:** Python 3
* **Libraries:** SciPy (Statistical Analysis)
* **Metrics:** Dunning's Log-Likelihood Ratio, Fisher's Exact Test

## 📄 Official Paper & Dataset
The complete peer-reviewed dataset mapping, methodology, and full PDF are officially published on Zenodo:  
👉 **[DOI: 10.5281/zenodo.24015414](https://doi.org)**
