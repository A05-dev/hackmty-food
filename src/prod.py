from roboflow import Roboflow
import requests
from io import BytesIO
from PIL import Image
import cv2  # opencv
import numpy as np

rf = Roboflow(api_key="5fLOPWRg1OT4LIUuGTsX")
project = rf.workspace().project("sandoval_fridge")
model = project.version(3).model

# infer on a local image

# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())

prediction = model.predict("src/assets/2.jpeg", confidence=40, overlap=30).json()
image_url = prediction["image"]
# print(type(prediction))
# print(prediction)

# Assuming you already have the `prediction` dictionary
unique_classes = set()

for item in prediction["predictions"]:
    unique_classes.add(item["class"])

# Convert the set to a list if needed
classes = list(unique_classes)

# Print the array of unique "class" elements
print(classes)
print(prediction)  # prints all the info

json_data = {
    "predictions": [
        {
            "x": 399,
            "y": 1013,
            "width": 56,
            "height": 42,
            "confidence": 0.9890433549880981,
            "class": "orange",
            "class_id": 8,
            "image_path": "src/assets/2.jpeg",
            "prediction_type": "ObjectDetectionModel",
        },
        {
            "x": 348,
            "y": 1006,
            "width": 48,
            "height": 42,
            "confidence": 0.9853593111038208,
            "class": "avocado",
            "class_id": 1,
            "image_path": "src/assets/2.jpeg",
            "prediction_type": "ObjectDetectionModel",
        },
        {
            "x": 608,
            "y": 1005,
            "width": 58,
            "height": 55,
            "confidence": 0.9817637205123901,
            "class": "avocado",
            "class_id": 1,
            "image_path": "src/assets/2.jpeg",
            "prediction_type": "ObjectDetectionModel",
        },
        {
            "x": 492,
            "y": 705,
            "width": 76,
            "height": 75,
            "confidence": 0.9310282468795776,
            "class": "milk",
            "class_id": 7,
            "image_path": "src/assets/2.jpeg",
            "prediction_type": "ObjectDetectionModel",
        },
        {
            "x": 413,
            "y": 708,
            "width": 95,
            "height": 77,
            "confidence": 0.9268764853477478,
            "class": "juice",
            "class_id": 6,
            "image_path": "src/assets/2.jpeg",
            "prediction_type": "ObjectDetectionModel",
        },
        {
            "x": 718,
            "y": 992,
            "width": 60,
            "height": 55,
            "confidence": 0.9110139608383179,
            "class": "avocado",
            "class_id": 1,
            "image_path": "src/assets/2.jpeg",
            "prediction_type": "ObjectDetectionModel",
        },
        {
            "x": 516,
            "y": 992,
            "width": 50,
            "height": 45,
            "confidence": 0.8491873741149902,
            "class": "apple",
            "class_id": 0,
            "image_path": "src/assets/2.jpeg",
            "prediction_type": "ObjectDetectionModel",
        },
        {
            "x": 161,
            "y": 1276,
            "width": 131,
            "height": 227,
            "confidence": 0.8219552040100098,
            "class": "milk",
            "class_id": 7,
            "image_path": "src/assets/2.jpeg",
            "prediction_type": "ObjectDetectionModel",
        },
        {
            "x": 600,
            "y": 492,
            "width": 180,
            "height": 135,
            "confidence": 0.8070927858352661,
            "class": "bread",
            "class_id": 2,
            "image_path": "src/assets/2.jpeg",
            "prediction_type": "ObjectDetectionModel",
        },
        {
            "x": 662,
            "y": 1000,
            "width": 58,
            "height": 60,
            "confidence": 0.71308833360672,
            "class": "apple",
            "class_id": 0,
            "image_path": "src/assets/2.jpeg",
            "prediction_type": "ObjectDetectionModel",
        },
        {
            "x": 938,
            "y": 1337,
            "width": 219,
            "height": 210,
            "confidence": 0.6860628128051758,
            "class": "egg",
            "class_id": 5,
            "image_path": "src/assets/2.jpeg",
            "prediction_type": "ObjectDetectionModel",
        },
        {
            "x": 610,
            "y": 840,
            "width": 95,
            "height": 80,
            "confidence": 0.5231884121894836,
            "class": "cabagge",
            "class_id": 3,
            "image_path": "src/assets/2.jpeg",
            "prediction_type": "ObjectDetectionModel",
        },
    ],
    "image": {"width": "1200", "height": "1600"},
}

# Load the image
image_path = "src/assets/2.jpeg"
image = cv2.imread(image_path)

# Iterate through predictions and draw squares
# Define the offset values to move the rectangles left and up

# Iterate through predictions and draw adjusted rectangles
for prediction in json_data["predictions"]:
    x = prediction["x"]  # Subtract the x offset
    y = prediction["y"]  # Subtract the y offset
    width = prediction["width"]
    height = prediction["height"]
    color = (
        np.random.randint(0, 255),
        np.random.randint(0, 255),
        np.random.randint(0, 255),
    )  # Random color
    thickness = 4

    # Draw a rectangle on the image with adjusted position
    cv2.rectangle(image, (x - height, y - width), (x + width, y + height), color, thickness)

# Save or display the image with adjusted rectangles
output_filename = "src/assets/2_output.png"
cv2.imwrite(output_filename, image)