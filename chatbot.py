import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today?", ]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi!", ]
    ],
    [
        r"(.*) relationship (.*)",
        ["It seems like you're talking about relationships. Can you tell me more?", ]
    ],
    [
        r"how are you?",
        ["I'm good, how about you?", ]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no problem at all.", ]
    ],
    [
        r"quit",
        ["Bye! Take care. See you soon!", ]
    ]
]

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "me": "you"
}

def start_chat():
    print("Hi! I'm your relationship chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == '__main__':
    start_chat()