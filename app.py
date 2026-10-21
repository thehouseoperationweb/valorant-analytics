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
