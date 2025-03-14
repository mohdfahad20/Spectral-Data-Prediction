# Spectral Data Analysis and Prediction

## 📌 Project Overview
This project aims to predict vomitoxin levels using spectral data. The model is trained using **Principal Component Analysis (PCA)** and **XGBoost**, achieving a high accuracy of **94%**. A **Streamlit application** is also included for real-time predictions.

---

## 📁 Repository Structure  

📂 Spectral-Data-Prediction
├── 📂 main-code
│ ├── 📄 ML_InternTask_ImagoAI.ipynb # Jupyter notebook with model training
│
├── 📂 models
│ ├── 📄 pca_model.pkl # Saved PCA model
│ ├── 📄 scaler.pkl # Scaler for feature normalization
│ ├── 📄 xgb_model.json # Trained XGBoost model
│
├── 📂 myenv # Virtual environment (not included in Git)
│
├── 📄 .gitignore # Files to ignore in Git
├── 📄 app.py # Streamlit app for predictions
├── 📄 requirements.txt # List of dependencies
├── 📄 README.md

---

## 🛠 Installation & Setup

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/mohdfahad20/Spectral-Data-Prediction.git
cd Spectral-Data-Prediction

Step 2: Create and Activate Virtual Environment

python -m venv myenv
source myenv/bin/activate  # On Windows use: myenv\Scripts\activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Run the Streamlit App
streamlit run app.py

🎯 Model Performance
Best Model: XGBoost
Accuracy: 94%
Deployment: Streamlit

🔥 Future Improvements
Optimize feature selection for better accuracy
Explore additional ML models for higher performance
Implement a better UI for enhanced user experience
