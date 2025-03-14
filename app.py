import streamlit as st
import pandas as pd
import joblib
import xgboost as xgb

# Load trained models
scaler = joblib.load('models/scaler.pkl')  # Load StandardScaler
pca = joblib.load('models/pca_model.pkl')  # Load PCA model
xgb_best = xgb.Booster()
xgb_best.load_model("models/xgb_model.json")  # Load trained XGBoost model

# Streamlit UI
st.title("Spectral Data Prediction App")
st.write("Upload your spectral data file for predictions.")

# File uploader
uploaded_file = st.file_uploader("📂 Upload CSV or Excel file", type=['csv', 'xlsx'])

if uploaded_file:
    try:
        # Read uploaded file
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.write("Uploaded Data Preview:")
        st.write(df.head(10))

        # Drop unwanted columns if they exist
        drop_cols = ['hsi_id', 'vomitoxin_ppb']  # Columns to remove
        X_new = df.drop(columns=[col for col in drop_cols if col in df.columns], errors='ignore')

        # Preprocess: Standardize & Apply PCA
        X_scaled = scaler.transform(X_new)  # Use saved StandardScaler
        X_pca = pca.transform(X_scaled)  # Apply PCA transformation

        # Convert to XGBoost DMatrix
        dmatrix = xgb.DMatrix(X_pca)

        # Make predictions
        predictions = xgb_best.predict(dmatrix)

        # Add predictions to the DataFrame
        df['Predicted Value'] = predictions

        # Show predictions
        st.write("Predictions: ")
        st.write(df[['Predicted Value']].head(10))  # Display first 10 predictions

        # Provide download option
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Predictions", csv, "predictions.csv", "text/csv")

    except Exception as e:
        st.error(f"Error processing file: {e}")
