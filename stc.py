#LOAD DATA AND PREPROCESS
import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
nltk.download('stopwords')

# Load dataset
data = pd.read_csv("data.csv")

# Preprocessing function
def preprocess(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return ' '.join(words)

# Apply preprocessing
data['clean_text'] = data['Ticket'].apply(preprocess)

print(data.head())

#Convert Text → Numbers (TF-IDF)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['clean_text'])
y = data['Category']

#Train Machine Learning Model

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

#Evaluate Model

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

#Add Priority System

def assign_priority(text):
    text = text.lower()

    if any(word in text for word in ["refund", "money deducted", "failed"]):
        return "High"
    elif any(word in text for word in ["error", "issue", "problem"]):
        return "Medium"
    else:
        return "Low"
    
#Final Prediction Function

def predict_ticket(text):
    clean = preprocess(text)
    vector = vectorizer.transform([clean])

    category = model.predict(vector)[0]
    priority = assign_priority(text)

    return category, priority

# Test
print(predict_ticket("My payment failed and money deducted"))

#STREAMLIT UI

import streamlit as st

st.title("Support Ticket Classifier")

text = st.text_area("Enter your issue")

if st.button("Predict"):
    category, priority = predict_ticket(text)
    st.write("Category:", category)
    st.write("Priority:", priority)

#SAVING MODEL

import pickle

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))