import streamlit as st
import base64
from viz_style import load_local_css

load_local_css()

greeting = "Hi, 我是蔡克梅"
role = "一个热爱数据和AI的产品设计师"
resume = """
**用户与业务洞察：** 
拥有13年用户体验背景，7年智能车SaaS、车机HMI、手机车控APP从业经验，擅长将复杂业务与用户需求转化为清晰的产品策略与设计方案。

**产品策划与协作：**
具备跨职能协作与团队管理能力，能够独立完成产品调研、规划、执行，推动项目高效落地并实现业务目标。

**技术理解与创新：**
熟悉Python与数据分析，结合AI工具开发多个LLM应用，持续推动新技术在实际产品中的落地与应用。
"""


project_module = "最近工作"
title_1 = "咕咕记"
info_1 = """
通过播客音频的转写与说话人分离，结合LLM生成内容摘要与结构化笔记，实现从“声音”到“知识”的自动化转化流程。
"""
label_1 = ":grey-badge[ASR]  :grey-badge[Speaker Diarization]  :grey-badge[LLM Sumarize]"


title_2 = "车辆故障反馈信息分析工具"
info_2 = """
基于微调大语言模型，实现车辆故障反馈的自动化分析，精准提取关键信息并分类归因，助力产品优化和售后服务体验。
"""
label_2 = ":grey-badge[LLM Fine-tuning]  :grey-badge[LLM 数据标注]  :grey-badge[信息抽取]  :grey-badge[数据可视化]"

title_3 = "智能车配置趋势分析工具"
info_3 = """
通过自动化采集行业竞品车型数据，结合智能分析模型，动态洞察智能配置的发展趋势，助力产品规划和战略决策。
"""
label_3 = ":grey-badge[数据采集]  :grey-badge[数据分析]  :grey-badge[数据可视化]"

photo = "assets/photo.png"
image_1 = "assets/photo.png"
image_2 = "assets/photo.png"
image_3 = "assets/photo.png"

page_1 = "pages/podcast_to_knowledge.py"
page_2 = "pages/info_extract.py"
page_3 = "pages/config_analysis.py"


projects = {"title": [title_1, title_2, title_3],
            "info": [info_1, info_2, info_3],
            "label": [label_1, label_2, label_3],
            "links": [page_1, page_2, page_3]
            }


# @st.cache_data
# def get_pdf():
#     with open("assets/resume.pdf", "rb") as f:
#         return f.read()  # 返回原始二进制内容

# pdf_resume = get_pdf()

cols = st.columns([1,1], gap="large")
with cols[0]:
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.text(greeting)
    st.subheader(role)
    st.markdown(resume)
    # st.download_button(label="下载我的简历", data=pdf_resume, file_name="caikemei_resume.pdf", mime="application/pdf", icon=":material/download:", type="tertiary")
with cols[1]:
    st.write("")
    st.write("")
    st.image("assets/photo.png")


# st.caption(project_module)
st.write("")
st.write("")
st.write("")
st.write("")
selected = st.radio(label="最近", options=projects["title"], captions= [f'{projects["info"][i]} \n {projects["label"][i]}' for i in range(3)], horizontal=True, index=None)
if selected == projects["title"][0]:
    st.switch_page(projects["links"][0])

if selected == projects["title"][1]:
    st.switch_page(projects["links"][1])

if selected == projects["title"][2]:
    st.switch_page(projects["links"][2])






# project_cols = st.columns(3)
# for i, col in enumerate(project_cols):
#     with col:
#         with st.container(border=True):
#             st.page_link(projects["links"][i], label = projects["title"][i])
#             st.caption(projects["info"][i])
#             st.markdown(projects["label"][i])













# poject1_cols = st.columns([2,2], gap="large")
# poject1_cols[0].image(project_1_image)
# # poject1_cols[1].subheader(project_1_title)
# poject1_cols[1].page_link("pages/podcast_to_knowlogy.py", label=project_1_title)

# poject1_cols[1].text(project_1_info)
# poject1_cols[1].markdown(project_1_label)

# st.write("")
# st.write("")
# st.write("")
# st.write("")

# poject2_cols = st.columns([2,2], gap="large")
# poject2_cols[0].subheader(project_2_title)
# poject2_cols[0].text(project_2_info)
# poject2_cols[0].markdown(project_2_label)
# poject2_cols[1].image(project_2_image)

# st.write("")
# st.write("")
# st.write("")
# st.write("")

# poject3_cols = st.columns([2,2], gap="large")
# poject3_cols[0].image(project_3_image)
# poject3_cols[1].subheader(project_3_title)
# poject3_cols[1].text(project_3_info)
# poject3_cols[1].markdown(project_3_label)

