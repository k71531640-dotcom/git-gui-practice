import streamlit as st

st.title("간단한 계산기")

a = st.number_input("첫 번째 숫자", value=10)
b = st.number_input("두 번째 숫자", value=20)

st.write("덧셈 결과:", a + b)
st.write("뺄셈 결과:", a - b)
