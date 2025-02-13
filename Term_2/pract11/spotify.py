
class Song():
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def __str__(self):
        return f"{self.name}, {self.length}"


class Playlist():

    def __init__(self, name):
        self.name = name
        self.playlist_songs = []
    
    def add_song(self, song):
        self.playlist_songs.append(song)
        print("Song added")
    
    def remove_song(self, song_title):
        for song in self.playlist_songs:
            if song.title == song_title:
                self.playlist_songs.remove(song)
                print("Removed")
                return
        print("Song not found")


class Spotify():
    
    def __init__(self):
        self.playlists = []
        self.songs = []

    def add_song(self):
        title = input("Title: ")
        artist = input("Artist: ")
        length = float(input("Length: "))
        new_song = Song(title, length)
        self.songs.append(new_song)
        print("New song")
    
    def add_playlist(self):
        name = input("Name: ")
        new_playlist = Playlist(name)
        self.playlists.append(new_playlist)
        print("New playlists")

    def add_song_playlist(self):
        if not self.playlists:
            print("There isnt any playlists!")
            return
        for song in self.songs:
            print(song)
        song_select = input("Please enter a song to add: ")
        selected_song = next((song for song in self.songs if song.name == song_select), None)
        for playlist in self.playlists:
            print(f"{playlist.name}")
        playlist_select = input("Please enter the playlist name: ")
        selected_playlist = next((pl for pl in self.playlists if pl.name == playlist_select), None)
        selected_playlist.add_song(selected_song)

    def view_songs(self):
        print("All songs: ")
        for song in self.songs:
            print(song)

    def view_playlists(self):
        print("All Playlists: ")
        for playlist in self.playlists:
            print(playlist)
    
    def menu(self):
        while True:
            print("\n🎶 Music System Menu 🎶")
            print("1. Add Song")
            print("2. Create Playlist")
            print("3. Add Song to Playlist")
            print("4. View Songs")
            print("5. View Playlists")
            print("Else, exit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.add_song()
            elif choice == "2":
                self.add_playlist()
            elif choice == "3":
                self.add_song_playlist()
            elif choice == "4":
                self.view_songs()
            elif choice == "5":
                self.view_playlists()
            else:
                print("Exiting music system. Goodbye!")
                break
    