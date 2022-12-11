import time, os, getpass
import logging
import streamlit as st
import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt
from PIL import Image
from settings import IMAGE_DIR, DURATION, WAVE_OUTPUT_FILE
from src.sound import sound
from src.transcript import get_text_from_audio
from src.imagine import save_image_from_prompt

##setup_logging()
logger = logging.getLogger('app')

def main():
    title = "Getting Images from Audio"
    st.title(title)
    image = Image.open(os.path.join(IMAGE_DIR, 'app_guitar.jpg'))
    st.image(image, use_column_width=True)

    if st.button('Record'):
        with st.spinner(f'Recording for {DURATION} seconds ....'):
            sound.record()
        st.success("Recording completed")

    if st.button('Play'):
        # sound.play()
        try:
            audio_file = open(WAVE_OUTPUT_FILE, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
        except:
            st.write("Please record sound first")

    # Add a placeholder
    if st.button('Display Spectrogram'):
        # type = st.radio("Scale of spectrogram:",
        #                 ('mel', 'DB'))
        if os.path.exists(WAVE_OUTPUT_FILE):
            spectrogram, format = get_spectrogram(type='mel')
            display(spectrogram, format)
        else:
            st.write("Please record sound first")

    if st.button('Get images from file'):
      text_from_audio = get_text_from_audio(WAVE_OUTPUT_FILE)
      save_image_from_prompt(text_from_audio)
      #TODO: This will be consumed and diaplayed by fronted

if __name__ == '__main__':
    main()