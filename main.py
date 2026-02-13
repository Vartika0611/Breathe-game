import time
import sys
import pygame

# ---------------------------
# Guided Breathing Meditation
# ---------------------------
def breathing_animation(text, duration):
    for i in range(duration):
        sys.stdout.write(f"\r{text} {'.' * (i % 4)}")
        sys.stdout.flush()
        time.sleep(1)
    print()

def guided_meditation():
    print("\n🌟 Guided Meditation Started 🌟")
    print("Sit comfortably, relax your shoulders...\n")
    time.sleep(2)

    cycles = 3  # Increase if you want a longer session
    for _ in range(cycles):
        breathing_animation("Breathe In", 4)
        breathing_animation("Hold", 4)
        breathing_animation("Breathe Out", 6)
        print()

    print("\n✨ You completed the relaxation cycle! ✨")
    input("Press Enter to return to menu...")

# ---------------------------
# Nature Soundscape Generator
# ---------------------------
pygame.mixer.init()

sounds = {
    "1": ("Rain", "rain.wav"),
    "2": ("Ocean Waves", "ocean.wav"),
    "3": ("Forest Birds", "birds.wav")
}

channels = {}

def show_sound_menu():
    print("\n🎧 Nature Soundscape Generator 🎧")
    print("Toggle sounds:")
    print("1 - Rain 🌧️")
    print("2 - Ocean Waves 🌊")
    print("3 - Forest Birds 🐦")
    print("4 - Stop all sounds & Exit to Main Menu")

def toggle_sound(choice):
    if choice not in channels:
        sound = pygame.mixer.Sound(sounds[choice][1])
        channel = sound.play(loops=-1)
        channels[choice] = channel
        print(f"✔ {sounds[choice][0]} sound ON")
    else:
        channels[choice].stop()
        del channels[choice]
        print(f"❌ {sounds[choice][0]} sound OFF")

def soundscape_game():
    while True:
        show_sound_menu()
        choice = input("Enter your choice: ")

        if choice in sounds:
            toggle_sound(choice)
        elif choice == "4":
            for ch in channels.values():
                ch.stop()
            channels.clear()
            print("🌿 Returning to main menu...")
            time.sleep(1)
            break
        else:
            print("Invalid choice!")

# ---------------------------
# Main Menu
# ---------------------------
def main_menu():
    while True:
        print("\n╔════════════════════════════════╗")
        print("║  🌿 Mindfulness Relaxation App 🌿  ║")
        print("╚════════════════════════════════╝")
        print("1️⃣ Guided Meditation")
        print("2️⃣ Nature Soundscape Generator")
        print("3️⃣ Exit")
        choice = input("Select option: ")

        if choice == "1":
            guided_meditation()
        elif choice == "2":
            soundscape_game()
        elif choice == "3":
            print("Thank you! Have a peaceful day 🌼")
            break
        else:
            print("⚠ Invalid option! Try again.")

if __name__ == "__main__":
    main_menu()
