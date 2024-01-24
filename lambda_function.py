#!/usr/bin/env python
# coding: utf-8


import tflite_runtime.interpreter as tflite
import numpy as np
from PIL import Image

model_path = '/home/jovyan/examples/examples/tensorflow/Seed3/model-00058-0.32378-0.29181-.h5'



labels = ['Black-grass', 'Charlock', 'Cleavers', 'Common Chickweed', 'Common wheat', 'Fat Hen', 'Loose Silky-bent', 'Maize', 'Scentless Mayweed', 'Shepherds Purse', 'Small-flowered Cranesbill', 'Sugar beet']


interpreter = tflite.Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']




def predict(url):
    
    with Image.open(url) as img:
        img = img.resize((120, 120), Image.NEAREST)
    
    x = np.array(img, dtype='float32')
    X = np.array([x])

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()

    return dict(zip(labels, float_predictions))


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result




