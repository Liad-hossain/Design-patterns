from Design_patterns.behavioral_design_patterns.iterator_design_pattern.example_1.Playlist import (
    Playlist,
)
from Design_patterns.behavioral_design_patterns.iterator_design_pattern.example_1.ReverseSongIterator import (
    ReverseSongIterator,
)
from Design_patterns.behavioral_design_patterns.iterator_design_pattern.example_1.Song import (
    Song,
)
from Design_patterns.behavioral_design_patterns.iterator_design_pattern.example_1.SongIterator import (
    SongIterator,
)


class PlaySong:
    def __init__(self, playlist: Playlist):
        self._playlist = playlist

    def play(self):
        iterator = SongIterator(self._playlist)
        while True:
            try:
                song = next(iterator)
                print(song)
            except StopIteration:
                break

    def reverse_play(self):
        iterator = ReverseSongIterator(self._playlist)
        while True:
            try:
                song = next(iterator)
                print(song)
            except StopIteration:
                break


if __name__ == "__main__":
    song1 = Song("Song 1", "Artist A", "03:45")
    song2 = Song("Song 2", "Artist B", "04:20")
    song3 = Song("Song 3", "Artist C", "1:12:30")

    playlist = Playlist()
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.add_song(song3)

    player = PlaySong(playlist)
    print("Playing Song in normal order:")
    player.play()
    print("\nPlaying Song in reverse order:")
    player.reverse_play()
