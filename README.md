# Mobile Price Predictor with IBM Watson and Streamlit

Welcome to the Mobile Price Predictor repository! This application is built using Jupyter Notebooks, Streamlit for the frontend, and IBM Watson for deploying the machine learning model. By accessing the model via API, users can predict mobile prices with ease. The application is hosted live at [https://mobile.streamlit.app/](https://mobile.streamlit.app/).

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation & Setup](#installation--setup)
4. [Usage](#usage)
5. [Deployment](#deployment)
6. [Contribution Guidelines](#contribution-guidelines)
7. [License](#license)

## Introduction

The Mobile Price Predictor application is designed to help users estimate the price of mobile devices based on their features. The machine learning model is trained on a dataset of mobile features and corresponding prices, providing accurate predictions for a wide range of devices. By leveraging IBM Watson services and Streamlit for the frontend, the application offers a user-friendly interface and seamless deployment.

## Features

- Intuitive web-based user interface powered by Streamlit
- Machine learning model deployment via IBM Watson services
- API integration for easy access to the deployed model
- Jupyter Notebook for model training, evaluation, and demonstration

## Installation & Setup

To set up the Mobile Price Predictor application on your local machine, follow these steps:

1. Clone the repository using 
```
git clone https://github.com/Briankim254/IBM-Watson-and-Sreamlit-deployment-of-mobile-price-predictor.git
```
2. Navigate to the project directory using 
```
cd IBM-Watson-and-Sreamlit-deployment-of-mobile-price-predictor
```
3. Create a virtual environment and activate it
4. Install the required dependencies using 
```
pip install -r requirements.txt
```
5. Open the Jupyter Notebook to explore the model training and evaluation process

## Usage

1. Run the Streamlit application locally using `streamlit run app.py`
2. Access the application in your web browser at `http://localhost:8501`
3. Input the mobile features into the corresponding fields
4. Click the "Predict" button to receive an estimated mobile price based on the input features

## Deployment

The Mobile Price Predictor application is deployed using Streamlit and hosted live at [https://mobile.streamlit.app/](https://mobile.streamlit.app/). The machine learning model is deployed via IBM Watson services and is accessed using an API for seamless integration.

## Contribution Guidelines

We welcome contributions to improve and expand the Mobile Price Predictor application. To contribute, please follow these steps:

1. Fork the repository and create a new branch for your changes
2. Make your changes or additions to the project
3. Create a pull request and wait for a review from a team member

Please ensure that your code adheres to best practices for code quality and documentation.

## License

The Mobile Price Predictor application is licensed under the [MIT License](LICENSE). This allows for open collaboration and sharing of the application while ensuring that contributors retain ownership of their work.
