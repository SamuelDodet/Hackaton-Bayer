from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import cv2
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def upload():
    try:
        imagefile = flask.request.files.get('imagefile', '')
        model = tf.keras.models.load_model("plant_disease")
        prediction = model.predict([prepare(imagefile)])
        return CATEGORIES[(np.argmax(prediction))]

    except:
        print('fuck this shit')

CATEGORIES =['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
             'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
             'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
             'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot',
             'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
             'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
             'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
             'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
             'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
             'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
             'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
             'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']


def prepare(filepath):
    IMG_SIZE = 224
    img_array = cv2.imread(filepath, cv2.IMREAD_COLOR)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE),3)
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)

def model_predict(imagefile):
    model = tf.keras.models.load_model("plant_disease")
    prediction = model.predict([prepare(imagefile)])
    print(CATEGORIES[(np.argmax(prediction))])

model_predict()

if __name__ == "__main__":
    app.run(debug=True)
