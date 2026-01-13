# ❤️ HeartGuard AI: Multi-Model Cardiac Diagnostic Tool

HeartGuard AI is a professional-grade web application that leverages four distinct Machine Learning architectures to predict the risk of heart disease. By using a **Consensus Engine**, the app cross-verifies patient data across multiple models to provide a highly reliable assessment.

<img width="1908" height="896" alt="image" src="https://github.com/user-attachments/assets/f320f920-67ca-4d78-9104-727a0958390b" />

🚀 **Live Demo:** [Click Here to View the App]((https://heartguardai-2004.streamlit.app/))

---
✨ Features
Individual Analysis: Real-time risk assessment for single patients.
Batch Processing: Upload a CSV file with up to 100+ patient records for instant screening.
AI Consensus: Uses Decision Tree, Logistic Regression, Random Forest, and SVM to verify results.
Modern Dark UI: A stunning, medical-grade dashboard optimized for readability.
Data Export: Download detailed batch reports as CSV files.

🛠️ Technology Stack
Frontend: Streamlit
Data Handling: Pandas, NumPy
Machine Learning: Scikit-Learn
Model Storage: Pickle

<img width="473" height="206" alt="image" src="https://github.com/user-attachments/assets/1ad89082-23de-4ace-891a-9fae86e19dd4" />

🚀 Local Installation
Clone the repository:


📊 How It Works
The system follows a 3-step pipeline:

Input: Clinical data (Age, BP, Cholesterol, etc.) is collected.

Processing: Data is normalized and fed into 4 different ML models.

Consensus: The app calculates the average "Risk Score." If the majority of models (>50%) flag the data, a "High Risk" alert is triggered.

📄 License
Distributed under the MIT License. See LICENSE for more information.

Disclaimer: This tool is for educational purposes only and should not be used as a substitute for professional medical advice.

---

## 🔍 Detailed Explanation of the README Sections

### 1. The Header & Deploy Link
* **The Title:** Clearly states what the project is.
* **Live Demo:** This is crucial. When you deploy (to Streamlit Community Cloud or Vercel), replace `YOUR_DEPLOYMENT_LINK_HERE` with the actual URL. It allows recruiters or users to try your app without downloading code.

### 2. Features
This section tells the user **why** they should use your app. Mentioning "Consensus Engine" makes your project sound more advanced than a basic single-model predictor.

### 3. Technology Stack
It lists the tools used. This is important for other developers who want to know if you used modern frameworks like Streamlit and Scikit-Learn.

### 4. Project Structure
A visual map of your files. This helps users understand where the models are and how the `app.py` relates to the `.pkl` files.

### 5. Local Installation
This is a step-by-step guide for someone who wants to run your code on their own computer.
* **Git Clone:** Downloads the code.
* **Requirements:** Installs all the necessary Python libraries (Pandas, Scikit-Learn, etc.) in one go.

### 6. The Pipeline Logic
This explains the "Brain" of your project. Instead of just saying "it predicts," you are explaining the **Consensus Strategy**, which adds intellectual value to your work.

---

## 🛠️ How to get your "Deploy Link"
1.  Push your code to **GitHub**.
2.  Go to [share.streamlit.io](https://share.streamlit.io).
3.  Connect your GitHub repository.
4.  Once it deploys, Streamlit will give you a URL (e.g., `https://heartguard-ai.streamlit.app`).
5.  **Copy that URL** and paste it into the README template above!
