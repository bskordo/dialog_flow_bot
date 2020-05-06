import requests
import random
import json


def create_sample_file():
    url = 'https://dvmn.org/media/filer_public/a7/db/a7db66c0-1259-4dac-9726-2d1fa9c44f20/questions.json'
    response = requests.get(url)
    json_content = response.json()
    with open('sample.json', 'w') as file_handler:
        json.dump(json_content, file_handler, ensure_ascii=False)


if __name__ == '__main__':
    create_sample_file()
