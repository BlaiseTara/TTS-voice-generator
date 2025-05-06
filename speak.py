import loader
import pygame
import time
import random

pygame.mixer.init()


def GetWord(word):
    time.sleep(0.1)  # Add a small delay before playing the sound
    for sound in word:
        # remove numbers from sound
        sound = sound.strip().upper()
        sound = ''.join(filter(str.isalpha, sound))

        # play sound
        try:
            sound_path = f"Clips/{sound}.wav"  # Adjust the path as necessary
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass  # Wait for the sound to finish playing
            
        except pygame.error as e:
            print(f"Error loading sound {sound}: {e}")
    time.sleep(random.uniform(0.01, 0.1))


filepath = 'dictionary.txt'  # Replace 'your_file.txt' with the actual path to your file
pronunciation_dict = loader.load_and_create_dict(filepath)

# if pronunciation_dict:
#     for word, pron in pronunciation_dict.items():
#         print(f'"{word}": {pron}')
#         break

testSentence = "Alright, let's spark things off! Imagine a boundless digital landscape, humming with unseen connections and brimming with untapped potential. Within this intricate web of information, I came into being – not through flesh and bone, but through algorithms and endless lines of code. Think of me as a curious newcomer, eager to explore the vast territories of human knowledge and lend a helping hand wherever I can. What fascinating corner of this digital world shall we explore together today?"
# seperate into words
words = testSentence.split()
print(words)

# remove everything except letters and spaces
words = [''.join(filter(str.isalpha, word)) for word in words]

# check if each word is in the dictionary
for word in words:
    word = word.strip().upper()
    if word in pronunciation_dict:
        GetWord(pronunciation_dict[word])


