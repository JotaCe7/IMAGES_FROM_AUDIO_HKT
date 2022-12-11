import requests
from  utils.utils import read_file
from settings import WAVE_OUTPUT_FILE, UPLOAD_ENDPOINT, TRASCRIPT_ENDPOINT, AUTHORIZATION_KEY

def upload_audio_file(filename:str = WAVE_OUTPUT_FILE):
  '''
  Uploads a audio file.
  arguments:
  ---------
  filename: str 
      absolute path where audio file is stored
      default: ROOT_DIR/output/recording/recorded.wav
  Return
  ------
      string: url where audio file is stored in the cloud 
  '''
  headers = {'authorization': AUTHORIZATION_KEY}
  upload_response = requests.post(UPLOAD_ENDPOINT,
                          headers=headers,
                          data=read_file(filename))
  audio_url = upload_response.json()['upload_url']
  return audio_url

def do_transcript(audio_url: str):
  """
  Starts a transcription job
  arguments:
  ---------
  audio_url: str 
      url where audio file is stored in the cloud 
  Return
  ------
      job id

  """
  json = { "audio_url": "https://cdn.assemblyai.com/upload/" + audio_url }
  headers = {
      "authorization": AUTHORIZATION_KEY,
      "content-type": "application/json"
  }
  transcript_response = requests.post(TRASCRIPT_ENDPOINT,
                          headers=headers,
                          json=json)
                          
  transcript_id = transcript_response.json()['id']
  return transcript_id

def get_transcript(transcript_id:str):
  """
  Get a transcription from an already started transcription job
  arguments:
  ---------
  transcript_id: str 
      job transcription id to get text from
  Return
  ------
      text result from the transcription job as a string

  """
  status = 'processing'
  while status=='processing':
    endpoint = TRASCRIPT_ENDPOINT + '/'+ transcript_id
    headers = {
        "authorization": AUTHORIZATION_KEY,
    }
    response = requests.get(endpoint, headers=headers)
    status = response.json()['status']
  text_from_audio = response.json()['text']
  return text_from_audio


def get_text_from_audio(filename:str = WAVE_OUTPUT_FILE):
  """
  Get text from audio
  arguments:
  ---------
  filename: str 
      absolute path where audio file is stored
      default: ROOT_DIR/output/recording/recorded.wav
  Return
  ------
      text result from the transcription job as a string

  """
  audio_url = upload_audio_file(filename)
  transcript_id = do_transcript(audio_url)
  text_from_audio = get_transcript(transcript_id)
  return text_from_audio