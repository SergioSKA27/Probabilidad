import streamlit as st
from .rule_event_editor import rule_event_editor

def event_editor():
    st.write('###### Editor de Eventos')


    create_by = st.selectbox('Crear Evento por', ['Regla', 'Grupo Combinatorio', 'Seleccion', 'Union', 'Interseccion', 'Diferencia', 'Complemento',])

    with st.expander('Outcomes Vars', expanded=False):
        st.write(st.session_state.outcomes)
    if create_by == 'Regla':

        rule_event_editor()
