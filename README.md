# ❤️ HeartGuard AI: Multi-Model Cardiac Diagnostic Tool

HeartGuard AI is a professional-grade web application that I built to predict the risk of heart disease using four distinct Machine Learning architectures. By implementing a **Consensus Engine**, the system cross-verifies patient data across multiple models to deliver a more reliable and trustworthy risk assessment.

<img width="1908" height="896" alt="image" src="https://github.com/user-attachments/assets/f320f920-67ca-4d78-9104-727a0958390b" />

🚀 **Live Demo:** [Click Here to View the App](https://heartguardai-2004.streamlit.app/)

---

## ✨ Features

- **Individual Analysis:** I provide real-time heart disease risk assessment for a single patient based on clinical parameters.  
- **Batch Processing:** Users can upload a CSV file containing 100+ patient records for instant large-scale screening.  
- **AI Consensus Engine:** The system combines predictions from Decision Tree, Logistic Regression, Random Forest, and SVM models to verify outcomes.  
- **Modern Dark UI:** I designed a clean, medical-grade dark dashboard optimized for clarity and readability.  
- **Data Export:** Detailed batch prediction reports can be downloaded as CSV files for further analysis.

---

## 🛠️ Technology Stack

- **Frontend:** Streamlit  
- **Data Handling:** Pandas, NumPy  
- **Machine Learning:** Scikit-Learn  
- **Model Storage:** Pickle  

<img width="473" height="206" alt="image" src="https://github.com/user-attachments/assets/1ad89082-23de-4ace-891a-9fae86e19dd4" />

---

## 📊 How It Works

The application follows a simple yet robust 3-step pipeline:

- **Input:** I collect essential clinical data such as Age, Blood Pressure, Cholesterol, and other medical indicators.  
- **Processing:** The data is preprocessed and normalized before being passed into four independent ML models.  
- **Consensus:** Each model generates a prediction, and the system computes an overall risk score. If more than 50% of the models classify the patient as high risk, the app triggers a **High Risk** alert.
## 🛠️ How I Deployed the Application

- I pushed the complete project to **GitHub**.  
- I connected the repository to **Streamlit Community Cloud** at https://share.streamlit.io.  
- Streamlit handled the build and deployment automatically.  
- Once deployed, I received a public URL (e.g., https://heartguard-ai.streamlit.app).  
- I added this deployment link directly to the README for easy access.
