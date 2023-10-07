from gradio_client import Client
import sys
import time
client = Client("https://ysharma-explore-llamav2-with-tgi.hf.space/")
print("Ask a question")
def autotype(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        now = 0.005
        time.sleep(now)
    sys.stdout.write('\n')
while True:
  n = input("You: ")
  question = n
  result = client.predict(question, api_name="/chat_1")
  autotype(result)
  
