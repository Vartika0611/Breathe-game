import time
import sys

def breathing_animation(text, duration):
    for i in range(duration):
        sys.stdout.write(f"\r{text} {'.' * (i % 4)}")
        sys.stdout.flush()
        time.sleep(1)
    print()

def guided_meditation():
    print("🌟 Welcome to the Guided Meditation Game 🌟")
    print("Find a comfortable position and relax...\n")
    time.sleep(2)

    cycles = 3  # You can increase the number of cycles for longer meditation

    for _ in range(cycles):
        breathing_animation("Breathe In", 4)
        breathing_animation("Hold", 4)
        breathing_animation("Breathe Out", 6)
        print()

    print("\n✨ Great job! You completed the relaxation cycle✨")
    print("Take this peace with you through the rest of your day 💛")

if __name__ == "__main__":
    guided_meditation()
