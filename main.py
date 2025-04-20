import streamlit as st
import tensorflow as tf 
import numpy as np
import openai
from translations import TRANSLATIONS

# Load model and make prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_cnn_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_array = tf.keras.preprocessing.image.img_to_array(image)
    input_array = np.array([input_array])
    prediction = model.predict(input_array)
    result_index = np.argmax(prediction)
    return result_index

# Initialize session state
if 'language' not in st.session_state:
    st.session_state.language = 'en'
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Language helper
def get_text(key):
    return TRANSLATIONS[st.session_state.language][key]

# Sidebar
st.sidebar.title(get_text('sidebar_title'))

languages = {
    'English': 'en',
    'हिंदी': 'hi',
    'Español': 'es'
}
selected_language = st.sidebar.selectbox("🌐 Language/भाषा/Idioma", options=list(languages.keys()))
st.session_state.language = languages[selected_language]

app_mode = st.sidebar.selectbox(get_text('select_page'), [get_text('home'), get_text('about'), get_text('diseases_prediction')])

# Toggle theme
def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

# Dark mode styles
if st.session_state.dark_mode:
    st.markdown("""
        <style>
        body { background-color: #1e1e1e; color: white; }
        .sidebar .sidebar-content { background-color: #333; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        body { background-color: white; color: black; }
        .sidebar .sidebar-content { background-color: #f7f7f7; }
        </style>
    """, unsafe_allow_html=True)

# OpenAI API Key input
st.sidebar.markdown("🔑 Enter your OpenAI API Key to get remedies and solutions")
openai_api_key = st.sidebar.text_input("API Key", type="password")

# App Pages
if app_mode == get_text('home'):
    st.header(get_text('main_header'))
    st.image("static/plant2.jpg", use_column_width=True)
    st.markdown(get_text('intro_text'))
    
    st.markdown(get_text('why_choose_title'))
    st.markdown(get_text('why_choose_points'))
    
    st.markdown(get_text('vision_title'))
    st.markdown(get_text('vision_text'))
    
    st.markdown(get_text('mission_title'))
    st.markdown(get_text('mission_points'))
    
    st.markdown(get_text('values_title'))
    st.markdown(get_text('values_points'))
    
    st.image("static/plant_disease.jpg", use_column_width=True)

elif app_mode == get_text('about'):
    st.header(get_text('about'))
    st.image("static/team.png", use_column_width=True)
    
    st.markdown(get_text('about_mission_title'))
    st.markdown(get_text('about_mission_text'))
    
    st.markdown(get_text('about_importance_title'))
    st.markdown(get_text('about_importance_text'))
    
    st.markdown(get_text('about_dataset_title'))
    st.markdown(get_text('about_dataset_text'))

elif app_mode == get_text('diseases_prediction'):
    st.header(get_text('diseases_prediction'))

    test_image = st.file_uploader(get_text('upload_image'), type=["jpg", "jpeg", "png"])

    if test_image is not None:
        st.image(test_image, caption="Uploaded Image", use_column_width=True)

    if st.button(get_text('predict_button')) and test_image is not None:
        with st.spinner(get_text('predicting')):
            result_index = model_prediction(test_image)
            class_name = [
                'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 
                'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
                'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 
                'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 
                'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 
                'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 
                'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
            ]

            disease = class_name[result_index]
            st.markdown(get_text('predicted_disease').format(disease))
            st.success(get_text('prediction_complete'))

            # Remedy from OpenAI
            if openai_api_key:
                try:
                    openai.api_key = openai_api_key
                    prompt = f"Suggest effective remedies, treatments, and solutions for this plant disease: {disease.replace('_', ' ')}. Give simple and actionable advice for farmers in the {selected_language}."

                    with st.spinner("🧠 Generating remedies using OpenAI..."):
                        response = openai.ChatCompletion.create(
                            model="gpt-4.1-nano",
                            messages=[
                                {"role": "system", "content": "You are a plant disease expert."},
                                {"role": "user", "content": prompt}
                            ],
                            temperature=0.7,
                            max_tokens=400
                        )
                        remedy = response['choices'][0]['message']['content']
                        st.markdown("### 🩺 Remedies and Solutions")
                        st.info(remedy)
                except Exception as e:
                    st.error(f"OpenAI Error: {e}")
            else:
                st.warning("Please enter a valid OpenAI API key in the sidebar to view remedies.")

    st.markdown(get_text('how_it_works_title'))
    st.markdown(get_text('how_it_works_steps'))
    
    st.markdown(get_text('tips_title'))
    st.markdown(get_text('tips_points'))
    
    st.markdown(get_text('need_help_title'))
    st.markdown(get_text('need_help_text'))
