#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install easygui')


# In[2]:


get_ipython().system(' pip install opencv-python')


# In[3]:


import cv2


# In[4]:


import easygui


# In[5]:


import numpy as np


# In[6]:


import imageio


# In[7]:


import sys


# In[8]:


import matplotlib.pyplot as plt


# In[9]:


import os


# In[10]:


import tkinter as tk


# In[11]:


from tkinter import filedialog


# In[12]:


from tkinter import *


# In[13]:


from PIL import ImageTk,Image


# In[14]:


def upload():
    ImagePath=easygui.fileopenbox()
    cartoonify(ImagePath)


# In[15]:


def cartoonify(ImagePath):
    originalmage=cv2.imread(ImagePath)
    originalmage=cv2.cvtColor(originalmage,cv2.COLOR_BGR2RGB)
    
    
    if originalmage is None:
        print("can not find any image .Chose appropriate file")
        sys.exit()
        
    ReSized1=cv2.resize(originalmage,(960,540))
    grayScaleImage=cv2.cvtColor(originalmage,cv2.COLOR_BGR2GRAY)
    ReSized2=cv2.resize(greyScaleImage,(960,540))
    
    
    smoothGrayScale=cv2.medianBlur(grayScaleImage,5)
    ReSized3=cv2.resize(smoothGrayScale,(960,540))
    
    
    getEdge=cv2.adaptiveThreshold(smoothGrayScale,255,
                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY,9,9)
    ReSized4=cv2.resize(getEdge,(960,540))
    
    colorImage=cv2.bilateralFilter(originalmage,9,300,300)
    ReSized5=cv2.resize(colorImage,(960,540))
    
    
    cartoonImage=cv2.bitwise_and(colorImage,colorImage,mask=getEdge)
    ReSized6=cv2.resize(cartoonImage,(960,540))
    
    images=[ReSized1,ReSized2,ReSized3,ReSized4,ReSized5,ReSized6]
    fig,axes=plt.subplots(3,2,figsize(8,8),subplot_kw={'xticks':[],'yticks':[]},
                         gridspec_kw=dict(hspace=0.1,wspace=0.1))
    for i,ax in enumerate(axes.flat):
        ax.imshow(images[i],cmap='gray')
        
    save1=Button(top,text="save cartoon image",command=lambda:save(ReSized6,ImagePath),padx=30,pady=5)
    save1.configure(background="#364156",foreground='white',font=('calibri',10,'bold'))
    save1.pack(side=TOP,pady=50)
    
    plt.show()
    


# In[16]:


def save(ReSized6, ImagePath):
    
    newName="cartoonified_Image"
    path1=os.path.dirname(ImagePath)
    extension=os.path.splitext(ImagePath)[1]
    path=os.path.join(path1,newName+extension)
    cv2.imwrite(path,cv2.cvtColor(Resized6,cv2.COLOR_RGB2BGR))
    I="Image saved by name" + newName + "at " + path
    tk.messagebox.showinfo(title=None,message=I)
    


# In[ ]:


top=tk.Tk()
top.geometry('400x400')
top.title('Cartoonify your image !')
top.configure(background='white')
label=Label(top,background='#CDCDCD',font=('calibri',20,'bold'))

upload=Button(top,text="Cartoonify an Image",command=upload,padx=10,pady=5)
upload.configure(background='#364156',foreground='white',font=('calibri',10,'bold'))
upload.pack(side=TOP,pady=50)

save1=Button(top,text="Save cartoon image",command=lambda:save(ImagePath,ReSized6),padx=30,pady=5)
save1.configure(background='#364156',foreground='white',font=('calibri',10,'bold'))
save1.pack(side=TOP,pady=50)
top.mainloop()


# In[ ]:




