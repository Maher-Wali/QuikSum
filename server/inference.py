import sys
import json
import google.generativeai as genai
#from IPython.display import HTML, Markdown, display
import math
from dotenv import load_dotenv
import os

load_dotenv() 
API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)


# Read input data from stdin
input_data = sys.stdin.read()
data = json.loads(input_data)

try:
    user_input = data.get("input")
    summary_length = data.get("length")
    length = len(user_input.split(" "))
    number_of_words = math.floor(float(summary_length)/100 * length)
    flash = genai.GenerativeModel('gemini-1.5-flash')
    prompt = "summarize in " + str(number_of_words) +  " words : " + user_input
    summary = flash.generate_content(prompt)

    # Output the summary as a JSON object
    print(json.dumps({"result": summary.text}))

except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}", file=sys.stderr)
    sys.exit(1)  # Exit with error code if JSON decoding fails
