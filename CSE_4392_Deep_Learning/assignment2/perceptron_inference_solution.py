# Name: Minh Trinh
# UTA ID: 1001705984
# Date Modified: 2/5/2023
# Description: 
#   Run the perceptron_inference_base.py file in order to test this function.
#   Takes in a bias weight, weight list, activation function of either step or
#   sigmoid, and an input list. Computes the "a" and "z" of the perceptrons

import math

def perceptron_inference(b, w, activation, input_vector):
    arr = [] # array used to store the results "a" and "z" later
    loop = len(w) # to loop through the bias and weight lists later
    dotProd = b # add bias to dotProd beforehand

    # loops through both the weights and input and finds the summation of their products
    for elem in range(loop):
        dotProd += w[elem] * input_vector[elem]
    arr.append(dotProd)

    # if activation is "step" does the step function as the activation function
    if (activation == "step"):
        if(dotProd < 0):
            arr.append(0)
        elif(dotProd >= 0):
            arr.append(1)
    # if activation is "sigmoid" does the sigmoid function as the activation function
    elif (activation == "sigmoid"):
        arr.append(1/(1+(pow(math.e,-dotProd))))

    return arr[0], arr[1]