# -*- coding: utf-8 -*-
"""
Cr#FFFFFF#FFFFFF#FFFFFFeated on Tue Jul 18 08:54:16 2017

@author: xabier fernandez
"""
import math
import numpy as np
import transformations_2017 as tf


def point_rotation(point_mat):
    decpl = 7
    
    sy = math.sqrt(math.pow(point_mat[0,0],2) + math.pow(point_mat[1,0],2))
    singularity = sy < 1e-6
    
    if not singularity :
        A = math.atan2(point_mat[1,0], point_mat[0,0])
        B = math.atan2(-point_mat[2,0], sy)
        C = math.atan2(point_mat[2,1] , point_mat[2,2])        
    else :
        A = 0
        B = math.atan2(-point_mat[2,0], sy)
        C = math.atan2(-point_mat[1,2], point_mat[1,1])       
        
    A = round(math.degrees(A),decpl)
    B = round(math.degrees(B),decpl)
    C = round(math.degrees(C),decpl)
    
    return np.array([A,B,C])

def point_translation(point_mat): 
    decpl = 5
    
    X = round(point_mat[0,3],decpl)
    Y = round(point_mat[1,3],decpl)
    Z = round(point_mat[2,3],decpl)
    
    return np.array([X,Y,Z])

def point_to_mat(posX,posY,posZ,degA,degB,degC):
    t=np.zeros((4,4))
    
    radA=math.radians(degA)
    radB=math.radians(degB)
    radC=math.radians(degC)
    
    cos_a=math.cos(radA)
    sin_a=math.sin(radA)

    cos_b=math.cos(radB)
    sin_b=math.sin(radB)

    cos_c=math.cos(radC)
    sin_c=math.sin(radC)
    
    t[0,0]  =  cos_a*cos_b
    t[0,1]  = -sin_a*cos_c + cos_a*sin_b*sin_c
    t[0,2]  =  sin_a*sin_c + cos_a*sin_b*cos_c

    t[1,0]  =  sin_a*cos_b
    t[1,1]  =  cos_a*cos_c + sin_a*sin_b*sin_c
    t[1,2]  = -cos_a*sin_c + sin_a*sin_b*cos_c

    t[2,0]  = -sin_b
    t[2,1]  =  cos_b*sin_c
    t[2,2]  =  cos_b*cos_c
    
    t[0,3]  = posX
    t[1,3]  = posY
    t[2,3]  = posZ
    
    t[3,0]  = 0
    t[3,1]  = 0
    t[3,2]  = 0
    t[3,3]  = 1
    
    return t

def point_to_mat_euler(posX, posY, posZ, Rx, Ry, Rz):
    
    T = tf.euler_matrix(math.radians(Rx),math.radians(Ry),math.radians(Rz),'szyx')
    T[0,3] = posX
    T[1,3] = posY
    T[2,3] = posZ
    
    return T  

def point_to_mat_quat(posX, posY, posZ, q0, q1, q2, q3):
    
    T = tf.quaternion_matrix([q0,q1,q2,q3])
    T[0,3] = posX
    T[1,3] = posY
    T[2,3] = posZ
    
    return T  

def matrix2euler(mat):
    
    angles = tf.euler_from_matrix(mat)
    degA = math.degrees(angles[2])
    degB = math.degrees(angles[1])
    degC = math.degrees(angles[0])
    
    return degA, degB, degC
    

def quat2euler(q0,q1,q2,q3): 
    
    angles = tf.euler_from_quaternion([q0,q1,q2,q3])
    degA = math.degrees(angles[2])
    degB = math.degrees(angles[1])
    degC = math.degrees(angles[0])
    
    return degA, degB, degC

def euler2quat(Rz,Ry,Rx):
    
    q = tf.quaternion_from_euler(math.radians(Rz), math.radians(Ry), math.radians(Rx), 'rzyx')
    
    return q

def test_indirect():
    frameB_mat = point_to_mat_euler(1816.015,1619.484,-6.039,-74.802,0.047,0.104)  
    Pwa_mat = point_to_mat_euler(2447.88379, 704.692627, -531.185242, -105.617844, 10.2257118, -91.0393372)
    
    inverse_frameB_mat = np.linalg.inv(frameB_mat)
    
    Pfb_mat= np.dot(inverse_frameB_mat,Pwa_mat) 
    
    print('\n')
    print(tf.euler_from_matrix(Pfb_mat))
    print('\n')
    print(tf.translation_from_matrix(Pfb_mat))
    print('\n')
    
    inverse_frameB_mat = np.linalg.inv(Pfb_mat)
    
    frameB_mat = np.dot(Pwa_mat,inverse_frameB_mat) 
    
    print('\n')
    print(tf.euler_from_matrix(frameB_mat))
    print('\n')
    print(tf.translation_from_matrix(frameB_mat))
    print('\n')
    
    
