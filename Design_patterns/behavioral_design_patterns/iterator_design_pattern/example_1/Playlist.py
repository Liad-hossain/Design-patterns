from Design_patterns.behavioral_design_patterns.iterator_design_pattern.example_1.Song import (
    Song,
)


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)

    def remove_song(self, song: Song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed {song} from the playlist.")
        else:
            print(f"{song} not found in the playlist.")
