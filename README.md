# &#x20;Titanic Survival Predictor

### Predicting Passenger Survival Using Machine Learning

The **Titanic Survival Predictor** is a machine learning web application that uses a trained Random Forest classifier to predict whether a passenger would have survived the Titanic disaster based on selected passenger information.

The application is built with Python and Streamlit, providing a simple and interactive interface for making predictions.

## &#x20;Live Application

**Try the application here:** https://omololafalusi17-star-titanic-demo-app-d7hegw.streamlit.app/

## 🎯 Project Objective

The objective of this project is to demonstrate how machine learning can be applied to a real-world historical dataset to identify patterns and make predictions.

It also demonstrates the process of developing, deploying, and presenting a machine learning model through an interactive web application.

## ✨ Features

- Predicts passenger survival using a trained Random Forest model.
- Interactive passenger information form.
- Quick sample presets for testing different passenger profiles.
- Displays survival or death predictions.
- Shows prediction probabilities.
- Deployed online using Streamlit Community Cloud.

## 🛠️ Technologies Used

- **Python** – Programming language.
- **Pandas** – Data manipulation and processing.
- **Scikit-learn** – Machine learning model development.
- **Random Forest Classifier** – Prediction algorithm.
- **Joblib** – Saving and loading the trained model.
- **Streamlit** – Web application development and deployment.
- **GitHub** – Version control and project hosting.

## 📊 Model Features

The model uses the following passenger information:

| Feature | Description                 |
| ------- | --------------------------- |
| Pclass  | Passenger class             |
| Sex     | Passenger sex               |
| Age     | Passenger age               |
| SibSp   | Siblings and spouses aboard |
| PaCh    | Parents and children aboard |
| Fare    | Passenger fare              |

## ⚙️ How It Works

1. The user enters passenger information.
2. The application processes the information into a Pandas DataFrame.
3. The trained Random Forest model receives the passenger information.
4. The model generates a survival prediction.
5. The application displays the predicted outcome and probability.

## &#x20;Project Structure

```text
titanic_demo/
│
├── app.py
│
├── Models/
│   └── forest_model.joblib
│
├── requirements.txt
│
└── README.md
```

## &#x20;Run Locally

Follow these steps to run the application on your computer.

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Navigate into the project folder**

```bash
cd titanic_demo
```

**3. Install the dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the Streamlit application**

```bash
streamlit run app.py
```

The application will open in your browser.

## 📈 What I Learned

Through this project, I gained practical experience in:

- Working with machine learning models.
- Preparing input data for model predictions.
- Using Random Forest for classification.
- Saving and loading trained models with Joblib.
- Building interactive applications with Streamlit.
- Deploying machine learning applications to the cloud.
- Managing projects using Git and GitHub.

## ⚠️ Disclaimer

This project is an educational machine learning demonstration. Its predictions are based on patterns learned from historical Titanic passenger data and should not be interpreted as definitive outcomes.

## &#x20;Author

**Falusi Omolola Oluwatobi**

Junior AI/ML Engineer | Women in AI Fellow 2026

- **GitHub:** [Omololafalusi](https://github.com/omololafalusi17-star)

---

⭐ If you find this project interesting, feel free to explore the repository and try the live application!
