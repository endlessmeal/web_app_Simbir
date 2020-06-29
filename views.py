from flask import render_template, send_file, make_response
import requests
import uuid
# import Pillow library for image processing
from config import app_dir, app
from models import ImageEdit
import actions


@app.route('/animal/dog')
def dog():
    img_url = actions.get_image_url('dog')
    # create name for image with uuid4
    img_name = str(uuid.uuid4())
    # open image in static/animals/ folder with jpg extension
    img_src = app_dir + '/static/animals/' + img_name + '.jpg'

    # get a link for image from json and then download it in bytes
    img = requests.get(img_url[0], stream=True).raw

    actions.process_image(img, img_src)

    # create class instance where processed image is uuid4
    image = ImageEdit(animal_type='Dog', processed_image=img_name)

    actions.insert_data_in_db(image)

    # return an image with correct mime type
    return send_file(img_src, mimetype='image/jpeg')


@app.route('/animal/fox')
def fox():
    img_url = actions.get_image_url('fox')

    img_name = str(uuid.uuid4())
    img_src = app_dir + '/static/animals/' + img_name + '.jpg'

    img = requests.get(img_url['image'], stream=True).raw

    actions.process_image(img, img_src)

    image = ImageEdit(animal_type='Fox', processed_image=img_name)

    actions.insert_data_in_db(image)

    return send_file(img_src, mimetype='image/jpeg')


@app.route('/animal/cat')
def cat():
    img_url = actions.get_image_url('cat')

    img_name = str(uuid.uuid4())
    img_src = app_dir + '/static/animals/' + img_name + '.jpg'

    img = requests.get(img_url[0]['url'], stream=True).raw

    actions.process_image(img, img_src)

    image = ImageEdit(animal_type='Cat', processed_image=img_name)

    actions.insert_data_in_db(image)

    return send_file(img_src, mimetype='image/jpeg')


@app.route('/history')
def history():
    # getting a list with all requests in decreasing order
    animals = ImageEdit.query.order_by(ImageEdit.date.desc()).all()
    return render_template('index.html', animals=animals)


@app.route('/history/static/<string:processed_image>')
def post(processed_image):
    # getting an image src
    img_src = app_dir + '/static/animals/' + processed_image + '.jpg'
    return send_file(img_src, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True)
