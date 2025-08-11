import streamlit as st

# Título da página
st.markdown("""
<div style="background: linear-gradient(90deg, #2E86AB 0%, #5DADE2 100%); padding: 1rem; border-radius: 10px; margin-bottom: 2rem;">
    <h1 style="color: white; text-align: center; margin: 0;">🏥 Detalhes do Paciente</h1>
</div>
""", unsafe_allow_html=True)

# Layout em colunas
col1, spacer, col2 = st.columns([1, 0.2, 2])

with col1:
    st.markdown("<h3 style='text-align: center;'>📋 Seleções</h3>", unsafe_allow_html=True)
    
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
    st.markdown("<h3 style='text-align: center;'>👤 Informações</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        Aqui estão os detalhes do paciente. Adicione mais informações ou elementos conforme necessário.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; color: #1B4F72; padding: 1rem;">
    <small>🏥 Sistema desenvolvido para auxílio ao diagnóstico médico • Versão 1.0</small>
</div>
""", unsafe_allow_html=True)