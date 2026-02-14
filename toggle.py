import pygame
import time

pygame.init()

# Load nature sounds (You need these mp3/wav files in the same folder)
sounds = {
    "1": ("Rain", "rain.wav"),
    "2": ("Ocean Waves", "ocean.wav"),
    "3": ("Forest Birds", "birds.wav")
}

channels = {}

def menu():
    print("\n🎧 Nature Soundscape Generator 🎧")
    print("Choose sounds to toggle them ON/OFF:")
    print("1 - Rain 🌧️")
    print("2 - Ocean Waves 🌊")
    print("3 - Forest Birds 🐦")
    print("4 - Stop all sounds & Exit ❌")

def toggle_sound(key):
    if key not in channels:
        sound = pygame.mixer.Sound(sounds[key][1])
        channel = sound.play(loops=-1)
        channels[key] = channel
        print(f"✔️ {sounds[key][0]} sound ON")
    else:
        channels[key].stop()
        del channels[key]
        print(f"❌ {sounds[key][0]} sound OFF")

def main():
    while True:
        menu()
        choice = input("Enter choice: ")
        if choice in sounds:
            toggle_sound(choice)
        elif choice == "4":
            print("Stopping all sounds…")
            for ch in channels.values():
                ch.stop()
            break
        else:
            print("Invalid choice!")
        time.sleep(1)

if __name__ == "__main__":
    main()
