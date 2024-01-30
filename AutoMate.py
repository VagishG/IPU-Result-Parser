'''
Take a audio of english song 
convert it into text format 
for every 5 second of the clip then take if there are certain characters then write that on to an image else create one more image for doing the same repeat this process until the song has run out 
if there is a pause or musical part then create certain amount of frames that can replicate that part 

Output video len is to be 24 fps ie for every 1 second there are supoosed to be 24 frames 
'''

import mutagen.id3

def extract_lyrics_from_mp3(filename):
  """Extracts lyrics from an MP3 file.

  Args:
    filename: The path to the MP3 file.

  Returns:
    The lyrics of the song, or None if not found.
  """

  try:
    # Open the MP3 file and access its ID3 tags
    audio = mutagen.id3.ID3(filename)
    lyrics_frame = audio.getall("USLT")

    # Check if lyrics are present
    if lyrics_frame:
      lyrics = lyrics_frame[0].text.strip()  # Extract and clean lyrics
      return lyrics
    else:
      print(f"No lyrics found in '{filename}'.")
      return None
  except Exception as e:
    print(f"Error reading MP3 file: {e}")
    return None

# Get input for the MP3 file path
filename = "./Years.mp3"

# Extract the lyrics
lyrics = extract_lyrics_from_mp3(filename)

# Print the lyrics if found
if lyrics:
  print("\nLyrics:\n")
  print(lyrics)
else:
  print("Lyrics not found.")
