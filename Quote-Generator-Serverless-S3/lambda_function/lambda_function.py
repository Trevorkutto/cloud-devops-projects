import json
import random

quotes = [
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "Innovation distinguishes between a leader and a follower.", "author": "Steve Jobs"},
    {"text": "Stay hungry, stay foolish.", "author": "Steve Wozniak"},
    {"text": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"}
    { text: "It is during our darkest moments that we must focus to see the light.", author: "Aristotle" },
    { text: "Success is not final, failure is not fatal: it is the courage to continue that counts.", author: "Winston Churchill" },
    { text: "The only impossible journey is the one you never begin.", author: "Tony Robbins" },
]

def lambda_handler(event, context):
    quote = random.choice(quotes)
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(quote)
    }
