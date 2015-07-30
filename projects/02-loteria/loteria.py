import random
import os

from flask import (
    Flask,
    request, session,
    url_for, render_template, redirect
)


# Create a Flask application object
app = Flask(__name__)

# Session variables are stored client-side (on the user's browser).
# The content of these variables is encrypted, so users can't actually
# read thir contents. They could edit the sesson data, but because it 
# would not be "signed" with the secret key below, the server would
# reject is as invalid.
# You need to set a secret key (random text) and keep it secret!
app.secret_key = "shhhhhh! don't tell anyone what I am"

# The path to the directory containing our card images.
# We will store a list of image file names in a session variable.
IMAGE_DIR = app.static_folder


########################
### Helper functions ###
########################

def init_game():
    # initialize a new deck (a list of filenames)
    image_names = os.listdir(IMAGE_DIR)
    # shuffle the deck
    random.shuffle(image_names)
    # store it in the user's session
    # 'session' is a special global object that Flask provides
    # which exposes the basic session management functionality
    session['images'] = image_names


def select_from_deck():
    try:
        image_name = session['images'].pop()
    except IndexError:
        image_name = None  # sentinel
    return image_name


######################
### View functions ###
######################

@app.route('/')
def index():
    init_game()
    return render_template("index.html")


@app.route('/draw')
def draw_card():
    image_name = select_from_deck()
    if image_name is None:
        return render_template("gameover.html")
    return render_template("showcard.html", image_name=image_name)


if __name__ == '__main__':
    app.run(debug=True)


