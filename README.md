# 🧠 Diabetes Prediction Using LVQ

This is a simple web-based application built with **Streamlit** that predicts the likelihood of diabetes based on medical data inputs. The prediction is powered by the **Learning Vector Quantization (LVQ)** machine learning algorithm.

## 🚀 Features

- Interactive input form for medical indicators such as glucose, BMI, and insulin levels.
- Uses a pre-trained LVQ model to classify whether a user has diabetes.
- Real-time prediction result with clear output.
- Lightweight and easy to deploy.

⚠️ **Model Accuracy:**  
The current LVQ model achieves an accuracy of **71%** on test data. While this shows initial promise, we plan to improve performance in future iterations through better preprocessing, feature selection, or alternative model architectures.

## 🧬 About LVQ (Learning Vector Quantization)

**Learning Vector Quantization (LVQ)** is a prototype-based supervised classification algorithm. It uses a set of codebook vectors (also called weights) to represent class prototypes in the feature space. During prediction, the algorithm calculates the distance between an input and these prototypes and assigns the input to the class of the nearest prototype.

**Why LVQ?**
- Simple and fast for real-time prediction.
- Effective for low-dimensional data like structured medical records.
- Interpretable decision-making process based on distances.

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/diabetes-lvq-app.git
   cd diabetes-lvq-app
    ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

Make sure you have the model_lvq.pkl file in the same directory as app.py.


## 📝 Input Fields

| Feature                  | Description                                 |
| ------------------------ | ------------------------------------------- |
| Pregnancies              | Number of times pregnant                    |
| Glucose                  | Plasma glucose concentration                |
| BloodPressure            | Diastolic blood pressure (mm Hg)            |
| SkinThickness            | Triceps skin fold thickness (mm)            |
| Insulin                  | 2-Hour serum insulin (mu U/ml)              |
| BMI                      | Body Mass Index                             |
| DiabetesPedigreeFunction | Function that scores likelihood of diabetes |


## 📊 Output

  - Positive Diabetes (1) — Likely to have diabetes.
  - Negative Diabetes (0) — Not likely to have diabetes.

The result is displayed immediately after clicking the Start button.

## Credits

This application is built using domain knowledge in diabetes prediction and LVQ modeling. 
