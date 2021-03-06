import matplotlib.pyplot as plt
from keras.models import load_model
from keras.preprocessing.image import image
import numpy as np
import glob

classifier=load_model("model.h5")

def load_image(img_path, show=True):
    img_original = image.load_img(img_path)
    img = image.load_img(img_path, target_size=(64, 64))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]
    if show:
        plt.imshow(img_original)                           
        plt.axis('off')
        plt.show()
    return img_tensor

'''import glob
for img_file in glob.iglob("dir_name/*"):
  new_image = load_image(img_file)
  pred = classifier.predict(new_image)
  if pred<.5 : print("chat")
  else : print("not chat")'''
flag1=0
flag2=0

new_image = load_image("D:\\Project_Like_Prediction\\data_1\\frame0.jpg")
pred = classifier._make_predict_function(new_image)        # predict() function may be used when flask is not used 
if pred<.5 : flag1=1
# print("Presentation")
else : flag2=1
#print("Not Presentation")

if flag1==1 and flag2==0 : print("Presentation screen")
if flag2==1 and flag1==0 : print("non Presentation")

if flag1==1 and flag2==1 : print("Mix")



