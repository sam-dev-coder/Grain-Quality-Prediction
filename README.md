# Grain Quality Predictor

The project is a web application that predicts grain quality based on size, shape, color, and texture. It utilizes logistic regression models and label encoders trained on a grain quality dataset. The user interacts with the application through a user-friendly interface built with streamlit widgets and functions.

## Description

This project is a web application that can predict the quality of different types of grains based on their size, shape, color, and texture. The project uses logistic regression models and label encoders that were trained and saved using a dataset of grain quality. The web application provides a user-friendly interface for inputting and displaying the data and predictions using streamlit widgets and functions. The web application can also run on a local or remote server using flask.

## Installation

To run this project, you will need the following:

- Python 3
- Anaconda
- Streamlit
- Flask
- Pandas
- Sklearn
- Joblib
- Pickle

You can install these packages using the following commands:

```
conda install -c anaconda pandas
conda install -c anaconda scikit-learn
conda install -c anaconda joblib
pip install streamlit
pip install flask
```

You will also need to clone this repository to your local machine using the following command:

```
git clone https://github.com/YOUR-USERNAME/Grain-Quality-Predictor.git
```

## Usage

To run this project, you will need to do the following steps:

1. Navigate to the project directory using the terminal or console.
2. Run the streamlit app using the following command:

```
streamlit run '.\Grain_Quality_Prediction - Web App.py'
```

3. Open your browser and go to the URL that streamlit provides (usually http://localhost:8501).
4. Use the sidebar to input the grain type, size, shape, color, and texture of your grain sample.
5. See the output data and prediction on the main page.
6. Enjoy!

## Contributing

This project is open for contributions. If you want to contribute to this project, you can do the following:

- Fork this repository to your GitHub account.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with clear and descriptive messages.
- Push your changes to your forked repository.
- Create a pull request to the main branch of this repository.
- Wait for your pull request to be reviewed and merged.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
