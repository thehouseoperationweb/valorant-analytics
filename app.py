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
    /* VALORANT公式キービジュアルを背景にした圧倒的ヒーローヘッダー */
    .valorant-hero-header {
        position: relative;
        width: 100%;
        height: 240px;
        background: linear-gradient(90deg, rgba(8,13,18,0.95) 0%, rgba(8,13,18,0.7) 50%, rgba(255,70,85,0.3) 100%),
                    url('https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=1600&q=80') center/cover no-repeat;
        border: 1px solid #1e2d3d;
        border-left: 5px solid #ff4655;
        border-radius: 4px;
        padding: 30px 40px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 8px 32px rgba(0,0,0,0.7);
    }
    .hero-title-area {
        display: flex;
        align-items: center;
        gap: 24px;
    }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 900;
        letter-spacing: 3px;
        color: #ffffff;
        margin: 0;
        font-family: 'Impact', 'Trebuchet MS', sans-serif !important;
        text-transform: uppercase;
        text-shadow: 0 2px 10px rgba(0,0,0,0.8);
    }
    .hero-sub {
        font-size: 0.88rem;
        color: #8b9bb4;
        margin-top: 6px;
        letter-spacing: 1.5px;
        font-weight: 700;
        text-transform: uppercase;
    }

    /* ターゲットバッジ */
    .target-badge {
        background: #090f16;
        border: 1px solid #1e2d3d;
        border-left: 3px solid #2b7fff;
        padding: 8px 16px;
        border-radius: 2px;
        display: inline-block;
        font-size: 0.85rem;
        color: #8b9bb4;
        margin-bottom: 25px;
        letter-spacing: 1.5px;
    }
    .target-badge strong {
        color: #ffffff;
        font-size: 1.0rem;
    }

    /* メトリックカード（白抜き対応） */
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

    /* セクションタイトル */
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

    /* カスタムバー表示 */
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
# ヘッダーエリア（QT DIG ロゴ ＆ キービジュアル背景）
# ---------------------------------------------------------
st.markdown("""
<div class="valorant-hero-header">
    <div class="hero-title-area">
        <svg width="60" height="60" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0 2px 8px rgba(0,0,0,0.8));">
            <path d="M5 10H38V30H22V70H38V90H5V10Z" fill="#FF4655"/>
            <path d="M48 10H75V40H62V30H62V70H75V60H90V90H48V10Z" fill="#FF4655"/>
            <path d="M62 42H85V58H62V42Z" fill="#FF4655"/>
        </
