import spacy

nlp = spacy.load("en_core_web_sm")

intents = {
    "greetings":["hi","hey","hello"],
    "goodbye":["ok","bye","quit","exit"],
    "thanks":["thanks","thank you","greatful"],
    "name":["name","who are you"]
}

response = {
    "greetings": "Hello! How are you ?",
    "goodbye": "Goodbye! Have a nice day 👋",
    "thanks": "You're welcome 😊",
    "name": "I am a basic NLP chatbot."
}

def get_intent(text):
    doc = nlp(text.lower())
    tokens = [token.text for token in doc]

    for intent, keywords in intents.items():
        for word in tokens:
            if word in keywords:
                return intent 
    return "unknown" 

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("User:")
    intent = get_intent(user_input)

    if intent == "unknown":
        print("Bot: Sorry, I didn't understand that.")
    else:
        print("Bot:", response[intent])
    
    if intent == "goodbye":
        break
