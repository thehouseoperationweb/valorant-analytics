import streamlit as st
import pandas as pd
import os

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
    .title-flex-container {
        display: flex;
        align-items: center;
        gap: 20px;
        margin-top: 15px;
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
# 1. 1枚目の画像（VALORANT公式キービジュアル）をヘッダーとしてそのまま配置
# ---------------------------------------------------------
header_img_path = "header.jpg"  # またはお持ちのファイル名
if os.path.exists(header_img_path):
    st.image(header_img_path, use_container_width=True)
else:
    # フォールバックとして指定の画像をそのまま表示
    st.image("https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=1600&q=80", use_container_width=True)

# ---------------------------------------------------------
# 2. 2枚目の画像（QT DIGロゴ）をタイトルの左側に配置
# ---------------------------------------------------------
col_logo, col_title = st.columns([0.10, 0.90])

logo_img_path = "logo.png"  # またはお持ちのロゴファイル名
with col_logo:
    if os.path.exists(logo_img_path):
        st.image(logo_img_path, width=70)
    else:
        st.image("https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=200&q=80", width=70)

with col_title:
    st.markdown("""
    <div>
        <div class="hero-title" style="line-height: 1.1;">QT DIG ANALYTICS</div>
        <div class="hero-sub">VALORANT OFFICIAL MATCH ANALYSIS & PERFORMANCE PROTOTYPE</div>
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
# 3. KPI概要 (3列カード)
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
    <div class="kpi-card red-border">
        <div class="kpi-label">直近20試合 勝率</div>
        <div class="kpi-value">65.0%</div>
        <div class="kpi-delta green">800RR 到達ペース</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------------------------------------------------
# 4. SECTION 01 : FK / FD 相関分析
# ---------------------------------------------------------
st.markdown("""
<div class="section-tag">SECTION 01 / OPENING DUEL</div>
<div class="section-title">ファーストキル (FK) / ファーストデス (FD) 発生時のラウンド勝率</div>

<div class="custom-bar-container">
    <div class="bar-row">
        <div class="bar-label-container">
            <span style="color: #ff4655;">ファーストキル (FK) 獲得時</span>
            <span style="color: #ffffff; font-weight: 800;">78.3%</span>
        </div>
        <div class="bar-track">
            <div class="bar-fill-red" style="width: 78.3%;"></div>
        </div>
    </div>
    <div class="bar-row">
        <div class="bar-label-container">
            <span style="color: #8b9bb4;">通常展開 (FK/FDなし)</span>
            <span style="color: #ffffff; font-weight: 800;">51.2%</span>
        </div>
        <div class="bar-track">
            <div class="bar-fill-gray" style="width: 51.2%;"></div>
        </div>
    </div>
    <div class="bar-row">
        <div class="bar-label-container">
            <span style="color: #2b7fff;">ファーストデス (FD) 発生時</span>
            <span style="color: #ffffff; font-weight: 800;">24.4%</span>
        </div>
        <div class="bar-track">
            <div class="bar-fill-blue" style="width: 24.4%;"></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ---------------------------------------------------------
# 5. SECTION 02 : アビリティ効率分析
# ---------------------------------------------------------
st.markdown("""
<div class="section-tag">SECTION 02 / ABILITY UTILIZATION</div>
<div class="section-title">アビリティ使用効率とラウンド獲得貢献</div>
""", unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    st.write("▼ **スキル使用後の交戦勝率**")
    df_ability = pd.DataFrame({
        'アビリティ種別': ['メインスキル (C/Q)', 'シグネチャー (E)', 'アルティメット (X)'],
        '発動時ラウンド勝率 (%)': [58.5, 64.2, 81.0],
        '平均ダメージ貢献': [35.0, 52.0, 110.0]
    })
    st.dataframe(df_ability, use_container_width=True)

with col_b:
    st.write("▼ **サポートアビリティ / フラッシュ有効率**")
    st.metric("味方カバーへの貢献率", "71.4%", "目標 75%")
    st.metric("有効フラッシュ率 (敵目を奪う)", "42.8%", "改善推奨")

st.write("---")

# ---------------------------------------------------------
# 6. SECTION 03 : マネー別戦術分析
# ---------------------------------------------------------
st.markdown("""
<div class="section-tag">SECTION 03 / ECONOMY & TACTICS</div>
<div class="section-title">相手装備（マネー状況）別の交戦勝率分析</div>
""", unsafe_allow_html=True)

df_econ = pd.DataFrame({
    '自軍装備状況': ['フルバイ (4300+)', 'フルバイ (4300+)', 'ハーフバイ (2000-3000)', 'エコ / 節約 (0-2000)'],
    '敵軍装備状況': ['フルバイ (重装・主力銃)', 'エコ / 相手弱武装', 'フルバイ (強武装)', 'エコ / 同等武装'],
    '交戦ラウンド勝率 (%)': [55.0, 88.0, 31.0, 60.0],
    '推奨立ち回り': ['標準展開・遅めエントリー', '強気なファーストコンタクト', 'グループアップ・リテイク狙い', '集団ラッシュ / 武器拾い']
})
st.dataframe(df_econ, use_container_width=True)

st.write("---")

# ---------------------------------------------------------
# 7. SECTION 04 : マップ別 & サイド別パフォーマンス
# ---------------------------------------------------------
st.markdown("""
<div class="section-tag">SECTION 04 / MAP & SIDE PERFORMANCE</div>
<div class="section-title">マップ別 ＆ サイド別（攻撃/防衛）勝率</div>
""", unsafe_allow_html=True)

df_map = pd.DataFrame({
    'マップ': ['アセンド', 'バインド', 'ヘイヴン', 'サンセット'],
    '攻撃(ATK)勝率': ['62.5%', '48.0%', '55.2%', '70.0%'],
    '防衛(DEF)勝率': ['68.0%', '58.3%', '60.0%', '52.4%'],
    'FK獲得率': ['18.2%', '14.5%', '21.0%', '19.5%']
})
st.dataframe(df_map, use_container_width=True)

st.write("---")

# ---------------------------------------------------------
# 8. SECTION 05 : エージェント別スタッツ
# ---------------------------------------------------------
st.markdown("""
<div class="section-tag">SECTION 05 / AGENT STATS</div>
<div class="section-title">エージェント別パフォーマンス (ACS / K/D / KAST)</div>
""", unsafe_allow_html=True)

df_agent = pd.DataFrame({
    'エージェント': ['ジェット', 'レイズ', 'サイファー'],
    'ピック率': ['50%', '30%', '20%'],
    '平均ACS': [245, 220, 185],
    'K/D': [1.25, 1.10, 0.95],
    'KAST (%)': [74.5, 71.0, 78.2]
})
st.dataframe(df_agent, use_container_width=True)

st.write("---")

# ---------------------------------------------------------
# 9. SECTION 06 : クラッチ成功率 (1vsX)
# ---------------------------------------------------------
st.markdown("""
<div class="section-tag">SECTION 06 / CLUTCH SITUATIONS</div>
<div class="section-title">クラッチ状況（人数不利克服）成功率</div>
""", unsafe_allow_html=True)

col_c1, col_c2, col_c3 = st.columns(3)
col_c1.metric("1 vs 1 勝率", "45.0%", "勝敗を分ける局面")
col_c2.metric("1 vs 2 勝率", "22.5%", "高水準")
col_c3.metric("1 vs 3+ 成功数", "3回", "直近20試合")
