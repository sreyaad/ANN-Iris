
# Multi-Class Classification using Iris dataset

This is a Python project for Classification of Iris species into Setosa, Versicolor and Virginica.


## Motivation
I started this project as a motivation to learn about different Machine Learning and Deep Learning Algorithms.
## Data Collection
- The dataset is collected from Kaggle.
- This dataset consists of 3 categories of species which is setosa, versicolor and virginica.
- We can find the Iris dataset in .csv file
- Each iris species consists of 50 samples.
- The features of iris flower are Sepal Length in cm, Sepal Width in cm, Petal Length in cm and Petal Width in cm.
## Dependencies
    pip install -r requirements.txt

## Project Description
- The project is based on Deep Learning framework.
- Only 1 hidden layer has been used while designing the neural netwok.
- In hidden layer, I have used `relu` as the activation function, as it solves the vanishing gradient problem.
- In the output layer, I have used `Softmax` as the activation function, as it is a multi-class classification problem.
- As optimizer, `stochastic gradient descent` have been used.
- In the loss function, `sparse categorical crossentropy` have been used.

## Results
 The model achieved **76.85%** accuracy on **training data** and an accuracy of **97.78%** on **test data**.