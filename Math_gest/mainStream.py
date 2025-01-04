import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    st.markdown("""
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #f5f5f5;
            }
            .title {
                font-size: 3em;
                font-weight: bold;
                color: #4CAF50;
                text-align: center;
                margin-top: 20px;
            }
            .description {
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 30px;
            }
            .container {
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 50px;
            }
            .card {
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
                transition: 0.3s;
                width: 80%;
                max-width: 400px;
                text-align: center;
                margin-bottom: 30px;
            }
            .card:hover {
                box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
            }
            .button {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin-top: 10px;
                cursor: pointer;
                border-radius: 5px;
                transition: background-color 0.3s ease;
            }
            .button:hover {
                background-color: #45a049;
            }
            .card img {
                border-radius: 10px;
                max-height: 200px;
                width: auto;
            }
        </style>
    """, unsafe_allow_html=True)

    lottie_animation_1 = "https://lottie.host/91fe3eb1-f734-4dd0-a42d-f9cd7c05bf41/KdhnxKznkT.json"
    lottie_anime_json_1 = load_lottie_url(lottie_animation_1)

    lottie_animation_2 = "https://lottie.host/85ee42ed-6bcd-4c3c-ada9-550eba743f1c/8zHYd2FA7w.json"
    lottie_anime_json = load_lottie_url(lottie_animation_2)

    # Center the Lottie animation and text
    st_lottie(lottie_anime_json_1, key="student", height=300)
    st.markdown(
        "<h1 style='text-align:center; color: green;'>Gesture <span style='color: orange;'>Learn</span></h1>", 
        unsafe_allow_html=True
    )

    st.markdown('<p class="description">Welcome to Gesture Learn! This platform offers two main features: A Gemini Math Solver and a Sign Language Detection app.</p>', unsafe_allow_html=True)

    st.markdown('<div class="container">', unsafe_allow_html=True)

    # Sign Language Detection Section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(Image.open("images/signlang.jpg"), use_column_width=True)
    if st.button("Go to Sign Language Detection", key="sign_language_button"):
        st.session_state.page = "sign_language_detection"
    st.markdown('</div>', unsafe_allow_html=True)


    # Math Solver Section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(Image.open("images/Mathsolver.jpg"), use_column_width=True)
    if st.button("Go to Math Solver", key="math_solver_button"):
        st.session_state.page = "math_solver"
    st.markdown('</div>', unsafe_allow_html=True)
    

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "main"

# Page navigation
if st.session_state.page == "main":
    main()
elif st.session_state.page == "math_solver":
    import mathsapp       # Import the math solver script
    mathsapp.run_math_solver()  # Call the function to run the math solver page
elif st.session_state.page == "sign_language_detection":
    import Sign_language_detetion
    Sign_language_detetion.app()  # Ensure sign_language_detection.py has an `app()` function
