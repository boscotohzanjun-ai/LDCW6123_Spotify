#part of the main page #
from recommender import get_mood_recommendation, add_listening_history, get_listening_stats
from plans import get_plan_details, calculate_annual_cost, compare_plans, simulate_upgrade
from playlist import add_song, remove_song, view_playlist, search_by_genre, sort_by_duration

listening_history = []
my_playlist = []

def main():
    while True:
        print("\n=== SPOTIFY-INSPIRED MUSIC & PLAN MANAGER ===")
        print("1. Mood recommendation")
        print("2. View listening stats")
        print("3. Compare subscription plans")
        print("4. Simulate plan upgrade/downgrade")
        print("5. Add song to playlist")
        print("6. View playlist")
        print("7. Search playlist by genre")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            mood = input("Your mood: ")
            print(get_mood_recommendation(mood))
        elif choice == "2":
            song = input("Song just played: ")
            minutes = float(input("Minutes listened: "))
            add_listening_history(listening_history, song, minutes)
            print(get_listening_stats(listening_history))
        elif choice == "3":
            print(compare_plans())
        elif choice == "4":
            current = input("Current plan: ")
            new = input("New plan: ")
            print(simulate_upgrade(current, new))
        elif choice == "5":
            name = input("Song name: ")
            genre = input("Genre: ")
            duration = float(input("Duration (min): "))
            add_song(my_playlist, name, genre, duration)
            print("Added!")
        elif choice == "6":
            print(view_playlist(my_playlist))
        elif choice == "7":
            genre = input("Search genre: ")
            print(search_by_genre(my_playlist, genre))
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()