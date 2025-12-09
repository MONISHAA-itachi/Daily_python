import random

words = ["python", "coffee", "future", "holiday", "planet", "coding", "network"]
score = 0

print("🌀 Word Scramble Game")
print("Unscramble the word! Type EXIT to quit.\n")

while True:
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))

    print(f"🔹 Scrambled word: {scrambled}")
    guess = input("👉 Your guess: ").lower()

    if guess == "exit":
        print(f"\n🏁 Final Score: {score}")
        print("👋 Goodbye!")
        break

    if guess == word:
        score += 1
        print("✅ Correct! +1 point\n")
    else:
        print(f"❌ Wrong! The word was: {word}\n")
