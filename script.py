import cv2
import numpy as np
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image

# Load the VGG16 model with pre-trained weights
model = VGG16(weights='imagenet')

# Load the image
image_path = 'fridge.png'  # Change this to the path of your 'fridge.png' image
img = image.load_img(image_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Predict the image class
predictions = model.predict(x)
decoded_predictions = decode_predictions(predictions, top=5)[0]

# Check if any of the top-5 predicted classes contain food-related labels
food_labels = ["banana", "apple", "pizza", "sandwich", "spaghetti", "ice_cream", "hotdog", "sushi", "steak"]
contains_food = any(label.lower() in label.lower() for (_, label, _) in decoded_predictions)

# Display the results
if contains_food:
    print("The image contains food!")
else:
    print("The image does not contain food.")
