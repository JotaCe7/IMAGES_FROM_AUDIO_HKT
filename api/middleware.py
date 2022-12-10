import json
import time
from uuid import uuid4

import redis
import settings

# TODO
# Connect to Redis and assign to variable `db``
# Make use of settings.py module to get Redis settings like host, port, etc.
db = None


def model_generate(audio_name):
    """
    Receives an audio file name and queues the job into Redis.
    Will loop until getting the answer from our ML service.

    Parameters
    ----------
    audio_name : str
        Name for the audio file uploaded by the user.

    Returns
    -------
    text_from_audio,  : tuple(str, str)
        Return text converted from audio and the path wheregenereated images are stored
    """
    text_from_audio = None
    images_path = None

    # Assign an unique ID for this job and add it to the queue.
    # We need to assing this ID because we must be able to keep track
    # of this particular job across all the services
    # TODO
    job_id = None

    # Create a dict with the job data we will send through Redis having the
    # following shape:
    # {
    #    "id": str,
    #    "audio_name": str,
    # }
    # TODO
    job_data = None

    # Send the job to the model service using Redis
    # Hint: Using Redis `lpush()` function should be enough to accomplish this.
    # TODO

    # Loop until we received the response from our ML model
    while True:
        # Attempt to get model predictions using job_id
        # TODO
        output = None

        # Don't forget to delete the job from Redis after we get the results!
        # Then exit the loop
        # TODO

        # Sleep some time waiting for model results
        time.sleep(settings.API_SLEEP)
        
        # Do not forget break condition
        break

    return text_from_audio, images_path
