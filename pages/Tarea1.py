import streamlit as st
import itertools
import random

st.set_page_config(layout="wide")
st.markdown("<style>#MainMenu, header, footer {visibility: hidden;} </style>", unsafe_allow_html=True)


st.title('Tarea 1: Ejercicios de Python')



def conditional_probability(A, B):
    return len(A.intersection(B)) / len(B)

def probability(A, omega):
    return len(A) / len(omega)




@st.experimental_fragment
def ejercicio_5():
    
    @st.cache_data
    def get_eventS(n):
        return set([(i, j) for i, j in omega if i + j == n])
    
    @st.cache_data
    def get_eventD(m):
        return set([(i, j) for i, j in omega if (i - j) >= m])
    
    def getans(omega):
        nm_combs = list(itertools.product(range(2, 13), range(0, 6)))
        st.write('Los valores posibles de n y m son:')
        st.write(f"{set(nm_combs)}")
        for n, m in nm_combs:
            s = get_eventS(n)
            d = get_eventD(m)
            cond = conditional_probability(d, s)
            ps = probability(s, omega)
            pd = probability(d, omega)
            if cond == ps*pd:
                st.write(f'Los eventos $S_{n}$ y $D_{m}$ son independientes')
                st.write(f'La probabilidad de $P(D_{m}|S_{n})$ es:')
                st.write(f"$P(D_{m}|S_{n}) = {conditional_probability(d, s)}$")
                st.write(f'La probabilidad de $P(D_{m})$ es:')
                st.write(f"$P(D_{m}) = {probability(d, omega)}$")
                st.write(f'La probabilidad de $P(S_{n})$ es:')
                st.write(f"$P(S_{n}) = {probability(s, omega)}$")
                st.write(f'La probabilidad de $P(D_{m})P(S_{n})$ es: {ps*pd}')
                return
            else:
                with st.expander(f'Para n = {n} y m = {m}'):
                    st.write(f'Los eventos $S_{n}$ y $D_{m}$ no son independientes')
                    st.write(f'La probabilidad de $P(D_{m}|S_{n})$ es:')
                    st.write(f"$P(D_{m}|S_{n}) = {conditional_probability(d, s)}$")
                    st.write(f'La probabilidad de $P(D_{m})$ es:')
                    st.write(f"$P(D_{m}) = {probability(d, omega)}$")
                    st.write(f'La probabilidad de $P(S_{n})$ es:')
                    st.write(f"$P(S_{n}) = {probability(s, omega)}$")
                    st.write(f'La probabilidad de $P(D_{m})P(S_{n})$ es: {ps*pd}')
        #events = get_eventS(n)
        #eventd = get_eventD(m)
        st.write('No Existe $(n, m)$ tal que $P(S_n ∩ D_m) = P(S_n)P(D_m)$')
        
    st.write( """
    5) Supongamos que se lanzan dos dados honestos. Considere los siguientes eventos:
    
• $S_n$ : la suma de las caras de los dados es $n$.

• $D_m$ : la diferencia de las caras de los dados es mayor o igual a $m$.

    """)
    
    n = st.number_input('Ingrese el valor de n:', min_value=2, max_value=12, value=7)
    m = st.number_input('Ingrese el valor de m:', min_value=0, max_value=5, value=2)
    
    
    
    omega = list(itertools.product(range(1,7), repeat=2))
    
    st.write('El espacio muestral $\Omega$ es:')
    st.write(f"{set(omega)}")
    s = get_eventS(n)
    d = get_eventD(m)
    st.write(f'El evento $S_{n}$ es:')
    st.write(f"$S_{n} = {s}$")
    st.write(f'El evento $D_{m}$ es:')
    st.write(f"$D_{m} = {d}$")
    
    st.write(f'La probabilidad de $P(S_{n})$ es:')
    st.write(f"$P(S_{n}) = {probability(s, omega)}$")
    st.write(f'La probabilidad de $P(D_{m})$ es:')
    st.write(f"$P(D_{m}) = {probability(d, omega)}$")
    st.write(f'La probabilidad de $P(D_{m}|S_{n})$ es:')
    st.write(f"$P(D_{m}|S_{n}) = {conditional_probability(d, s)}$")
    
    st.write("¿Existe $(n, m)$ tal que $P(S_n ∩ D_m) = P(S_n)P(D_m)$?")
    if st.button('Calcular'):
        with st.spinner('Calculando...'):
            getans(omega)
        
    

@st.experimental_fragment
def ejercicio_14():
    
    
    st.write("""
    14) De una urna que contiene 10 bolas rojas, 10 bolas negras y 10 bolas blancas, se seleccionan
2 bolas al azar y sin reemplazo. Calcule la probabilidad de que las dos bolas seleccionadas sean de
distinto color.""")
    
    B_white = ["W"+str(i) for i in range(1, 11)]
    B_black = ["N"+str(i) for i in range(1, 11)]
    B_red = ["R"+str(i) for i in range(1, 11)]
    
    omega = list(itertools.combinations(B_white + B_black + B_red, 2))
    st.write('El espacio muestral $\Omega$ es:')
    with st.expander('Ver espacio muestral'):
        st.write(f"{set(omega)}")
    
    A = set([(i, j) for i, j in omega if i[0] != j[0]])
    
    st.write('El evento $A$ es:')
    with st.expander('Ver evento A'):
        st.write(f"{set(A)}")
    
    st.write('La probabilidad de $P(A)$ es:')
    st.write(f"$P(A) = {probability(A, omega)}$")
    

