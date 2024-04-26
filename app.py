import streamlit as st

from components.event_editor import event_editor
from components.muestral_editor import muestral_space_editor
from components.outcomes_editor import outcomes_editor

st.set_page_config(layout="wide")

if "events" not in st.session_state:
    st.session_state.events = {}

if "events_workspace" not in st.session_state:
    st.session_state.events_workspace = set()

def conditional_probability(A, B):
    return len(A.intersection(B)) / len(B)


def probability(A, omega):
    return len(A) / len(omega)


def current_config():
    with st.container(border=True):
        st.write("###### Configuración Actual")
        st.write("Outcomes:", st.session_state.outcomes)
        st.write("Longitud de Outcomes:", st.session_state.outcomes_numb)
        with st.expander("Espacio Muestral", expanded=True):
            st.write(st.session_state.omega)
        st.write("Longitud de Espacio Muestral:", len(st.session_state.omega))
        st.write("Grupos Combinatorios:", st.session_state.combinatorial_groups)
        st.write("Eventos:", st.session_state.events)

def workspace_view():
    with st.container(border=True):
        st.write("###### Espacio de Trabajo")
        st.write("Eventos en el espacio de trabajo:", str(st.session_state.events_workspace))

def event_view():
    if len(st.session_state.events_workspace) == 0:
        return
    with st.container(border=True):
        st.write("###### Eventos")
        selected_event = st.selectbox(
            "Selecciona un evento", list(st.session_state.events.keys()),
            label_visibility="collapsed"
        )
        with st.expander("Ver Evento", expanded=True):
            st.write(str(st.session_state.events[selected_event]))

def probability_calculator_conditional(main):
    A = main.selectbox(
                "Evento A",
                list(st.session_state.events.keys()),
                placeholder="Selecciona un evento",
            )
    B = main.selectbox(
        "Evento B",
        list(st.session_state.events.keys()),
        placeholder="Selecciona un evento",
    )
    if main.button("Calcular Probabilidad Condicional"):
        prob_cond = conditional_probability(
            st.session_state.events[A], st.session_state.events[B]
        )
        st.write(f"La probabilidad condicional de {A} dado {B} es {prob_cond}")
        st.write(f"$P({A}|{B}) = {len(st.session_state.events[A].intersection(st.session_state.events[B]))}/{len(st.session_state.events[B])}$")

def probability_calculator(main):
    A = main.selectbox(
                "Evento",
                list(st.session_state.events.keys()),
                placeholder="Selecciona un evento",
            )
    if main.button("Calcular Probabilidad"):
        prob = probability(st.session_state.events[A], st.session_state.omega)
        st.write(f"La probabilidad de {A} es {prob}")
        st.write(f"$P({A}) = {len(st.session_state.events[A])}/{len(st.session_state.omega)}$")

if __name__ == "__main__":
    with st.popover(
        "Outcomes Editor",
        help="Edita los resultados posibles de un experimento",
        use_container_width=True,
    ):
        outcomes_editor()

    with st.popover(
        "Muestral Space Editor",
        help="Edita el espacio muestral de un experimento",
        use_container_width=True,
    ):
        muestral_space_editor()

    lateral, main = st.columns([0.4, 0.6])
    if lateral.toggle("Añadir Evento al espacio de trabajo",):
        addev = main.selectbox(
            "Evento a añadir",
            list(st.session_state.events.keys()),
            placeholder="Selecciona un evento",
        )
        addevcols = main.columns([0.6, 0.4], gap="large")
        if addevcols[1].button(
            "Añadir Evento", use_container_width=True,
        ):
            if addev not in st.session_state.events_workspace:
                st.session_state.events_workspace.add(addev)
                st.toast("Evento añadido con éxito", icon="🎉")
            else:
                st.toast("Evento ya añadido", icon="❌")


    if lateral.toggle("Calcular Probabilidad Condicional",):
        with main.container(border=True):
            probability_calculator_conditional(main)
    if lateral.toggle("Calcular Probabilidad",):
        with main.container(border=True):
            probability_calculator(main)

    with lateral:
        with st.popover(
            "Configuración Actual",
            help="Muestra la configuración actual del experimento",
            use_container_width=True,
        ):
            current_config()

        with st.popover(
            "Event Editor",
            help="Edita los eventos de un experimento",
            use_container_width=True,
        ):
            event_editor()

        workspace_view()
        event_view()
