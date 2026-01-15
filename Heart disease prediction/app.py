import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import io

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="HeartGuard AI", 
    page_icon="❤️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ADVANCED CUSTOM CSS FOR DARK THEME ---
st.markdown("""
    <style>
    /* Main background and text */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }

    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #161b22;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        color: #8b949e;
    }

    .stTabs [aria-selected="true"] {
        background-color: #1f2937;
        color: #ff4b4b !important;
        border-bottom: 2px solid #ff4b4b !important;
    }

    /* Cards/Containers */
    div[data-testid="stVerticalBlock"] > div:has(div.stMetric) {
        background-color: #1c2128;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363d;
    }

    /* Professional Button */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        background: linear-gradient(45deg, #ff4b4b, #ff7575);
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255, 75, 75, 0.4);
    }

    /* Inputs */
    .stNumberInput input, .stSelectbox div {
        background-color: #0d1117 !important;
        color: white !important;
        border: 1px solid #30363d !important;
    }
    
    h1, h2, h3, h5 {
        color: #f0f6fc;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MODEL LOADING ---
@st.cache_resource
def load_models():
    """
    Load all ML models from disk.
    Uses the directory of this file instead of the current working directory
    so that it also works when Streamlit runs the app from the repo root.

    Returns
    -------
    (dict, list[tuple[str, str]]):
        - dict of successfully loaded models
        - list of (model_name, error_message) for any failures
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))

    algonames = ['Decision Tree', 'Logistic Regression', 'Random Forest', 'Support Vector Machine']
    model_filenames = ['DecisionTree.pkl', 'LogisticRegression.pkl', 'GridRandomForest.pkl', 'SVM.pkl']

    loaded_models = {}
    load_errors = []

    for name, filename in zip(algonames, model_filenames):
        model_path = os.path.join(base_dir, filename)
        if not os.path.exists(model_path):
            load_errors.append((name, f"File not found at: {model_path}"))
            continue

        try:
            with open(model_path, 'rb') as f:
                loaded_models[name] = pickle.load(f)
        except Exception as e:
            load_errors.append((name, f"{type(e).__name__}: {e}"))

    return loaded_models, load_errors

models_dict, model_load_errors = load_models()

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>❤️ HeartGuard</h1>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/822/822118.png", width=80)
    st.markdown("---")
    st.markdown("### 🧬 AI Consensus Engine")
    st.write("Current Status: **Operational**")
    st.write("Models Loaded: **4 Active**")
    st.divider()
    st.caption("© 2026 Medical AI Solutions. For educational use only.")

# --- MAIN CONTENT ---
tab1, tab2, tab3 = st.tabs(["🎯 ANALYSIS DASHBOARD", "📁 BATCH PROCESSING", "ℹ️ SYSTEM INFO"])

