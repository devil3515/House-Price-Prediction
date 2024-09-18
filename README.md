# 🏠 House Price Prediction

**A machine learning project that predicts house prices based on various factors like location, size, and the number of rooms. This project uses multiple algorithms to build predictive models and provides a web interface for real-time predictions.**

## 📋 Overview

The goal of this project is to accurately predict house prices using a dataset of historical housing data. The project involves data preprocessing, model building, evaluation, and deployment using a simple Flask web application.

## 🚀 Features
- **Machine Learning Models**: Predict house prices using **Linear Regression**, **Random Forest**, and other algorithms.
- **Data Preprocessing**: Handling missing values, encoding categorical variables, and scaling numerical features.
- **Model Evaluation**: Model performance is evaluated using metrics such as **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)**.
- **Flask Web App**: An interactive web interface where users can input house features and get price predictions in real-time.

## ⚙️ Tech Stack
- **Languages**: Python
- **Libraries**: 
  - Pandas
  - NumPy
  - Scikit-learn
  - **Framework**: Flask (for web application)
- **Tools**: Jupyter Notebook, Git

## 📂 Project Structure
```
├── app.py              # Flask application
├── model.py            # Code for training and saving the model
├── templates/          # HTML templates for web pages
│   └── index.html      # Main page for house price prediction
├── static/             # CSS and image files
├── data/               # Dataset (CSV file)
├── notebooks/          # Jupyter notebooks for data analysis and model development
├── models              # Saved machine learning model

```

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/house-price-prediction.git
   cd house-price-prediction
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000/` to access the web app.

## 🛠️ Usage
- Launch the Flask web app.
- Input the house features such as location, square footage, number of bedrooms, and bathrooms.
- Click "Predict" to get the predicted house price.

## 📊 Data Preprocessing
The dataset used in this project required:
- **Handling missing values** in important features like house size and price.
- **Encoding categorical variables** such as neighborhood and house type.
- **Feature scaling** to standardize the data for optimal model performance.

## 🧠 Machine Learning Models
- **Linear Regression**: A simple model to get baseline predictions.
- **Random Forest**: A more robust model that performs well with larger datasets and multiple features.
- **Model Evaluation**: Used cross-validation and hyperparameter tuning to optimize the models for better accuracy.

## 📈 Results
The models were evaluated using:
- **MAE (Mean Absolute Error)**: Measures the average magnitude of the errors.
- **RMSE (Root Mean Squared Error)**: Penalizes larger errors more heavily than MAE.

The Random Forest model showed the best performance with the lowest RMSE.

## 💡 Future Improvements
- Add more advanced models like **Gradient Boosting** for better accuracy.
- Implement a more feature-rich web interface with dynamic visualizations.
- Incorporate additional features such as market trends and neighborhood crime rates.

## 👨‍💻 Contributors
- **Abhishek Kumar** - Developer and Data Scientist
