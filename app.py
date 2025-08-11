import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Sistema Médico - CKD",
    page_icon="🏥",
    layout="wide"
)

# Header principal
st.markdown("""
<div style="background: linear-gradient(90deg, #2E86AB 0%, #5DADE2 100%); padding: 1rem; border-radius: 10px; margin-bottom: 2rem;">
    <h1 style="color: white; text-align: center; margin: 0;">🏥 Sistema de Análise Médica</h1>
    <p style="color: white; text-align: center; margin: 0; opacity: 0.9;">Diagnóstico de Doença Renal Crônica (CKD)</p>
</div>
""", unsafe_allow_html=True)

# CSS customizado para estilo hospitalar
st.markdown("""
<style>
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #2E86AB;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
    
    .info-box {
        background: #E8F4F8;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #2E86AB;
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #2E86AB, #5DADE2);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)
    
st.link_button("🔗 Acessar Dataset CKD", "https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease")

# Layout em colunas
col1, spacer, col2 = st.columns([1, 0.2, 2])

with col1:
    st.markdown("<h3 style='text-align: center;'>🤖 Modelo de IA</h3>", unsafe_allow_html=True)
    
    opcoes_modelo = st.selectbox(
        "Selecione o modelo de análise:",
        ["SHAP"]
    )
    
    elbow = st.checkbox(
        "Elbow Method decide número de clusters?",
        value=False,
    )

    if not elbow:
        qtd_cluster = st.number_input(
            "Número de Clusters:",
            min_value=1,
            value=1,
        step=1,
    )
        
    min_casos_cluster = st.number_input(
        "Número Mínimo de Casos por Cluster:",
        min_value=1,
        value=1,
        step=1,
    )

    min_casos_nuns = st.number_input(
        "Número Mínimo de Nuns:",
        min_value=1,
        value=1,
        step=1,
    )

    treshold = st.number_input(
        "Treshold de recuperação de KNN:",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01,
    )
    
with spacer:
    # Espaço vazio para separação visual
    st.write("")

with col2:
    st.markdown("<h3 style='text-align: center;'>👤 Dados do Paciente</h3>", unsafe_allow_html=True)

    # Dados pessoais
    col2a, spacer2, col2b = st.columns([1, 0.05, 1])
        
    
    with col2a:
        idade = st.number_input(
            "🎂 Idade:",
            min_value=0,
            max_value=120,
            value=45,
        )
        
        pressao_arterial_sistolica = st.number_input(
            "🩺 Pressão Arterial Sistólica (mmHg):",
            min_value=50,
            max_value=250,
            value=120,
        )
        
        imc = st.number_input(
            "⚖️ IMC (Índice de Massa Corporal):",
            min_value=10.0,
            max_value=60.0,
            value=22.5,
            step=0.1,
        )
    
        hemoglobina = st.number_input(
            "🩸 Hemoglobina (g/dL):",
            min_value=0.0,
            max_value=20.0,
            value=13.5,
            step=0.1,
        )
        
        albumina = st.number_input(
            "🧪 Albumina (g/dL):",
            min_value=0.0,
            max_value=10.0,
            value=4.0,
            step=0.1,
        )
        
        tfge = st.number_input(
            "🧬 TFGe (Taxa de Filtração Glomerular Estimada):",
            min_value=0.0,
            max_value=200.0,
            value=90.0,
            step=1.0,
        )
    
    with spacer2:
        # Espaço vazio para separação visual
        st.write("")
    
    with col2b:
        proteinura = st.checkbox(
            "💧 Proteinúria Presente",
            value=False,
        )
        
        sangue_oculto = st.checkbox(
            "🩸 Sangue Oculto na Urina",
            value=False,
        )
        
        hipertensao = st.checkbox(
            "🩺 Hipertensão Presente",
            value=False,
        )
        
        historico_dcv = st.checkbox(
            "❤️ Histórico de Doenças Cardiovasculares",
            value=False,
        )
        
        diabetes = st.checkbox(
            "🍭 Diabetes Presente",
            value=False,
        )
        
        inibidor_sraa = st.checkbox(
            "💊 Uso de Inibidores do Sistema Renina-Angiotensina-Aldosterona (SRAA)",
            value=False,
        )
        
        bloquador_calcio = st.checkbox(
            "💊 Uso de Bloqueadores de Cálcio",
            value=False,
        )
        
        diuretico = st.checkbox(
            "💊 Uso de Diuréticos",
            value=False,
        )
        
        progressao_drc = st.checkbox(
            "📈 Progressão da Doença Renal Crônica",
            value=False,
        ) 
        
        sexo_opcao = st.radio(
            "👤 Sexo:",
            options=["Masculino", "Feminino"],
            index=0,
        )
        sexo = 1 if sexo_opcao == "Masculino" else 2

st.markdown("")
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

with col_btn2:
    if st.button("🔍 Realizar Análise", use_container_width=True):     
        st.switch_page("Resultado")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #1B4F72; padding: 1rem;">
    <small>🏥 Sistema desenvolvido para auxílio ao diagnóstico médico • Versão 1.0</small>
</div>
""", unsafe_allow_html=True)