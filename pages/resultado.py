import streamlit as st
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

def show_contrafactuais():
    st.markdown("<h3 style='text-align: center;'>Contrafactuais</h3>", unsafe_allow_html=True)

def show_metrics():
    st.markdown("<h3 style='text-align: center;'>Métricas</h3>", unsafe_allow_html=True)

def show_contrafactuais_metricas():
    col1, spacer, col2 = st.columns([1, 0.1, 1])
    
    with col1:
        show_contrafactuais()

    with spacer:
        st.markdown("")
        
    with col2:
        show_metrics()

def show_insert_button():
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("Inserir dados", use_container_width=True):     
            st.switch_page("app.py")

def main():
    visual.set_config(title="Resultado")
    visual.inject_css()
    
    visual.show_title(title="Resultado da Análise")
    
    progrediu = False  
    show_result(progrediu)
    
    col1, spacer, col2 = st.columns([1, 0.2, 2])
    with col1:
        show_filters()
    with spacer:
        st.write("") 
    with col2:
        show_contrafactuais_metricas()
    st.markdown("---")
    
    show_insert_button()
    
    visual.show_footer()

if __name__ == "__main__":
    main()