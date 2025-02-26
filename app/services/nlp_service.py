from typing import Dict, Tuple
from datetime import datetime
import random

class NLPService:
    def __init__(self):
        self.intent_patterns = {
            'greeting': ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening'],
            'farewell': ['goodbye', 'bye', 'see you', 'later', 'take care', 'cya'],
            'weather': ['weather', 'temperature', 'forecast', 'rain', 'sunny'],
            'time': ['time', 'clock', 'hour', 'date'],
            'help': ['help', 'assist', 'support', 'guide', 'what can you do'],
            'mood': ['how are you', 'feeling', 'mood'],
            'name': ['your name', 'who are you', 'what are you'],
            'joke': ['joke', 'funny', 'make me laugh'],
            'unknown': []
        }

        self.greeting_responses = [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Greetings! How may I assist you?",
            "Hey! Nice to hear from you!",
        ]

        self.farewell_responses = [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Bye! It was nice talking to you!",
            "Until next time! Stay awesome!",
        ]

        self.jokes = [
            "Why don't programmers like nature? It has too many bugs!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call a fake noodle? An impasta!",
        ]

    def get_time_response(self) -> str:
        current_time = datetime.now()
        return f"It's {current_time.strftime('%I:%M %p')} on {current_time.strftime('%A, %B %d, %Y')}"

    def get_help_response(self) -> str:
        capabilities = [
            "- Greet you and chat casually",
            "- Tell you the current time and date",
            "- Tell you jokes",
            "- Respond to questions about my mood or name",
            "- Say goodbye when you're leaving"
        ]
        return "I can help you with several things:\n" + "\n".join(capabilities)

    def process_input(self, text: str) -> Tuple[str, str]:
        """
        Process the input text and return the detected intent and response
        """
        text = text.lower()
        
        # Find matching intent
        detected_intent = 'unknown'
        for intent, patterns in self.intent_patterns.items():
            if any(pattern in text for pattern in patterns):
                detected_intent = intent
                break
        
        # Generate appropriate response based on intent
        if detected_intent == 'greeting':
            response = random.choice(self.greeting_responses)
        elif detected_intent == 'farewell':
            response = random.choice(self.farewell_responses)
        elif detected_intent == 'time':
            response = self.get_time_response()
        elif detected_intent == 'weather':
            response = "I'm not connected to a weather service yet, but I'm working on it!"
        elif detected_intent == 'help':
            response = self.get_help_response()
        elif detected_intent == 'mood':
            response = "I'm feeling great and excited to help you! How are you doing?"
        elif detected_intent == 'name':
            response = "I'm your AI assistant, created to help make your day a little easier!"
        elif detected_intent == 'joke':
            response = random.choice(self.jokes)
        else:
            response = "I'm not sure how to help with that. Try asking me for 'help' to see what I can do!"

        return detected_intent, response
