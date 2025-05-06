import loader
import pygame
import time
import random

pygame.mixer.init()

# You will need to create a Clips folder with every possible sound below:
# AA.wav
# AE.wav
# AH.wav
# AO.wav
# AW.wav
# AY.wav
# B.wav
# CH.wav
# D.wav
# DH.wav
# EH.wav
# ER.wav
# EY.wav
# F.wav
# G.wav
# HH.wav
# IH.wav
# IY.wav
# JH.wav
# K.wav
# L.wav
# M.wav
# N.wav
# NG.wav
# OW.wav
# OY.wav
# P.wav
# R.wav
# S.wav
# SH.wav
# T.wav
# TH.wav
# UH.wav
# UW.wav
# V.wav
# W.wav
# Y.wav
# Z.wav
# ZH.wav

# for proper ponounciations see the pronounce.json file


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


filepath = 'dictionary.txt'
pronunciation_dict = loader.load_and_create_dict(filepath)


testSentence = "This is a test sentence"
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


