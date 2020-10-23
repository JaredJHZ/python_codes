import base64
import requests
import json



if __name__ == '__main__':
    URL = 'https://apiUrl/test/name/format'
    with open("name.format", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    r = requests.post(URL,data=encoded_string)
    print(r.text)