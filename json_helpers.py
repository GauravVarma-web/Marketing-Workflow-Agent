# json_helpers.py
import re
import json

def extract_json(text):
    """
    Extract JSON object from text
    
    Args:
        text (str): Text containing JSON
        
    Returns:
        list: List of extracted JSON objects, or None if none found
    """
    pattern = r'\{.*?\}'
    matches = re.finditer(pattern, text, re.DOTALL)
    json_objects = []

    for match in matches:
        json_str = extend_search(text, match.span())
        try:
            json_obj = json.loads(json_str)
            json_objects.append(json_obj)
        except json.JSONDecodeError:
            continue

    return json_objects if json_objects else None

def extend_search(text, span):
    """
    Handle nested JSON structures
    
    Args:
        text (str): Full text
        span (tuple): Start and end position of the match
        
    Returns:
        str: Extended JSON string
    """
    start, end = span
    nest_count = 1  # Starts with 1 since we know '{' is at the start position
    for i in range(end, len(text)):
        if text[i] == '{':
            nest_count += 1
        elif text[i] == '}':
            nest_count -= 1
            if nest_count == 0:
                return text[start:i+1]
    return text[start:end]