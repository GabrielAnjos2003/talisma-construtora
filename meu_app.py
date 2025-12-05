import streamlit as st
import base64

# ---------- CONFIGURAÇÕES DO SITE ----------
st.set_page_config(
    page_title="Construtora Talismã ",
    page_icon="💎",
    layout="wide"
)

# ---------- OCULTAR SIDEBAR ----------
st.markdown("""
<style>
section[data-testid="stSidebar"] {display: none;}
div[data-testid="collapsedControl"] {display: none;}
</style>
""", unsafe_allow_html=True)


# ---------- MENU SUPERIOR FIXO ----------
st.markdown("""
<style>

.top-menu {
    width: 100%;
    background: rgba(0,63,92,0.85);   /* 🔥 fundo translúcido */
    backdrop-filter: blur(6px);       /* 🔥 efeito vidro */
    padding: 18px 0;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 10000;
    display: flex;
    justify-content: center;
    gap: 50px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.3);
}

.top-menu a {
    color: white;
    font-size: 22px;
    font-weight: 700;
    text-decoration: none;
}

.top-menu a:hover {
    color: #FFA600;
    transition: 0.3s;
}

body {
    padding-top: 90px !important;
}

</style>

<div class="top-menu">
    <a href="#inicio">Início</a>
    <a href="#quem">Quem Somos</a>
    <a href="#servicos">Serviços</a>
    <a href="#portfolio">Portfólio</a>
    <a href="#contato">Contato</a>
</div>
""", unsafe_allow_html=True)

# ---------- FUNDO GRADIENTE ----------
st.markdown("""
<style>
html, body, [class*="block-container"] {
    background: linear-gradient(135deg, #4184e1 0%, #FFFFFF 100%) !important;   
    background-attachment: fixed;
}

.main { background: none; }
</style>
""", unsafe_allow_html=True)

# ---------- ESTILOS GERAIS ----------
st.markdown("""
<style>

body {
    font-family: 'Segoe UI', sans-serif;
}

/* 🔥 AUMENTAR APENAS TEXTOS COMUNS */
p, li, div.stMarkdown, .markdown-text-container {
    font-size: 22px !important;
    line-height: 1.55 !important;
}

/* HERO */
.hero-section {
    position: relative;
    background-size: cover;
    background-position: center;
    height: 520px;
    border-radius: 12px;
    margin-bottom: 40px;
}

.hero-overlay {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.25) 100%);
}

.hero-content {
    position: relative;
    z-index: 2;
    padding: 60px;
    color: white;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.7);
    animation: fadeIn 1.2s ease-in-out;
}

@keyframes fadeIn {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}            

.hero-title { font-size: 80px; font-weight: bold; }
.hero-subtitle { font-size: 25px; margin-top: 10px; }

.hero-button {
    display: inline-block;
    padding: 12px 28px;
    background: #FFA600;
    border-radius: 8px;
    font-size: 20px;
    font-weight: bold;
    color: black;
    text-decoration: none;
}

.big-title-custom {
    font-size: 35px !important;
    font-weight: 900 !important;
    color: #003F5C !important;
    margin-top: 30px;
}

.card {
    background: #F5F5F5;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 20px;
    transition: 0.3s;
}
.card:hover { transform: translateY(-4px); background: #e9ecef; }

.footer {
    text-align: center;
    padding: 25px;
    margin-top: 50px;
    color: #777;
    border-top: 1px solid #ddd;
}

/* BOTÕES FLUTUANTES */
.whatsapp-btn, .instagram-btn {
    position: fixed;
    bottom: 25px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 2px 2px 12px rgba(0,0,0,0.3);
    z-index: 9999;
}
.whatsapp-btn { right: 25px; background: #25D366; }
.instagram-btn { right: 95px; background: #E4405F; }

.whatsapp-btn img, .instagram-btn img {
    width: 35px; height: auto;
}

</style>
""", unsafe_allow_html=True)

# ---------- IMAGEM DO HERO ----------
file = "talisma-construtora/imagens_site/imagem03.jpg"
with open(file, "rb") as f:
    encoded = base64.b64encode(f.read()).decode()

st.markdown(f"""
<style>
.hero-section {{
    background-image: url("data:image/jpeg;base64,{encoded}");
}}
</style>
""", unsafe_allow_html=True)

# ======================================================================
# =============================== INÍCIO ================================
# ======================================================================

st.markdown("<h1 id='inicio'></h1>", unsafe_allow_html=True)



st.markdown("""
<div class="hero-section">
    <div class="hero-overlay"></div>
    <div class="hero-content">
        <div class="hero-title">Construtora Talismã 💎</div>
        <div class="hero-subtitle">Excelência em infraestrutura, drenagem urbana e obras de arte.</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title-custom">Nossos Diferenciais</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""<div class="card"><h4>🏗️ Obras de Artes Especiais</h4>Construção de pontes, galerias e estruturas.</div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="card"><h4>🌧️ Drenagem Urbana</h4>Instalação de manilhas, valetas e dissipadores.</div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="card"><h4>👷 Execução Profissional</h4>Equipes experientes e controle rigoroso.</div>""", unsafe_allow_html=True)

