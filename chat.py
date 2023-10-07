from gradio_client import Client
import sys
import time
client = Client("https://ysharma-explore-llamav2-with-tgi.hf.space/")
print("Ask a question")
COLOR_BLUE = '\033[94m'
COLOR_RED = '\033[91m'
def autotype(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        now = 0.005
        time.sleep(now)
    sys.stdout.write('\n')
while True:
  sys.stdout.write(COLOR_RED)
  n = input("You: ")
  question = n
  result = client.predict(question, api_name="/chat_1")
  sys.stdout.write(COLOR_BLUE)
  autotype(result)
  
