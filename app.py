import streamlit as st

st.set_page_config(layout="wide")
st.html(
    """
    <style>
        #MainMenu, header, footer {visibility: hidden;}
        .appview-container .main .block-container
        {
            padding-top: 0.5px;
            padding-left: 0rem;
            padding-right: 0rem;
            padding-bottom: 0.5rem;
        }
        .hero{
            background: rgb(250,112,112);
            background: linear-gradient(180deg, rgba(250,112,112,1) 35%, rgba(112,181,250,1) 100%);
            background-size: cover;
            position: relative;
            width: 100%;
            height: 100vh;
            transform: skewY(-5deg);
        }
        .herocta{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            color: white;
        }
        .bouncing_arrow {
            animation: bounce 2s infinite;
            position: absolute;
            bottom: 20px;
            left: 50%;
            margin-left: -16px;
            width: 32px;
            height: 32px;
            border: 2px solid white;
            border-radius: 50%;

        }
        .arrow:before, .arrow:after {
            content: '';
            position: absolute;
            top: 0;
            width: 0.5rem;
            height: 0.5rem;
            background: white;
        }
        .scroll-prompt {
	position: relative;
	z-index: 998;
	bottom: 0;
	left: 50%;
	margin-left: -80px;
	width: 160px;
	height: 160px;
    transform: translateY(-120px);

	.scroll-prompt-arrow-container {
		position: absolute;
		top: 0;
		left: 50%;
		margin-left: -18px;
		animation-name: bounce;
		animation-duration: 1.5s;
		animation-iteration-count: infinite;
	}
	.scroll-prompt-arrow {
		animation-name: opacity;
		animation-duration: 1.5s;
		animation-iteration-count: infinite;
	}
	.scroll-prompt-arrow:last-child {
		animation-direction: reverse;
		margin-top: -6px;
	}
	.scroll-prompt-arrow > div {
		width: 36px;
		height: 36px;
		border-right: 8px solid #fefded;
		border-bottom: 8px solid #bebebe;
		transform: rotate(45deg) translateZ(1px);
	}
}

@keyframes opacity {
	0% {
		opacity: 0;
	}

	10% {
		opacity: 0.1;
	}

	20% {
		opacity: 0.2;
	}

	30% {
		opacity: 0.3;
	}

	40% {
		opacity: 0.4;
	}

	50% {
		opacity: 0.5;
	}

	60% {
		opacity: 0.6;
	}

	70% {
		opacity: 0.7;
	}

	80% {
		opacity: 0.8;
	}

	90% {
		opacity: 0.9;
	}

	100% {
		opacity: 1;
	}
}

@keyframes bounce {
	0% {
		transform: translateY(0);
	}

	10% {
		transform: translateY(3px);
	}

	20% {
		transform: translateY(6px);
	}

	30% {
		transform: translateY(9px);
	}

	40% {
		transform: translateY(12px);
	}

	50% {
		transform: translateY(15px);
	}

	60% {
		transform: translateY(18px);
	}

	70% {
		transform: translateY(21px);
	}

	80% {
		transform: translateY(24px);
	}

	90% {
		transform: translateY(27px);
	}

	100% {
		transform: translateY(30px);
	}
}

    </style>
    <div class="hero">
        <div class="herocta">
            <h1 style="font-size: 4rem;family: 'Roboto', sans-serif;">
            PyStreamlit Probability Calculator
            </h1>
            <h2 style="font-size: 2rem;">Calculadora de Probabilidad Condicional y Eventos de Probabilidad
            </h2>
        </div>
    </div>

    <div class="scroll-prompt" scroll-prompt="" ng-show="showPrompt" style="opacity: 1;">
    <div class="scroll-prompt-arrow-container">
        <div class="scroll-prompt-arrow"><div></div></div>
        <div class="scroll-prompt-arrow"><div></div></div>
    </div>
</div>

""",
)


_, col = st.columns([0.7, 0.3])
col.page_link(
    "pages/calculator.py",
    label="Ir a la Calculadora de Probabilidad",
    use_container_width=True,
    icon="🧮",
)

col.page_link(
    "pages/tareas_index.py",
    label="Ir a la página de Tareas",
    use_container_width=True,
    icon="📚",
)
