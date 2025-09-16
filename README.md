# 🌿 Plant Diseases Prediction - Complete Project Documentation

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg) ![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Project Structure](#project-structure)
4. [File and Folder Descriptions](#file-and-folder-descriptions)
5. [How the System Works](#how-the-system-works)
6. [Model Architecture](#model-architecture)
7. [Installation and Setup](#installation-and-setup)
8. [Usage Guide](#usage-guide)
9. [Features](#features)
10. [API Endpoints](#api-endpoints)
11. [Multi-language Support](#multi-language-support)
12. [Docker Deployment](#docker-deployment)
13. [Model Performance](#model-performance)
14. [Troubleshooting](#troubleshooting)

---

## 🎯 Project Overview

The **Plant Disease Prediction System** is an AI-powered web application that helps farmers, gardeners, and agricultural experts identify plant diseases quickly and accurately. The system uses deep learning (Convolutional Neural Networks) to analyze plant leaf images and predict potential diseases.

### Key Features:
- **🔍 AI-Powered Disease Detection**: Uses a trained CNN model with 98.4% accuracy
- **🌐 Multi-language Support**: Available in English, Hindi, Spanish, and Marathi
- **🩺 Expert Treatment Recommendations**: AI-generated remedies using GROQ API
- **📱 User-friendly Interface**: Modern, responsive web design
- **⚡ Real-time Processing**: Instant disease identification from uploaded images
- **📊 Performance Analytics**: Detailed model training statistics and visualizations

### Target Users:
- Farmers and agricultural workers
- Gardening enthusiasts
- Agricultural researchers and students
- Plant health consultants

---

## 🛠️ Technologies Used

### Backend Technologies:
- **Python 3.8+**: Core programming language
- **Flask**: Web application framework
- **TensorFlow 2.19.0**: Deep learning model training and inference
- **OpenCV**: Image processing
- **NumPy & Pandas**: Data manipulation and analysis

### Frontend Technologies:
- **HTML5**: Structure and content
- **Tailwind CSS**: Modern, responsive styling
- **JavaScript**: Interactive functionality
- **Jinja2**: Template engine for dynamic content

### AI & Machine Learning:
- **CNN (Convolutional Neural Network)**: Disease classification model
- **Keras**: High-level neural network API
- **GROQ API**: AI-powered treatment recommendations
- **LangChain**: Integration with language models

### Additional Tools:
- **Docker**: Containerization for easy deployment
- **Gunicorn**: Python WSGI HTTP server
- **Matplotlib & Seaborn**: Data visualization
- **Kaggle**: Dataset source

---

## 📁 Project Structure

```
Plant-Diseases-Prediction/
├── 📄 app.py                          # Main Flask application
├── 📄 requirements.txt                # Python dependencies
├── 📄 Dockerfile                      # Docker configuration
├── 📄 LICENSE                         # MIT License
├── 📄 README.md                       # Project overview
├── 📄 translations.py                 # Multi-language translations
├── 🤖 trained_cnn_model.keras          # Pre-trained CNN model (63.39 MB)
├── 📊 train.ipynb                      # Model training notebook
├── 📊 test.ipynb                       # Model testing and evaluation
├── 📂 Training Specs/                  # Model training specifications
│   ├── 📄 class_names.json            # List of 38 disease classes
│   ├── 📄 specs.json                  # Training performance metrics
│   ├── 📄 training_hist.json          # Training history data
│   ├── 📸 Epochs vs. Training Accuracy.JPG
│   ├── 📸 Training Accuracy and Validation Accuracy vs. No. of Epochs.JPG
│   └── 📸 Validation Accuracy vs. No. of Epochs.JPG
├── 📂 templates/                       # HTML templates
│   ├── 📄 base.html                   # Base template with navigation
│   ├── 📄 home.html                   # Landing page
│   ├── 📄 about.html                  # About page
│   ├── 📄 predict.html               # Disease prediction page
│   └── 📄 analysis.html               # Model performance analysis
├── 📂 static/                         # Static assets
│   ├── 🖼️ plant_disease.jpg           # Hero image
│   ├── 🖼️ plant2.jpg                  # Secondary image
│   ├── 🖼️ plant3.jpg                  # Tertiary image
│   └── 🖼️ team.png                    # Team image
├── 📂 app/                            # Additional application files
│   └── 📄 global.css                  # Global CSS styles
├── 📂 .vscode/                        # VS Code configuration
│   └── ⚙️ settings.json               # Editor settings
├── 📄 .gitignore                      # Git ignore rules
└── 📄 .gitattributes                  # Git attributes
```

---

## 📋 File and Folder Descriptions

### Core Application Files

#### 🔥 `app.py` (Main Application)
- **Purpose**: The heart of the Flask web application
- **Key Functions**:
  - `model_prediction()`: Loads the CNN model and makes disease predictions
  - Route handlers for different pages (home, about, predict, analysis)
  - Image upload and processing logic
  - Integration with GROQ API for treatment recommendations
  - Multi-language support through session management
- **Dependencies**: Flask, TensorFlow, PIL, OpenCV, LangChain

#### 📝 `requirements.txt`
- **Purpose**: Lists all Python packages needed to run the project
- **Key Dependencies**:
  - `tensorflow==2.19.0`: Deep learning framework
  - `flask`: Web application framework
  - `opencv-python`: Image processing
  - `streamlit`: Additional UI framework
  - `langchain_groq`: AI-powered recommendations
  - `gunicorn`: Production server

#### 🐳 `Dockerfile`
- **Purpose**: Containerizes the application for easy deployment
- **Configuration**:
  - Uses Python 3.10-slim base image
  - Installs system dependencies for OpenCV
  - Sets up Flask environment variables
  - Exposes port 5000 for web access

### Machine Learning Files

#### 🧠 `trained_cnn_model.keras` (AI Model)
- **Purpose**: Pre-trained Convolutional Neural Network for disease classification
- **Architecture**: Sequential model with 10 convolutional layers
- **Size**: 63.39 MB (16.6M total parameters, 5.5M trainable)
- **Input**: 128x128 RGB images
- **Output**: 38 disease classes with confidence scores
- **Performance**: 98.4% training accuracy, 96.1% validation accuracy

#### 📊 `train.ipynb` (Training Notebook)
- **Purpose**: Jupyter notebook containing model training code
- **Process**:
  - Data loading from Kaggle dataset
  - Image preprocessing and augmentation
  - CNN architecture definition
  - Training loop with validation
  - Performance visualization
- **Dataset**: 70,295 training images, 17,572 validation images

#### 📊 `test.ipynb` (Testing Notebook)
- **Purpose**: Model evaluation and testing procedures
- **Features**:
  - Model loading and architecture inspection
  - Test image prediction examples
  - Performance analysis
  - Prediction confidence evaluation

### Training Specifications

#### 📂 `Training Specs/` Directory
Contains all model training related data and visualizations:

- **`class_names.json`**: List of 38 plant disease classes including:
  - Apple diseases (Apple Scab, Black Rot, Cedar Apple Rust)
  - Tomato diseases (Early Blight, Late Blight, Leaf Mold, etc.)
  - Corn diseases (Common Rust, Northern Leaf Blight)
  - And many more fruit and vegetable diseases

- **`specs.json`**: Final training performance metrics
  - Training Loss: 0.0497 (very low, indicating good learning)
  - Training Accuracy: 98.42%
  - Validation Loss: 0.1307
  - Validation Accuracy: 96.15%

- **Training Charts**: Visual representations of model performance
  - Accuracy vs. Epochs progression
  - Loss curves over training periods
  - Validation performance tracking

### Web Interface Files

#### 📂 `templates/` Directory

##### 🏠 `base.html`
- **Purpose**: Master template providing consistent layout
- **Features**:
  - Responsive navigation bar
  - Dark/Light theme toggle
  - Language selector dropdown
  - Mobile-friendly design
  - Tailwind CSS integration

##### 🏡 `home.html`
- **Purpose**: Landing page showcasing system capabilities
- **Sections**:
  - Hero section with main image
  - Feature highlights grid
  - Vision and mission statements
  - Call-to-action buttons
  - Animated elements for better UX

##### ℹ️ `about.html`
- **Purpose**: Detailed information about the project
- **Content**:
  - Project mission and vision
  - Dataset information (87,000 images)
  - Technology stack explanation
  - Team information

##### 🔍 `predict.html`
- **Purpose**: Main prediction interface
- **Functionality**:
  - Image upload area (drag & drop)
  - Prediction button
  - Results display with confidence
  - Treatment recommendations
  - Progress indicators

##### 📊 `analysis.html`
- **Purpose**: Model performance visualization
- **Features**:
  - Training accuracy charts
  - Validation performance graphs
  - Model architecture details
  - Technical specifications

#### 📂 `static/` Directory
Contains all static assets:
- **Images**: Plant disease examples, hero images, team photos
- **Purpose**: Visual content for better user experience

### Configuration Files

#### 🌐 `translations.py`
- **Purpose**: Multi-language support system
- **Languages Supported**:
  - English (en): Default language
  - Hindi (hi): हिंदी support for Indian farmers
  - Spanish (es): Español for Latin American users
  - Marathi (mr): मराठी for regional Indian users
- **Content**: UI text, labels, descriptions, and help content

---

## ⚙️ How the System Works

### 1. **Image Upload Process**
```
User uploads plant image → Image validation → Secure file handling → Processing
```

### 2. **Disease Detection Pipeline**
```
Image → Resize to 128x128 → Normalize pixels → CNN Model → Confidence scores → Disease prediction
```

### 3. **Treatment Recommendation**
```
Disease identified → GROQ API call → Expert knowledge → Localized recommendations → Display to user
```

### 4. **Multi-language Flow**
```
User selects language → Session storage → Template rendering → Localized content display
```

---

## 🧠 Model Architecture

### CNN Architecture Details:
```
Input Layer: 128x128x3 (RGB images)
├── Conv2D (32 filters, 3x3) + ReLU
├── Conv2D (32 filters, 3x3) + ReLU
├── MaxPooling2D (2x2)
├── Conv2D (64 filters, 3x3) + ReLU
├── Conv2D (64 filters, 3x3) + ReLU
├── MaxPooling2D (2x2)
├── Conv2D (128 filters, 3x3) + ReLU
├── Conv2D (128 filters, 3x3) + ReLU
├── MaxPooling2D (2x2)
├── Conv2D (256 filters, 3x3) + ReLU
├── Conv2D (256 filters, 3x3) + ReLU
├── MaxPooling2D (2x2)
├── Conv2D (512 filters, 3x3) + ReLU
├── Conv2D (512 filters, 3x3) + ReLU
├── MaxPooling2D (2x2)
├── GlobalAveragePooling2D
├── Dropout (0.5)
├── Flatten
├── Dense (1500 units) + ReLU
├── Dropout (0.5)
└── Dense (38 units) + Softmax → Output: 38 disease classes
```

### Training Configuration:
- **Optimizer**: Adam
- **Loss Function**: Categorical Crossentropy
- **Metrics**: Accuracy
- **Image Size**: 128x128 pixels
- **Batch Size**: 32
- **Classes**: 38 different plant diseases

---

## 🚀 Installation and Setup

### Prerequisites:
- Python 3.8 or higher
- pip package manager
- 4GB+ RAM (for model loading)
- Internet connection (for API calls)

### Step-by-Step Installation:

#### 1. Clone the Repository
```bash
git clone <repository-url>
cd Plant-Diseases-Prediction
```

#### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Environment Variables Setup
Create a `.env` file in the root directory:
```env
APP_SECRET_KEY=your-secret-key-here
GROQ_API_KEY=your-groq-api-key-here
```

#### 5. Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Docker Installation (Alternative):
```bash
# Build the Docker image
docker build -t plant-disease-app .

# Run the container
docker run -p 5000:5000 -e GROQ_API_KEY=your-key plant-disease-app
```

---

## 📖 Usage Guide

### For Farmers and Users:

#### 1. **Access the System**
- Open your web browser
- Navigate to the application URL
- Choose your preferred language from the dropdown

#### 2. **Upload Plant Image**
- Go to the "Diseases Prediction" page
- Click "Upload Plant Image" or drag & drop your image
- Supported formats: PNG, JPG, JPEG
- Recommended: Clear, close-up leaf images

#### 3. **Get Disease Prediction**
- Click "Predict Disease" button
- Wait for AI analysis (usually 2-5 seconds)
- View results with confidence percentage

#### 4. **Review Treatment Recommendations**
- Read AI-generated treatment advice
- Follow step-by-step remedies
- Consider consulting local agricultural experts

### For Developers:

#### 1. **Model Integration**
```python
import tensorflow as tf

# Load the model
model = tf.keras.models.load_model('trained_cnn_model.keras')

# Make prediction
prediction = model.predict(preprocessed_image)
disease_index = np.argmax(prediction)
confidence = float(np.max(prediction))
```

#### 2. **Adding New Languages**
- Edit `translations.py`
- Add new language dictionary
- Update language selector in templates

---

## ✨ Features

### 🔍 **Disease Detection**
- **38 Disease Classes**: Covers major crops including tomatoes, apples, corn, grapes, potatoes, and more
- **High Accuracy**: 96%+ validation accuracy
- **Fast Processing**: Results in under 5 seconds
- **Confidence Scoring**: Shows prediction certainty

### 🌐 **Multi-language Support**
- **4 Languages**: English, Hindi, Spanish, Marathi
- **Complete Translation**: All UI elements and content
- **Cultural Adaptation**: Farming advice tailored to regions

### 🩺 **AI Treatment Recommendations**
- **Expert Knowledge**: Leverages agricultural expertise
- **Localized Advice**: Recommendations in user's language
- **Practical Solutions**: Low-cost, accessible treatments
- **Step-by-step Guidance**: Easy-to-follow instructions

### 📱 **User Experience**
- **Responsive Design**: Works on phones, tablets, computers
- **Dark/Light Mode**: User preference themes
- **Intuitive Interface**: Simple, farmer-friendly design
- **Visual Feedback**: Progress indicators and animations

### 📊 **Performance Analytics**
- **Training Visualizations**: Model performance charts
- **Accuracy Metrics**: Detailed statistics
- **Technical Details**: Model architecture information

---

## 🔌 API Endpoints

### Main Routes:

#### `GET /`
- **Purpose**: Home page
- **Response**: Landing page with system overview

#### `GET /about`
- **Purpose**: About page
- **Response**: Project information and mission

#### `GET /predict`
- **Purpose**: Prediction interface
- **Response**: Image upload and prediction form

#### `GET /analysis`
- **Purpose**: Model performance analysis
- **Response**: Training charts and statistics

#### `POST /upload`
- **Purpose**: Image upload and disease prediction
- **Parameters**:
  - `file`: Image file (PNG, JPG, JPEG)
- **Response**: JSON with prediction results
```json
{
    "disease": "Tomato___Early_blight",
    "confidence": 0.95,
    "image": "base64_encoded_image",
    "remedy": "AI-generated treatment advice",
    "success": true
}
```

#### `GET /set_language/<language>`
- **Purpose**: Language switching
- **Parameters**:
  - `language`: Language code (en, hi, es, mr)
- **Response**: Redirects with new language setting

#### `GET /training_charts/<filename>`
- **Purpose**: Serve training visualization images
- **Response**: Chart images from Training Specs folder

---

## 🌍 Multi-language Support

### Supported Languages:

#### 🇺🇸 **English (en)**
- Default language
- Complete interface translation
- Technical documentation

#### 🇮🇳 **Hindi (hi)**
- देवनागरी script support
- Farming terminology in Hindi
- Cultural context for Indian agriculture

#### 🇪🇸 **Spanish (es)**
- Latin American Spanish
- Agricultural terms in Spanish
- Suitable for Hispanic farming communities

#### 🇮🇳 **Marathi (mr)**
- Regional Indian language
- Maharashtra farming context
- Local agricultural practices

### Translation Structure:
```python
TRANSLATIONS = {
    'en': {
        'welcome_header': '🌿 Welcome to Our Plant Diseases Recognition System! 🌿',
        'upload_image': '📸 Upload Plant Image',
        'predict_button': '🔍 Predict Disease',
        # ... more translations
    },
    'hi': {
        'welcome_header': '🌿 हमारी पौधों की बीमारियों की पहचान प्रणाली में आपका स्वागत है! 🌿',
        'upload_image': '📸 पौधे की छवि अपलोड करें',
        'predict_button': '🔍 रोग की पहचान करें',
        # ... more translations
    }
    # ... other languages
}
```

---

## 🐳 Docker Deployment

### Dockerfile Configuration:
- **Base Image**: Python 3.10-slim
- **Dependencies**: OpenCV system libraries
- **Port**: 5000
- **Environment**: Production-ready Flask setup

### Deployment Steps:

#### 1. **Build Image**
```bash
docker build -t plant-disease-prediction .
```

#### 2. **Run Container**
```bash
docker run -d \
  -p 5000:5000 \
  -e GROQ_API_KEY=your-api-key \
  -e APP_SECRET_KEY=your-secret-key \
  --name plant-disease-app \
  plant-disease-prediction
```

#### 3. **Production Deployment**
```bash
# With persistent data
docker run -d \
  -p 80:5000 \
  -v /host/uploads:/app/uploads \
  -e GROQ_API_KEY=your-api-key \
  plant-disease-prediction
```

---

## 📈 Model Performance

### Training Results:
- **Training Accuracy**: 98.42%
- **Validation Accuracy**: 96.15%
- **Training Loss**: 0.0497
- **Validation Loss**: 0.1307

### Dataset Statistics:
- **Total Images**: 87,867
- **Training Set**: 70,295 images
- **Validation Set**: 17,572 images
- **Image Resolution**: 128x128 pixels
- **Classes**: 38 disease types

### Performance Metrics:
- **Model Size**: 63.39 MB
- **Parameters**: 16.6M total (5.5M trainable)
- **Inference Time**: ~2-3 seconds per image
- **Memory Usage**: ~1GB RAM during inference

### Supported Plant Diseases:

#### 🍎 **Apple Diseases**
- Apple Scab
- Black Rot
- Cedar Apple Rust
- Healthy Apple

#### 🍅 **Tomato Diseases**
- Bacterial Spot
- Early Blight
- Late Blight
- Leaf Mold
- Septoria Leaf Spot
- Spider Mites
- Target Spot
- Yellow Leaf Curl Virus
- Mosaic Virus
- Healthy Tomato

#### 🌽 **Corn Diseases**
- Cercospora Leaf Spot
- Common Rust
- Northern Leaf Blight
- Healthy Corn

#### 🍇 **Grape Diseases**
- Black Rot
- Esca (Black Measles)
- Leaf Blight
- Healthy Grape

And many more for potatoes, peppers, peaches, oranges, strawberries, and other crops.

---

## 🔧 Troubleshooting

### Common Issues and Solutions:

#### **1. Model Loading Error**
**Problem**: "Unable to load trained_cnn_model.keras"
**Solutions**:
- Ensure the model file is in the root directory
- Check file permissions
- Verify TensorFlow installation: `pip install tensorflow==2.19.0`

#### **2. Image Upload Fails**
**Problem**: "Invalid file type" or upload errors
**Solutions**:
- Use PNG, JPG, or JPEG formats only
- Check file size (recommended: under 10MB)
- Ensure image is not corrupted
- Try different browsers

#### **3. GROQ API Error**
**Problem**: "GROQ_API_KEY not found" or API failures
**Solutions**:
- Set environment variable: `export GROQ_API_KEY=your-key`
- Check API key validity
- Verify internet connection
- Review API usage limits

#### **4. Language Switching Issues**
**Problem**: Language not changing or displaying incorrectly
**Solutions**:
- Clear browser cache
- Check browser language settings
- Verify translations.py file integrity
- Restart the application

#### **5. Docker Container Issues**
**Problem**: Container fails to start or crashes
**Solutions**:
```bash
# Check container logs
docker logs plant-disease-app

# Restart container
docker restart plant-disease-app

# Rebuild image
docker build --no-cache -t plant-disease-prediction .
```

#### **6. Performance Issues**
**Problem**: Slow prediction or high memory usage
**Solutions**:
- Ensure 4GB+ RAM available
- Close other applications
- Use smaller image files
- Consider using GPU acceleration if available

#### **7. Port Already in Use**
**Problem**: "Port 5000 already in use"
**Solutions**:
```bash
# Find process using port 5000
netstat -an | find "5000"

# Kill the process or use different port
python app.py --port=5001
```

### Getting Help:
1. Check the GitHub repository issues
2. Review application logs
3. Test with different browsers
4. Verify system requirements
5. Contact the development team

---

## 📞 Support and Contact

For technical support, feature requests, or bug reports:
- **Email**: arpitkadam922@gmail.com
- **GitHub**: Check the repository issues section
- **Documentation**: This comprehensive guide covers most scenarios

### Contributing:
We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request
4. Include proper documentation

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

**Developed by Arpit Kadam** - Empowering farmers with AI-powered plant disease detection technology.

*Last updated: January 2025*
