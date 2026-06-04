import streamlit as st
from recommender import recommend, new_df

st.set_page_config(
    page_title="CineMatch",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Inter:wght@400;600;800;900&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(0, 212, 255, 0.26), transparent 24%),
        radial-gradient(circle at 90% 20%, rgba(168, 85, 247, 0.28), transparent 26%),
        radial-gradient(circle at 50% 100%, rgba(236, 72, 153, 0.16), transparent 32%),
        linear-gradient(135deg, #020617 0%, #030712 45%, #090014 100%);
    color: white;
}

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(255,255,255,0.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.035) 1px, transparent 1px);
    background-size: 55px 55px;
    mask-image: radial-gradient(circle at center, black, transparent 78%);
    pointer-events: none;
}

.block-container {
    max-width: 1280px;
    padding-top: 2.2rem;
}

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #94a3b8;
    letter-spacing: 4px;
    font-size: 12px;
    margin-bottom: 70px;
}

.logo {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 30px;
    font-weight: 900;
    color: white;
    letter-spacing: 8px;
}

.logo span {
    color: #22d3ee;
    text-shadow: 0 0 28px rgba(34,211,238,0.95);
}

.hero {
    text-align: center;
}

.badge {
    display: inline-block;
    padding: 13px 30px;
    border-radius: 999px;
    color: #e0f2fe;
    letter-spacing: 4px;
    font-size: 12px;
    font-weight: 800;
    background: rgba(15,23,42,0.62);
    border: 1px solid rgba(34,211,238,0.38);
    box-shadow:
        0 0 45px rgba(34,211,238,0.18),
        inset 0 1px 0 rgba(255,255,255,0.12);
    backdrop-filter: blur(22px);
    margin-bottom: 32px;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(82px, 10vw, 155px);
    line-height: 0.85;
    font-weight: 900;
    letter-spacing: -7px;
    margin-bottom: 34px;
    background: linear-gradient(90deg, #22d3ee, #38bdf8, #a855f7, #ec4899, #22d3ee);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientShift 7s ease infinite;
    filter: drop-shadow(0 0 38px rgba(34,211,238,0.2));
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.subtitle {
    color: #cbd5e1;
    font-size: 24px;
    max-width: 920px;
    margin: auto;
    line-height: 1.65;
}

.steps {
    display: flex;
    justify-content: center;
    gap: 76px;
    color: #94a3b8;
    letter-spacing: 5px;
    margin-top: 58px;
    margin-bottom: 56px;
    font-size: 12px;
    font-weight: 800;
}

.panel {
    max-width: 1100px;
    margin: auto;
    padding: 34px;
    border-radius: 30px;
    background:
        linear-gradient(135deg, rgba(15,23,42,0.88), rgba(88,28,135,0.35)),
        rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.16);
    box-shadow:
        0 0 100px rgba(168,85,247,0.25),
        0 30px 100px rgba(0,0,0,0.45),
        inset 0 1px 0 rgba(255,255,255,0.14);
    backdrop-filter: blur(28px);
}

.panel-head {
    display: flex;
    justify-content: space-between;
    color: #22d3ee;
    letter-spacing: 5px;
    font-weight: 900;
    margin-bottom: 24px;
    font-size: 12px;
}

.stSelectbox {
    max-width: 1100px;
    margin: auto;
}

div[data-baseweb="select"] > div {
    background: rgba(2, 6, 23, 0.92) !important;
    border: 1px solid rgba(148,163,184,0.22) !important;
    border-radius: 22px !important;
    min-height: 68px;
    color: white !important;
    box-shadow:
        inset 0 0 24px rgba(0,0,0,0.55),
        0 0 35px rgba(34,211,238,0.08);
}

.stSelectbox label {
    color: #94a3b8 !important;
    letter-spacing: 4px;
    font-weight: 900;
    font-size: 12px;
}

.stButton {
    text-align: center;
}

.stButton button {
    width: 430px;
    height: 76px;
    border-radius: 24px;
    border: none;
    background: linear-gradient(90deg, #22d3ee, #38bdf8, #a855f7);
    color: #020617;
    font-weight: 1000;
    font-size: 18px;
    letter-spacing: 5px;
    box-shadow:
        0 0 55px rgba(34,211,238,0.32),
        0 18px 60px rgba(168,85,247,0.2);
    transition: all 0.25s ease;
    margin-top: 14px;
}

.stButton button:hover {
    transform: translateY(-4px) scale(1.01);
    filter: brightness(1.16);
    box-shadow:
        0 0 80px rgba(34,211,238,0.42),
        0 0 95px rgba(168,85,247,0.35);
}

.results-title {
    margin-top: 95px;
    margin-bottom: 38px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(42px, 5.8vw, 76px);
    line-height: 1;
    font-weight: 900;
    color: white;
    letter-spacing: -3px;
}

.results-title span {
    background: linear-gradient(90deg, #22d3ee, #38bdf8, #a855f7, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.card {
    height: 285px;
    padding: 32px;
    border-radius: 32px;
    background:
        radial-gradient(circle at top right, rgba(34,211,238,0.22), transparent 32%),
        linear-gradient(135deg, rgba(15,23,42,0.84), rgba(88,28,135,0.35));
    border: 1px solid rgba(34,211,238,0.28);
    margin-bottom: 30px;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(22px);
    box-shadow:
        0 28px 90px rgba(0,0,0,0.42),
        inset 0 1px 0 rgba(255,255,255,0.12);
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-10px) scale(1.01);
    border-color: rgba(168,85,247,0.85);
    box-shadow:
        0 35px 110px rgba(168,85,247,0.26),
        0 0 70px rgba(34,211,238,0.20);
}

.card::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(120deg, transparent, rgba(255,255,255,0.10), transparent);
    transform: translateX(-110%);
    transition: 0.75s;
}

.card:hover::before {
    transform: translateX(110%);
}

.rank {
    color: #22d3ee;
    letter-spacing: 5px;
    font-weight: 1000;
    font-size: 12px;
}

.movie-title {
    position: absolute;
    bottom: 48px;
    left: 32px;
    right: 32px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(26px, 3vw, 38px);
    line-height: 1.02;
    font-weight: 900;
    color: white;
    z-index: 2;
}

.match {
    position: absolute;
    bottom: 22px;
    left: 32px;
    color: #94a3b8;
    letter-spacing: 4px;
    font-size: 12px;
    font-weight: 800;
}

.big-number {
    position: absolute;
    right: 18px;
    bottom: -64px;
    font-size: 205px;
    font-weight: 1000;
    color: rgba(255,255,255,0.045);
}

.footer {
    margin-top: 90px;
    margin-bottom: 20px;
    color: #94a3b8;
    letter-spacing: 5px;
    font-size: 12px;
    text-align: center;
    font-weight: 800;
}

@media (max-width: 768px) {
    .topbar {
        flex-direction: column;
        gap: 16px;
        text-align: center;
    }

    .steps {
        flex-direction: column;
        gap: 18px;
    }

    .panel {
        padding: 28px;
    }

    .stButton button {
        width: 100%;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
    <div class="logo">CINE<span>/</span>MATCH<span>.</span></div>
    <div>4800+ TITLES INDEXED</div>
    <div>COUNTVECTORIZER · COSINE</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="badge">✦ CONTENT-BASED ML RECOMMENDER</div>
    <div class="hero-title">CINEMATCH</div>
    <div class="subtitle">
        Discover movies similar to your favorites using a content-based recommendation engine powered by CountVectorizer and Cosine Similarity.
    </div>
    <div class="steps">
        <div>01 · PICK</div>
        <div>02 · VECTORIZE</div>
        <div>03 · MATCH</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="panel">
    <div class="panel-head">
        <div>STEP · 01</div>
        <div>SELECT MOVIE</div>
    </div>
""", unsafe_allow_html=True)

movie_list = new_df["title"].values

selected_movie = st.selectbox(
    "SEARCH MOVIE",
    movie_list
)

button = st.button("GET RECOMMENDATIONS →")

st.markdown("</div>", unsafe_allow_html=True)

if button:
    recommendations = recommend(selected_movie)

    st.markdown(
        f"""
        <div class="results-title">
            BECAUSE YOU PICKED <br>
            <span>"{selected_movie.upper()}"</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    for index, movie in enumerate(recommendations, start=1):
        card_html = f"""
        <div class="card">
            <div class="rank">RANK · {index:02}</div>
            <div class="movie-title">{movie.upper()}</div>
            <div class="match">COSINE MATCH</div>
            <div class="big-number">{index:02}</div>
        </div>
        """

        if index % 2 == 1:
            with col1:
                st.markdown(card_html, unsafe_allow_html=True)
        else:
            with col2:
                st.markdown(card_html, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    CINEMATCH · ML POWERED · PYTHON · SCIKIT-LEARN · COUNTVECTORIZER · COSINE SIMILARITY
</div>
""", unsafe_allow_html=True)