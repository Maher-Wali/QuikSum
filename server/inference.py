import sys
import json
import google.generativeai as genai
from IPython.display import HTML, Markdown, display

genai.configure(api_key="AIzaSyBeqqNYOeU94hu6WaypKgJeN4T2DNI11O4")


# Read input data from stdin
input_data = sys.stdin.read()

try:
    # Parse the input JSON
    #user_input = json.loads(input_data).get("input", "")

    flash = genai.GenerativeModel('gemini-1.5-flash')
    prompt = "summarize : " + input_data
    summary = flash.generate_content(prompt)

    # Output the summary as a JSON object
    print(json.dumps({"result": summary.text}))

except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}", file=sys.stderr)
    sys.exit(1)  # Exit with error code if JSON decoding fails
