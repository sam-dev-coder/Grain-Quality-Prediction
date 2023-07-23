# Import the required libraries
import streamlit as st
import pandas as pd
from joblib import load
import pickle

# Load all Models and Encoders
# Each model is a tuple of (model, shape encoder, color encoder, texture encoder)
models = {
  "Wheat": (load('Models/Wheat_model.pkl'), pickle.load(open('Encoders/Wheat_le_shape.pkl', 'rb')), pickle.load(open('Encoders/Wheat_le_color.pkl', 'rb')), pickle.load(open('Encoders/Wheat_le_texture.pkl', 'rb'))),
  "Rye": (load('Models/Rye_model.pkl'), pickle.load(open('Encoders/Rye_le_shape.pkl', 'rb')), pickle.load(open('Encoders/Rye_le_color.pkl', 'rb')), pickle.load(open('Encoders/Rye_le_texture.pkl', 'rb'))),
  "Barley": (load('Models/Barley_model.pkl'), pickle.load(open('Encoders/Barley_le_shape.pkl', 'rb')), pickle.load(open('Encoders/Barley_le_color.pkl', 'rb')), pickle.load(open('Encoders/Barley_le_texture.pkl', 'rb'))),
  "Rice": (load('Models/Rice_model.pkl'), pickle.load(open('Encoders/Rice_le_shape.pkl', 'rb')), pickle.load(open('Encoders/Rice_le_color.pkl', 'rb')), pickle.load(open('Encoders/Rice_le_texture.pkl', 'rb')))
}

# Define the possible values for each feature
shapes = {
    "Wheat": ["Long","Round", "Short","Irregular"],
    "Rye": ["Long","Oval","Round", "Short","Irregular"],
    "Barley": ["Oval","Elliptical"],
    "Rice":["Long", "Round", "Short","Irregular"]
}
colors = {
    "Wheat": ["White", "Yellow","Cream", "Brown","Black","Red"],
    "Rye": ["White", "Yellow","Cream", "Brown","Black","Red"],
    "Barley": ["White", "Yellow", "Red", "Black"],
    "Rice": ["White", "Yellow", "Cream","Brown","Black","Red"]
}
textures = {
    "Wheat": ["Smooth","Soft","Chewy","Creamy","Sticky","Firm","Nutty","Rough"],
    "Rye": ["Smooth","Soft","Chewy","Creamy","Sticky","Firm","Nutty","Rough","Hard"],
    "Barley": ["Hard", "Chewy"],
    "Rice":  ["Smooth", "Soft", "Chewy", "Creamy", "Sticky", "Firm", "Nutty", "Rough"]
}

def display_sidebar():
    """Display the sidebar with user input parameters.

    Returns:
        data: A dictionary of user input parameters.
        grain_type: A string of the selected grain type.
    """
    # Create a header for the sidebar
    st.sidebar.header('User Input Parameters')

    # Create a dropdown menu for the grain type
    grain_type = st.sidebar.selectbox('Grain Type', list(models.keys()))

    # Create a slider for the grain size
    size = st.sidebar.slider('Size', 0.0, 1.0, 0.5)

    # Create a dropdown menu for the grain shape
    shape = st.sidebar.selectbox('Shape', shapes[grain_type])

    # Create a dropdown menu for the grain color
    color = st.sidebar.selectbox('Color', colors[grain_type])

    # Create a dropdown menu for the grain texture
    texture = st.sidebar.selectbox('Texture', textures[grain_type])
    
    # Store the user input parameters in a dictionary
    data = {
        'Grain Size': [size],
        'Grain Shape': [shape],
        'Grain Color': [color],
        'Grain Texture': [texture],
    }

    # Return the data and the grain type
    return data, grain_type

def get_prediction(data, grain_type):
    """Get the prediction of the grain quality based on the user input parameters.

    Args:
        data: A dictionary of user input parameters.
        grain_type: A string of the selected grain type.

    Returns:
        prediction: A numpy array of the predicted quality.
    """
    # Convert the data into a pandas dataframe
    df = pd.DataFrame(data)

    # Handle encoding logic here
    # Get the model and the encoders for the selected grain type
    model, le_shape, le_color, le_texture = models[grain_type]

    # Encode the categorical features using the label encoders
    df['Grain Shape'] = le_shape.transform(df['Grain Shape'])
    df['Grain Color'] = le_color.transform(df['Grain Color'])
    df['Grain Texture'] = le_texture.transform(df['Grain Texture'])

    # Predict the quality using the model
    prediction = model.predict(df)

    # Return the prediction
    return prediction

def display_output(data, grain_type, prediction):
    """Display the output of the prediction in a dataframe.

    Args:
        data: A dictionary of user input parameters.
        grain_type: A string of the selected grain type.
        prediction: A numpy array of the predicted quality.
    """
    # Convert the data into a pandas dataframe
    df = pd.DataFrame(data)

    # Add the prediction column to the dataframe
    df["Quality Prediction"] = prediction

    # Display the dataframe using streamlit
    st.dataframe(df)

def main():
    """The main function of the app."""
    # Create a title for the app
    st.title('Grain Quality Predictor')

    # Write a brief introduction for the app
    st.write("This app predicts the quality of a grain based on its size, shape, color and texture.")

    # Get the user input parameters and the grain type from the sidebar
    data, grain_type = display_sidebar()

    # Get the prediction of the grain quality based on the user input parameters and the grain type
    prediction = get_prediction(data, grain_type)

    # Display the output of the prediction in a dataframe
    display_output(data, grain_type, prediction)

    # Display an image of grains using streamlit
    st.image("Images/1.jpg", width=5000)

if __name__ == "__main__":
    # Run the main function
    main()
