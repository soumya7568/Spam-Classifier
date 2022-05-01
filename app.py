import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def transform_text(text):
    text.lower()
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
    ps = PorterStemmer()
    for i in text:
        y.append(ps.stem(i))
    return ' '.join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))


st.title("SPAM MESSAGE CLASSIFIEr")

input_msg = st.text_area("Enter a message...")

if st.button("predict"):

    #preprocess sms
    transformed_text = transform_text(input_msg)
    #vectorizer
    vector_input = tfidf.transform([transformed_text])
    #predict 
    result = model.predict(vector_input)[0]
    #Display
    if result==1:
        st.header('SPAM')
    else:
        st.header('NOT SPAM :)')

