# 🤖 AI Duplicate Question Detector

# Flow Diagram :

<img width="1024" height="1536" alt="AI duplicate question detection flowchart" src="https://github.com/user-attachments/assets/080ab5c4-d88a-4ef7-b92e-b30b8ea2df48" />



## 📌 Project Overview

This project builds a machine learning system to detect whether two questions are **semantically similar (duplicate)** or **different**. It leverages Natural Language Processing (NLP) techniques and ensemble learning models to improve accuracy and robustness.

---

## 🎯 Objective

* Identify duplicate questions automatically
* Reduce redundancy in Q&A platforms
* Improve search relevance and user experience

---

## 🧠 Approach & Methodology

### 🔹 1. Data Collection

* Dataset: Quora Question Pairs
* Contains labeled pairs:

  * `1` → Duplicate
  * `0` → Not Duplicate

---

### 🔹 2. Data Preprocessing

* Removed missing values
* Converted text to lowercase
* Basic text normalization

---

### 🔹 3. Feature Engineering

We extracted multiple types of features:

#### ✅ Basic Features

* Length of questions
* Word count
* Character count

#### ✅ Common Word Features

* Number of shared words between questions

#### ✅ Fuzzy Matching Features

* `fuzz.ratio`
* `token_sort_ratio`
* `token_set_ratio`

👉 These features capture semantic similarity even when wording differs.

---

### 🔹 4. Text Vectorization

* Used **Bag of Words / TF-IDF**
* Converts text into numerical vectors for model input

---

### 🔹 5. Feature Combination

All features were combined into a single feature matrix:

* Basic features
* Fuzzy features
* Vectorized text features

---

### 🔹 6. Model Training

Two models were trained and compared:

#### 🌲 Random Forest

* Ensemble of decision trees
* Handles mixed feature types effectively

#### ⚡ XGBoost

* Gradient boosting algorithm
* Powerful but sensitive to tuning

---

## 📊 Model Performance

| Model         | Accuracy   |
| ------------- | ---------- |
| Random Forest | **78.95%** |
| XGBoost       | 78.88%     |

👉 Accuracy difference is very small.

---

## 📉 Confusion Matrix Analysis

### 🔹 Random Forest

* False Positives (FP): **576**

### 🔹 XGBoost

* False Positives (FP): **650**

---

## ❗ Why Confusion Matrix Matters

Accuracy alone is not enough.

In this problem:

* False Positive = Predicting duplicate when it is NOT
* This leads to incorrect merging of different questions

👉 This is a critical error in real-world systems.

---

## ✅ Final Model Selection: Random Forest

Although both models have similar accuracy, **Random Forest was selected** based on:

### ✔ Lower False Positives

* RF: 576
* XGB: 650

👉 RF makes fewer critical mistakes.

---

### ✔ Better Real-World Performance

* More reliable predictions
* Safer for production use

---

### ✔ Simpler & More Stable

* Less sensitive to hyperparameters
* Lower risk of overfitting

---

## 🚀 Deployment

* Built an interactive UI using **Streamlit**
* Users can input two questions
* Model predicts:

  * Duplicate ✅
  * Not Duplicate ❌
* Optional confidence score displayed

---

## 🧩 Project Structure

```
├── model.pkl              # Trained ML model
├── helper.py             # Feature engineering functions
├── app.py                # Streamlit app
├── Reduce dataset With Advance Features.ipynb        # Training pipeline
├── README.md             # Project documentation
```

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* FuzzyWuzzy
* Streamlit

---

## 📌 Conclusion

Both Random Forest and XGBoost achieved similar accuracy (~78.9%).
However, Random Forest produced fewer false positives, making it more reliable for duplicate detection tasks.


👉 Therefore, Random Forest was chosen as the final model for deployment.

## 🈸 Application Layout : 

<img width="1537" height="907" alt="image" src="https://github.com/user-attachments/assets/87c8ab55-641e-4b5d-b676-f8fd7b9ba516" />





---
