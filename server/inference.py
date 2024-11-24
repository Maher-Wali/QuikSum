import sys
import json
from transformers import BartForConditionalGeneration, BartTokenizer

# Read input data from stdin
input_data = sys.stdin.read()

try:
    # Parse the input JSON
    user_input = json.loads(input_data).get("input", "")

    # Load the tokenizer and fine-tuned summarization model
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

    # Tokenize the input text
    inputs = tokenizer.encode(user_input, return_tensors="pt", max_length=1024, truncation=True)

    # Generate the summary
    summary_ids = model.generate(
        inputs, 
        max_length=50, 
        min_length=10, 
        length_penalty=4.0, 
        num_beams=6, 
        early_stopping=True
    )

    # Decode the summary
    summary = str(tokenizer.decode(summary_ids[0], skip_special_tokens=True))

    # Output the summary as a JSON object
    print(json.dumps({"result": summary}))

except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}", file=sys.stderr)
    sys.exit(1)  # Exit with error code if JSON decoding fails
