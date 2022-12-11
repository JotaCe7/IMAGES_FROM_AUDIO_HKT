import os, io, warnings
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

from settings import STABILITY_KEY

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
    seed=992446758, # If a seed is provided, the resulting generated image will be deterministic.
                    # What this means is that as long as all generation parameters remain the same, you can always recall the same image simply by generating it again.
                    # Note: This isn't quite the case for Clip Guided generations, which we'll tackle in a future example notebook.
    steps=30, # Amount of inference steps performed on image generation. Defaults to 30. 
    cfg_scale=8.0, # Influences how strongly your generation is guided to match your prompt.
                  # Setting this value higher increases the strength in which it tries to match your prompt.
                  # Defaults to 7.0 if not specified.
    width=512, # Generation width, defaults to 512 if not included.
    height=512, # Generation height, defaults to 512 if not included.
    samples=1, # Number of images to generate, defaults to 1 if not included.
    sampler=generation.SAMPLER_K_DPMPP_2M # Choose which sampler we want to denoise our generation with.
                                                # Defaults to k_dpmpp_2m if not specified. Clip Guidance only supports ancestral samplers.
                                                # (Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral, k_dpmpp_2s_ancestral, k_lms, k_dpmpp_2m)
  )

  # Set up our warning to print to the console if the adult content classifier is tripped.
  # If adult content classifier is not tripped, save generated images.
  for resp in answers:
      for artifact in resp.artifacts:
          if artifact.finish_reason == generation.FILTER:
              warnings.warn(
                  "Your request activated the API's safety filters and could not be processed."
                  "Please modify the prompt and try again.")
          if artifact.type == generation.ARTIFACT_IMAGE:
              # img = Image.open(io.BytesIO(artifact.binary))
              # display(img)
              binary_data = io.BytesIO(artifact.binary)
              #TODO: Save this binary_data as an image file to IMAGE_OUPUT_FILE
