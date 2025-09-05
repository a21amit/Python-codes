# simple_chatbot.py

import random
import nltk
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Initialize the lemmatizer
lemmer = WordNetLemmatizer()

# Define some greetings and responses
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "hello", "hi there", "greetings!"]

# Define some predefined questions and answers
FAQ = {
    "what is your name?": "I am a simple chatbot created for this mini project.",
    "how are you?": "I'm just a program, but thanks for asking!",
    "what can you do?": "I can chat with you and answer some basic questions.",
    "bye": "Goodbye! Have a great day!"
}

def greeting(sentence):
    """If user's input is a greeting, return a greeting response."""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def respond(user_input):
    """Generate a response based on user input."""
    user_input = user_input.lower()
    
    # Check for greetings
    if greeting(user_input) is not None:
        return greeting(user_input)
    
    # Check for predefined questions
    for question in FAQ:
        if user_input == question:
            return FAQ[question]
    
    return "I'm sorry, I don't understand that."

def chat():
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = respond(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    chat()