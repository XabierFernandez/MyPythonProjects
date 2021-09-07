import numpy as np
import math as mt


frame_old = np.zeros(3)
frame_new = np.zeros(3)
point = np.zeros(3)
diff = np.zeros(3)

frame_old[0] = -571.1622
frame_old[1] = 1168.7170
frame_old[2] = 0

frame_new[0] = 0
frame_new[1] = 1168.7170
frame_new[2] = -372.4046

point[0] = -0.999981838
point[1] = -0.004829328
point[2] = 0.003605842




diff = np.subtract(frame_old,frame_new)
diff= np.add(frame_new,diff)

print(np.dot(point,frame_old[0]))
print(np.dot(point,frame_old[1]))
print(np.dot(point,frame_old[2]))








