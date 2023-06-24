from lib2to3.pgen2.pgen import DFAState
import streamlit as st
import pandas as pd

teste ='teste de viraveç'

st.selectbox('selecione uma opção', ['opção ', 'opção '])

st.sidebar.title('menu')
paginadelecionada = st.sidebar.selectbox('selecione a pagina', ['Pagina 1', 'Pagina 2'])

if paginadelecionada =='Pagina 2':
    st.title('video exemplo')
    st.markdown(teste)