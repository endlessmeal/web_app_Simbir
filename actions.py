from flask import make_response
import requests
# import Pillow library for image processing
from PIL import Image, ImageFilter
from config import db
from sqlalchemy import exc


def get_image_url(animal):
    links = {'fox': 'https://randomfox.ca/floof/',
             'cat': 'https://api.thecatapi.com/v1/images/search',
             'dog': 'http://shibe.online/api/shibes?count=1'}
    url = links[animal]
    # get a correct json
    try:
        r = requests.get(url)
    except requests.exceptions.HTTPError as http_err:
        return make_response(f'При url запросе произошла ошибка: {http_err}', 400)
    # get a link of image from json
    img_url = r.json()
    return img_url


def process_image(img, img_src):
    try:
        # decode an original image
        original = Image.open(img)
        # add blur filter
        blur = original.filter(ImageFilter.BLUR)
        blur.save(img_src)
    except ValueError as va_err:
        make_response(f'При обработке файла произошла ошибка: {va_err}')


def insert_data_in_db(image):
    try:
        # add changes to db and commit it
        db.session.add(image)
        db.session.commit()
    except exc.IntegrityError as i:
        make_response(f'При добавлении в базу данных произошла ошибка: {i}', 1092)


