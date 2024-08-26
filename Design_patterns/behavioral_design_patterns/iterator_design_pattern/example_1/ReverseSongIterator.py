from collections.abc import Iterator


class ReverseSongIterator(Iterator):
    def __init__(self, playlist):
        self._playlist = playlist
        self._index = len(playlist.songs) - 1

    def __next__(self):
        if self._index >= 0:
            song = self._playlist.songs[self._index]
            self._index -= 1
            return song
        raise StopIteration
