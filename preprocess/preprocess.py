from keras import *
import numpy as np
import keras 
def load_and_preprocess_image(img_path,target_size):
    img=keras.preprocessing.image.load_img(img_path,target_size=target_size)
    img_arr=keras.preprocessing.image.img_to_array(img)
    img_arr=np.expand_dims(img_arr,axis=0)
    img_arr/=255.0
    return img_arr