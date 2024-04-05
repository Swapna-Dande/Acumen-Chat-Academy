import streamlit as st
from streamlit_lottie import st_lottie  # For Lottie animations
import importlib
import os

# -- Navigation Bar --
st.sidebar.header("Navigation")
selected_page = st.sidebar.selectbox("Select a page:", ["Home", "Teachers", "Students", "About", "Contact Us"])

# -- Home Page Content --
if selected_page == "Home":
    st.title("Acumen Chat Academy")
    st.write("Welcome to Our Educational Platform!")
    st.write("A platform designed to empower both teachers and students.")

    # Add columns for a more organized layout
    col1, col2 = st.columns(2)
    with col1:
        st.header("For Teachers")
        st.write(
            """
            - Create engaging learning experiences.
            - Get Visualization of student progres.
            - Collaborate with colleagues and share resources.
            """
        )
    with col2:
        st.header("For Students")
        st.write(
            """
            - Access interactive learning materials.
            - Upskill your skills.
            - Track your progress and stay motivated.
            """
        )

# -- About Us Page --
if selected_page == "About":
    st.title("About Us")
    st.write(
        """
        We are a passionate team dedicated to creating a better learning experience for students.
        Our mission is to empower educators and students through innovative technology.
        """
    )
    st.write("")
    st.markdown('Created by: [Acumen Chat Academy])')
    st.markdown('Contact via mail: [acumenchatacademy1@gmail.com]')
    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
    with col2:
        st_lottie("https://lottie.host/dceed925-932c-4ea4-b140-3aebdeaaf1f0/JZyKl8qgfG.json", width=250, height=250)


# -- Contact Us Page --
if selected_page == "Contact Us":
    st.title("Contact Us")
    st.write("We'd love to hear from you!")

    # Contact form using Streamlit Forms (replace with your form handling logic)
    contact_form = st.form("contact_form")
    name = contact_form.text_input("Your Name")
    email = contact_form.text_input("Your Email Address")
    message = contact_form.text_area("Your Message")
    submitted = contact_form.form_submit_button("Submit")

    if submitted:
        st.success(f"Thanks for contacting us, {name}! We'll get back to you soon.")

# -- Loading Teacher or Student Applications --
def load_external_app(app_path, app_type="Teacher"):
    """Loads a Streamlit application from a separate Python file, handling Teachers and Students.

    Args:
        app_path (str): The path to the Python file containing the Streamlit app.
        app_type (str, optional): Either "Teacher" (default) or "Student" to differentiate app behavior.

    Returns:
        None: This function doesn't return anything, it displays the loaded app.
    """

    try:
        # Import the external app module
        app_module = importlib.import_module(os.path.splitext(os.path.basename(app_path))[0])

        # Handle Teacher and Student applications differently (assuming `run` function exists in both)
        if app_type == "Teacher":
            app_module.MultiApp() # Call MultiApp.run() from teacher_main.py
        elif app_type == "Student":
            app_module.MultiApp()  # Call run() directly from student_main.py (assuming no MultiApp)

    except ModuleNotFoundError:
        st.error(f"Failed to import app from '{app_path}'. Check the file path and module name.")

# Load Teacher or Student Application based on Selection
if selected_page == "Teachers":
    load_external_app("/Users/swapnadande/Desktop/mainprojectcode/projectcode/Student App/teacher_main.py", app_type="Teacher")  # Replace with actual path
#def run():
 #   if app == "File Uploader":
  #      file_uploader.app()
   # if app == "Chat with Data":
    #    chat_data.app(input_excel) 
    #f app == "Visualization":
      #  visualization.app(input_excel) 
    #run()
                     
if selected_page == "Students":
    load_external_app("/Users/swapnadande/Desktop/mainprojectcode/projectcode/Student App/student_main.py", app_type="Student")  # Replace with actual path

 

# Lottie Animation (replace with your animation file path)
def show_lottie(lottie_url):
    st_lottie(lottie_url, key="animation", height=300, width=500)

if selected_page == "Home":
    show_lottie("https://lottie.host/dceed925-932c-4ea4-b140-3aebdeaaf1f0/JZyKl8qgfG.json") 