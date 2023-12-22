from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# ANSI escape code for green text
GREEN = "\033[92m"
RESET = "\033[0m"  # Resets the color to default

# Function to load chat history from file
def load_chat_history():
    try:
        with open('chat.txt', 'r') as file:
            content = file.read()
            if content.strip() == "":
                # Empty content indicates an 'even' session, start fresh
                return [{"role": "system", "content": "You are a helpful assistant."}]
            else:
                # Non-empty content indicates an 'odd' session, load history
                return eval(content)
    except FileNotFoundError:
        # File not found, start fresh
        return [{"role": "system", "content": "You are a helpful assistant."}]

# Function to save chat history to file
def save_chat_history(messages):
    with open('chat.txt', 'w') as file:
        file.write(str(messages))

# Function to clear chat history
def clear_chat_history():
    with open('chat.txt', 'w') as file:
        file.write("")

# Load chat history
messages = load_chat_history()

# Start the conversation loop
while True:
    # Send messages to the API and get a response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extract the response message
    assistant_message = response.choices[0].message.content
    print(GREEN + "Assistant:", assistant_message + RESET)

    # Add assistant's message to the conversation history
    messages.append({"role": "assistant", "content": assistant_message})

    # Get user input
    user_message = input("You: ")

    # Break the loop if the user types 'exit'
    if user_message.lower() == 'exit':
        break        
    # Clear chat history and break the loop if user enters 'clear'
    elif user_message.lower() == 'clear':
       
        clear_chat_history()
        break

    # Add user message to the conversation history
    messages.append({"role": "user", "content": user_message})

    # Save messages after each interaction
    save_chat_history(messages)
