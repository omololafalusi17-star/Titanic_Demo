import joblib
import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Titanic Survival Predictor", page_icon="🚢")

# Load the trained model safely using path resolution
@st.cache_resource
def load_model():
    model_path = Path(__file__).parent / "models" / "forest_model.joblib"
    return joblib.load(model_path)

random_forest = load_model()

# Prediction logic
def predict_survival(name, Pclass, Sex, Age, SibSp, PaCh, Fare):
    input_data = pd.DataFrame({
        "Pclass": [Pclass],
        "Sex": [Sex],
        "Age": [Age],
        "SibSp": [SibSp],
        "PaCh": [PaCh],
        "Fare": [Fare],
    })

    prediction = random_forest.predict(input_data)[0]
    probabilities = random_forest.predict_proba(input_data)[0]

    name = name.strip().title() or "Passenger"
    if prediction == 0:
        result = f"Wooo 😮 {name}, you Died 😢"
    else:
        result = f"Cheers 🥂 {name}, you Survived 😁"

    return prediction, result, probabilities

# UI Elements
st.title("Titanic Survival Predictor")
st.write("Enter a passenger's details and see if our random forest thinks they'd survive.")

# Presets/Examples Section (Safely triggers re-runs to populate fields)
st.subheader("Quick Presets")
col_ex1, col_ex2 = st.columns(2)

if col_ex1.button("👩‍💼 Sample: 1st Class Female"):
    st.session_state["name"] = "Rose DeWitt Bukater"
    st.session_state["pclass"] = 1
    st.session_state["sex"] = 1
    st.session_state["age"] = 17
    st.session_state["sibsp"] = 0
    st.session_state["pach"] = 1
    st.session_state["fare"] = 150.0
    st.rerun()

if col_ex2.button("🧑‍🎨 Sample: 3rd Class Male"):
    st.session_state["name"] = "Jack Dawson"
    st.session_state["pclass"] = 3
    st.session_state["sex"] = 0
    st.session_state["age"] = 20
    st.session_state["sibsp"] = 0
    st.session_state["pach"] = 0
    st.session_state["fare"] = 7.5
    st.rerun()

# Form configuration with fallbacks for preset injection
with st.form("passenger_form"):
    name = st.text_input("Name", placeholder="e.g. Benjamin Ogbonna", key="name")
    
    pclass = st.radio(
        "Passenger Class (1 = First)", [1, 2, 3],
        index=[1, 2, 3].index(st.session_state.get("pclass", 3)),
        horizontal=True
    )
    
    sex = st.radio(
        "Sex", [0, 1],
        index=[0, 1].index(st.session_state.get("sex", 0)),
        format_func=lambda x: "Male" if x == 0 else "Female",
        horizontal=True
    )
    
    age = st.slider("Age", 0, 80, int(st.session_state.get("age", 30)), step=1)

    c1, c2, c3 = st.columns(3)
    sibsp = c1.number_input("Siblings/Spouses aboard", min_value=0, step=1, value=int(st.session_state.get("sibsp", 0)))
    pach = c2.number_input("Parents/Children aboard", min_value=0, step=1, value=int(st.session_state.get("pach", 0)))
    fare = c3.number_input("Fare paid (£)", min_value=0.0, step=1.0, value=float(st.session_state.get("fare", 30.0)))

    submitted = st.form_submit_button("Predict", type="primary")

# Evaluation Output
if submitted:
    prediction, result, probabilities = predict_survival(
        name, pclass, sex, age, sibsp, pach, fare
    )

    st.subheader("Prediction Result")
    if prediction == 0:
        st.error(result)
        st.metric(label="Death Probability", value=f"{probabilities[0]:.1%}")
    else:
        st.success(result)
        st.metric(label="Survival Probability", value=f"{probabilities[1]:.1%}")
