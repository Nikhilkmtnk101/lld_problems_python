from snake_and_ladder.entities.jumps.interface import IJumps


class Ladder(IJumps):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def set_head(self, head):
        self.start = head

    def set_tail(self, tail):
        self.end = tail

    def get_start_position(self):
        return self.start

    def get_end_position(self):
        return self.end
