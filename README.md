# 🎫 Support Ticket Classification & Priority System

## 🚀 Overview

This project presents an **NLP-powered support ticket classification system** that automatically categorizes customer issues and assigns priority levels (**High / Medium / Low**).

It is designed to help organizations **reduce response time, automate ticket routing, and improve customer support efficiency**.

---

## 🎯 Problem Statement

Customer support teams receive a large volume of tickets daily. Manually classifying and prioritizing them:

* Takes time ⏳
* Is error-prone ❌
* Slows down response for critical issues 🚨

This project solves that by **automating classification and priority assignment using Machine Learning and NLP**.

---

## 🧠 Key Features

* ✔ **Text Preprocessing** (lowercasing, stopword removal, punctuation cleaning)
* ✔ **Ticket Classification** using Machine Learning
* ✔ **Priority Assignment** (rule-based logic)
* ✔ **Model Evaluation** (accuracy, precision, recall, F1-score)
* ✔ **Interactive Web App** using Streamlit

---

## 🛠️ Tech Stack

| Category      | Tools Used                                  |
| ------------- | ------------------------------------------- |
| Language      | Python                                      |
| NLP           | NLTK                                        |
| ML Model      | Scikit-learn (TF-IDF + Logistic Regression) |
| Data Handling | Pandas, NumPy                               |
| Visualization | Matplotlib                                  |
| Deployment UI | Streamlit                                   |

---

## ⚙️ How It Works

1. **Input:** User enters a support ticket
2. **Preprocessing:** Text is cleaned and tokenized
3. **Vectorization:** TF-IDF converts text into numerical features
4. **Prediction:** ML model predicts ticket category
5. **Priority Logic:** Rule-based system assigns priority

---

## 📂 Project Structure

support-ticket-classifier/
│
├── app.py                # Streamlit web app
├── stc.py                # Model training script
├── model.pkl             # Trained ML model
├── vectorizer.pkl        # TF-IDF vectorizer
├── data.csv              # Dataset
├── requirements.txt      # Dependencies
└── README.md             # Project documentation

---

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/support-ticket-classifier.git
cd support-ticket-classifier
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open the browser link provided (usually: http://localhost:8501)

---

## 🧪 Example Usage

**Input Ticket:**

```
My payment failed and money was deducted
```

**Output:**

```
Category: Billing  
Priority: High
```

---

## 📊 Model Performance

* Algorithm: Logistic Regression
* Feature Extraction: TF-IDF
* Accuracy: ~66% *(with small dataset)*

> ⚠️ Accuracy can be significantly improved with a larger dataset and advanced models.

---

## 💡 Future Enhancements

* 🔹 Increase dataset size (1000+ samples)
* 🔹 Use advanced NLP models (BERT, Transformers)
* 🔹 Replace rule-based priority with ML-based prediction
* 🔹 Deploy live on Streamlit Cloud / AWS
* 🔹 Add dashboard for analytics

---

## 🌍 Real-World Applications

* Customer support automation
* Helpdesk systems
* Chatbot integration
* CRM platforms

---

## 👨‍💻 Author

**Manoj Badhan**
BTech in AI & Robotics Engineering

---

## ⭐ Acknowledgment

This project was developed as part of an internship task to demonstrate practical implementation of **NLP and Machine Learning in real-world business scenarios**.
