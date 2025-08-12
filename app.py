import streamlit as st
import utils.visual as visual

def show_dataset_link():
    st.link_button("🔗 Acessar Dataset CKD", "https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease")

def show_modelo_ia():
    visual.section_title("Modelo de IA", emoji="🤖")
    
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

def show_dados_paciente():
    visual.section_title("Dados do Paciente", emoji="👤")
    
    col1, spacer, col2 = st.columns([1, 0.05, 1])
    
    with col1:
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
    
    with spacer:
        st.write("")
        
    with col2:
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

def show_analisar_button():
    st.markdown("")
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("🔍 Realizar Análise", use_container_width=True):     
            st.switch_page("pages/resultado.py")

def main():
    visual.inject_css()
    visual.set_config(title="Sistema Médico - CKD")

    visual.show_title(title="Sistema Médico - CKD")
    
    show_dataset_link()
    
    col1, spacer, col2 = st.columns([1, 0.2, 2])
    with col1:
        show_modelo_ia()
    with spacer:
        st.write("")
    with col2:
        show_dados_paciente()
        
    show_analisar_button()
    
    st.markdown("---")
    
    visual.show_footer()

if __name__ == "__main__":
    main()