import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd

credential_path = r"C:\Users\gulab\OneDrive\Documents\Python_Venv\VisionAPIDemo\Token_key.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS']= credential_path

client = vision.ImageAnnotatorClient()

def detectText(img):
    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    df =pd.DataFrame(columns=['locale', 'description'])
    for text in texts:
        df = df._append(
            dict(
                locale=text.locale,
                
                description=text.description
            ),
            ignore_index=True
        )
    return df

FILE_NAME = 'text3.jpeg'
FOLDER_PATH = r'C:\Users\gulab\OneDrive\Documents\Python_Venv\VisionAPIDemo\Images\texts'
print (detectText(os.path.join(FOLDER_PATH, FILE_NAME)))

# img_url = "https://i.ytimg.com/vi/4sbDsv_ejrQ/maxresdefault.jpg"
# image = vision.Image()
# image.source.image_uri = img_url
# response = client.text_detection(image=image)
# texts = response.text_annotations

# df =pd.DataFrame(columns=['locale', 'description'])
# for text in texts:
#     df = df._append(
#         dict(
#             locale=text.locale,
#             description=text.description
#         ),
#         ignore_index=True
#     )
# print (df)