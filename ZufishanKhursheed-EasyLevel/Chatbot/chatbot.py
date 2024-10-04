import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK resources
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hi there!", "Greetings!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created using NLTK!",]
    ],
    [
        r"how are you?",
        ["I'm just a computer program, but thanks for asking!", "Doing well, how about you?"]
    ],
    [
        r"what can you do?",
        ["I can chat with you and answer your questions!",]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day!", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that. Can you rephrase?"]
    ]
]

def chatbot():
    print("Hi! I'm a simple chatbot. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input()  # Get user input
        response = chat.respond(user_input)  # Get response from the chatbot
        
        print(response)  # Print the response
        
        if "Goodbye!" in response or "See you later!" in response:
            break
    
if __name__ == "__main__":
    chatbot()
