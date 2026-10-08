📩 SMS Spam Detector

A Machine Learning and NLP based web application that detects whether an SMS message is **Spam** or **Ham (Not Spam)**.

🚀 Live Demo

[Click here to try the SMS Spam Detector](https://sms-spam-detector0.streamlit.app/)

📌 Project Overview

This project uses Natural Language Processing (NLP) and Machine Learning to classify SMS messages as Spam or Ham.

The text is cleaned and transformed using NLP techniques, then converted into numerical features using TF-IDF. A Multinomial Naive Bayes model is used for the final prediction.

✨ Features

- 📩 SMS Spam/Ham classification
- 🧹 Text preprocessing
- 🔤 NLP-based text transformation
- 📊 TF-IDF vectorization
- 🤖 Multinomial Naive Bayes model
- 📈 Prediction confidence percentage
- 🌐 Deployed using Streamlit Community Cloud

🛠️ Technologies Used

- Python
- Pandas
- NLTK
- Scikit-learn
- TF-IDF
- Multinomial Naive Bayes
- Streamlit

## 🔄 Machine Learning Workflow

```text
SMS Message
     ↓
Text Preprocessing
     ↓
Tokenization
     ↓
Stop Words & Punctuation Removal
     ↓
Stemming
     ↓
TF-IDF Vectorization
     ↓
Multinomial Naive Bayes
     ↓
Spam / Ham Prediction
