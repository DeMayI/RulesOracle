import streamlit as st
from query import answer

st.set_page_config(page_title="0th Edition Rules Oracle")
st.title("0th Edition Rules Oracle")
st.caption("Ask a question about this custom ruleset.")

q = st.text_input('Your rules question')
if q:
    with st.spinner("Searching the rules..."):
        ans, sources = answer(q)
    st.markdown(ans)
    