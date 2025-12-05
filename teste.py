import streamlit as st
import base64

# ---------- CONFIGURAÇÕES DO SITE ----------
st.set_page_config(
    page_title="Construtora Talismã",
    page_icon="🏗️",
    layout="wide"
)

# ---------- GRADIENTE DE FUNDO ---------- COLORAÇÃO DA PAGIANA

st.markdown("""
<style>
/* Aplica gradiente em toda a página */
html, body, [class*="block-container"] {
    background: linear-gradient(135deg, #4184e1 0%, #FFFFFF 100%) !important;   
    background-attachment: fixed; /* Fixa o gradiente ao rolar */
}

/* Remove o fundo branco padrão do Streamlit */
.main {
    background: none; /* Remove o fundo branco do container principal */
}
</style>
""", unsafe_allow_html=True)


# ---------- ESTILO GLOBAL PREMIUM ----------
st.markdown("""
<style>

body {
    font-family: 'Segoe UI', sans-serif;
}

/* HERO SECTION ------------------------------------------------------ */
.hero-section {
    position: relative;
    background-image: url('https://images.unsplash.com/photo-1581091012184-5c7b28c8ad9b');
    background-size: cover;
    background-position: center;
    height: 380px;
    border-radius: 12px;
    margin-bottom: 40px;
}

.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.45);
    border-radius: 12px;
}

.hero-content {
    position: relative;
    z-index: 2;
    padding: 60px;
    color: white;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.7);
}

.hero-title {
    font-size: 50px;
    font-weight: bold;
}

.hero-subtitle {
    font-size: 22px;
    margin-top: 10px;
}

.hero-button {
    display: inline-block;
    margin-top: 20px;
    padding: 12px 28px;
    background-color: #FFA600;
    color: black;
    font-size: 20px;
    font-weight: bold;
    border-radius: 8px;
    text-decoration: none;
}

/* SECTION TITLES ----------------------------------------------------- */
.section-title {
    font-size: 30px;
    font-weight: bold;
    color: #003F5C;
    margin-top: 30px;
    margin-bottom: 20px;
}

/* CARDS -------------------------------------------------------------- */
.card {
    padding: 18px;
    background-color: #F5F5F5;
    border-radius: 12px;
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-4px);
    background-color: #e9ecef;
}

/* FOOTER ------------------------------------------------------------- */
.footer {
    text-align: center;
    padding: 25px;
    margin-top: 50px;
    color: #777;
    border-top: 1px solid #ddd;
}

/* BOTÃO WHATSAPP FLUTUANTE -------------------------------------------- */
.whatsapp-btn {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background-color: #25D366;
    color: white;
    width: 58px;
    height: 58px;
    border-radius: 50%;
    font-size: 32px;
    text-align: center;
    line-height: 58px;
    box-shadow: 2px 2px 12px rgba(0,0,0,0.3);
    text-decoration: none;
    z-index: 9999;
}

</style>
""", unsafe_allow_html=True)

#==========================# Butão whatsapp flutuante===========================

st.markdown("""
<style>
.whatsapp-btn {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background-color: #25D366;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 2px 2px 12px rgba(0,0,0,0.3);
    z-index: 9999;
}
.whatsapp-btn img {
    width: 35px;
    height: auto;
}
</style>
""", unsafe_allow_html=True)



# ==========================================================
# ==================== butão do instagram =======================

st.markdown("""
<style>
.instagram-btn {
    position: fixed;
    bottom: 25px;
    right: 95px;   /* afastado do WhatsApp */
    background-color: #E4405F;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 2px 2px 12px rgba(0,0,0,0.3);
    z-index: 9999;
}
.instagram-btn img {
    width: 32px;
    height: auto;
}
</style>
""", unsafe_allow_html=True)



# Mudança da cor da barra lateral ====================================================================================

