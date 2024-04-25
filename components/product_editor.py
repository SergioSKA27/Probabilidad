import streamlit as st
import itertools




def product_editor():
    if 'omega' not in st.session_state:
        st.session_state.omega = set()

    if 'combinatorial_groups' not in st.session_state:
        st.session_state.combinatorial_groups = {}

    def reset_omega():
        st.session_state.omega = set()
        
    combinatorial_space = st.session_state.outcomes if  len(st.session_state.outcomes) > 0 else range(st.session_state.outcomes_numb)

    repeat = st.checkbox('Crear Grupo de Productos')
    if repeat:
        group = st.text_input('Nombre del grupo', value='Grupo 1')
        group_outcomes = st.multiselect('Elementos del grupo', combinatorial_space)
        colsgr = st.columns(3)
        if colsgr[2].button('Agregar Grupo',use_container_width=True):
            if group not in st.session_state.combinatorial_groups and len(group_outcomes) > 0:
                st.session_state.combinatorial_groups.update({group: group_outcomes})
            else:
                st.toast('Grupo ya creado', icon='❌')
        if colsgr[0].button('Resetear grupos',use_container_width=True):
            st.session_state.combinatorial_groups = {}
        if colsgr[1].button('Mostrar grupos',use_container_width=True):
            st.write(st.session_state.combinatorial_groups)

        productord = st.multiselect('Seleccionar grupos en orden', list(st.session_state.combinatorial_groups.keys()))
        plist = [st.session_state.combinatorial_groups[i] for i in productord]
        
        colsgr2 = st.columns(3)
        if colsgr2[2].button('Calcular Producto',use_container_width=True):
            omega = set(itertools.product(*plist))
            st.write(omega)
            st.write(f'Número de elementos en $\Omega$: {len(omega)}')

        
        if colsgr2[1].button('Crear Espacio Muestral',use_container_width=True):
            st.session_state.omega = set(itertools.product(*plist))
            st.toast('Espacio Muestral creado', icon='🎲')

        if colsgr2[0].button('Resetear Espacio Muestral',use_container_width=True):
            reset_omega()
            st.toast('Espacio Muestral reseteado', icon='🔄')
    else:
        repeattimes = st.number_input('Número de veces a repetir', min_value=1, value=2, step=1)
        cols1 = st.columns(3)
        if cols1[2].button('Calcular Producto',use_container_width=True):
            omega = set(itertools.product(combinatorial_space, repeat=repeattimes))
            st.write(omega)
            st.write(f'Número de elementos en $\Omega$: {len(omega)}')

        if cols1[1].button('Crear Espacio Muestral',use_container_width=True):
            st.session_state.omega = set(itertools.product(combinatorial_space, repeat=repeattimes))
            st.toast('Espacio Muestral creado', icon='🎲')
        
        if cols1[0].button('Resetear Espacio Muestral',use_container_width=True):
            reset_omega()
            st.toast('Espacio Muestral reseteado', icon='🔄')