@st.experimental_fragment
def ejercicio_18():
    st.write("""
    18) Una urna contiene 2N bolas numeradas del 1 al 2N. Un experimento consiste en elegir
al azar una bola de esa urna, dejándola fuera, y después, en elegir al azar una segunda. Calcule la
probabilidad de que la suma de los números elegidos sea par.
    """)

    N = st.number_input('Ingrese el valor de N:', min_value=1, value=1)
    
    omega = list(itertools.combinations(range(1, 2*N+1), 2))
    st.write('El espacio muestral $\Omega$ es:')
    with st.expander('Ver espacio muestral'):
        st.write(f"{set(omega)}")
    
    A = set([(i, j) for i, j in omega if (i+j) % 2 == 0])
    
    st.write('El evento $A$ es:')
    with st.expander('Ver evento A'):
        st.write(f"{set(A)}")
    
    st.write('La probabilidad de $P(A)$ es:')
    st.write(f"$P(A) = {probability(A, omega)}$")


@st.experimental_fragment
def ejercicio_19():
    
    def is_eventB(n):
        blues = [True for i in n if i[0] == 'B']
        whites = [True for i in n if i[0] == 'W']
        reds = [True for i in n if i[0] == 'R']
        
        return len(blues) == 2 and len(whites) == 1 and len(reds) == 1
        
        
            
    st.write("""
    19) Una urna contiene 20 bolas: 5, 8 azúles, y 7 rojas. Seleccionamos 4 bolas al azar. Calcula
la probabilidad de los siguientes eventos::

• todas sean rojas.

• 2 sean azules, 1 sea blanca y 1 sea roja.

• exactamente 4 sean blancas.
""")
    
    B_blue = ["B"+str(i) for i in range(1, 9)]
    
    B_red = ["R"+str(i) for i in range(1, 8)]
    
    B_white = ["W"+str(i) for i in range(1, 6)]
    
    omega = list(itertools.combinations(B_blue + B_red + B_white, 4))
    st.write('El espacio muestral $\Omega$ es:')
    with st.expander('Ver espacio muestral'):
        st.write(f"{set(omega)}")
     
    st.write('El evento $A$ (todas sean rojas) es:')
    A = set([(i, j, k, ll) for i, j, k, ll in omega if i[0] == 'R' and j[0] == 'R' and k[0] == 'R' and ll[0] == 'R'])
    with st.expander('Ver evento A'):
        st.write(f"{set(A)}")
    
    st.write('La probabilidad de $P(A)$ es:')
    st.write(f"$P(A) = {probability(A, omega)}$")
    
    st.write('El evento $B$ (2 sean azules, 1 sea blanca y 1 sea roja) es:')
    B = set([(i, j, k, ll) for i, j, k, ll in omega if is_eventB([i, j, k, ll])])
    with st.expander('Ver evento B'):
        st.write(f"{set(B)}")
    
    st.write('La probabilidad de $P(B)$ es:')
    st.write(f"$P(B) = {probability(B, omega)}$")
    
    st.write('El evento $C$ (exactamente 4 sean blancas) es:')
    C = set([(i, j, k, ll) for i, j, k, ll in omega if i[0] == 'W' and j[0] == 'W' and k[0] == 'W' and ll[0] == 'W'])
    with st.expander('Ver evento C'):
        st.write(f"{set(C)}")
    
    st.write('La probabilidad de $P(C)$ es:')
    st.write(f"$P(C) = {probability(C, omega)}$")


def ejercicio_20():
    def simulate(t):
        omega = []
        for _ in range(t):
            A = random.uniform(0, 30)
            B = random.uniform(0, 30)
            omega.append((A, B))
        return omega
            
    st.write("""
    20) Dos personas A y B, quedan de verse en un determinado lugar a las 12 hrs. Cada una
de ellas llega al lugar de la cita en un tiempo al azar entre las 12 y a las 12 : 30 hrs. Una vez que
llega al lugar de la cita, la persona A está dispuesta a esperar a lo más 5 minutos a que llegue la
persona B, mientras que la persona B está dispuesta a esperar a la persona A a lo más 10 minutos.
¿Cuál es la probabilidad de que las 2 personas se encuentren? 

**(Resuelve este problema usando probabilidad frecuentista)**.
""")
    
    time = st.number_input('Ingrese el número de simulaciones:', min_value=1, value=100)
    
    omega = simulate(time)
    st.write('El espacio muestral $\Omega$ es:')
    with st.expander('Ver espacio muestral'):
        st.write(f"{set(omega)}")
    A = set([(i, j) for i, j in omega if abs(i-j) <= 5 or abs(j-i) <= 10])
    
    st.write('El evento $A$ (las dos personas se encuentran) es:')
    with st.expander('Ver evento A'):
        st.write(f"{set(A)}")
    
    st.write('La probabilidad de $P(A)$ es:')
    st.write(f"$P(A) = {probability(A, omega)}$")
   
tabs = st.tabs(["Ejercicio 5", "Ejercicio 14", "Ejercicio 18", "Ejercicio 19", "Ejercicio 20"])   
    

with tabs[0]:
    ejercicio_5()

with tabs[1]:
    ejercicio_14()
    
with tabs[2]:
    ejercicio_18()

with tabs[3]:
    ejercicio_19()

with tabs[4]:
    ejercicio_20()