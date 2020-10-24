import json
import numpy as np
import cv2
import requests


class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


IMG_SIZE = 30

img_array = cv2.imread("./samples/dog.125.jpg", cv2.IMREAD_GRAYSCALE)
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
new_array1 = new_array.flatten()
s1 = json.dumps(new_array1, cls=NumpyEncoder)
url = 'http://localhost:3000/analyze-image'
x = requests.post(
    url, headers={'Content-Type': 'application/json'}, data=s1)
print(x.text)
