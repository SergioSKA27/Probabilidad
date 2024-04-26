import streamlit as st
from .expr_eval import Evaluator



def rule_event_editor():
    symbs = list(st.session_state.outcomes)
    event_name = st.text_input('Nombre del Evento', 'A')
    rule = st.text_input('Regla', f'{symbs[0]} # omega;')

    evaluator = Evaluator(st.session_state.omega, list(map(str, symbs)))
    evaluator.set_rule(rule)
    evcols = st.columns(2)
    if evcols[1].button('Ver Evento',use_container_width=True):
        data = evaluator.find_all()
        st.write(set(data))
    
    if evcols[0].button('Crear Evento',use_container_width=True):
        data = evaluator.find_all()
        if event_name in st.session_state.events:
            st.write('Evento ya existe, se sobreescribirá',use_container_width=True)
            accols = st.columns(2)
            if accols[1].button('Sobreescribir'):
                st.session_state.events[event_name] = set(data)
                st.toast('Evento sobreescribido con éxito', icon='🔄')
            
            if accols[0].button('Cancelar',use_container_width=True):
                st.toast('Operación Cancelada', icon='❌')
        else:
            st.session_state.events[event_name] = set(data)
            st.toast('Evento creado con éxito', icon='🎉')
        st.rerun()
    
    with st.expander('Guía de Uso', expanded=False):

        r"""
        ## GUIA DE USO
        Para crear un evento por regla, debes seguir los siguientes pasos:
        1. Escribe el nombre de la variable que deseas utilizar.
        2. Escribe la regla que deseas utilizar.
            - '#' para referenciar pertenencia a un conjunto.
            - '_name_\$_pos_' para referenciar una posición específica en un conjunto.
            - '<', '>', '<=', '>=', '==', '!=' para comparaciones.
            - 'and', 'or', 'not' para operaciones lógicas.
            - '+', '-', '*', '/', '**' para operaciones aritméticas.
            - '(', ')' para agrupar operaciones.
            - Use ';' para finalizar la regla no se mezclen operaciones lógicas y aritméticas.
        3. Presiona el botón 'Crear Evento'.

        Ejemplos:
        - Para crear el evento de que el outcome x este en cualquier conjunto del espacio muestral,
        escribe 'x # omega;'. Esto creará el evento
        $$\{x \in \omega | \forall \omega \in \Omega\}$$.
        - Para crear el evento de que el outcome x se encuentre en la posición 2 de cualquier conjunto del espacio muestral,
        escribe 'x # omega[1];'. Esto creará el evento
        $$\{x \in \omega_1 | \forall \omega \in \Omega\}$$.
        - Para crear el evento de que el outcome x sea mayor a 5 y menor a 10,
        escribe 'x > 5; and x < 10;'. Esto creará el evento
        $$\{x \in \omega | x > 5 \land x < 10\}$$.
        - Para crear el evento donde dados dos outcomes x e y, su suma sea mayor a 10,
        escribe 'x; + y; > 10;'. Esto creará el evento
        $$\{x, y \in \omega | x + y > 10 \land \forall \omega \in \Omega\}$$.
        """