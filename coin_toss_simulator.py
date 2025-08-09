# 🪙 Coin Toss Simulator Mini Project
# 📌 Simulates a real coin toss using random module

import random

def coin_toss():
    print("🪙 Welcome to the Coin Toss Simulator!")
    print("🎯 You can guess: Heads or Tails.")
    print("🔄 Let's start...")

    # 🔹 Asking the user to start or stop
    user_input = input("👉 Type 'start' to play or 'stop' to exit: ").lower()

    if user_input == 'start':
        # Tossing the coin
        coin_result = random.choice(["Heads", "Tails"])

        try:
            # Taking user's guess
            guess = input("🔮 Enter your guess (Heads/Tails): ").title()

            if guess not in ["Heads", "Tails"]:
                print("⚠️ Please enter either 'Heads' or 'Tails'.")
                return

            print(f"\n🧑 Your Guess: {guess}")
            print(f"💻 Coin Result: {coin_result}")

            if guess == coin_result:
                print("🎉 You win! Great guess!")
            else:
                print("😢 You lose! Better luck next time.")

        except ValueError:
            print("⚠️ Invalid input! Please try again.")

    elif user_input == 'stop':
        print("👋 Thanks for using the Coin Toss Simulator! See you again.")
    else:
        print("⚠️ Invalid option. Please type 'start' or 'stop'.")

# ▶️ Start the simulator
coin_toss()
