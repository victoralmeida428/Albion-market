import streamlit as st
from albion import Mercado
st.set_page_config(page_title='Mercado - Albion',page_icon='https://downloadr2.apkmirror.com/wp-content/uploads/2018/10/5bb4077aae6c0.png')

options_itens = Mercado().pegar_itens()
item = st.sidebar.multiselect('Itens', options=options_itens)
qualidade = st.sidebar.multiselect('Qualidade', options=[str(i) for i in range(1,10)])
st.title('Mercado - Albion')
st.write('Veja os melhores preços de venda rápida do mundo Albion')
if st.sidebar.button('Buscar'):
    df = Mercado().pegar_preco(item = item, qualidade = qualidade)
    if len(df)>0:
        st.write(df)
    else:
        st.warning('Não possui item vendendo no momento')