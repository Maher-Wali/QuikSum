import google.generativeai as genai
#from IPython.display import HTML, Markdown, display
from dotenv import load_dotenv
import os

load_dotenv() 
API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)

text ="The BART model is a powerful tool for text summarization. It uses a Transformer-based architecture and can handle various natural language processing tasks. BART is particularly effective for summarizing long passages of text, generating concise summaries while preserving essential information."

flash = genai.GenerativeModel('gemini-1.5-flash')
prompt = "summarize : " + text
response = flash.generate_content(prompt)
print(response.text)


