import numpy as np
weight = 0.5
goal_pred = 0.8
input0 = 2
alpha = 0.1

for iteration in range(20):
    pred = input0 * weight
    error = (pred - goal_pred) ** 2
    derivative = input0 * (pred - goal_pred)
    weight = weight - (derivative * alpha)
    print("Error:{0:.15f}, Pred:{1:.3f}, Weight:{2:.3f}, Iteration:{3}".format(error, pred, weight, iteration))
    if np.isclose(goal_pred, pred, rtol=.01):
        break
