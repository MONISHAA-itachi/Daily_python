import random
from datetime import datetime

quotes = [
    "Discipline beats motivation.",
    "Small steps every day lead to big results.",
    "You don’t need to be perfect, just consistent.",
    "Focus on progress, not speed.",
    "You will thank yourself later — keep going."
]

def display_quote():
    today = datetime.now().strftime("%Y-%m-%d")
    quote = random.choice(quotes)

    print("\n-----------------------------------------")
    print(f" 📅 Today: {today}")
    print(f" 💭 Quote of the Day:\n   \"{quote}\"")
    print("-----------------------------------------\n")

if __name__ == "__main__":
    display_quote()
