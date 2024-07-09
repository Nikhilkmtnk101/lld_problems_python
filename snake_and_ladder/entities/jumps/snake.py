from snake_and_ladder.entities.jumps.interface import IJumps


class Snake(IJumps):
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def set_head(self, head):
        self.head = head

    def set_tail(self, tail):
        self.tail = tail

    def get_start_position(self):
        return self.head

    def get_end_position(self):
        return self.tail