# ======================================================================
# =========================== QUEM SOMOS ===============================
# ======================================================================

st.markdown("<h1 id='quem'></h1>", unsafe_allow_html=True)
st.markdown('<p class="big-title-custom">Sobre a Construtora Talismã</p>', unsafe_allow_html=True)

st.write("""
A **Construtora Talismã** atua com excelência na execução de obras de infraestrutura,
drenagem urbana e obras de arte, entregando soluções eficientes e de alta qualidade.
""")

st.markdown("""
<style>
.bloco-info {
    background: #f8f9fa;
    padding: 25px;
    border-radius: 12px;
    margin-bottom: 25px;
    border-left: 6px solid #003F5C;
}

.bloco-titulo {
    font-size: 26px;
    font-weight: 800;
    color: #003F5C;
    margin-bottom: 10px;
}

.bloco-texto {
    font-size: 20px;
    line-height: 1.55;
}
</style>
""", unsafe_allow_html=True)

# ---------- MISSÃO ----------
st.markdown("""
<div class="bloco-info">
    <div class="bloco-titulo">Missão</div>
    <div class="bloco-texto">
        Transformar cidades por meio de soluções de engenharia seguras e eficientes.
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- VISÃO ----------
st.markdown("""
<div class="bloco-info">
    <div class="bloco-titulo">Visão</div>
    <div class="bloco-texto">
        Ser referência regional em obras de infraestrutura.
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- VALORES ----------
st.markdown("""
<div class="bloco-info">
    <div class="bloco-titulo">Valores</div>
    <div class="bloco-texto">
        • Qualidade<br>
        • Segurança<br>
        • Ética<br>
        • Responsabilidade socioambiental<br>
        • Excelência técnica
    </div>
</div>
""", unsafe_allow_html=True)

# ======================================================================
# ===================== QUALIDADE E NÚMEROS =============================
# ======================================================================

st.markdown("<h1 id='numeros'></h1>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; margin-top: 40px;'>
    <h1 style="color:#003F5C; font-size:40px; font-weight:900;">
        Qualidade e credibilidade <span style="color:#d11f3e;">comprovadas em números.</span>
    </h1>

""", unsafe_allow_html=True)

st.markdown("""
<div class="bloco-info">
    <div class="bloco-titulo">Nossa História</div>
    <div class="bloco-texto">
        São quatro décadas de dedicação, pensando e agindo com os olhos no futuro para transformar
        a vida das pessoas e realizar sonhos. Muito além dos números, nossa maior conquista é a
        satisfação dos nossos clientes.
    </div>
</div>
""", unsafe_allow_html=True)



# ---------------------------- CARTÕES ------------------------------

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div style="
        background:white; padding:25px; border-radius:12px; text-align:center;
        box-shadow:0px 4px 10px rgba(0,0,0,0.15);
    ">
        <img src="https://cdn-icons-png.flaticon.com/512/709/709790.png"
             width="70">
        <h3 style="color:#d11f3e; font-size:34px;">43 anos</h3>
        <p style="font-size:18px;">realizando sonhos</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background:white; padding:25px; border-radius:12px; text-align:center;
        box-shadow:0px 4px 10px rgba(0,0,0,0.15);
    ">
        <img src="https://cdn-icons-png.flaticon.com/512/1828/1828673.png"
             width="70">
        <h3 style="color:#d11f3e; font-size:34px;">25 mil</h3>
        <p style="font-size:18px;">lares entregues</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background:white; padding:25px; border-radius:12px; text-align:center;
        box-shadow:0px 4px 10px rgba(0,0,0,0.15);
    ">
        <img src="https://cdn-icons-png.flaticon.com/512/854/854866.png"
             width="70">
        <h3 style="color:#d11f3e; font-size:34px;">5 estados</h3>
        <p style="font-size:18px;">presença nacional</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="
        background:white; padding:25px; border-radius:12px; text-align:center;
        box-shadow:0px 4px 10px rgba(0,0,0,0.15);
    ">
        <img src="https://cdn-icons-png.flaticon.com/512/1828/1828884.png"
             width="70">
        <h3 style="color:#d11f3e; font-size:34px;">1 milhão</h3>
        <p style="font-size:18px;">m² construídos</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div style="
        background:white; padding:25px; border-radius:12px; text-align:center;
        box-shadow:0px 4px 10px rgba(0,0,0,0.15);
    ">
        <img src="https://cdn-icons-png.flaticon.com/512/709/709722.png"
             width="70">
        <h3 style="color:#d11f3e; font-size:34px;">3 mil</h3>
        <p style="font-size:18px;">colaboradores</p>
    </div>
    """, unsafe_allow_html=True)



# ======================================================================
# ============================ SERVIÇOS ================================
# ======================================================================

st.markdown("<h1 id='servicos'></h1>", unsafe_allow_html=True)
st.markdown('<p class="big-title-custom">Serviços</p>', unsafe_allow_html=True)

# ---------- CSS atualizado ----------
st.markdown("""
<style>
.servico-card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
    transition: 0.3s;
    width: 100%;
}

.servico-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 6px 15px rgba(0,0,0,0.25);
}

.servico-icon {
    width: 70px;
    display: block;
    margin: 0 auto 15px auto;
}

.servico-title {
    font-size: 26px;
    font-weight: 900;
    color: #003F5C;
    text-align: center;
    margin-bottom: 12px;
}

/* 🔥 Alinha itens à esquerda */
.servico-lista {
    font-size: 19px;
    line-height: 1.55;
    text-align: left;
    margin-left: 20%;
}

.espaco-linha {
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)


# ------------------------ PRIMEIRA LINHA ------------------------------

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="servico-card">
        <img class="servico-icon" src="https://cdn-icons-png.flaticon.com/512/709/709790.png">
        <div class="servico-title">Obras de Arte Especiais</div>
        <div class="servico-lista">
            • Pontes<br>
            • Galerias Celulares<br>
            • Travessias Estruturais<br>
            • Contenções e Bueiros
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="servico-card">
        <img class="servico-icon" src="https://cdn-icons-png.flaticon.com/512/854/854866.png">
        <div class="servico-title">Obras de Arte Correntes</div>
        <div class="servico-lista">
            • Boca de Lobo<br>
            • Guias e Sarjetas<br>
            • Meios-fios<br>
            • Caixas de Ligação e PV
        </div>
    </div>
    """, unsafe_allow_html=True)


# ------------------------ ESPAÇO ENTRE LINHAS ------------------------------
st.markdown("<div class='espaco-linha'></div>", unsafe_allow_html=True)


# ------------------------ SEGUNDA LINHA ------------------------------

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="servico-card">
        <img class="servico-icon" src="https://cdn-icons-png.flaticon.com/512/1828/1828673.png">
        <div class="servico-title">Drenagem Urbana</div>
        <div class="servico-lista">
            • Manilhas de Concreto<br>
            • Redes Pluviais<br>
            • Dissipadores<br>
            • Valetas e Sarjetas
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="servico-card">
        <img class="servico-icon" src="https://cdn-icons-png.flaticon.com/512/2950/2950711.png">
        <div class="servico-title">Construção Civil</div>
        <div class="servico-lista">
            • Edificações<br>
            • Reformas Estruturais<br>
            • Recuperação de Obras<br>
            • Execução Completa de Projetos
        </div>
    </div>
    """, unsafe_allow_html=True)

# ======================================================================
# ============================ PORTFÓLIO ===============================
# ======================================================================

st.markdown("<h1 id='portfolio'></h1>", unsafe_allow_html=True)
st.markdown('<p class="big-title-custom">Portfólio</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image("talisma-construtora\imagens_site\imagem01.jpg")
    st.write("**Obra 1 – Execução de drenagem**")
with col2:
    st.image("talisma-construtora\imagens_site\imagem02.jpg")
    st.write("**Obra 2 – Galeria celular**")

col3, col4 = st.columns(2)
with col3:
    st.image("talisma-construtora\imagens_site\imagem03.jpg")
    st.write("**Obra 3 – Manilhas**")
with col4:
    st.image("talisma-construtora\imagens_site\imagem04.jpg")
    st.write("**Obra 4 – Travessia estrutural**")

# ======================================================================
# ============================ CONTATO ================================
# ======================================================================

st.markdown("<h1 id='contato'></h1>", unsafe_allow_html=True)
st.markdown('<p class="big-title-custom">Contato</p>', unsafe_allow_html=True)

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
            """.replace("\n", "%0A")

            link = f"https://wa.me/5564984266591?text={texto}"

            st.success("Clique abaixo para enviar pelo WhatsApp:")
            st.markdown(f"<a href='{link}' target='_blank' class='hero-button'>Enviar pelo WhatsApp</a>", unsafe_allow_html=True)
        else:
            st.error("Preencha nome e mensagem.")

st.write("---")
st.write("📱 **WhatsApp:** (64) 9 8426-6591")
st.write("📧 **E-mail:** fernandomar.borges@gmail.com")
st.write("📍 **Endereço:** Avenida Anhanguera, 1201 – Vila União, Catalão – GO")

# ======================================================================
# ============================= FOOTER ================================
# ======================================================================

st.markdown("""
<div class="footer">
© 2025 Construtora Talismã — Todos os direitos reservados.
</div>
""", unsafe_allow_html=True)

# ======================================================================
# ======================= BOTÕES FLUTUANTES ===========================
# ======================================================================

st.markdown("""
<a class="whatsapp-btn" href="https://wa.me/5564984266591" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg">
</a>

<a class="instagram-btn" href="https://www.instagram.com/const_talisma" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png">
</a>
""", unsafe_allow_html=True)
