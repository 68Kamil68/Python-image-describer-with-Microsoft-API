import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()
# my subscription key
SUBSCRIPTION_KEY = os.getenv('SUBSCRIPTION_KEY')
# endpoint address and function we want to call
vision_service_address = "https://imageanalyse.cognitiveservices.azure.com/"
address = vision_service_address + "vision/v1.0/analyze"

# parameters wanted from the request
parameters = {'visualFeatures': 'Tags, Description, Faces, Adult',
              'details': 'Celebrities', 'language': 'en'}

# path to the image and converting to raw binary data
img_path = 'picture.jpg'
image_data = open(img_path, 'rb').read()

# required headers - subscription key and content type
headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

# http POST to call this function
response = requests.post(address, headers=headers, params=parameters,
                         data=image_data)

# raise an exception if the call returns an error
response.raise_for_status()

# Display json results
results = response.json()
print(json.dumps(results))

for item in results['categories']:
    print(item)
