from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_from_directory
import tensorflow as tf
import numpy as np
import json
import os
from werkzeug.utils import secure_filename
from PIL import Image
import io
import base64
from langchain_groq import ChatGroq
from translations import TRANSLATIONS
from dotenv import load_dotenv
import markdown

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load class names
with open("Training Specs/class_names.json", "r") as f:
    CLASS_NAMES = json.load(f)

# Load training specs
with open("Training Specs/specs.json", "r") as f:
    TRAINING_SPECS = json.load(f)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def model_prediction(image_file):
    """Load model and make prediction"""
    model = tf.keras.models.load_model("trained_cnn_model.keras")
    
    # Process the image
    image = Image.open(image_file)
    image = image.resize((128, 128))
    input_array = tf.keras.preprocessing.image.img_to_array(image)
    input_array = np.array([input_array])
    
    prediction = model.predict(input_array)
    result_index = np.argmax(prediction)
    confidence = float(np.max(prediction))
    
    return result_index, confidence

def get_text(key, language='en'):
    """Get translated text"""
    return TRANSLATIONS.get(language, {}).get(key, key)

@app.route('/training_charts/<filename>')
def training_charts(filename):
    """Serve training chart images"""
    return send_from_directory('Training Specs', filename)

@app.route('/')
def home():
    language = session.get('language', 'en')
    return render_template('home.html', get_text=lambda key: get_text(key, language), language=language)

@app.route('/about')
def about():
    language = session.get('language', 'en')
    return render_template('about.html', get_text=lambda key: get_text(key, language), language=language)

@app.route('/predict')
def predict_page():
    language = session.get('language', 'en')
    return render_template('predict.html', get_text=lambda key: get_text(key, language), language=language)

@app.route('/analysis')
def analysis():
    language = session.get('language', 'en')
    chart_files = {
        'epochs_training_accuracy': os.path.exists('Training Specs/Epochs vs. Training Accuracy.JPG'),
        'training_validation_accuracy': os.path.exists('Training Specs/Training Accuracy and Validation Accuracy vs. No. of Epochs.JPG'),
        'validation_accuracy': os.path.exists('Training Specs/Validation Accuracy vs. No. of Epochs.JPG')
    }
    
    return render_template('analysis.html', 
                         get_text=lambda key: get_text(key, language), 
                         language=language,
                         specs=TRAINING_SPECS,
                         chart_files=chart_files)

@app.route('/set_language/<language>')
def set_language(language):
    session['language'] = language
    return redirect(request.referrer or url_for('home'))

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file selected'})
    
    file = request.files['file']
    language = session.get('language', 'en')
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'})
    
    if file and allowed_file(file.filename):
        try:
            # Make prediction
            result_index, confidence = model_prediction(file)
            disease = CLASS_NAMES[result_index]
            
            # Convert image to base64 for display
            file.seek(0)
            img_data = base64.b64encode(file.read()).decode()
            
            result = {
                'disease': disease,
                'confidence': confidence,
                'image': img_data,
                'success': True
            }
            
            groq_api_key = os.getenv('GROQ_API_KEY')
            if groq_api_key:
                try:
                    language_names = {
                        'en': 'English',
                        'hi': 'Hindi',
                        'es': 'Spanish',
                        'mr': 'Marathi'
                    }
                    lang_name = language_names.get(language, 'English')
                    
                    prompt = (
                                f"Act as an expert agricultural advisor. Provide clear, practical, and low-cost remedies, treatments, and "
                                f"preventive measures for the plant disease: {disease.replace('_', ' ')}. "
                                f"Explain the cause and symptoms briefly, then give step-by-step solutions using easily available materials "
                                f"and farming practices. Ensure the advice is easy to understand and follow by local farmers, and write the response "
                                f"in language {lang_name}."
                             )

                    
                    llm = ChatGroq(api_key=groq_api_key, model="openai/gpt-oss-20b")
                    response = llm.invoke(prompt)
                    result['remedy'] = markdown.markdown(response.content, extensions=['tables'])
                except Exception as e:
                    result['remedy_error'] = str(e)
            else:
                result['remedy_error'] = "GROQ_API_KEY not found in environment variables"
            
            return jsonify(result)
            
        except Exception as e:
            return jsonify({'error': f'Prediction failed: {str(e)}'})
    
    return jsonify({'error': 'Invalid file type'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

