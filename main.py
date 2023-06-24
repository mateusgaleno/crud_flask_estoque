from os import write
from numpy.core.fromnumeric import size
import streamlit as st;
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente
import streamlit.components as components
import pandas as pd
import pages.cliente.Create as PageIncluirCliente
import pages.cliente.list as PageListarCliente


st.sidebar.title('Menu')
page_cliente = st.sidebar.selectbox('cliente',['Incluir','Consultar'])

if page_cliente == 'Consultar':
    PageListarCliente.list()


if page_cliente =='Incluir':
    st.experimental_set_query_params()
    PageIncluirCliente.IncluirClientePage()