st.markdown("""
<style>

section[data-testid="stSidebar"] {
    background-color: #E6F2FF !important;  /* azul claro */
}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# ====================== BARRA LATERAL ======================
# ==========================================================

menu = st.sidebar.radio(
    "Navegação",
    ["Início", "Quem Somos", "Serviços", "Portfólio", "Contato"]
)


# Imagem de fundo do inicio ajeitar depois ==============================================================================================

import base64

file = "09_construtora_Talismaa/logo_talisma.png"

with open(file, "rb") as f:
    data = f.read()
encoded = base64.b64encode(data).decode()

st.markdown(f"""
<style>
.hero-section {{
    background-image: url("data:image/jpeg;base64,{encoded}");
    background-size: cover;
    background-position: center;
    height: 380px;
    border-radius: 12px;
}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.big-title-custom {
    font-size: 35px !important;   /* tamanho da fonte */
    font-weight: 900 !important;  /* deixa mais forte */
    color: #003F5C !important;    /* azul do seu tema */
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)



# ==========================================================================================================
# ======================== INÍCIO ==========================================================================
# ==========================================================================================================

if menu == "Início":

    st.markdown("""
    <div class="hero-section">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <div class="hero-title">CONSTRUTORA TALISMÃ</div>
            <div class="hero-subtitle">
                Excelência em infraestrutura, drenagem urbana e obras de arte.
            </div>
          
    </div>
    """, unsafe_allow_html=True)




    st.markdown('<p class="big-title-custom">Nossos Diferenciais</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""<div class="card">
        <h4>🏗️ Obras de Artes Especiais</h4>
        Construção de pontes, galerias e grandes estruturas.
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""<div class="card">
        <h4>🌧️ Drenagem Urbana</h4>
        Instalação de manilhas, valetas, dissipadores e redes pluviais.
        </div>""", unsafe_allow_html=True)

    with col3:
        st.markdown("""<div class="card">
        <h4>👷 Execução Profissional</h4>
        Equipes experientes e controle de qualidade rigoroso.
        </div>""", unsafe_allow_html=True)



# ==========================================================
# ======================= QUEM SOMOS ========================
# ==========================================================



elif menu == "Quem Somos":

    st.markdown('<p class="big-title-custom">Sobre a Construtora Talismã</p>', unsafe_allow_html=True)

    st.write("""
    A **Construtora Talismã** atua com excelência na execução de obras de infraestrutura, 
    drenagem urbana e obras de arte, combinando tecnologia, segurança e qualidade em todas as etapas.

    Nosso compromisso é entregar **soluções duráveis, eficientes e alinhadas às normas técnicas**, 
    atendendo obras públicas e privadas com responsabilidade e alto desempenho.
    """)

    st.markdown("### Missão")
    st.write("Promover soluções de engenharia capazes de transformar cidades com segurança e eficiência.")

    st.markdown("### Visão")
    st.write("Ser referência regional em infraestrutura e drenagem urbana.")

    st.markdown("### Valores")
    st.write("""
    - Compromisso com a qualidade  
    - Segurança em primeiro lugar  
    - Ética e transparência  
    - Responsabilidade socioambiental  
    - Engenharia baseada em excelência técnica  
    """)


# ==========================================================
# ======================= SERVIÇOS ==========================
# ==========================================================

elif menu == "Serviços":

    st.markdown('<p class="big-title-custom">Serviços</p>', unsafe_allow_html=True)

    st.write("### Obras de Arte Especiais")
    st.write("""
    - Pontes e pontilhões  
    - Galerias celulares  
    - Travessias estruturais  
    - Contenções e bueiros
    """)

    st.write("### Obras de Arte Correntes")
    st.write("""
    - Boca de lobo  
    - Guia/sarja reta e extravasora  
    - Meios-fios  
    - Caixas de ligação e PV  
    """)

    st.write("### Drenagem Urbana")
    st.write("""
    - Manilhas de concreto  
    - Redes pluviais  
    - Dissipadores  
    - Valetas, sarjetas e talvegues  
    """)


# ==========================================================
# ======================== PORTFÓLIO ========================
# ==========================================================

elif menu == "Portfólio":

    st.markdown('<p class="big-title-custom">Portfólio</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image("09_construtora_Talismaa\imagens_site\imagem01.jpg", None)
        st.write("**Obra 1 – Execução de drenagem**")

    with col2:
        st.image("09_construtora_Talismaa\imagens_site\imagem02.jpg", None)
        st.write("**Obra 2 – Galeria celular**")

    col3, col4 = st.columns(2)

    with col3:
        st.image("09_construtora_Talismaa\imagens_site\imagem03.jpg", None)
        st.write("**Obra 3 – Instalação de manilhas**")

    with col4:
        st.image("09_construtora_Talismaa\imagens_site\imagem04.jpg", None)
        st.write("**Obra 4 – Travessia estrutural**")


# ==========================================================
# ======================== CONTATO ==========================
# ==========================================================

elif menu == "Contato":

    st.markdown('<p class="big-title-custom" id="contato">Contato</p>', unsafe_allow_html=True)

    with st.form("form_contato"):
        nome = st.text_input("Nome")
        telefone = st.text_input("Telefone")
        mensagem = st.text_area("Mensagem")
        enviar = st.form_submit_button("Enviar")

        if enviar:
            if nome and mensagem:
                texto = f"""
                Solicitação pelo site:

                Nome: {nome}
                Telefone: {telefone}
                Mensagem: {mensagem}
                """

                texto = texto.replace("\n", "%0A")  # Quebra de linha no WhatsApp

                link = f"https://wa.me/5564984266591?text={texto}"

                st.success("Mensagem enviada! Clique abaixo para enviar pelo WhatsApp:")
                st.markdown(f"<a href='{link}' target='_blank' class='hero-button'>Enviar pelo WhatsApp</a>", unsafe_allow_html=True)
            else:
                st.error("Por favor, preencha pelo menos nome e mensagem.")


    st.write("---")
    st.write("📱 **WhatsApp:** (64) 9 8426-6591")
    st.write("📧 **E-mail:** fernandomar.borges@gmail.com")
    # st.write("📞 **Contato 2:** (62) 9 8569-1599")
    st.write("📍 **Endereço:** Avenida Anhanguera, 1201 – Vila União, Catalão – GO")


# ==========================================================
# ========================== FOOTER =========================
# ==========================================================

st.markdown("""
<div class="footer">
© 2025 Construtora Talismã — Todos os direitos reservados.
</div>
""", unsafe_allow_html=True)


# ==========================================================
# =============== BOTÃO WHATSAPP FLUTUANTE =================
# ==========================================================

st.markdown("""
<a class="whatsapp-btn" href="https://wa.me/5564984266591" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="32px">
</a>
""", unsafe_allow_html=True)


# ==========================================================
# =============== BOTÃO WHATSAPP FLUTUANTE =================
# ==========================================================

st.markdown("""
<a class="instagram-btn" href="https://www.instagram.com/const_talisma" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png">
</a>
""", unsafe_allow_html=True)

