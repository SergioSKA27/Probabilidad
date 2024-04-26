import streamlit as st
import asyncio
from .product_editor import product_editor
from .permutation_editor import permutation_editor
from .combination_editor import combination_editor
from .combinationrep_editor import combinationrep_editor



def muestral_space_editor():

    st.write('###### Editor de Espacio Muestral')
    if 'omega' not in st.session_state:
        st.session_state.omega = set()

    if 'combinatorial_groups' not in st.session_state:
        st.session_state.combinatorial_groups = {}

    def reset_omega():
        st.session_state.omega = set()

    combinatorial_space = st.session_state.outcomes if  len(st.session_state.outcomes) > 0 else range(st.session_state.outcomes_numb)
    with st.expander('Outcomes',expanded=True):
        st.write(combinatorial_space)
        st.button('Actualizar Outcomes')
    combinatorial_type = st.selectbox('Acción a realizar', ['Producto', 'Permutación', 'Combinación', 'Combinación con repetición',])

    if combinatorial_type == 'Producto':
        product_editor()
    if combinatorial_type == 'Permutación':
        permutation_editor()
    if combinatorial_type == 'Combinación':
        asyncio.run(combination_editor())
    if combinatorial_type == 'Combinación con repetición':
        combinationrep_editor()

    st.write('Espacio Muestral actual:')
    st.write(st.session_state.omega)