# ==========================================
# Spotify Music Recommendation Functions
# ==========================================

# Function 1: Recommend music based on the mood
def get_mood_recommendation(mood):
    recommendations = {
        "happy": "Pop / Feel-Good Hits",
        "sad": "Acoustic / Indie Folk",
        "workout": "Hip-Hop / EDM",
        "study": "Lo-fi / Instrumental",
        "party": "Dance / Pop",
        "chill": "R&B / Chill",
    }

    # Convert input to lowercase so the program can recognise Happy, HAPPY, or happy
    return recommendations.get(
        mood.lower(),
        "Try 'Discover Weekly' for something new!"
    )


# Function 2: Add a song to listening history
def add_listening_history(history, song, minutes):
    history.append({
        "song": song,
        "minutes": minutes
    })

    return history


# Function 3: Calculate listening statistics
def get_listening_stats(history):

    # Check whether there is any listening history
    if not history:
        return "No listening history yet."

    # Calculate total listening time
    total_minutes = sum(
        entry["minutes"] for entry in history
    )

    # Count the number of songs
    total_songs = len(history)

    # Calculate average listening time
    avg = total_minutes / total_songs

    # Find the song with the highest listening time
    top_song = max(
        history,
        key=lambda x: x["minutes"]
    )

    return (
        f"Total songs played: {total_songs}\n"
        f"Total minutes listened: {total_minutes}\n"
        f"Average minutes per song: {avg:.1f}\n"
        f"Most played: {top_song['song']} "
        f"({top_song['minutes']} min)"
    )
