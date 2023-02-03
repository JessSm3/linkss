import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/streamlit/streamlit.svg?logo=github&style=social)](https://gitHub.com/streamlit/streamlit)")

col1, col2, col3 = st.columns(3)

st.header('Streamlit')

st.info('A faster way to build and share data and ML apps')

icon_size = 20

st_button('blog', 'https://blog.streamlit.io', 'Streamlit blog', icon_size)
st_button('youtube', 'https://www.youtube.com/@streamlit5916', 'Streamlit YouTube', icon_size)
st_button('twitter', 'https://twitter.com/streamlit/', 'Follow on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/company/streamlit/', 'Follow on LinkedIn', icon_size)
