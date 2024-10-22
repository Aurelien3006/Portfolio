import streamlit as st

st.set_page_config(
    page_title='Portfolio',
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar navigation
st.sidebar.page_link('Curriculum_vitae.py', label='Curriculum vitae')
st.sidebar.page_link('./pages/Portfolio.py', label='Portfolio')

st.header('**Portfolio**', divider=True)
st.markdown(" ")
st.markdown("***A Data Visualization project about the Public Transportation services' data in Ile de France :***")
result = st.button(label="Data Visualization Project",type="primary",use_container_width=True)
if result:
    st.switch_page("./pages/DataVisualizationProject.py")