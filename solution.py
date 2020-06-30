"""Solution by <USERNAME>."""


class Block:
    """Represents a block in the infinite tape."""

    def __init__(self, data, _next=None):
        """Initialize block."""
        self.data = data
        self.next = _next


class Solution:
    """Solution to the halting problem (kind of)."""

    def does_it_halt(self, block: Block) -> bool:
        """Return whether Alan's program will halt or not."""
        return False
