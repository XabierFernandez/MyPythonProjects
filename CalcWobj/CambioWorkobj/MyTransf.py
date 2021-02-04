# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:04:27 2017

@author: xabier fernandez
"""
import math 
import numpy as np
import transformations_2017 as tf

class MyTransf(object):
            
        def p2MatEul(self,posX, posY, posZ, Rx, Ry, Rz):
    
            T = tf.euler_matrix(math.radians(Rx),math.radians(Ry),math.radians(Rz),'szyx')
            T[0,3] = posX
            T[1,3] = posY
            T[2,3] = posZ
    
            return T
        
        def p2MatQuat(self, aPoint):
    
            T = tf.quaternion_matrix([aPoint[3],aPoint[4],aPoint[5],aPoint[6]])
            T[0,3] = aPoint[0]
            T[1,3] = aPoint[1]
            T[2,3] = aPoint[2]
    
            return T 
        
        def matrix2euler(self,mat):
    
            angles = tf.euler_from_matrix(mat)
            degA = math.degrees(angles[2])
            degB = math.degrees(angles[1])
            degC = math.degrees(angles[0])
    
            return degA, degB, degC
        
        def quat2euler(self,aQuat): 
    
            angles = tf.euler_from_quaternion([aQuat[0],aQuat[1],aQuat[2],aQuat[3]])
            degA = math.degrees(angles[2])
            degB = math.degrees(angles[1])
            degC = math.degrees(angles[0])
    
            return degA, degB, degC
        
        def euler2quat(self,ZYX):
    
            q = tf.quaternion_from_euler(math.radians(ZYX[0]), math.radians(ZYX[1]), math.radians(ZYX[2]), 'rzyx')
    
            return q
        
        def pointFrameA2FrameB(self,aPoint,aFrameA, aFrameB):
            
                       
            pTransl = aPoint[:3]
            fTranslA = aFrameA[:3]
            fTranslB = aFrameB[:3]
            
            pRot = self.euler2quat(aPoint[3:])
            fRotA = self.euler2quat(aFrameA[3:])
            fRotB = self.euler2quat(aFrameB[3:])          
     
            pointA = np.concatenate((pTransl,pRot),axis=0)
            frameA = np.concatenate((fTranslA,fRotA),axis=0)
            frameB = np.concatenate((fTranslB,fRotB),axis=0)  
                 
            Pfa_mat = self.p2MatQuat(pointA)
            frameA_mat = self.p2MatQuat(frameA)
            frameB_mat = self.p2MatQuat(frameB)   
    
            inverse_frameB_mat = np.linalg.inv(frameB_mat)
    
            Pwa_mat = np.dot(frameA_mat,Pfa_mat)
    
            Pfb_mat= np.dot(inverse_frameB_mat,Pwa_mat)           
            
            translation = tf.translation_from_matrix(Pfb_mat)
            rotation = self.quat2euler(tf.quaternion_from_matrix(Pfb_mat))
            
            pointB = np.concatenate((translation,rotation),axis=0)
            
            return pointB
        

pointA = [-534.884033, -825.747070, 1037.32373, -165.214142, -3.16937923, -178.672119]
frameA = [571.162170, -1168.71704, 372.404694, -179.723297, -0.206600, 0.856200]
frameB = [575.243103, -2053.79492,381.968811, 179.904297, 0.0230000, 0.540800]

kuka = MyTransf()

pointB = kuka.pointFrameA2FrameB(pointA,frameA,frameB)

print(pointB)
            
            
            
            
            
            
            
            