with tab1:
    st.markdown("### 📊 Patient Clinical Profile")
    
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("##### 👤 Basics")
            age = st.number_input("Age", min_value=0, max_value=120, value=45)
            sex_raw = st.selectbox("Sex", ["Male", "Female"])
            chest_pain_raw = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
        
        with col2:
            st.markdown("##### 🩺 Vitals")
            resting_bp = st.number_input("Resting BP (mm Hg)", min_value=0, max_value=300, value=125)
            cholesterol = st.number_input("Cholesterol (mg/dl)", min_value=0, value=210)
            fasting_bs_raw = st.selectbox("Fasting Blood Sugar", ["<= 120 mg/dl", "> 120 mg/dl"])
            
        with col3:
            st.markdown("##### ⚡ Diagnostics")
            max_hr = st.number_input("Max Heart Rate", min_value=60, max_value=220, value=140)
            exercise_angina_raw = st.selectbox("Exercise Angina", ["No", "Yes"])
            st_slope_raw = st.selectbox("ST Slope", ["Upsloping", "Flat", "Downsloping"])

        with st.expander("Advanced Clinical Markers"):
            ae_col1, ae_col2 = st.columns(2)
            with ae_col1:
                resting_ecg_raw = st.selectbox("Resting ECG", ["Normal", "ST-T Wave Abnormality", "LV Hypertrophy"])
            with ae_col2:
                oldpeak = st.number_input("ST Depression (Oldpeak)", min_value=0.0, max_value=10.0, step=0.1, value=1.0)

    # Transform Data
    sex = 1 if sex_raw == "Male" else 0
    chest_pain = ["Atypical Angina", "Non-Anginal Pain", "Asymptomatic", "Typical Angina"].index(chest_pain_raw)
    fasting_bs = 1 if fasting_bs_raw == "> 120 mg/dl" else 0
    resting_ecg = ["Normal", "ST-T Wave Abnormality", "LV Hypertrophy"].index(resting_ecg_raw)
    exercise_angina = 1 if exercise_angina_raw == "Yes" else 0
    st_slope = ["Upsloping", "Flat", "Downsloping"].index(st_slope_raw)

    input_data = pd.DataFrame({
        'Age': [age], 'Sex': [sex], 'ChestPainType': [chest_pain],
        'RestingBP': [resting_bp], 'Cholesterol': [cholesterol], 'FastingBS': [fasting_bs],
        'RestingECG': [resting_ecg], 'MaxHR': [max_hr], 'ExerciseAngina': [exercise_angina],
        'Oldpeak': [oldpeak], 'ST_Slope': [st_slope]
    })

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("EXECUTE HEART ANALYSIS"):
        if not models_dict:
            st.error("Missing system files.")
            if model_load_errors:
                with st.expander("View technical details"):
                    for name, msg in model_load_errors:
                        st.write(f"**{name}** → {msg}")
        else:
            st.divider()
            res_cols = st.columns(len(models_dict))
            preds = []
            
            for idx, (name, model) in enumerate(models_dict.items()):
                p = model.predict(input_data)[0]
                preds.append(p)
                with res_cols[idx]:
                    if p == 1:
                        st.metric(label=name, value="⚠️ RISK", delta="Detected", delta_color="inverse")
                    else:
                        st.metric(label=name, value="✅ CLEAR", delta="Healthy", delta_color="normal")
            
            # Final Result Card
            risk_score = sum(preds) / len(preds)
            if risk_score > 0.5:
                st.markdown(f"<div style='padding:20px; border-radius:10px; background-color:#4a0e0e; border: 1px solid #ff4b4b;'><h3>High Priority Alert</h3>Consensus suggests elevated risk markers ({risk_score*100:.0f}% Agreement).</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='padding:20px; border-radius:10px; background-color:#0e2a14; border: 1px solid #2ea44f;'><h3>Cardiac Health Stable</h3>Consensus indicates low risk of heart disease.</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("### 📁 Batch Processing")
    uploaded_file = st.file_uploader("Drop patient CSV file here", type="csv")
    if uploaded_file:
        df_bulk = pd.read_csv(uploaded_file)
        if st.button("PROCESS BATCH"):
            results_df = df_bulk.copy()
            for name, model in models_dict.items():
                results_df[f'{name}'] = model.predict(df_bulk).astype(str)
                results_df[f'{name}'] = results_df[f'{name}'].replace({'1': 'Risk', '0': 'Healthy'})
            st.dataframe(results_df, use_container_width=True)
            
            # Export
            csv_buffer = io.StringIO()
            results_df.to_csv(csv_buffer, index=False)
            st.download_button("📥 DOWNLOAD REPORT", data=csv_buffer.getvalue(), file_name="batch_report.csv")

with tab3:
    st.markdown("### ℹ️ Core Technologies")
    st.write("HeartGuard AI utilizes an ensemble approach, combining multiple mathematical strategies to verify findings.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        **Neural Strategies:**
        * **Decision Trees:** Rule-based logic paths.
        * **Random Forests:** Aggregated decision voting.
        """)
        
    with col_b:
        st.markdown("""
        **Statistical Strategies:**
        * **Logistic Regression:** Probability curve analysis.
        * **SVM:** Multi-dimensional spatial separation.
        """)
        
    
    st.divider()
    st.markdown("<p style='text-align: center;'>Our system uses <b>Consensus Voting</b>: Results are cross-verified by all four models before a final assessment is generated.</p>", unsafe_allow_html=True)

    # Diagnostics for model loading (to help when deploying)
    st.markdown("#### 🔍 Model Loading Diagnostics")
    if models_dict:
        st.success(f"{len(models_dict)} models loaded successfully.")
    else:
        st.error("No models loaded. See details below.")

    if model_load_errors:
        for name, msg in model_load_errors:
            st.write(f"- **{name}**: {msg}")
    else:
        st.caption("No model loading errors reported.")
