import streamlit as st
import sympy as sp
from components.outcomes_editor import outcomes_editor
from components.muestral_editor import muestral_space_editor
from components.expr_eval import Evaluator

st.set_page_config(layout="wide")



if 'signal' not in st.session_state:
    st.session_state.signal = False
else:
    if st.session_state.signal:
        st.session_state.signal = False
        st.rerun()

def conditional_probability(A, B):
    return len(A.intersection(B)) / len(B)

def probability(A, omega):
    return len(A) / len(omega)

def current_config():
    with st.container(border=True):
        st.write('###### Configuración Actual')
        st.write('Outcomes:', st.session_state.outcomes)
        st.write('Longitud de Outcomes:', st.session_state.outcomes_numb)
        with st.expander('Espacio Muestral',expanded=True):
            st.write(st.session_state.omega)
        st.write('Longitud de Espacio Muestral:', len(st.session_state.omega))
        st.write('Grupos Combinatorios:', st.session_state.combinatorial_groups)


if __name__ == '__main__':
    with st.popover('Outcomes Editor', help='Edita los resultados posibles de un experimento',use_container_width=True):
        outcomes_editor()

    with st.popover('Muestral Space Editor', help='Edita el espacio muestral de un experimento',use_container_width=True):
        muestral_space_editor()

    lateral, main = st.columns([1, 4])
    with lateral:
        with st.popover('Configuración Actual', help='Muestra la configuración actual del experimento',use_container_width=True):
            current_config()




st.write('###### Editor de Eventos')

create_by = st.selectbox('Crear Evento por', ['Regla', 'Grupo Combinatorio', 'Seleccion', 'Union', 'Interseccion', 'Diferencia', 'Complemento',])

if create_by == 'Regla':

    symbs = list(st.session_state.outcomes)

    rule = st.text_input('Regla', 'x # omega;')

    evaluator = Evaluator(st.session_state.omega, list(map(str, symbs)))
    evaluator.set_rule(rule)

    st.write(evaluator.tokenize(rule))
    st.write(evaluator.to_sufix())

    st.latex(symbs)

    r"""
    ## GUIA DE USO
    Para crear un evento por regla, debes seguir los siguientes pasos:
    1. Escribe el nombre de la variable que deseas utilizar.
    2. Escribe la regla que deseas utilizar.
        - '#' para referenciar pertenencia a un conjunto.
        - '\[{posición - 1}]$' para referenciar una posición específica en un conjunto.
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