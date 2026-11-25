import streamlit as st
import requests

st.markdown(
"""
# Zoologist front
""", text_alignment='center'
)
with st.container(horizontal_alignment="center"):
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGmsf23FcBuGEuqO0S_v8wPCFIs9I6KOCjwJsj2Dlsle7cSl1wm_yB8NSy&s=10')

st.markdown(
    """
## Welcome to the Penguin species portal !

We propose penguin species classsification based on their characteristics
"""
)


st.markdown("""Please input your penguins characteristics to know his species !""")


island = st.selectbox('Island', ['Biscoe', 'Dream', 'Torgersen'])
bill_length_mm = st.number_input('Bill length', value=51.9)
bill_depth_mm = st.number_input('Bill depth', value=19.5)
flipper_length_mm = st.number_input('Flipper length', value=206)
body_mass_g = st.number_input('Body mass', value=3950)
sex = st.selectbox('Sex', ['Male', 'Female'])

if st.button('Click to predict'):

    url_penguin = f'{st.secrets["API_URL"]}/predict'

    api_pm = {
        'island' : island,
        'bill_length_mm' : bill_length_mm ,
        'bill_depth_mm' : bill_depth_mm ,
        'flipper_length_mm' : flipper_length_mm,
        'body_mass_g' : body_mass_g,
        'sex' : sex
    }

    response = requests.get(url=url_penguin, params=api_pm)

    result = response.json()['prediction']

    st.write(f'# The penguin you are looking for is a **{result}**!')

    if result == 'Chinstrap':
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8eECy91ENp86zY15vsOSBbOFxZwXsMRfUQrCgekzlGw&s=10')
    elif result == 'Adelie':
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYfjJkHUn9ereRifooWAjrE-aynSfYtOR3IYAwotw9plS0Ph0EGv-Kh8E&s=10')
    elif result == 'Gentoo':
        st.image('https://www.visitsealife.com/sydney/media/fjfjlkr3/lara.jpg?format=jpg')
