import streamlit as st
import pandas as pd

# ページ基本設定
st.set_page_config(
    page_title="QT DIG VALORANT Analytics",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# パスワード保護 (安全な認証処理)
# ---------------------------------------------------------
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #080d12 !important;
        color: #ffffff !important;
        font-family: 'Trebuchet MS', sans-serif !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔒 QT DIG VALORANT Analytics - Security")

user_input = st.text_input("アクセスパスワードを入力", type="password", key="security_password_input")
normalized_input = user_input.strip().upper().replace(" ", "_")

CORRECT_PASSWORD = "AIM_FOR_NUMBER_1"

if normalized_input != CORRECT_PASSWORD:
    if user_input != "":
        st.error("❌ パスワードが違います")
    st.warning("🔒 チーム専用アクセス制限がかかっています。パスワードを入力してください。")
    st.info("※正しいパスワードを入力すると、ダッシュボードが表示されます。")
    st.stop()

# ---------------------------------------------------------
# 認証完了後のプロフェッショナルUI定義
# ---------------------------------------------------------
st.markdown("""
<style>
    .valorant-top-banner {
        width: 100%;
        height: 380px;
        background: url('https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=1600&q=80') center/cover no-repeat;
        border: 1px solid #1e2d3d;
        border-radius: 4px;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.8);
    }
    .title-flex-container {
        display: flex;
        align-items: center;
        gap: 18px;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    .hero-title {
        font-size: 2.6rem;
        font-weight: 900;
        letter-spacing: 3px;
        color: #ffffff;
        margin: 0;
        font-family: 'Impact', 'Trebuchet MS', sans-serif !important;
        text-transform: uppercase;
    }
    .hero-sub {
        font-size: 0.88rem;
        color: #ff4655;
        margin-top: 4px;
        letter-spacing: 2px;
        font-weight: 800;
        text-transform: uppercase;
    }
    .target-badge {
        background: #090f16;
        border: 1px solid #1e2d3d;
        border-left: 3px solid #2b7fff;
        padding: 8px 16px;
        border-radius: 2px;
        display: inline-block;
        font-size: 0.85rem;
        color: #8b9bb4;
        margin-top: 15px;
        margin-bottom: 25px;
        letter-spacing: 1.5px;
    }
    .target-badge strong {
        color: #ffffff;
        font-size: 1.0rem;
    }
    .kpi-card {
        background: #090f16;
        border: 1px solid #1e2d3d;
        border-radius: 4px;
        padding: 18px 22px;
        height: 100%;
    }
    .kpi-card.red-border { border-left: 3px solid #ff4655; }
    .kpi-card.blue-border { border-left: 3px solid #2b7fff; }
    .kpi-label {
        font-size: 0.85rem;
        color: #8b9bb4;
        margin-bottom: 8px;
        font-weight: 700;
    }
    .kpi-value {
        font-size: 2.8rem;
        font-weight: 900;
        color: #ffffff !important;
        font-family: 'Impact', 'Trebuchet MS', sans-serif !important;
        line-height: 1.0;
        letter-spacing: 1px;
    }
    .kpi-delta {
        font-size: 0.82rem;
        margin-top: 10px;
        font-weight: 700;
    }
    .kpi-delta.green { color: #00f0ff; }
    .kpi-delta.red { color: #ff4655; }
    div[data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-family: 'Impact', 'Trebuchet MS', sans-serif !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #8b9bb4 !important;
    }
    .section-tag {
        color: #ff4655;
        font-size: 0.78rem;
        font-weight: 900;
        letter-spacing: 2px;
        margin-top: 30px;
        margin-bottom: 4px;
    }
    .section-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 15px;
    }
    .custom-bar-container {
        background: #090f16;
        border: 1px solid #1e2d3d;
        padding: 22px 26px;
        border-radius: 4px;
        margin-bottom: 25px;
    }
    .bar-row { margin-bottom: 18px; }
    .bar-row:last-child { margin-bottom: 0; }
    .bar-label-container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 6px;
        font-size: 0.92rem;
        font-weight: 700;
    }
    .bar-track {
        background: #152230;
        height: 24px;
        border-radius: 3px;
        overflow: hidden;
    }
    .bar-fill-red { background: linear-gradient(90deg, #ff4655 0%, #ff6b78 100%); height: 100%; border-radius: 3px; }
    .bar-fill-blue { background: linear-gradient(90deg, #2b7fff 0%, #5299ff 100%); height: 100%; border-radius: 3px; }
    .bar-fill-gray { background: linear-gradient(90deg, #4a5d73 0%, #70849c 100%); height: 100%; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 1. 一番上にヘッダー画像をそのまま配置
# ---------------------------------------------------------
st.markdown('<div class="valorant-top-banner"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. タイトルの前にQT DIGのロゴ（背景透過）を配置
# ---------------------------------------------------------
st.markdown("""
<div class="title-flex-container">
    <svg width="55" height="55" viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0 2px 6px rgba(0,0,0,0.8));">
        <path d="M40 20H180V120H110V380H180V480H40V20Z" fill="#FF4655"/>
        <path d="M220 20H360V180H290V120H290V380H360V320H460V480H220V20Z" fill="#FF4655"/>
        <path d="M290 200H420V300H290V200Z" fill="#FF4655"/>
    </svg>
    <div>
        <div class="hero-title">QT DIG ANALYTICS</div>
        <div class="hero-sub">VALORANT OFFICIAL MATCH ANALYSIS & PERFORMANCE PROTOTYPE</div>
    </div>
</div>
""", unsafe_allow_html=True)

# サイドバー設定
st.sidebar.header("プレイヤー設定")
riot_id = st.sidebar.text_input("Riot ID (名前)", value="Hust is so VLY")
tag = st.sidebar.text_input("Tag (タグ)", value="Bang")
region = st.sidebar.selectbox("リージョン", ["ap", "na", "eu", "kr"], index=0)

if st.sidebar.button("データを取得・更新"):
    st.cache_data.clear()

# ターゲット表示
st.markdown(f"""
<div class="target-badge">
    ANALYSIS TARGET &nbsp;&nbsp;<strong>{riot_id}#{tag}</strong> &nbsp;·&nbsp; {region.upper()}
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# KPI概要 (3列カード)
# ---------------------------------------------------------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="kpi-card red-border">
        <div class="kpi-label">ファーストキル (FK) 時 勝率</div>
        <div class="kpi-value">78.3%</div>
        <div class="kpi-delta green">+27.1% vs 通常展開</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="kpi-card blue-border">
        <div class="kpi-label">初落ち (FD) 時 カバー率</div>
        <div class="kpi-value">62.2%</div>
        <div class="kpi-delta red">目標 70% まで +7.8pt</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="kpi-card
