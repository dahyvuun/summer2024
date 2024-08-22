import google.generativeai as genai

with open("API_KEY.txt", "r") as f: # API 키 읽어오기
    API_KEY = f.read().strip()

genai.configure(api_key=API_KEY) # API 키 설정