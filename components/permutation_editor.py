import streamlit as st
import itertools






def permutation_editor():
    if 'omega' not in st.session_state:
        st.session_state.omega = set()

    if 'combinatorial_groups' not in st.session_state:
        st.session_state.combinatorial_groups = {}

    def reset_omega():
        st.session_state.omega = set()

    combinatorial_space = st.session_state.outcomes if  len(st.session_state.outcomes) > 0 else range(st.session_state.outcomes_numb)

    cols = st.columns(3)
    if cols[2].button('Calcular Permutación',use_container_width=True):
        omega = set(itertools.permutations(combinatorial_space))
        st.write(omega)
        st.write(f'Número de elementos en $\Omega$: {len(omega)}')

    if cols[1].button('Crear Espacio Muestral',use_container_width=True):
        st.session_state.omega = set(itertools.permutations(combinatorial_space))
        st.toast('Espacio Muestral creado', icon='🎲')

    if cols[0].button('Resetear Espacio Muestral',use_container_width=True):
        reset_omega()
        st.toast('Espacio Muestral reseteado', icon='🔄')
