# Delivery_Time_Predictor
predict delivery time en fonction de parameter like the weather, distance, traffic, etc... 
# Project Title

Delivery Time Predictor

## Description

This project is about predicting the delivery time of a parcel based on different parameters like the weather, distance, traffic, etc... 

## Getting Started

### Dependencies

* Python 3.7
* Jupyter Notebook
* Pandas
* Numpy
* Scikit-learn
* Matplotlib
* Seaborn

### Installing

* Install Python 3.7
* Install Jupyter Notebook
* Install Pandas
* Install Numpy
* Install Scikit-learn
* Install Matplotlib
* Install Seaborn

### Executing program

* Run the jupyter notebook and open the Delivery Time Predictor.ipynb
* Run all the cells in the notebook
* The model will be trained and tested on the data
* The model will be saved in a file called 'delivery_time_predictor.pkl'
* You can use this model to predict the delivery time of a parcel


- Download the requirment.txt in the back and front. 

- Start the back using this line 
```sh 
uvicorn main:app --reload
```

- Start the front using this line 
```sh
python app.py
```

- Start MLFlow using this line 
```sh
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns
```
## Authors

Contributors names and contact info

PAILLOT Jefferson
HAYEK Sofiene