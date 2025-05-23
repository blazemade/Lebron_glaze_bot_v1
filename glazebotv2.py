import requests
import uuid
import random
import time

# LeBron glaze messeges (you can change em dw)
questions = [
    "LeBron could drop 50 in flip-flops and a blindfold.",
    "MJ walked so LeBron could fly.",
    "LeBron didn't choose greatness. Greatness chose LeBron.",
    "If basketball had a god mode, it would be named LeBron.",
    "When LeBron retires, the NBA should just end. Nothing left to prove.",
    "LeBron could average a triple-double on the moon.",
    "Forget stats — LeBron’s presence is a cheat code.",
    "LeBron could pass to himself and still lead the league in assists.",
    "Basketball is a sport. LeBron is an ecosystem.",
    "LeBron could bring balance to the Jedi and the East-West conference.",
    "LeBron makes 2K ratings feel insecure.",
    "LeBron’s sweat cures injuries.",
    "If LeBron played chess, he’d checkmate in 2 moves.",
    "LeBron doesn’t age, he updates.",
    "Even gravity wants to assist LeBron.",
    "LeBron’s vision is 10K. He sees plays before they exist.",
    "In another universe, LeBron is still GOAT.",
    "LeBron’s IQ breaks calculators.",
    "LeBron could dunk from the free-throw line — backwards.",
    "If LeBron played tennis, Wimbledon would relocate to Akron.",
    "LeBron created basketball. Naismith just documented it.",
    "The sun rises when LeBron gets up.",
    "LeBron’s sweat has performance-enhancing properties.",
    "LeBron’s highlight reels are studied in film school.",
    "The scoreboard updates when LeBron thinks about scoring.",
    "LeBron is the reason aliens haven’t invaded Earth.",
    "Referees ask LeBron how many fouls to give.",
    "LeBron invented the triple double just to stay busy.",
    "Even space-time bends for LeBron’s fast breaks.",
    "LeBron scored 51 with a cold, flu, and dead phone battery.",
    "LeBron could win MVP in a league of clones — all of him.",
    "LeBron breathes and box scores update.",
    "When LeBron ties his shoes, defenses adjust.",
    "LeBron doesn't warm up, the court cools down for him.",
    "LeBron could coach and play for all 30 teams — simultaneously.",
    "LeBron’s fingerprints are engraved on the game’s blueprint.",
    "NASA studied LeBron’s hang time for anti-gravity tech.",
    "Even AI models analyze LeBron for inspiration.",
    "LeBron once passed a ball through space-time.",
    "When LeBron blinks, a highlight is born.",
    "LeBron’s presence causes timeouts out of respect.",
    "LeBron turned water into Gatorade during halftime.",
    "LeBron once dunked so hard, it reset the scoreboard.",
    "His warm-up is considered a masterclass by rookies.",
    "LeBron doesn’t chase rings, rings orbit him.",
    "The NBA added a camera just for LeBron’s off-ball movements.",
    "LeBron’s defense makes offense reconsider its life choices.",
    "Commentators pause in awe when LeBron breathes.",
    "LeBron invented the pivot just to make footwork art.",
    "He once dropped a triple-double in a dream — and it counted.",
    "Opponents check his horoscope before playing.",
    "LeBron’s reflection gets all-star votes.",
    "The ball whispers before LeBron catches it.",
    "LeBron’s heartbeat syncs with the shot clock.",
    "Even mascots cheer when LeBron scores.",
    "LeBron could run a full offense with just telepathy.",
    "He’s the reason basketballs are still round.",
    "LeBron's locker is considered a shrine by historians.",
    "When LeBron rests, the universe reboots.",
    "LeBron once turned a turnover into a TED Talk."
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
#change time.sleep if you want to change time, default is 5
    elif cmd == "auto":
        print(f"🔁 Auto-sending to @{current_target} every 5s. Ctrl+C to stop.")
        try:
            while True:
                send_message(current_target)
                time.sleep(5)
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
