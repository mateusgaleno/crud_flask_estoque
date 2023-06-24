from os import write
from numpy.core.fromnumeric import size
import streamlit as st;
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente
import streamlit.components as components
import pages.cliente.Create as PageCreateCliente


def list():
    paramId = st.experimental_get_query_params()
    if paramId.get("id")== None:
        st.experimental_set_query_params()
        colms = st.columns((1,2,1,2,1,1))
        campos =['Nª','Nome','Idade','Profissão','Excluir','Alterar']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)

#buscar informações no banco

        for item in ClienteController.SelecionarTodos():
            col1, col2, col3, col4, col5, col6 = st.columns((1,2,1,2,1,1))
            col1.write(item.id)
            col2.write(item.nome)
            col3.write(item.idade)
            col4.write(item.profissao)
            button_space_excluir = col5.empty() #a variavel button_space_excluir button_space recece col5.empty pq ela será uma coluna vazia
            on_click_excluir = button_space_excluir.button('Excluir','btnExcluir'+ str(item.id)) # concatenou pq o ID par excluir é unico, para concatenar teve que converter em string usando o str
            button_space_alterar = col6.empty()
            on_click_alterar = button_space_alterar.button('Alterar','btnAlterar' + str(item.id))


            if on_click_excluir:
                ClienteController.Excluir(item.id)
                button_space_excluir.button(
                'Excluido','btnExcluiro'+ str(item.id))
                st.experimental_rerun()
            if on_click_alterar:
                st.experimental_set_query_params(
                    id =[item.id]
                )
                st.experimental_rerun()
    else:
        on_click_voltar = st.button("Voltar")

        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageCreateCliente.IncluirClientePage()       





#listar usando o pandas
    # costumerlist =[]

    # for item in ClienteController.SelecionarTodos():
    #     costumerlist.append([item.nome, item.idade, item.profissao])


    # df = pd.DataFrame(
    #     costumerlist,
    #     columns=['Nome','Idade','Profissão']

    # )

    # st.table(df)
