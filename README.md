# ANN-Iris
Activation function is a very important feature of an artificial neural network and basically decides, whether a neuron will be activated or not.
Generally, neural networks use non-linear activation functions, which help them to learn complex data and learn from functions to predict results accurately.
Instead of sigmoid or tanh AF, I used ReLU( Rectified Linear Unit) in hidden layer as it rectifies the vanishing gradient problem, and is also less computationally expensive.
I used Softmax AF in the output layer, as it can handle multiple classes.
I used SGD as Optimizer instead of Adam, even though it is slower, because Adam has convergence problems.
Since my target classes are mutually exclusive, I used sparse categorical crossentropy instead of categorical classentropy.
