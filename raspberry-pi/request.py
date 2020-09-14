import cv2
import requests
import json
import numpy as np


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
url = 'https://90ypu1bv59.execute-api.us-east-1.amazonaws.com/dev/analyze-image'

img_array = cv2.imread("./samples/cat.123.jpg",
                       cv2.IMREAD_GRAYSCALE)
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE)).flatten()
JSON_array = json.dumps(new_array, cls=NumpyEncoder)
response = requests.post(url, data=JSON_array)
print(response.text)
