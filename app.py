import streamlit as st
import requests


def send_request(text, length):
    api_url = 'https://master-marketing-slogan-generator-backend-vanshika2703.endpoint.ainize.ai/predict'
    files = {
        'base_text': (None, text),
        'length': (None, length),
    }
    response = requests.post(api_url, files=files)
    status_code = response.status_code

    return status_code, response


st.title("Market Slogan Generator")
st.header("Generate market slogans given a product and description using GPT-2 model")

#length_slider = st.sidebar.slider("Length", 0, 50)

product = st.text_input("Product")
description = st.text_input("Description")
st.button("Submit")
    #    status_code, response = send_request(base_story, length_slider)
    #    if status_code == 200:
    #       prediction = response.json()
    #       st.success(prediction["prediction"])
    #    else:
    #        st.error(str(status_code) + " Error")

st.markdown('''
<div style="display:flex">
        <a target="_blank" href="https://ainize.ai/scy6500/ainize-tutorial-front?branch=main">
            <img src="https://i.imgur.com/UnJzwth.png"/>
        </a>
        <a style="margin-left:10px" target="_blank" href="https://github.com/scy6500/ainize-tutorial-front">
            <img src="https://i.imgur.com/ASkTsnj.png"/>
        </a>
<div>
    ''',
    unsafe_allow_html=True
)