class Pacman:
    def __init__(self, width=3, frames="Cc", fillers=" ·", borders="[]"):
        self._width = width
        self._frames = frames
        self._fillers = fillers
        self._borders = borders
        self._pos = 0

    def update(self):
        self._pos = (self._pos + 1) % self._width
        print(
            self._borders[0],
            self._fillers[0] * self._pos,
            self._frames[self._pos % len(self._frames)],
            self._fillers[1] * (self._width - self._pos - 1),
            self._borders[1],
            "\b" * (self._width + 2),
            sep="", end="", flush=True
        )

    def clear(self):
        print(
            " " * (self._width + 2),
            "\b" * (self._width + 3),
            end="", flush=True
        )
