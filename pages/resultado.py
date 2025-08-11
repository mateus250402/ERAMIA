import streamlit as st

st.markdown("""
<style>
    .stButton > button {
        background: linear-gradient(90deg, #2E86AB, #5DADE2);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
</style
""", unsafe_allow_html=True)

# Título da página
st.markdown("""
<div style="background: linear-gradient(90deg, #2E86AB 0%, #5DADE2 100%); padding: 1rem; border-radius: 10px; margin-bottom: 2rem;">
    <h1 style="color: white; text-align: center; margin: 0;">🏥 Detalhes do Paciente</h1>
</div>
""", unsafe_allow_html=True)

# Layout em colunas
col1, spacer, col2 = st.columns([1, 0.2, 2])

with col1:
    st.markdown("<h3>Filtros</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <details>
        <summary>🔹 Grupo 1</summary>
        <ul style="padding-left: 20px;">
            <li style="margin-left: 20px;"><a href="?resultado=opcao1" target="_self">Opção 1</a></li>
            <li style="margin-left: 20px;"><a href="?resultado=opcao2" target="_self">Opção 2</a></li>
            <li style="margin-left: 20px;"><a href="?resultado=opcao3" target="_self">Opção 3</a></li>
        </ul>
    </details>
    <details>
        <summary>🔹 Grupo 2</summary>
        <ul style="padding-left: 20px;">
            <li style="margin-left: 20px;"><a href="?resultado=opcaoA" target="_self">Opção A</a></li>
            <li style="margin-left: 20px;"><a href="?resultado=opcaoB" target="_self">Opção B</a></li>
            <li style="margin-left: 20px;"><a href="?resultado=opcaoC" target="_self">Opção C</a></li>
        </ul>
    </details>
    <details>
        <summary>🔹 Grupo 3</summary>
        <ul style="padding-left: 20px;">
            <li style="margin-left: 20px;"><a href="?resultado=opcaoX" target="_self">Opção X</a></li>
            <li style="margin-left: 20px;"><a href="?resultado=opcaoY" target="_self">Opção Y</a></li>
            <li style="margin-left: 20px;"><a href="?resultado=opcaoZ" target="_self">Opção Z</a></li>
        </ul>
    </details>
    """, unsafe_allow_html=True)

with spacer:
    st.write("") 
    
with col2:
    col2a, spacer2, col2b = st.columns([1, 0.1, 1])
    
    with col2a:
        st.markdown("<h3 style='text-align: center;'>Contrafactuais</h3>", unsafe_allow_html=True)
        
    with spacer2:
        st.markdown("")
        
    with col2b:
        st.markdown("<h3 style='text-align: center;'>Métricas</h3>", unsafe_allow_html=True)
    
st.markdown("---")

col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

with col_btn2:
    if st.button("Inserir dados", use_container_width=True):     
        st.switch_page("../app.py")


# Footer
st.markdown("""
<div style="text-align: center; color: #1B4F72; padding: 1rem;">
    <small>🏥 Sistema desenvolvido para auxílio ao diagnóstico médico • Versão 1.0</small>
</div>
""", unsafe_allow_html=True)