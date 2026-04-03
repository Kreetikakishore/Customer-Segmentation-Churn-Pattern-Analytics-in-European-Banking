# Code Smell Detection: FNN & RNN Training Pipeline
## Based on: "Application of Language Models on Code Analysis" — Francesca Console, Sapienza University of Rome

---

## 📖 Paper Summary

This PhD thesis applies deep learning language models to **code analysis**. Chapter 5 focuses on **Code Smell Detection** — automatically detecting poor design patterns in Java source code using neural networks (FNN and RNN/LSTM/BiRNN).

### Code Smells Covered
**Method-level:** Complex Method, Complex Conditional, Feature Envy, Long Method, Long Parameter List, Switch Statements  
**Class-level:** Data Class, God Class, Multifaceted Abstraction, Refused Bequest, Shotgun Surgery

---

## 📦 Where to Get the Dataset

### Primary Dataset (Used in the Paper)
The paper uses the dataset from **Arcelli Fontana et al.** — publicly available:

1. **Fontana Code Smell Dataset** (original, used in the thesis):
   - URL: https://github.com/opus-research/code-smell-dataset
   - 420 labeled samples per code smell, Java source code
   - Labels: smelly (1) or not smelly (0)
   - Smells: Data Class, Large Class, Feature Envy, Long Method, Long Parameter List, Switch Statements

2. **Expanded version with more smells**:
   - URL: https://github.com/Simone-Lorenzi/code-smells-ml-classification
   - Contains ~4,000,000 samples as mentioned in the paper

3. **Qualitas Corpus** (original software corpus):
   - URL: http://qualitascorpus.com/
   - 74 Java software systems, 52,000 classes, 404,000 methods

### Alternative Datasets
- **MLCQCodeSmellDataset**: https://github.com/Moosssss/MLCQCodeSmellDataset
- **CodeSmellExploration**: https://github.com/xiye17/CodeSmellExploration
- **SmellyML**: https://github.com/LaurentBruneau/SmellyML

### Quick Start Dataset (for this pipeline)
Run `python download_dataset.py` to auto-download and prepare data.

---

## 🗂️ Project Structure

```
code_smell_detection/
├── README.md
├── download_dataset.py        # Dataset download & preparation
├── preprocess.py              # Feature extraction & tokenization
├── models/
│   ├── feedforward.py         # FNN model definition
│   └── rnn_model.py           # RNN/LSTM/BiRNN model definition
├── train.py                   # Main training script (both models)
├── evaluate.py                # Metric analysis: Acc, Precision, Recall, F1
├── hyperparameter_tuning.py   # Grid search / Optuna tuning
├── requirements.txt
└── saved_models/              # Model weights saved here
```

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
python download_dataset.py
python preprocess.py
python train.py --model ffn
python train.py --model rnn
python evaluate.py --model ffn
python evaluate.py --model rnn
python hyperparameter_tuning.py --model ffn
```
