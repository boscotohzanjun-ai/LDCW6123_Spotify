# Each song is stored as a dictionary with 3 pieces of info:
# name, genre, and duration (in minutes)
 

# Function 1: Add a new song to the playlist
def add_song(playlist, song_name, genre, duration):
    new_song = {"name": song_name, "genre": genre, "duration": duration}
    playlist.append(new_song)
    return playlist
 
 
# Function 2: Remove a song from the playlist by name
def remove_song(playlist, song_name):
    new_playlist = []  # start with an empty list
 
    # go through every song one by one
    for song in playlist:
        # keep the song only if the name does NOT match
        if song["name"].lower() != song_name.lower():
            new_playlist.append(song)
 
    return new_playlist
 
# Function 3: Show every song currently in the playlist
def view_playlist(playlist):
    if len(playlist) == 0:
        return "Playlist is empty."
 
    result = ""
    for song in playlist:
        result = result + song["name"] + " | " + song["genre"] + " | " + str(song["duration"]) + " min\n"
 
    return result
 
# Function 4: Search for songs that match a genre
def search_by_genre(playlist, genre):
    matches = []
 
    for song in playlist:
        if song["genre"].lower() == genre.lower():
            matches.append(song)
 
    if len(matches) == 0:
        return "No songs found in that genre."
 
    return matches
 
# Function 5: Sort the songs from shortest to longest duration
def sort_by_duration(playlist):
    # make a copy so we don't change the original list order
    sorted_list = playlist.copy()
 
    # simple bubble sort: compare each pair and swap if out of order
    n = len(sorted_list)
    for i in range(n):
        for j in range(n - i - 1):
            if sorted_list[j]["duration"] > sorted_list[j + 1]["duration"]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
 
    return sorted_list
 
# ------------------------------------------
# Test menu — run this file on its own to test your part
# ------------------------------------------
if __name__ == "__main__":
    my_playlist = []
 
    while True:
        print("\n=== Playlist Manager (Member C) ===")
        print("1. Add song")
        print("2. Remove song")
        print("3. View playlist")
        print("4. Search by genre")
        print("5. Sort by duration")
        print("6. Exit")
 
        choice = input("Please select an option (1-6): ").strip()
 
        if choice == "1":
            name = input("Song name: ").strip()
            genre = input("Genre: ").strip()
            duration = float(input("Duration (min): ").strip())
            add_song(my_playlist, name, genre, duration)
            print("Song added!")
 
        elif choice == "2":
            name = input("Song name to remove: ").strip()
            my_playlist = remove_song(my_playlist, name)
            print("Removed (if it existed).")
 
        elif choice == "3":
            print(view_playlist(my_playlist))
 
        elif choice == "4":
            genre = input("Genre to search: ").strip()
            result = search_by_genre(my_playlist, genre)
            if isinstance(result, list):
                for song in result:
                    print(song["name"] + " | " + song["genre"] + " | " + str(song["duration"]) + " min")
            else:
                print(result)
 
        elif choice == "5":
            sorted_songs = sort_by_duration(my_playlist)
            for song in sorted_songs:
                print(song["name"] + " | " + song["genre"] + " | " + str(song["duration"]) + " min")
 
        elif choice == "6":
            print("Exiting, goodbye!")
            break
 
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")