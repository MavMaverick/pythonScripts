import json

# Define the path to the file
file_path = 'data.txt'

# List to store parsed messages
messages = []

# Open the file and read line by line
with open(file_path, 'r') as file:
    for line in file:
        # Strip whitespace and parse each line as JSON
        line = line.strip()
        if line:  # Only process non-empty lines
            message = json.loads(line)
            messages.append(message)

# Print each message to verify
for message in messages:
    print(f"Flag: {message['flag']}, Content: {message['content']}")
