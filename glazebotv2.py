import requests
import uuid
import random
import threading
import time

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
    "LeBron once turned a turnover into a TED Talk.",
    "LeBron’s dribble has its own gravitational field.",
    "LeBron once signed a sneaker deal mid fast-break.",
    "If LeBron was in the Matrix, he'd dunk in bullet time.",
    "LeBron sees X’s and O’s in real life.",
    "LeBron’s jersey number should be pi — never-ending.",
    "LeBron could outscore a team with one hand tied.",
    "LeBron blinked and a dynasty formed.",
    "Even his sweatbands average 10 assists.",
    "LeBron once challenged gravity to 1v1 — and won.",
    "Every time LeBron breathes, a stat is born.",
    "LeBron once taught a referee the rulebook mid-game.",
    "LeBron doesn’t play the game — he rewrites it.",
    "His shadow blocks shots.",
    "Even mirrors reflect his clutch gene.",
    "LeBron’s sneaker squeak breaks ankles.",
    "The court becomes sacred when LeBron steps on it.",
    "LeBron scored 30 in a scrimmage against fate.",
    "Defenses draw straws to guard him.",
    "LeBron’s layup package is DLC in real life.",
    "He signs contracts with exclamation marks — not pens."
]

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)"
]

try:
    with open("proxies.txt") as f:
        proxies = [line.strip() for line in f if line.strip()]
except:
    proxies = [None]

current_target = "demo_user"
use_proxies = True

def send_message(username, proxy=None):
    question = random.choice(questions)
    data = {
        "username": username,
        "question": question,
        "deviceId": str(uuid.uuid4()),
        "referrer": "https://snapchat.com"
    }
    headers = {
        "User-Agent": random.choice(user_agents),
        "Content-Type": "application/x-www-form-urlencoded"
    }

    proxy_dict = {
        "http": proxy,
        "https": proxy
    } if proxy else None

    try:
        res = requests.post("https://ngl.link/api/submit", data=data, headers=headers, proxies=proxy_dict, timeout=8)
        print(f" Sent to @{username}: {question} | Status: {res.status_code} | Proxy: {proxy or 'local'}")
    except Exception as e:
        print(f" Error ({proxy or 'local'}): {e}")

print("🟢 LeBron Glaze Bot Started")
print("Commands: send | auto | threaded | target | proxy | exit")

while True:
    cmd = input("Command: ").strip().lower()

    if cmd == "send":
        proxy = random.choice(proxies) if use_proxies else None
        send_message(current_target, proxy)

    elif cmd == "auto":
        print(f" Auto-sending to @{current_target} every 2s. Ctrl+C to stop. Proxies: {'ON' if use_proxies else 'OFF'}")
        try:
            while True:
                proxy = random.choice(proxies) if use_proxies else None
                send_message(current_target, proxy)
                time.sleep(2)
        except KeyboardInterrupt:
            print("\n Auto-send stopped.")

    elif cmd == "threaded":
        try:
            count = int(input(" Threads? "))
            def worker():
                proxy = random.choice(proxies) if use_proxies else None
                send_message(current_target, proxy)
                time.sleep(random.uniform(1, 4))
            threads = []
            for _ in range(count):
                t = threading.Thread(target=worker)
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
        except:
            print(" Invalid input.")

    elif cmd == "target":
        new_target = input(" Enter new target username (no @): ").strip()
        if new_target:
            current_target = new_target
            print(f" Target set to: @{current_target}")
        else:
            print(" Invalid username.")

    elif cmd == "proxy":
        use_proxies = not use_proxies
        print(f" Proxy usage is now {'ENABLED' if use_proxies else 'DISABLED'}.")

    elif cmd == "exit":
        print("Exiting bot.....")
        break

    else:
        print("❓ Unknown command. Try send | auto | threaded | target | proxy | exit")
#enjoy this friend =)