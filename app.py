import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Preprocessing function
def preprocess(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return ' '.join(words)

# Priority logic
def assign_priority(text):
    text = text.lower()

    if any(word in text for word in ["refund", "money deducted", "failed"]):
        return "High"
    elif any(word in text for word in ["error", "issue", "problem"]):
        return "Medium"
    else:
        return "Low"

# UI
st.title("🎫 Support Ticket Classifier")

user_input = st.text_area("Enter your issue")

if st.button("Predict"):
    clean = preprocess(user_input)
    vector = vectorizer.transform([clean])

    category = model.predict(vector)[0]
    priority = assign_priority(user_input)

    st.success(f"Category: {category}")
    st.warning(f"Priority: {priority}")