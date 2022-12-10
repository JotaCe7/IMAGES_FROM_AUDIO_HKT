import json
import os
import time

import numpy as np
import redis
import settings
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import decode_predictions, preprocess_input
from tensorflow.keras.preprocessing import image

# TODO
# Connect to Redis and assign to variable `db``
# Make use of settings.py module to get Redis settings like host, port, etc.
db = None

# TODO
# Load your ML model and assign to variable `model`
# See https://drive.google.com/file/d/1ADuBSE4z2ZVIdn66YDSwxKv-58U7WEOn/view?usp=sharing
# for more information about how to use this model.
model = None


def model_generate(audio_name):
    """
    Load audio file from the corresponding folder based on the audio file name
    received, then, run our ML model to convert it to text and generate strings.

    Parameters
    ----------
    audio_name : str
        Audio filename.

    Returns
    -------
    text_from_audio, images_path : tuple(str, str)
        Text generated from the audio file, 
        path were the generated images were saved.
    """
    text_from_audio = None
    images_path = None
    # TODO

    return text_from_audio, images_path


def main():
    """
    Loop indefinitely asking Redis for new jobs.
    When a new job arrives, takes it from the Redis queue, process it
    and stores the results back in Redis using
    the original job ID so other services can see it was processed and access
    the results.

    Load audio file from the corresponding folder based on the audio name
    received, then, run our ML model to get text and genereted images.
    """
    while True:
        # Inside this loop you should add the code to:
        #   1. Take a new job from Redis
        #   2. Run your ML model on the given data
        #   3. Store model results in a dict with the following shape:
        #      {
        #         "text_from_audio": str,
        #         "images_path": str,
        #      }
        #   4. Store the results on Redis using the original job ID as the key
        #      so the API can match the results it gets to the original job
        #      sent
        # Hint: You should be able to successfully implement the communication
        #       code with Redis making use of functions `brpop()` and `set()`.
        # TODO

        # Don't forget to sleep for a bit at the end
        time.sleep(settings.SERVER_SLEEP)


if __name__ == "__main__":
    # Now launch process
    print("Launching ML service...")
    main()
