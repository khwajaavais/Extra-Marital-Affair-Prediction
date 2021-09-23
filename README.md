
# EXTRA MARITAL AFFAIR PREDICTION

## PROJECT DESCRIPTION
The context of this project is to predict the Extra Marital Affairs of the Woman/Wife
using Logistic Regression Machine Learning algorithm which played an important role in predicting 
whether women are involve in extra marital affairs or not  using various independent features.

## AIM & OBJECTIVE
The aim of this project is to investigate the Logistic Regression Algorithm executed in various areas and evaluate the performance of the chosen machine learning
algorithms to find out the best suitable and efficient model for the chosen data set.

#### OBJECTIVE
- To understand the efficient machine learning technique for predicting the marital affairs.
- To evaluate the performance of the selected machine learning algorithm.

## ABOUT THE DATA
    The affairs dataset that comes with Stats-Models as my dataset. 
    It was based on a women's study conducted by Red Book magazine in 1974, in which married women were asked about their involvement in extramarital affairs. 
    By generating a new binary variable affair (did the woman have at least one affair?) and attempting to forecast the classification for each woman, I opted to approach this as a Classification Problem.

    Attribute Information (in order):
        - Rate_marriage     Women’s rating for her marriage 
        - Age               Women’s age
        - Years_married     Number of Years Married 
        - Children          No. of children she has
        - Religious         on the scale of 1 -5 whether she believe in religion or not 
        - Education         Level of education
        - Occupation 
        - Occupation of husband 
        - Affairs

    Missing Attribute Values: None

## TECHNICAL ASPECTS

#### DATA PREPROCESSING
- Converting the Target Attribute(Affairs) in Binary Class in order to make it a Classification Problem.
    
        - If the value of the Target Attribute is 0 --> No Extra Marital Affair Found.
        - If the value of the Target Attribute is 1 --> Extra Marital Affair Found.

- Used Dmatrics to analyze the independent and the dependent attribute and to add some data if need to predicted the solution.

- Checked for null Values within the dataset.

#### STATISTICAL ANALYSIS OF DATA
- Description of the Data
        
        Data.describe()

- Finding the Correlation

        Data.corr()

- Shape of the Data

        print(df[df["affairs"]==0].shape)
        print(df[df["affairs"]==1].shape)
   
        [out]>> (4313, 18)
                (2053, 18)

**Our Dataset is imbalance as Class 0 is almost the double of Class 1. So we need to up-sample to balance the dataset.**

        from imblearn.random_sampling  import RandomOverSampler
    
        rdm=RandomOverSampler()
        X,y=rdm.fit_sample(X,y)

        print(Data[Data["affairs"]==0].shape)
        print(Data[Data["affairs"]==1].shape)

        [out]>> (4313, 18)
                (4313, 18)

**Now our Data is balance and good to go for the Classification Stage.**

#### IMPLEMENTATION OF LOGISTIC REGRESSION

        lr = LogisticRegression()

        lr.fit(x_train,y_train)
        y_predicted = lr.predict(x_test)

#### EVALUATION
For Evaluation of the Logistic Regression, I used various Matrics :

1. Accuracy Matrix
2. COnfusion Matrix
3. Precision, Recall and the F1 Score

## MODEL DEPLOYMENT

**LOCALHOST**

For implementating the project in your own system follow the steps;

- Download the directory
- Open the Command Prompt (CLI) and change the command line path to this current file path.
- Run the command

        python app.py

- Hit http://127.0.0.1:5000/


WEB APPLICATION

For deploying the project via Heroku platform

Follow Krish Naik`s Deployment of ML models in Heroku using Flask 
https://www.youtube.com/watch?v=mrExsjcvF4o

**Note**: Mandatory Files required while deploying ML Model in Heroku using Flask

1. app.py
2. Procfile
3. model.pkl file (Pickle File)
4. request.py
5. requirement.txt
6. templates / index.html (UI File)
7. static/css/ style.css
(You can use my Repository to follow the steps)


## INSTALLATION
The Code is written in Python 3.7. If you don't have Python installed you can find it [there](https://www.python.org/downloads/)
. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. 
To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:

    pip install -r requirements.

## Conclusion and Future Work
- Implementation of Logistic Regression Algorithm for the Predicting Extra Marital Affair is successful.

- Implementation of Logistic Regression can be done in all the Supervised Learning Data.

## Screenshots

**DEMO:  https://marital-affair-prediction04.herokuapp.com/**

### INDEX PAGE
![App Screenshot](https://github.com/khwajaavais/Extra-Marital-Affair-Prediction/blob/fbd960dbdbe416b9e8e54b6ef95e102bf6ddd1c8/templates/127.0.0.1_5000_(screenshot)%20(1).png)

### RESULT PAGE
![App Screenshot](https://github.com/khwajaavais/Extra-Marital-Affair-Prediction/blob/fbd960dbdbe416b9e8e54b6ef95e102bf6ddd1c8/templates/127.0.0.1_5000_predict(screenshot)%20(1).png)
  