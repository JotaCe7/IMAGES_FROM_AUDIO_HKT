import os, io, warnings
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from configparser import ConfigParser
from PIL import Image

from settings import STABILITY_KEY ,IMAGE_OUPUT_FILE,CONGIF_FILE

config=ConfigParser()
config.read(CONGIF_FILE)
config_stability=config['Stability']


os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
os.environ['STABILITY_KEY'] = STABILITY_KEY

# Set up our connection to the API.
stability_api = client.StabilityInference(
    key=STABILITY_KEY, # API Key reference.
    verbose=True, # Print debug messages.
    engine="stable-diffusion-v1-5", # Set the engine to use for generation. 
    # Available engines: stable-diffusion-v1 stable-diffusion-v1-5 stable-diffusion-512-v2-0 stable-diffusion-768-v2-0 stable-inpainting-v1-0 stable-inpainting-512-v2-0
)



#TODO Define these parameters in a config file
def save_image_from_prompt(prompt: str):
  answers = stability_api.generate(
    prompt=prompt,
    seed=int(config_stability['seed']),
    steps=int(config_stability['steps']), 
    cfg_scale=float(config_stability['cfg_scale']),
    width=int(config_stability['width']), 
    height=int(config_stability['height']), 
    samples=int(config_stability['samples']), 
    sampler=generation.SAMPLER_K_DPMPP_2M # Choose which sampler we want to denoise our generation with.
                                                # Defaults to k_dpmpp_2m if not specified. Clip Guidance only supports ancestral samplers.
                                                # (Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral, k_dpmpp_2s_ancestral, k_lms, k_dpmpp_2m)
  )

  for resp in answers:
      for artifact in resp.artifacts:
          if artifact.finish_reason == generation.FILTER:
              warnings.warn(
                  "Your request activated the API's safety filters and could not be processed."
                  "Please modify the prompt and try again.")
          if artifact.type == generation.ARTIFACT_IMAGE:
              img = Image.open(io.BytesIO(artifact.binary))
              img.save(IMAGE_OUPUT_FILE)
              binary_data = io.BytesIO(artifact.binary)
              

              