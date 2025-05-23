import requests
import uuid
import random
import time

# LeBron glaze messeges (you can change em dw)
questions = [
    "LeBron is the definition of longevity.",
    "What keeps LeBron performing like he's 25?",
    "Is LeBron the smartest player in the league?",
    "LeBron’s leadership is unmatched, agree?",
]

device_id = str(uuid.uuid4())
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

# placeholder target
current_target = "demo_user"

def send_message(username):
    question = random.choice(questions)
    data = {
        "username": username,
        "question": question,
        "deviceId": device_id,
        "referrer": "https://snapchat.com"
    }
    try:
        res = requests.post("https://ngl.link/api/submit", data=data, headers=headers)
        print(f"✅ Sent to @{username}: {question} | Status: {res.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")

print("🟢 LeBron Glaze Bot Started")
print("Type 'send' to send one message")
print("Type 'auto' to loop")
print("Type 'target' to change who you're sending to")
print("Type 'exit' to quit")

while True:
    cmd = input("👉 Command: ").strip().lower()

    if cmd == "send":
        send_message(current_target)
#change time.sleep if you want to change time, default is 10
    elif cmd == "auto":
        print(f"🔁 Auto-sending to @{current_target} every 10s. Ctrl+C to stop.")
        try:
            while True:
                send_message(current_target)
                time.sleep(10)
        except KeyboardInterrupt:
            print("\n⛔ Auto-send stopped.")

    elif cmd == "target":
        new_target = input("🎯 Enter new target username (no @): ").strip()
        if new_target:
            current_target = new_target
            print(f"✅ Target set to: @{current_target}")
        else:
            print("❌ Invalid username.")

    elif cmd == "exit":
        print("👋 Exiting bot.")
        break

    else:
        print("❓ Unknown command. Try 'send', 'auto', 'target', or 'exit'.")
#enjoy ts ;)