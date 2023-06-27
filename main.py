import streamlit as st

col1, col2 = st.columns(2) # return 2 column objects; column object instances

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Emily Waller")
    content = '''My name is Emily Waller and I am a rising junior studying Accounting and Data Science at Southern 
    Methodist University. Here, I am also a member of the Division I Women's Track and Field Program, as well as the 
    VP of Alumni Relations for the Alpha Kappa Psi Business Fraternity'''
    st.write(content)