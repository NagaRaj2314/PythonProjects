import heapq
class PuzzleState:
    def __init__(self, board, parent=None, move=""):
        self.board = board
        self.parent = parent
        self.move = move
        self.g = 0
        self.h = self.calculate_misplaced_tiles()
    def calculate_misplaced_tiles(self):
        misplaced = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0 and self.board[i][j] != i * 3 + j + 1:
                    misplaced += 1
        return misplaced
    def __lt__(self, other):
        return self.h < other.h
    # Other methods (get_blank_position, generate_possible_moves, apply_move)
def print_solution(final_state):
    if final_state is None:
        print("No solution found.")
        return
    moves_and_boards = []
    current_state = final_state
    while current_state.parent is not None:
        moves_and_boards.append((current_state.move, current_state.board))
        current_state = current_state.parent
    moves_and_boards.reverse()
    for move, board in moves_and_boards:
        print("Move:", move)
        for row in board:
            print(row)
        print()
    moves = []
    current_state = final_state
    while current_state.parent is not None:
        moves.append(current_state.move)
        current_state = current_state.parent
    moves.reverse()
    print("Solution found in", len(moves), "moves:", " -> ".join(moves))
def solve_puzzle(initial_state):
    open_set = []
    heapq.heappush(open_set, initial_state)
    closed_set = set()
    while open_set:
        current_state = heapq.heappop(open_set)
        if current_state.board == goal_state:
            print_solution(current_state)
            return
        closed_set.add(tuple(map(tuple, current_state.board)))
        i, j = current_state.get_blank_position(current_state.board)
        possible_moves = current_state.generate_possible_moves(i, j)
        for move in possible_moves:
            new_board = [row[:] for row in current_state.board]
            current_state.apply_move(new_board, move)
            if tuple(map(tuple, new_board)) not in closed_set:
                new_state = PuzzleState(new_board, parent=current_state, move="UDLR"[possible_moves.index(move)])
                new_state.g = current_state.g + 1
                heapq.heappush(open_set, new_state)
if __name__ == "__main__":
    print("Enter the goal state:")
    goal_state = [list(map(int, input().split())) for _ in range(3)]
    print("Enter the initial state:")
    initial_board = [list(map(int, input().split())) for _ in range(3)]
    initial_state = PuzzleState(initial_board)
    solve_puzzle(initial_state)
