# AI-Based Early Autism Screening Tool

# multimodal autism screening tool???
A machine learning-powered screening tool to assist in the early detection of Autism Spectrum Disorder (ASD) using publicly available datasets and explainable AI.  
This project is designed for educational and demonstration purposes, showcasing practical AI/ML development with real-world healthcare applications.

---

## Project Overview

Autism diagnosis is a complex and multi-step process, often delayed due to limited access to screening resources.  
This tool simulates a lightweight, privacy-respecting screening assistant that takes user inputs (age, behavioral traits, etc.) and predicts the likelihood of ASD using both traditional machine learning models and deep learning techniques (e.g., Deep Neural Networks).  
It also provides explainability insights using SHAP to interpret model predictions.  

Future extensions may incorporate visual data (e.g., eye-tracking) and deep learning models such as CNNs and RNNs to enhance diagnostic accuracy.

---

## Features

- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Classification model (Logistic Regression, Random Forest, XGBoost)
- Model explainability with SHAP
- Streamlit-based web interface for user interaction
- Optional: AI-generated diagnosis summary using OpenAI

---
### Project Structure

autism-screening-ai-tool/
│
├── data/                  # Dataset files (raw and cleaned)
├── notebooks/             # EDA, model training, and evaluation notebooks
├── app/                   # Streamlit app code (user input, prediction)
├── explainability/        # SHAP or LIME explanation visualizations
├── images/                # Screenshots, diagrams, flowcharts
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── LICENSE                # License file (optional)


---

## 📊 Dataset

- **Source**: [Autism Screening Adult Dataset - UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/Autism+Screening+Adult)
- Features: Age, gender, family history, responses to 10 behavioral screening questions
- Target: ASD classification (ASD or Not ASD)

---

## 🔍 Model Performance (coming soon)

| Model              | Accuracy | Precision | Recall | F1 Score |
|-------------------|----------|-----------|--------|----------|
| Logistic Regression | -        | -         | -      | -        |
| Random Forest      | -        | -         | -      | -        |
| XGBoost            | -        | -         | -      | -        |

*(To be updated after model training)*

---

## Explainability

This tool includes SHAP-based explanations to help users and developers understand which features influenced the prediction and to what extent.

---

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/JismaChoudhury/autism-screening-ai-tool.git
cd autism-screening-ai-tool

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run Streamlit app
streamlit run app/app.py

🌐 Live Demo

🚧 Coming soon — to be deployed on Hugging Face Spaces or Render.

⚠️ Disclaimer

This tool is developed for educational purposes only.
It is not a certified diagnostic tool and should not be used for real-world medical decision-making.
Always consult a qualified healthcare provider for diagnosis or treatment.

🧑‍💻 Author

Jisma Choudhury
Senior AI Engineer | Full-Stack Developer | Specialising in RAG, AI Agents & LLM Applications

📄 License

This project is licensed under the MIT License.
See the LICENSE file for more information.


---

### ✅ Next Steps:
1. Create folders (`data`, `notebooks`, `app`, etc.)
2. Add a placeholder file like `.gitkeep` in empty folders so they show up on GitHub
3. Push this `README.md` to your GitHub repo
4. Start working on notebooks or the app — and commit as you go

Let me know if you want help generating your `requirements.txt` file next or a starter notebook to begin with!


