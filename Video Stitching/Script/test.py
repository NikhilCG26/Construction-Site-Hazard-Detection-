import cv2
import numpy as np
import argparse
import pathlib
import os
import open3d as o3d
import matplotlib.pyplot as plt
import glob

path = pathlib.Path(__file__).parent.resolve()

def run_frames():
    """
    Cycles through frames to generate an output video
    """
    img_array = []
    for filename in glob.glob(path + "project-frames" + "*.png"):
        img = cv2.imread(filename)
        height,width,layers = img.shape
        size = (width,height)
        img_array.append(img)
    
    out = cv2.VideoWriter('Birdeye-view.mp4',cv2.VideoWriter_fourcc(*'MP4V'),20.0,size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()    

def video_slice():
    capture = cv2.VideoCapture(path + "trial.mp4")
 
    frameNr = 0
    
    while (True):
    
        success, frame = capture.read()
    
        if success:
            cv2.imwrite(f"frame_{frameNr}", frame)
    
        else:
            break
    
        frameNr = frameNr+1
    
    capture.release()

if __name__=="__main__":


