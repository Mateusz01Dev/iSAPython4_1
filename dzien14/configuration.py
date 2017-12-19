"""
This is configuration file for mscs_cv.py module
"""

API_KEY = ""

API_URL = "https://westeurope.api.cognitive.microsoft.com/vision/v1.0/analyze"
OCR_URL = "https://westeurope.api.cognitive.microsoft.com/vision/v1.0/ocr"


HEADER_URL = {'Content-Type': 'application/json',
              'Ocp-Apim-Subscription-Key': API_KEY}

HEADER_PIC = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': API_KEY}

PARAMS = {'visualFeatures': 'Categories,Description,Faces,Adult',
          'details': 'Celebrities'}

PARAMS_OCR = {'detectOrientation': True}


TARGET_DIR = "described_pics"
ROOT_NAME = "smart_pic_"
