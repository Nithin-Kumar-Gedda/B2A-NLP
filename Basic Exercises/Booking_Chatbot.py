from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
import re

# 1. Load the model

model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# 2. Slot storage

booking_info = {
    "departure_city":None,
    "destination_city":None,
    "travel_date":None,
    "travel_class": None
}

# 3. Slot function

def extract_slot(user_input):

    cities = ["India", 
              "Germany",
              "USA",
              "UK"
              "Dubai",
              "France",
              "China",
              "Africa",
              "Iran",
              "Italy",
              "Portugal",
              "Spain",
              "Irland",
              "Finland",
              "Newzland",
              "Australia",
              "Nethherland",
              "Greenland",
              "Swizerland"]
    for city in cities:
        if city.lower() in user_input.lower():
            if booking_info["departure_city"] is None:
                booking_info["departure_city"] = city
            elif booking_info["destination_city"] is None:
                booking_info["destination_city"] = city
            
    # data detection
    date_pattern = r"\b\d{1,2}/\d{1,2}/\d{4}\b"
    date_match = re.search(date_pattern, user_input)
    if date_match:
        booking_info["travel_date"] = date_match.group()

    # Class detection
    if "business" in user_input.lower():
        booking_info["travel_class"] = "Bussiness"
    elif "economy" in user_input.lower():
        booking_info["travel_class"] = "Economy"

# 4. Generate AI Response

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        max_length = 300,
        temperature = 0.7,
        do_sample = True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens = True)

# 5. Chat loop

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    extract_slot(user_input)

    # checking missing info
    missing = [key for key, value in booking_info.items() if value is None]
    if missing:
        next_question = f"""
        You are a professional flight booking assistant.
        The following details are missing: {missing}.
        Ask the user politely for the missing information. 
        """
        response = generate_response(next_question)

    else:
        confirmation_prompt = f"""
        Confirm the booking with the following details:
        Departure: {booking_info['departure_city']}
        Destination: {booking_info['destination_city']}
        Date: {booking_info['travel_date']}
        Class: {booking_info['travel_date']}

        Respond professionally. 
        """
        response = generate_response(confirmation_prompt)

    print("Bot:", response)