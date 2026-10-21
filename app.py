import streamlit as st
import pandas as pd

st.set_page_config(page_title="QT DIG VALORANT Analytics", layout="wide")

# スタイリング（ダークテーマ設定）
st.markdown("""
<style>
    .stApp {
        background-color: #0f1923;
        color: #f9f9f9;
    }
    div[data-testid="stMetricValue"] {
        color: #ff4655;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎮 QT DIG VALORANT 試合分析ダッシュボード")

# パスワード保護（簡易ロック機能）
st.sidebar.header("🔒 セキュリティ設定")
password = st.sidebar.text_input("アクセスパスワードを入力", type="password")

if password != "AIM_FOR_NUMBER_1":
    st.warning("🔒 AIM FOR NUMBER 1！ パスワードを入力してください")
    st.info("※正しいパスワードを入力すると、ダッシュボードが表示されます。")
else:
    st.success("🏆 認証完了：世界一位への軌跡")
    st.caption("コーチ提案指標 ＆ 拡張分析フルスペックプロトタイプ")

    # サイドバー設定
    st.sidebar.header("プレイヤー設定")
    riot_id = st.sidebar.text_input("Riot ID (名前)", value="Hust is so VLY")
    tag = st.sidebar.text_input("Tag (タグ)", value="Bang")
    region = st.sidebar.selectbox("リージョン", ["ap", "na", "eu", "kr"], index=0)

    use_sample = st.sidebar.checkbox("デモ用サンプルデータで表示する", value=True)

    if st.sidebar.button("データを取得・更新"):
        st.cache_data.clear()

    st.write(f"### 📊 分析対象: `{riot_id}#{tag}` ({region.upper()})")

    # KPI概要
    col1, col2, col3 = st.columns(3)
    col1.metric("ファーストキル(FK)時 勝率", "78.3%", "+27.1% (通常比)")
    col2.metric("初落ち(FD)時 カバー率", "62.2%", "目標 70%")
    col3.metric("直近20試合 勝率", "65.0%", "800RR到達ペース")

    st.write("---")

    # 1. FK / FD 相関分析
    st.subheader("1. ファーストキル(FK) / ファーストデス(FD) 発生時のラウンド勝率")
    df_fk = pd.DataFrame({
        '状況': ['FK獲得時', '通常展開', 'FD発生時'],
        'ラウンド勝率 (%)': [78.3, 51.2, 24.4]
    })
    st.bar_chart(data=df_fk, x='状況', y='ラウンド勝率 (%)')

    # 2. アビリティ効率分析
    st.subheader("2. アビリティ使用効率とラウンド獲得貢献")
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

    # 3. マネー別戦術分析
    st.subheader("3. 相手装備（マネー状況）別の交戦勝率分析")
    df_econ = pd.DataFrame({
        '自軍装備状況': ['フルバイ (4300+)', 'フルバイ (4300+)', 'ハーフバイ (2000-3000)', 'エコ / 節約 (0-2000)'],
        '敵軍装備状況': ['フルバイ (重装・主力銃)', 'エコ / 相手弱武装', 'フルバイ (強武装)', 'エコ / 同等武装'],
        '交戦ラウンド勝率 (%)': [55.0, 88.0, 31.0, 60.0],
        '推奨立ち回り': ['標準展開・遅めエントリー', '強気なファーストコンタクト', 'グループアップ・リテイク狙い', '集団ラッシュ / 武器拾い']
    })
    st.dataframe(df_econ, use_container_width=True)

    st.write("---")

    # 4. マップ別 ＆ サイド別パフォーマンス
    st.subheader("4. マップ別 ＆ サイド別（攻撃/防衛）勝率")
    df_map = pd.DataFrame({
        'マップ': ['アセンド', 'バインド', 'ヘイヴン', 'サンセット'],
        '攻撃(ATK)勝率': ['62.5%', '48.0%', '55.2%', '70.0%'],
        '防衛(DEF)勝率': ['68.0%', '58.3%', '60.0%', '52.4%'],
        'FK獲得率': ['18.2%', '14.5%', '21.0%', '19.5%']
    })
    st.dataframe(df_map, use_container_width=True)

    st.write("---")

    # 5. エージェント別スタッツ
    st.subheader("5. エージェント別パフォーマンス (ACS / K/D / KAST)")
    df_agent = pd.DataFrame({
        'エージェント': ['ジェット', 'レイズ', 'サイファー'],
        'ピック率': ['50%', '30%', '20%'],
        '平均ACS': [245, 220, 185],
        'K/D': [1.25, 1.10, 0.95],
        'KAST (%)': [74.5, 71.0, 78.2]
    })
    st.dataframe(df_agent, use_container_width=True)

    st.write("---")

    # 6. クラッチ成功率（1vsX）
    st.subheader("6. クラッチ状況（人数不利克服）成功率")
    col_c1, col_c2, col_c3 = st.columns(3)
    col_c1.metric("1 vs 1 勝率", "45.0%", "勝敗を分ける局面")
    col_c2.metric("1 vs 2 勝率", "22.5%", "高水準")
    col_c3.metric("1 vs 3+ 成功数", "3回", "直近20試合")
