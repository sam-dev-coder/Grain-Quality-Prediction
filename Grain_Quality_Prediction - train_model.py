# Import the necessary libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump
import pickle

def train_and_save_models(grain_types, model_dir='Models/', encoder_dir='Encoders/'):
    """Train and save logistic regression models and label encoders for different grain types.

    Args:
        grain_types: A list of strings of the grain types.
        model_dir: A string of the directory where the models are saved.
        encoder_dir: A string of the directory where the encoders are saved.
    """
    # Loop over the grain types
    for grain_type in grain_types:
        # Read the data from a csv file
        grain = pd.read_csv(f'Dataset/{grain_type}_quality.csv')
        
        # Create encoders for each categorical feature
        le_shape = LabelEncoder()
        le_color = LabelEncoder()
        le_texture = LabelEncoder()
        
        # Encode categorical features using the encoders
        grain['Grain Shape'] = le_shape.fit_transform(grain['Grain Shape'])
        grain['Grain Color'] = le_color.fit_transform(grain['Grain Color'])
        grain['Grain Texture'] = le_texture.fit_transform(grain['Grain Texture'])
        
        # Split the data into features and target
        X = grain[['Grain Size', 'Grain Shape', 'Grain Color', 'Grain Texture']]
        y = grain['Quality']
        
        # Split data into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Create and fit the logistic regression model
        model = LogisticRegression()
        model.fit(X_train, y_train)
        
        # Make predictions on the test set and evaluate the model accuracy
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f'Accuracy of {grain_type} model: {accuracy}')
        
        # Save the model to a file
        dump(model, f'{model_dir}{grain_type}_model.pkl')
        
        # Save the encoders to files
        pickle.dump(le_shape, open(f'{encoder_dir}{grain_type}_le_shape.pkl', 'wb'))
        pickle.dump(le_color, open(f'{encoder_dir}{grain_type}_le_color.pkl', 'wb'))
        pickle.dump(le_texture, open(f'{encoder_dir}{grain_type}_le_texture.pkl', 'wb'))

# Specify the grain types
grain_types = ['Wheat', 'Rye', 'Barley', 'Rice']

# Run the function to train and save models and encoders
train_and_save_models(grain_types)
