"""
This gradient descent(derivative method) algoritm for finding the correct weight,
overshoot if the input is too high
"""
weight = 0.5
goal_pred = 0.8
input_1 = 0.5
alpha = 0.1
for iteration in range(20):
    pred = input_1 * weight
    error = (pred - goal_pred) **2
    delta = pred - goal_pred
    weight_delta = input_1 * delta
    weight = weight - (alpha * weight_delta)
    print("Error:{0} Prediction:{1} Weight:{2} Iteration:{3}".format(str(error), str(pred), str(weight), str(iteration)))
