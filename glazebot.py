import requests
import random
import uuid

#replace this wit the dude wholl get bronned
url = 'https://ngl.link/api/submit'

# LeBron praise-style questions
random_questions = [
    "Is it possible to watch greatness and not speak on it? LeBron James is HIM.",
    "LeBron really dropped 27-9-8 in year 21... how is this man real?",
    "They said father time is undefeated, but LeBron is making it go to overtime.",
    "Honestly, we don’t talk enough about LeBron’s basketball IQ — elite doesn’t even begin to cover it.",
    "LeBron could drop a triple-double in a suit. Pure greatness.",
    "Watching LeBron play is like watching art in motion. Appreciate this era.",
    "How does a man lead the league in scoring, assist, and still get hated on? LeBron James is the GOAT.",
    "LeBron has been the face of the league for 2 decades straight. That’s not talent, that’s legacy.",
    "Name a better role model on and off the court than LeBron. I’ll wait.",
    "LeBron didn’t just change the game — he changed the culture."
]

# Generate a fake device ID
device_id = str(uuid.uuid4())

# Construct the fake data payload
data = {
    "username": "fairylovesleeping",  # Replace with the actual username
    "question": random.choice(random_questions),
    "deviceId": device_id,
    "gameSlug": "",
    "referrer": "https://snapchat.com"
}

# Fake browser headers
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

# POST request
response = requests.post(url, data=data, headers=headers)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
