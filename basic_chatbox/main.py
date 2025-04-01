import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses (pattern-response pairs)
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hey there!", "Hi! How can I help you?"]),
    (r"what is your name?", ["I'm ChatBot, your virtual assistant."]),
    (r"how are you?", ["I'm fine, thank you!", "I'm just a bot, but I'm doing great!"]),
    (r"bye", ["Goodbye!", "See you later!", "Take care!"])
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
def start_chat():
    print("Chatbot: Hi! Type 'bye' to exit.")
    chatbot.converse()

start_chat()