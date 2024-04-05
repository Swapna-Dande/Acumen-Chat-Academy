import streamlit as st
import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as stc


def app(input_excel):
    # st.set_page_config(page_title="about")
    st.header(":red[Visualize] Your Data... 📊",divider= 'rainbow')
    st.write("Effortlessly visualize your data through drag-and-drop")
    sidebar = st.sidebar
    input_excel = input_excel
    if input_excel:
         selected_file = sidebar.selectbox(
            "Select a excel file", [file.name for file in input_excel])
         selected_index = [file.name for file in input_excel].index(selected_file)
         sidebar.info("Excel file uploaded successfully")
         data = pd.read_excel(input_excel[selected_index])
         #pyg.walk function takes the dataframe as input and returns an html string that can be displayed in the streamlit app.
         #pygwalker core functinality lies in generating interactive visualizations.
         #often build using web technolgies like html, css and JS.
         pyg_html =pyg.walk(data, env='Streamlit', dark='dark',return_html=True)
        #stc.html integrates html conmponent into our application
        #by displaying user can directly interact by rendering the visualisation within the web app
         #this function will display the html string in streamlit application we've developed.
         stc.html(pyg_html,scrolling=True,width=1300, height=1000,)
         
         