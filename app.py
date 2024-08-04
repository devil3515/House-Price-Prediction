from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer

app = Flask(__name__)

# Load the model and preprocessing tools
with open('model1.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the feature columns (match with your dataset columns) 
categorical_columns = ['Pool', 'Central Air', 'Heating Type', 'Crime Rate']
numerical_columns = ['Square Footage', 'Bedrooms', 'Bathrooms', 'Floors', 'Garage', 'Distance to City Center', 'Property Tax', 'Previous Sale Price']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data
    form_data = {
        'Square Footage': float(request.form['Square Footage']),
        'Bedrooms': float(request.form['Bedrooms']),
        'Bathrooms': float(request.form['Bathrooms']),
        'Floors': int(request.form['Floors']),
        'Garage': int(request.form['Garage']),
        'Pool': request.form.get('Pool'),
        'Central Air': request.form.get('Central Air'),
        'Heating Type': request.form.get('Heating Type'),
        'Distance to City Center': float(request.form['Distance to City Center']),
        'Crime Rate': request.form.get('Crime Rate'),
        'Property Tax': float(request.form['Property Tax']),
        'Previous Sale Price': float(request.form['Previous Sale Price'])
    }

    # Convert form data to DataFrame
    df = pd.DataFrame([form_data])
    print(df)
    
#     labelencoder = LabelEncoder()

# # Apply LabelEncoder to each categorical column
#     categorical_columns = ['Pool', 'Central Air', 'Heating Type', 'Crime Rate']
#     for col in categorical_columns:
#         df[col] = labelencoder.fit_transform(df[col])



#     scaler = StandardScaler()
# # Scale the numerical features
#     numerical_columns = ['Square Footage', 'Bedrooms', 'Bathrooms', 'Floors', 'Garage', 'Distance to City Center', 'Property Tax', 'Previous Sale Price']
#     df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

    
    # Predict the price
    prediction = model.predict(df)[0]
    
    return render_template('index.html', prediction=prediction)


@app.route('/popout')
def popout():
    return render_template()

if __name__ == '__main__':
    app.run(debug=True)
