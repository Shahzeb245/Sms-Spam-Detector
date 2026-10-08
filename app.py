import streamlit as st
import pickle
import nltk
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()

    text = nltk.word_tokenize(text)

    y = []

    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📩",
    layout="centered"
)

st.title("📩 SMS Spam Detector")
st.write("Enter an SMS below and our AI model will predict whether it is Spam or Ham.")

st.divider()

message = st.text_area(
    "✍️ Enter your message",
    placeholder="Example: Congratulations! You won a prize...",
    height=120
)

predict_button = st.button("🔍 Check Message", use_container_width=True)

# Load trained model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

if predict_button:
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        transformed_message = transform_text(message)
        vector_input = vectorizer.transform([transformed_message])

        prediction = model.predict(vector_input)[0]
        probability = model.predict_proba(vector_input)[0]

        class_probs = dict(zip(model.classes_, probability))

        spam_probability = class_probs.get(1, 0)
        ham_probability = class_probs.get(0, 0)

        if prediction == 1:
            st.error("🚨 Spam Message")
            st.write(f"Spam confidence: {spam_probability * 100:.2f}%")
        else:
            st.success("✅ Ham Message")
            st.write(f"Ham confidence: {ham_probability * 100:.2f}%")