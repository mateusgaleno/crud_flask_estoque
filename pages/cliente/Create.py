
from pydoc import cli
import streamlit as st;
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente


def IncluirClientePage():
    idAlteracao = st.experimental_get_query_params()
    st.experimental_set_query_params()
    clienteRecuperado =None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        clienteRecuperado = ClienteController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[clienteRecuperado.id]
        )
        # st.write(ClienteController.SelecionarById(idAlteracao).nome)
        st.title("Alterar Cliente")
    else:
        st.title("Incluir Cliente")

    with st.form(key="include_cliente"):
        listOccupation =["Desenvolvedor","Musico","Designer","Professor"]
        if clienteRecuperado == None:
            input_name = st.text_input(label="Insira o seu nome")
            input_age = st.number_input(label="insira sua idade", format ="%d", step=1)
            input_occupation = st.selectbox(label ="selecione sua profissão",options=listOccupation)
            
        else:
            input_name = st.text_input(label="Insira o seu nome", value =clienteRecuperado.nome)
            input_age = st.number_input(label="insira sua idade", format ="%d", step=1, value =clienteRecuperado.idade)
            input_occupation = st.selectbox(label ="selecione sua profissão", options=listOccupation, index=listOccupation.index(clienteRecuperado.profissao))
        input_button_submit = st.form_submit_button("Enviar")
        

    if input_button_submit:
        if clienteRecuperado == None:
            ClienteController.incluir(cliente.Cliente(0,input_name,input_age,input_occupation))
            st.success("Dados incluido com Sucesso")
        else:
            st.experimental_set_query_params()
            ClienteController.alterar(cliente.Cliente(0,input_name,input_age,input_occupation))
            st.success("Dados Alterado com Sucesso")
        