import streamlit as st
import pandas as pd
import joblib

st.title('ToxiText')
st.write('A hate speech detection NLP powered web app')
st.image('toxic.png',width=300)

pipe_predict=joblib.load('hate_speech.pkl','r')

def predict_emotions(text):
    results=pipe_predict.predict([text])[0]
    if results==1:
        return 'Hate Speech'
    else:
        return 'Not Hate Speech'

def main():
    user_input=st.text_area("Enter the text to be analyzed:")

    if st.button("Predict"):
        if user_input is not None:
            prediction=predict_emotions(user_input)
            if prediction=='Hate Speech':
                st.warning('The text is classified as Hate Speech')
            else:
                st.success('The text is classified as Not Hate Speech')
            
        else:
            st.error("Please enter some text")

if __name__=='__main__':
    main()