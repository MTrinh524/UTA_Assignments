# Name: Minh Trinh
# UTA ID: 1001705984
# Date Modified: 2/8/2023
# Description: 
#   Computes the gradient of "foo" in "foo_gradient()."
#   Computes the gradient descent in "gradient_descent" and
#   returns the minimum x and y and history at each iteration.

import numpy as np
from numpy import linalg as LA

def foo_gradient(x, y):
    dfdx = -np.cos(np.cos(x) + np.sin((2*y))) * (np.sin(x))
    dfdy = 2*np.cos((2*y)) * np.cos(np.cos(x) + np.sin((2*y)))

    return (dfdx, dfdy)

def gradient_descent(function, gradient, x1, y1, eta, epsilon):
    t = 1
    xt = x1
    yt = y1
    x_next = 0
    y_next = 0

    history = [(x1, y1)]
    while(LA.norm(gradient(xt,yt)) >= epsilon):
        (x_next, y_next) = np.subtract((xt,yt), tuple(eta * elem for elem in gradient(xt,yt)))
        if (function(x_next, y_next) > function(xt,yt)):
            eta = eta/2
        else:
            (xt, yt) = (x_next, y_next)
            history.append((x_next, y_next))

    return (xt, yt, history)