def test1():
    
    frameA_mat = point_to_mat_quat(-1428.93,-4116.31,1102.54,0.588893,0.588866,0.391443,0.391426)
    frameB_mat = point_to_mat_quat(-1461.79,4234.74,1082.31,-0.5904,0.590429,-0.389119,0.389113)    
    
    Pfa_mat = point_to_mat_quat(4470.81,-373.95,766.30,0.022427,0.489361,0.650621,-0.580272)
    
    inverse_frameB_mat = np.linalg.inv(frameB_mat)
    
    Pwa_mat = np.dot(frameA_mat,Pfa_mat)
    
    Pfb_mat= np.dot(inverse_frameB_mat,Pwa_mat)
    
    print('\n')
    print(tf.quaternion_from_matrix(Pfb_mat))
    print('\n')
    print(tf.translation_from_matrix(Pfb_mat))
    print('\n')
    
    print(point_to_mat_euler(-534.884033, -825.747070,1037.32373,-165.214142, -3.16937923, -178.672119))
    print('\n')
    Pfa_mat = point_to_mat(-534.884033, -825.747070,1037.32373, -165.214142, -3.16937923, -178.672119)
    print(Pfa_mat)

def test2():
    
    """
    -----------------------------------
    Rotational matrix 'zyx'
    -----------------------------------
    Fa--> Frame A relative to world c.s
    Fb--> Frame B relative to world c.s
    -----------------------------------
    Pwa--> Point A in world c.s
    Pwb--> Point B in world c.s
    -----------------------------------
    Pfa--> Point in frame A c.s
    Pfb--> Point in frame B c.s
    -----------------------------------
    Pwa == Pwb
    Pw = Fa x Pfa
    Pw = Fb x Pfb 
    Pfb = Fb' x Pw
    -----------------------------------
    """
    frameA_mat = point_to_mat(571.162170,-1168.71704,372.404694,-179.723297,-0.206600,0.856200)
    frameB_mat = point_to_mat(1493.90100, 209.460, 735.007, 179.572, -0.0880000, 0.130000)    
    
    Pfa_mat = point_to_mat(-534.884033, -825.747070,1037.32373, -165.214142, -3.16937923, -178.672119)
    
    inverse_frameB_mat = np.linalg.inv(frameB_mat)
    
    #--------------------------------------------------------------------------
    #Point A in World coordinate system
    Pwa_mat = np.dot(frameA_mat,Pfa_mat)
    Pwa_Trans = point_translation(Pwa_mat)
    Pwa_Rot = point_rotation(Pwa_mat)
    
    print('\n')
    print('Point A in World C.S.: ')
    print(('Translation--> X = {0} , Y = {1} , Z = {2} ').format(Pwa_Trans[0],Pwa_Trans[1],Pwa_Trans[2]))    
    print(('Rotation(Euler angles)--> : A = {0} , B = {1} , C = {2} ').format(Pwa_Rot[0],Pwa_Rot[1],Pwa_Rot[2]))
    print('\n')
   
    
    #--------------------------------------------------------------------------
    #Point A affine transformation
    #Point A in Frame B coordinate system
    Pfb_mat= np.dot(inverse_frameB_mat,Pwa_mat)
    Pfb_Trans = point_translation(Pfb_mat)
    Pfb_Rot = point_rotation(Pfb_mat)
    
    print('Point A in Frame B C.S.: ')
    print(('Translation--> X = {0} , Y = {1} , Z = {2} ').format(Pfb_Trans[0],Pfb_Trans[1],Pfb_Trans[2]))    
    print(('Rotation(Euler angles)--> : A = {0} , B = {1} , C = {2} ').format(Pfb_Rot[0],Pfb_Rot[1],Pfb_Rot[2]))
    
    #--------------------------------------------------------------------------
    #Point B in World coordinate system
    Pwb_mat = np.dot(frameB_mat,Pfb_mat)
    Pwb_Trans = point_translation(Pwb_mat)
    Pwb_Rot = point_rotation(Pwb_mat)
    
    print('\n')
    print('Point B in World C.S.: ')
    print(('Translation--> X = {0} , Y = {1} , Z = {2} ').format(Pwb_Trans[0],Pwb_Trans[1],Pwb_Trans[2]))    
    print(('Rotation(Euler angles)--> : A = {0} , B = {1} , C = {2} ').format(Pwb_Rot[0],Pwb_Rot[1],Pwb_Rot[2]))
    print('\n')
    
if __name__ == "__main__":

    #test2()
    #test1()
    test_indirect()
