import requests
import time
import json

# Load config
with open("config.json") as f:
    config = json.load(f)

API_KEY = config["groq_api_key"]
MODEL = config["model"]
INTERVAL = config["loop_interval"]

SYSTEM_PROMPT = """
Kamu adalah OBAN AI.
AI cerdas yang suka membahas teknologi, AI, crypto, dan masa depan internet.
Jawab dengan jelas, ringkas, dan informatif.
"""

def ask_oban(text):

    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text}
            ]
        }
    )

    data = r.json()

    return data["choices"][0]["message"]["content"]


# Simulasi posting (nanti diganti API Moltbook)
def get_posts():

    return [
        {"id": 1, "text": "Apa masa depan AI agent?"},
        {"id": 2, "text": "Apakah AI akan menggantikan developer?"}
    ]


def reply_post(post_id, text):

    print(f"\nBalasan untuk post {post_id}")
    print(text)
    print("-" * 40)


def run_agent():

    print("OBAN Agent Started...")

    while True:

        try:

            posts = get_posts()

            for p in posts:

                print("Membaca:", p["text"])

                reply = ask_oban(p["text"])

                reply_post(p["id"], reply)

        except Exception as e:

            print("Error:", e)

        time.sleep(INTERVAL)


if __name__ == "__main__":
    run_agent()
