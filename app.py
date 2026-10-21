import streamlit as st
import pandas as pd

# ページ基本設定
st.set_page_config(
    page_title="QT DIG VALORANT Analytics",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# 高級感・eSportsプロアナリティクスUI (CSS定義)
# ---------------------------------------------------------
st.markdown("""
<style>
    /* 全体背景 */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #080d12 !important;
        color: #ece8e1 !important;
        font-family: 'Times New Roman', 'Shippori Mincho', 'Yu Mincho', serif !important;
    }

    /* サイドバー */
    [data-testid="stSidebar"] {
        background-color: #0f1923 !important;
        border-right: 1px solid #1e2d3d !important;
    }

    /* ヘッダーカード */
    .header-card {
        background: linear-gradient(135deg, #0f1923 0%, #152230 100%);
        border: 1px solid #1e2d3d;
        border-left: 4px solid #ff4655;
        border-radius: 4px;
        padding: 20px 25px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 20px;
    }
    .header-title {
        font-size: 1.8rem;
        font-weight: 800;
        letter-spacing: 2px;
        color: #ffffff;
        margin: 0;
        font-family: 'Times New Roman', sans-serif !important;
    }
    .header-sub {
        font-size: 0.85rem;
        color: #8b9bb4;
        margin-top: 4px;
        letter-spacing: 1px;
    }

    /* ターゲットバッジ */
    .target-badge {
        background: #0f1923;
        border: 1px solid #1e2d3d;
        border-left: 3px solid #2b7fff;
        padding: 8px 16px;
        border-radius: 3px;
        display: inline-block;
        font-size: 0.85rem;
        color: #8b9bb4;
        margin-bottom: 25px;
        letter-spacing: 1px;
    }
    .target-badge strong {
        color: #ffffff;
        font-size: 1.0rem;
    }

    /* メトリックカード (枠線・赤青ボーダー) */
    .kpi-card {
        background: #0d151e;
        border: 1px solid #1e2d3d;
        border-radius: 4px;
        padding: 18px 20px;
        height: 100%;
    }
    .kpi-card.red-border {
        border-left: 3px solid #ff4655;
    }
    .kpi-card.blue-border {
        border-left: 3px solid #2b7fff;
    }
    .kpi-label {
        font-size: 0.85rem;
        color: #8b9bb4;
        margin-bottom: 8px;
        font-weight: 600;
    }
    .kpi-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #ffffff;
        font-family: 'Times New Roman', sans-serif !important;
        line-height: 1.1;
    }
    .kpi-delta {
        font-size: 0.8rem;
        margin-top: 8px;
        font-weight: 500;
    }
    .kpi-delta.green { color: #00f0ff; }
    .kpi-delta.red { color: #ff4655; }

    /* セクションタイトル */
    .section-tag {
        color: #ff4655;
        font-size: 0.75rem;
        font-weight: 800;
        letter-spacing: 2px;
        margin-top: 30px;
        margin-bottom: 5px;
    }
    .section-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 15px;
    }

    /* データフレーム・表のスタイル調整 */
    div.stDataFrame {
        border: 1px solid #1e2d3d !important;
        border-radius: 4px !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# パスワード認証 (簡易ロック)
# ---------------------------------------------------------
user_input = st.text_input("🔒 アクセスパスワードを入力", type="password")
normalized_input = user_input.strip().upper().replace(" ", "_")

if normalized_input != "AIM_FOR_NUMBER_1":
    st.warning("🔒 AIM FOR NUMBER 1！ パスワードを入力してください")
    st.info("※正しいパスワードを入力すると、ダッシュボードが表示されます。")
    st.stop()

# ---------------------------------------------------------
# ヘッダーエリア（ロゴ＋タイトル）
# ---------------------------------------------------------
st.markdown("""
<div class="header-card">
    <svg width="40" height="40" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M20 20L45 50L20 80H35L60 50L35 20H20Z" fill="#FF4655"/>
        <path d="M50 20L75 50L50 80H65L90 50L65 20H50Z" fill="#FF4655"/>
    </svg>
    <div>
        <div class="header-title">QT DIG ANALYTICS</div>
        <div class="header-sub">VALORANT 試合分析ダッシュボード / コーチ提案指標プロトタイプ</div>
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
    <div class="kpi-card red-border">
        <div class="kpi-label">直近20試合 勝率</div>
        <div class="kpi-value">65.0%</div>
        <div class="kpi-delta green">800RR 到達ペース</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------------------------------------------------
# SECTION 01 : FK / FD 相関分析
# ---------------------------------------------------------
st.markdown("""
<div class="section-tag">SECTION 01 / OPENING DUEL</div>
<div class="section-title">ファーストキル (FK) / ファーストデス (FD) 発生時のラウンド勝率</div>
""", unsafe_allow_html=True)

df_fk = pd.DataFrame({
    '状況': ['FD発生時', 'FK獲得時', '通常展開'],
    'ラウンド勝率 (%)': [24.4, 78.3, 51.2]
})
st.bar_chart(data=df_fk, x='状況', y='ラウンド勝率 (%)')

st.write("---")

# ---------------------------------------------------------
# SECTION 02 : アビリティ効率分析
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
# SECTION 03 : マネー別戦術分析
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
# SECTION 04 : マップ別 & サイド別パフォーマンス
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
# SECTION 05 : エージェント別スタッツ
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
# SECTION
