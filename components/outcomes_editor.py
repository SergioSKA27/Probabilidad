import streamlit as st

@st.experimental_fragment
def outcomes_editor():
    if 'outcomes' not in st.session_state:
        st.session_state.outcomes = []
    if 'outcomes_numb' not in st.session_state:
        st.session_state.outcomes_numb = 2

    def reset_outcomes():
        st.session_state.outcomes = []

    outcomes = st.number_input('Número de posibles resultados', min_value=1, value=2, step=1,max_value=1000)
    st.session_state.outcomes_numb = outcomes
    list_outcomes = st.checkbox('Listar los posibles resultados', value=False)
    if list_outcomes:
        outcome = st.text_input('ID de resultado', placeholder='Ejemplo: CARA')
        index = st.checkbox('Crear índice', value=False)

        if index:
            indexrange = st.slider('Rango de índices', min_value=0, max_value=(outcomes-1), value=(0, outcomes-1))
            outcomes_index = [f'{outcome}_{i}' for i in range(indexrange[0], indexrange[1]+1)]
            with st.expander('Ver índices'):
                st.write(str(set(outcomes_index)))
            cols = st.columns(2)
            if cols[0].button('Añadir Indices'):
                for i in outcomes_index:
                    if i not in st.session_state.outcomes and len(st.session_state.outcomes) < outcomes:
                        st.session_state.outcomes.append(i)
                    elif len(st.session_state.outcomes) >= outcomes:
                        st.toast('Número máximo de resultados alcanzado',icon='❌')
                    else:
                        continue
        else:
            cols = st.columns(2)
            if cols[0].button('Agregar resultado'):
                if outcome not in st.session_state.outcomes and len(st.session_state.outcomes) < outcomes:
                    st.session_state.outcomes.append(outcome)
                elif len(st.session_state.outcomes) >= outcomes:
                    st.toast('Número máximo de resultados alcanzado',icon='❌')
                else:
                    st.toast('Resultado ya agregado',icon='❌')
        st.write('Resultados actuales:')
        st.write(str(set(st.session_state.outcomes)))
        if len(st.session_state.outcomes) < outcomes:
            st.warning('Faltan resultados por agregar')
            if st.button('Rellenar con resultados por defecto'):
                for i in range(outcomes-len(st.session_state.outcomes)):
                    if f'$IDD_{i+1}' not in st.session_state.outcomes and len(st.session_state.outcomes) < outcomes:
                        st.session_state.outcomes.append(f'IDD_{i+1}')
                    
        cols[1].button('Resetear resultados', on_click=reset_outcomes)
    else:
        reset_outcomes()
        st.session_state.outcomes = range(outcomes)

