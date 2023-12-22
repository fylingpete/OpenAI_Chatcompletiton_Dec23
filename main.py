from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# ANSI escape code for green text
GREEN = "\033[92m"
RESET = "\033[0m"  # Resets the color to defaultple

# Starting messages in the conversation
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
]

while True:
    # Send messages to the API and get a response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extract the response message
    assistant_message = response.choices[0].message.content
    print(GREEN + "Assistant:", assistant_message + RESET)

    # Get user input
    user_message = input("You: ")

    # Break the loop if the user types 'exit'
    if user_message.lower() == 'exit':
        break
    # Add user message to the conversation history
    messages.append({"role": "user", "content": user_message})

