#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a = np.array([0, 1, 2])
print(type(a))


# In[2]:


import numpy as np
import cv2
get_ipython().run_line_magic('matplotlib', 'inline')
#Comment: The purpose of the above line is to display matplotlib plots inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# In[3]:


print("Hello, world")


# In[4]:


5+5


# In[5]:


a = np.array([0, 1, 2])   
print(type(a))


# In[6]:


img_water = mpimg.imread('photo.jpg')
resized = cv2.resize(img_water, (300, 300))
plt.imshow(resized)
plt.title('Image')
plt.show()


# In[7]:


img_water = mpimg.imread('download.png')
resized = cv2.resize(img_water, (300, 300))
plt.imshow(resized)
plt.title('Image')
plt.show()


# In[1]:


img_water = mpimg.imread('photo.jpg')
resized = cv2.resize(img_water, (300, 300))
plt.imshow(resized)
plt.title('Image')
plt.show()


# In[2]:


# load and show an image with Pillow
from PIL import Image
# load the image
image = Image.open('hoo1.jpg')
# summarize some details about the image
print(image.format)
print(image.mode)
print(image.size)
# show the image
image.show()


# In[1]:


# load and show an image with Pillow
from PIL import Image
# load the image
image = Image.open('hoo1.jpg')
# summarize some details about the image
print(image.format)
print(image.mode)
print(image.size)
# show the image
image.show()


# In[2]:


# load and show an image with Pillow
from PIL import Image
# load the image
image = Image.open('hoo1.jpg')
# summarize some details about the image
print(image.format)
print(image.mode)
print(image.size)
# show the image
image.show()


# In[3]:


# load and show an image with Pillow
from PIL import Image
# load the image
image = Image.open('hoo2.jpg')
# summarize some details about the image
print(image.format)
print(image.mode)
print(image.size)
# show the image
image.show()


# In[4]:


# load and show an image with Pillow
from PIL import Image
# load the image
image = Image.open('hoo2.jpg')
# summarize some details about the image
print(image.format)
print(image.mode)
print(image.size)
# show the image
image.show()


# In[5]:



# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot
# load image as pixel array
data = image.imread('hoo2.jpg')
# summarize shape of the pixel array
print(data.dtype)
print(data.shape)
# display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()


# In[ ]:




