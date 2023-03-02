# Name: Minh Trinh
# UTA ID: 1001705984
# Date Modified: 2/8/2023
# Description: 

import numpy as np
import math

def nn_inference(layers, units, biases, weights, activation, input_vector):
    A = [] # Used to store the vectors of alphas
    Z = [] # Used to store the vectors of Zs
    Z.append(input_vector)

    input_vector = np.array(input_vector).transpose().flatten()
    for lay_num in range(2, layers+1):
        
        atemp = []
        ztemp = []

        for unit_num in range(units[lay_num]):

            Z_placeholder = 0

            if (lay_num == 1):
               # Z_placeholder = input_vector[unit_num]
                #Z_vector[unit_num] = Z_placeholder
                #_vector[unit_num] = Z_placeholder
                skip = 0
            else:  

                # print(np.dot(weights[2][0], input_vector))

                # Calculates the dot product for 'a' of a unit
                
                A_placeholder =  np.dot(weights[lay_num][unit_num], input_vector) + biases[lay_num][unit_num][0] 
                if (activation == "step"):
                    if(A_placeholder < 0):
                        Z_placeholder = 0
                    elif(A_placeholder >= 0):
                        Z_placeholder = 1
                elif (activation == "sigmoid"):
                    Z_placeholder = 1/(1 + (pow(math.e, -A_placeholder)))
            
                # A_vector[unit_num] = A_placeholder
                # Z_vector[unit_num] = Z_placeholder
            ztemp.append(Z_placeholder)
            atemp.append(A_placeholder)
        A.append(atemp)
        Z.append(ztemp)
        input_vector = np.array(ztemp)

    A_np = np.array(A, dtype=object)
    Z_np = np.array(Z, dtype=object)
    # print(A_np[0])
    # print(Z_np.shape[0])
    # print(A_np.reshape(2,1))
    # print(Z_np)
    return A_np, Z_np