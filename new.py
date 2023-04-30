import streamlit as st
from item import bbc as bb
st.header('NB Text Classifier')
text = st.text_area('Enter your text:')
if st.button("Predict"):
    vec = bb.vector.transform([text]).toarray()
    st.write('Label:',str(list(bb.naivebayes.predict(vec))[0]).replace('0', 'TECH').replace('1', 'BUSINESS').replace('2', 'SPORTS').replace('3','ENTERTAINMENT').replace('4','POLITICS'))
    