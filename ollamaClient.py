import requests
import json

class OllamaClient:

    def __init__(self, model="qwen3.5:4b", stream=False, url="http://localhost:11434/api/chat"):
        self.model = model
        self.stream = stream
        self.url = url

    def createPayload(self, prompt):
        data = {
            "model": self.model,
            "messages": [{"role":"user", "content": prompt}],
            "stream": self.stream
        }
        return data

    def getResponse(self, prompt):
        data = self.createPayload(prompt)
        response = requests.post(self.url, json=data)
        response_json = json.loads(response.text)
        ai_reply = response_json["message"]["content"]
        return ai_reply

if __name__ == "__main__":
    ollamaClient = OllamaClient()
    prompt = input("Prompt: ")
    while prompt != "exit" and prompt != "quit":
        response = ollamaClient.getResponse(prompt)
        print(response)
        prompt = input("Prompt: ")
