import os

# AssemblyAI API
UPLOAD_ENDPOINT = 'https://api.assemblyai.com/v2/upload'
TRASCRIPT_ENDPOINT = "https://api.assemblyai.com/v2/transcript"
AUTHORIZATION_KEY = 'YOUR_AUTHORIZATION_KEY_GOES_HERE'

# Stability API
STABILITY_KEY = 'YOUR_STABILITY_KEY_GOES_HERE'

# The Root Directory of the project
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

OUT_DIR = os.path.join(ROOT_DIR, 'output/')
RECORDING_DIR = os.path.join(OUT_DIR, 'recording')
IMAGE_DIR = os.path.join(OUT_DIR, 'images')

WAVE_OUTPUT_FILE = os.path.join(RECORDING_DIR, "recorded.wav")
IMAGE_OUPUT_FILE = os.path.join(IMAGE_DIR, "image.jpg")

# Audio configurations
INPUT_DEVICE = 0
MAX_INPUT_CHANNELS = 1  # Max input channels
DEFAULT_SAMPLE_RATE = 44100   # Default sample rate of microphone or recording device
DURATION = 10   # 3 seconds
CHUNK_SIZE = 1024