import streamlit as st
import sympy as sp
from components.outcomes_editor import outcomes_editor
from components.muestral_editor import muestral_space_editor

st.set_page_config(layout="wide")

def conditional_probability(A, B):
    return len(A.intersection(B)) / len(B)

def probability(A, omega):
    return len(A) / len(omega)

@st.cache_resource(experimental_allow_widgets=True)
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
    symbs = sp.symbols(st.session_state.outcomes)
    
    st.latex(symbs)

    """
    ## GUIA DE USO
    Para crear un evento por regla, debes seguir los siguientes pasos:
    1. Escribe el nombre de la variable que deseas utilizar.
    2. Escribe la regla que deseas utilizar.
        - '#' para referenciar pertenencia a un conjunto.
        - '${numero}$' para referenciar una posición específica en un conjunto.
        - '<', '>', '<=', '>=', '==', '!=' para comparaciones.
    """