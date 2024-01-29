class GameState:
    def __init__(self):
        board_dim_x = 9
        board_dim_y = 8
        self.board = [
            ["--", "--", "0w", "--", "--", "--", "1w", "--", "--"],
            ["--", "0k", "0b", "--", "--", "--", "1b", "1k", "--"],
            ["0n", "--", "0l2", "--", "--", "--", "1l2", "--", "1n"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["1g", "--", "1m", "--", "--", "--", "0m", "--", "0g"],
            ["--", "--", "1f", "--", "--", "--", "0f", "--", "--"],
            ["1q", "--", "1t", "--", "--", "--", "0t", "--", "0q"]]
        self.blobs_states = {(2, 0): 1, (2, 8): 1}
        self.kings_locations = [(1, 1), (1, 7)]

    def get_blob_tag(self, row, column):
        blob_tag = self.board[row][column]
        if blob_tag != "--":
            if (row, column) in self.blobs_states:
                blob_tag += str(self.blobs_states[(row, column)])
            return blob_tag
        return None
