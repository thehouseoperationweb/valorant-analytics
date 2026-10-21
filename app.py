import streamlit as st

# ページ全体のレイアウト・デザイン設定（一番上に記述）
st.set_page_config(
    page_title="QT DIG VALORANT 試合分析ダッシュボード",
    page_icon="🎮",
    layout="wide"
)

# パスワード保護（簡易ロック機能）
password = st.text_input("アクセスパスワードを入力", type="password")

if password != "AIM_FOR_NUMBER_1":
    st.warning("🔒 パスワードを入力してください")
    st.info("※正しいパスワードを入力すると、ダッシュボードが表示されます。")
    st.stop()

# --- ここからログイン後の最新メイン画面 ---
st.title("🎮 QT DIG VALORANT 試合分析ダッシュボード")
st.success("🏆 認証完了 : 世界一位への軌跡")
st.caption("コーチ提案指標 & 拡張分析フルスペックプロトタイプ")

# ※ロゴ画像やメインコンテンツのコードがここに続きます
