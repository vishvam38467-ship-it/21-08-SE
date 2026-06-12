def extract_artist(song_title):
    # Find where ' - ' occurs and slice everything after it
    dash_index = song_title.find(' - ')
    if dash_index!= -1:
        return song_title[dash_index + 3:] # +3 to skip ' - '
    return "Format error"

# Test
print(extract_artist("Blinding Lights - The Weeknd")) # The Weeknd
print(extract_artist("Kesariya - Arijit Singh")) # Arijit Singh