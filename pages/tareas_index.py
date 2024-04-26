import streamlit as st


st.markdown("<style>#MainMenu, header, footer {visibility: hidden;} </style>", unsafe_allow_html=True)



with st.container(border=True):
    st.title('Tareas')
    st.write('En esta sección se encuentran las tareas realizadas en el curso de Probabilidad .')
    col , _ = st.columns([.7,.3])

    col.page_link('pages/Tarea1.py',label='Tarea 1',use_container_width=True,icon='📚')

    col.page_link('app.py',label='Volver al inicio',use_container_width=True,icon='🏠')