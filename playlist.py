#Part of the playlist
def add_song(playlist, song_name, genre, duration):
    playlist.append({"name": song_name, "genre": genre, "duration": duration})
    return playlist

def remove_song(playlist, song_name):
    return [s for s in playlist if s["name"].lower() != song_name.lower()]

def view_playlist(playlist):
    if not playlist:
        return "Playlist is empty."
    lines = [f"{s['name']} | {s['genre']} | {s['duration']} min" for s in playlist]
    return "\n".join(lines)

def search_by_genre(playlist, genre):
    results = [s for s in playlist if s["genre"].lower() == genre.lower()]
    return results if results else "No songs found in that genre."

def sort_by_duration(playlist):
    return sorted(playlist, key=lambda s: s["duration"])