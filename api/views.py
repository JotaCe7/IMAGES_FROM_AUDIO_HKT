import os

import settings
import utils
from flask import (
    Blueprint,
    current_app,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)
from middleware import model_predict

router = Blueprint("app_router", __name__, template_folder="templates")


@router.route("/", methods=["GET", "POST"])
def index():
    """
    GET: Index endpoint, renders our HTML code.

    POST: Used in our frontend so we can upload an audio file.
    When it receives an audio file from the UI, it also calls our ML model to
    get and display the generated images.
    """
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        # No file received, show basic UI
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)

        # File received but no filename is provided, show basic UI
        file = request.files["file"]
        if file.filename == "":
            flash("No audio file found for uploading")
            return redirect(request.url)

        # File received and it's an image, we must show it and get predictions
        if file and utils.allowed_file(file.filename):
            # In order to correctly display the image in the UI and get model
            # predictions you should implement the following:
            #   1. Get an unique file name using utils.get_file_hash() function
            #   2. Store the audio file to disk using the new name
            #   3. Send the file to be processed by the `model` service
            #      Hint: Use middleware.model_generate() for sending jobs to model
            #            service using Redis.
            #   4. Update `context` dict with the corresponding values
            # TODO
            context = {
                "text_from_audio": None,
                "images_path": None,
                "filename": None,
            }
            # Update `render_template()` parameters as needed
            # TODO
            # TEAM: This will try torender audio file, modify this to render generated images
            return render_template("index.html", filename=None, context=None)
        # File received and but it isn't an image
        else:
            flash("Allowed audio formats are -> mp3, mp4, etc...")
            return redirect(request.url)


@router.route("/display/<filename>")
def display_image(filename):
    """
    Display genetated images in our UI.
    """
    return redirect(url_for("static", filename="uploads/" + filename), code=301)


@router.route("/predict", methods=["POST"])
def predict():
    """
    Endpoint used to get generated images without need to access the UI.

    Parameters
    ----------
    file : str
        Input audio file we want to get images from.

    Returns
    -------
    flask.Response
        JSON response from our API having the following format:
            {
                "success": bool,
                "text_from_audio": str,
                "images_path": float,
            }

        - "success" will be True if the input file is valid and we get a
          prediction from our ML model.
        - "text_from_audio" text converted from audio file.
        - "images_path" path were generated images were stored.
    """
    # To correctly implement this endpoint you should:
    #   1. Check a file was sent and that file is an audio file
    #   2. Store the audio file to disk
    #   3. Send the file to be processed by the `model` service
    #      Hint: Use middleware.model_generate() for sending jobs to model
    #            service using Redis.
    #   4. Update and return `rpse` dict with the corresponding values
    # If user sends an invalid request (e.g. no file provided) this endpoint
    # should return `rpse` dict with default values HTTP 400 Bad Request code
    # TODO
    rpse = {"success": False, "prediction": None, "score": None}



# TEAM: NO NNEDED BY NOW
@router.route("/feedback", methods=["GET", "POST"])
def feedback():
    """
    Store feedback from users about wrong predictions on a plain text file.

    Parameters
    ----------
    report : request.form
        Feedback given by the user with the following JSON format:
            {
                "filename": str,
                "prediction": str,
                "score": float
            }

        - "filename" corresponds to the image used stored in the uploads
          folder.
        - "prediction" is the model predicted class as string reported as
          incorrect.
        - "score" model confidence score for the predicted class as float.
    """
    report = request.form.get("report")

    # Store the reported data to a file on the corresponding path
    # already provided in settings.py module
    # TODO

    return render_template("index.html")
