# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 02:32:29 2019

@author: user
"""

#import cv2
import h5py as h5
from glob import glob
import numpy as np
#import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

c=1

file_path=r"C:\Users\NRAD\Desktop\snehashis internship 2019\medical dataset\brainTumorDataPublic_1766/*.mat"

pngs=glob(file_path)

zero=np.zeros((len(pngs),2))

df = pd.DataFrame(zero, columns = ['PID', 'CLASS NO']) 


for i in range(len(pngs)):

    f=h5.File(pngs[i],'a')
    image=np.mat(f['/cjdata/image'])
    PID=np.array(f['/cjdata/PID'])
    label=np.array(f['/cjdata/label'])
    tumorBorder=np.mat(f['/cjdata/tumorBorder'])
    tumorMask=np.mat(f['/cjdata/tumorMask'])
    
    name = r"C:\Users\NRAD\Desktop\snehashis internship 2019\medical dataset\brainTumorDataPublic_1766\image/id_" + str(c) +'.png'
    
    
    name_tumorMask = r"C:\Users\NRAD\Desktop\snehashis internship 2019\medical dataset\brainTumorDataPublic_1766\mask/mask_id" + str(c) +'.png'
    
    
    df['PID'][i]=c

    df['CLASS NO'][i]=label
    
    c=c+1
    
    plt.figure(figsize=(5,5))
    plt.imshow(image,cmap='gray')
    plt.tight_layout()
    plt.axis('off')
    plt.savefig(name, dpi=20, frameon='false')
    
    plt.figure(figsize=(5,5))
    plt.imshow(tumorMask,cmap='gray')
    plt.tight_layout()
    plt.axis('off')
    plt.savefig(name_tumorMask, dpi=20, frameon='false')

    
csv_path_name=r"C:\Users\NRAD\Desktop\snehashis internship 2019\medical dataset\brainTumorDataPublic_1766/mat2python_mri_tumor.csv"
df.to_csv(csv_path_name) 