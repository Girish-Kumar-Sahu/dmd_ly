import time

# Lyrics from 45-60 seconds of "Diet Mountain Dew" by Lana Del Rey (Verse 1 segment)
lyrics = [
    "Baby, put on heart-shaped sunglasses",
    "Cause we gonna take a ride",
    "I'm not gonna listen to what the past says",
    "I been waitin' up all night",
    "Take another drag, turn me to ashes",
    "Ready for another lie?"
]


delays = [3, 4, 3.5, 2.8, 3.2, 2.5]  # adjust these according to song timing

for i in range(len(lyrics)):
    print(lyrics[i])
    time.sleep(delays[i])
