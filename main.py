# ==========================================
# SPOTIFY-INSPIRED MUSIC & PLAN MANAGER
# All teammates' code combined into ONE file
# ==========================================

# ------------------------------------------
# Part of: Bosco Toh Zan Jun
# Mood Recommendation & Listening Stats
# ------------------------------------------

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



# ------------------------------------------
# Part of: Tai Teck Hwa
# Subscription Plans & Cost Calculator
# ------------------------------------------

PLANS = {
    "free": {"price": 0.00, "features": "Ads, shuffle-only play, standard audio"},
    "individual": {"price": 17.90, "features": "No ads, offline downloads, high audio quality"},
    "duo": {"price": 23.90, "features": "2 Premium accounts, Duo Mix playlist"},
    "family": {"price": 29.90, "features": "Up to 6 accounts, parental controls"},
    "student": {"price": 8.95, "features": "Premium features, discounted rate"},
}


def get_plan_details(plan):
    return PLANS.get(plan.lower())


def calculate_annual_cost(monthly_price):
    return monthly_price * 12


def compare_plans():
    lines = []
    lines.append(f"{'Plan':<12} {'Monthly':<10} {'Annual (RM)':<12} {'Features'}")
    lines.append("-" * 75)
    for name, info in PLANS.items():
        annual = calculate_annual_cost(info['price'])
        lines.append(f"{name.title():<12} RM{info['price']:<8.2f} RM{annual:<10.2f} {info['features']}")
    return "\n".join(lines)


def calculate_plan_change(current_plan, new_plan):
    current = get_plan_details(current_plan)
    new = get_plan_details(new_plan)
    if not current or not new:
        return "Invalid plan(s) selected."
    diff = new["price"] - current["price"]
    if diff > 0:
        return f"Upgrading from {current_plan} to {new_plan} costs RM{diff:.2f} more per month."
    elif diff < 0:
        return f"Downgrading from {current_plan} to {new_plan} saves RM{abs(diff):.2f} per month."
    else:
        return "Same price — no change in cost."


# ------------------------------------------
# Part of: Chen Shan Horng
# Playlist Manager
# ------------------------------------------

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


# ------------------------------------------
# Shared: Main Program (built together)
# ------------------------------------------

listening_history = []
my_playlist = []


def main():
    while True:
        print("\n=== SPOTIFY-INSPIRED MUSIC & PLAN MANAGER ===")
        print("1. Mood recommendation")
        print("2. Log a song & view listening stats")
        print("3. Compare subscription plans")
        print("4. Simulate plan upgrade/downgrade")
        print("5. Add song to playlist")
        print("6. View playlist")
        print("7. Search playlist by genre")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            mood = input("Your mood (happy/sad/workout/study/party/chill): ").strip()
            print(get_mood_recommendation(mood))

        elif choice == "2":
            song = input("Song just played: ").strip()
            minutes = float(input("Minutes listened: ").strip())
            add_listening_history(listening_history, song, minutes)
            print(get_listening_stats(listening_history))

        elif choice == "3":
            print(compare_plans())

        elif choice == "4":
            current = input("Current plan: ").strip()
            new = input("New plan: ").strip()
            print(calculate_plan_change(current, new))

        elif choice == "5":
            name = input("Song name: ").strip()
            genre = input("Genre: ").strip()
            duration = float(input("Duration (min): ").strip())
            add_song(my_playlist, name, genre, duration)
            print("Added!")

        elif choice == "6":
            print(view_playlist(my_playlist))

        elif choice == "7":
            genre = input("Search genre: ").strip()
            result = search_by_genre(my_playlist, genre)
            if isinstance(result, list):
                for s in result:
                    print(f"{s['name']} | {s['genre']} | {s['duration']} min")
            else:
                print(result)

        elif choice == "8":
            print("Thanks for using the app. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()