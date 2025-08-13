import streamlit as st
import pandas as pd
import utils.visual as visual

def show_result(progrediu: bool):
    if progrediu:
        indicador = "<span class='icon-success'>✅</span>"
        texto = "<span class='text-success'>Houve progressão da doença</span>"
    else:
        indicador = "<span class='icon-fail'>❌</span>"
        texto = "<span class='text-fail'>Não houve progressão da doença</span>"
    st.markdown(f"""<div class="result-indicator">{indicador}{texto}</div>""", unsafe_allow_html=True)

def show_filters():
    st.markdown("<h3>Filtros</h3>", unsafe_allow_html=True)
    st.markdown("""
    <details>
        <summary>🔹 Grupo 1</summary>
        <ul class="filters-ul">
            <li class="filters-li"><a href="?resultado=opcao1" target="_self">Opção 1</a></li>
            <li class="filters-li"><a href="?resultado=opcao2" target="_self">Opção 2</a></li>
            <li class="filters-li"><a href="?resultado=opcao3" target="_self">Opção 3</a></li>
        </ul>
    </details>
    <details>
        <summary>🔹 Grupo 2</summary>
        <ul class="filters-ul">
            <li class="filters-li"><a href="?resultado=opcaoA" target="_self">Opção A</a></li>
            <li class="filters-li"><a href="?resultado=opcaoB" target="_self">Opção B</a></li>
            <li class="filters-li"><a href="?resultado=opcaoC" target="_self">Opção C</a></li>
        </ul>
    </details>
    <details>
        <summary>🔹 Grupo 3</summary>
        <ul class="filters-ul">
            <li class="filters-li"><a href="?resultado=opcaoX" target="_self">Opção X</a></li>
            <li class="filters-li"><a href="?resultado=opcaoY" target="_self">Opção Y</a></li>
            <li class="filters-li"><a href="?resultado=opcaoZ" target="_self">Opção Z</a></li>
        </ul>
    </details>
    """, unsafe_allow_html=True)

def show_contrafactuais_metricas():
    # Dados dos contrafactuais
    contrafactuais = [
        "Em um cenário que: **TFGe** -> 21.04, **Pressão_Arterial_Sistólica** -> 152.78, **IMC** -> 24.92, **Albumina** -> 4.16, **Diabetes** ausente, **Bloqueador_Canal_Cálcio** presente, **Diuréticos** ausente, **Histórico_DCV** ausente, **Hipertensão** presente, **Inibidor_SRA** presente. Detectada semelhança com **Cluster 2**, que possui: **Hipertensão presente**, **Histórico_DCV ausente**.",

        "Em um cenário que: **TFGe** -> 38.08. Detectada semelhança com **Cluster 1**, que possui: **Diabetes ausente**, **Hipertensão presente**, **Histórico_DCV ausente**",

        "Em um cenário que: **TFGe** -> 25.41, **Pressão_Arterial_Sistólica** -> 139.47, **IMC** -> 34.36, **Hemoglobina** -> 12.56, **Albumina** -> 4.29, **Diabetes** -> 0, **Diuréticos** -> 1. Detectada semelhança com **Cluster 3**, que possui: **Diabetes ausente**, **Hipertensão presente**, **Histórico_DCV ausente**"
    ]
    
    # Métricas correspondentes
    metricas = [
        [0.738, 0.972, 5, 0.727, 0.75, 0],
        [0.87, 0.972, 2, 0.752, 0.5, 1],
        [0.642, 0.972, 7, 0.717, 0.875, 1]
    ]
    
    nomes_metricas = ["Similarity", "Quality", "Sparsity", "Smoothness", "Plausibility", "Validation"]

    # Cabeçalho principal
    st.markdown("<h3 style='text-align: center; margin-bottom: 1rem;'>Contrafactuais & Métricas</h3>", unsafe_allow_html=True)
    
    # Para cada contrafactual e suas métricas
    for i, (contra, metrica) in enumerate(zip(contrafactuais, metricas)):
        st.markdown(f"**Contrafactual {i+1}:**")
        st.markdown(contra)
        
        # Criar DataFrame para as métricas
        df_metricas = pd.DataFrame([metrica], columns=nomes_metricas)

        # Converte DataFrame em tabela HTML
        html_table = df_metricas.to_html(index=False, escape=False, table_id="metrics-table")
        st.markdown(f'<div class="table-container">{html_table}</div>', unsafe_allow_html=True)
        
        st.markdown("---")  # Separador entre contrafactuais
        
def show_insert_button():
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("Inserir dados", use_container_width=True):     
            st.switch_page("app.py")

def main():
    visual.set_config(title="Resultado")
    visual.inject_css()
    
    visual.show_title(title="Resultado da Análise")
    
    progrediu = True  
    show_result(progrediu)
    
    col1, spacer, col2 = st.columns([1, 0.05, 2])
    with col1:
        show_filters()
    with spacer:
        st.write("") 
    with col2:
        show_contrafactuais_metricas()
    
    show_insert_button()
    
    visual.show_footer()

if __name__ == "__main__":
    main()