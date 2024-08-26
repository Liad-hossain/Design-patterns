from collections.abc import Iterator

from Design_patterns.behavioral_design_patterns.iterator_design_pattern.example_1.Playlist import (
    Playlist,
)


class SongIterator(Iterator):
    def __init__(self, playlist: Playlist):
        self._playlist = playlist
        self._index = 0

    def __next__(self):
        if self._index < len(self._playlist.songs):
            song = self._playlist.songs[self._index]
            self._index += 1
            return song
        else:
            raise StopIteration
