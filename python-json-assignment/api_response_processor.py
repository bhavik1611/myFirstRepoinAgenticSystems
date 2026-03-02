"""
Python JSON Assignment
JSON Based API Response Processor
"""

import json
from datetime import datetime

def read_api_response(content, file_path=None) -> dict:
    """
    Read JSON content from a string or a file and return a dictionary
    """
    if content is not None:
        return json.loads(content)
    elif file_path is not None:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        raise ValueError("Invalid input type. Expected a string or a file path.")

def process_api_response(api_response):
    """
    Process the API response and return the follow-up result as a JSON-formatted string
    """

    request_id = api_response.get("id")
    status = api_response.get("status")
    result = api_response.get("result", {})
    text_result = result.get("text")
    confidence = result.get("confidence")

    print(f"==================Request Start - {request_id}=============================")
    print(f"Status: {status}")
    print(f"Text: {text_result}")
    print(f"Confidence: {confidence:.2f}")

    if isinstance(confidence, (int, float)) and confidence < 0.9:
        print("Warning: Confidence score is below 0.9")

    print(f"==================Request End - {request_id}=============================")
    followup_result = {
        "id": request_id,
        "status": status,
        "followup": {
            "message": "Thank you for your response.",
            "timestamp": datetime.now().isoformat()
        }
    }
    return json.dumps(followup_result, indent=2)

def write_json_to_file(json_string, file_path):
    """
    Write JSON content to a file
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(json_string)

JSON_STRING = '''
{
  "id": "req_999",
  "status": "failed",
  "result": {
    "text": "Goodbye world",
    "confidence": 0.45
  }
}
'''

def main():
    """
    Main function
    """
    # Method 1: Read JSON content from a string using json.loads
    api_response_from_string = read_api_response(JSON_STRING, None)
    # Method 2: Read JSON content from a file using json.load
    api_response_from_file = read_api_response(None, "./python-json-assignment/api-response.json")

    followup_json_from_string = process_api_response(api_response_from_string)
    followup_json_from_file = process_api_response(api_response_from_file)

    # Write the follow-up result to a file named response.json
    write_json_to_file(followup_json_from_string, "./python-json-assignment/response1.json")
    write_json_to_file(followup_json_from_file, "./python-json-assignment/response2.json")

if __name__ == "__main__":
    main()
