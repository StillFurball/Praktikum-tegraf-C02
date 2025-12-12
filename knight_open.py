import tkinter as tk
import random
import time
import threading

N = 8

# Knight move offsets
cx = [1, 1, 2, 2, -1, -1, -2, -2]
cy = [2, -2, 1, -1, 2, -2, 1, -1]

# Check if inside board
def limits(x, y):
    return 0 <= x < N and 0 <= y < N

# Check empty
def isempty(board, x, y):
    return limits(x, y) and board[y][x] < 0

# Count degree
def get_degree(board, x, y):
    count = 0
    for i in range(N):
        nx = x + cx[i]
        ny = y + cy[i]
        if isempty(board, nx, ny):
            count += 1
    return count

# Warnsdorff next move
def next_move(board, pos):
    x, y = pos
    min_deg = 9
    min_idx = -1

    start = random.randint(0, 7)

    for c in range(N):
        i = (start + c) % N
        nx = x + cx[i]
        ny = y + cy[i]

        if isempty(board, nx, ny):
            deg = get_degree(board, nx, ny)
            if deg < min_deg:
                min_deg = deg
                min_idx = i

    if min_idx == -1:
        return None

    nx = x + cx[min_idx]
    ny = y + cy[min_idx]
    board[ny][nx] = board[y][x] + 1
    return nx, ny


# Generate OPEN tour (no closed-cycle check)
def generate_open_tour():
    while True:
        board = [[-1] * N for _ in range(N)]

        # Random start
        #x = random.randint(0, N - 1)
        #y = random.randint(0, N - 1)
        x = 2
        y = 4
        board[y][x] = 1

        path = [(x, y)]

        # Warnsdorff until stuck
        for _ in range(63):
            nxt = next_move(board, (x, y))
            if nxt is None:
                break
            x, y = nxt
            path.append((x, y))

        if len(path) == 64:   # only need a full Hamiltonian path
            return path


###########################################################################
# GUI TKINTER
###########################################################################

CELL = 70
PADDING = 20
SIZE = CELL * N

root = tk.Tk()
root.title("Open Knight's Tour - Warnsdorff (with Arrows)")

canvas = tk.Canvas(root, width=SIZE + PADDING*2, height=SIZE + PADDING*2, bg="white")
canvas.pack()


def draw_board():
    canvas.delete("all")
    colors = ("#EEEED2", "#769656")  # light, dark

    for i in range(N):
        for j in range(N):
            color = colors[(i + j) % 2]
            x1 = PADDING + i * CELL
            y1 = PADDING + j * CELL
            x2 = x1 + CELL
            y2 = y1 + CELL
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")


def draw_knight(x, y, color="blue"):
    cx_ = PADDING + x * CELL + CELL//2
    cy_ = PADDING + y * CELL + CELL//2
    canvas.create_oval(cx_-15, cy_-15, cx_+15, cy_+15, fill=color)


def draw_arrow(x1, y1, x2, y2):
    ax1 = PADDING + x1 * CELL + CELL//2
    ay1 = PADDING + y1 * CELL + CELL//2
    ax2 = PADDING + x2 * CELL + CELL//2
    ay2 = PADDING + y2 * CELL + CELL//2

    canvas.create_line(ax1, ay1, ax2, ay2, width=3, arrow=tk.LAST, fill="red")


def animate(path):
    draw_board()
    canvas.update()

    prev = path[0]
    # Draw start node in GREEN
    draw_knight(prev[0], prev[1], color="green")
    canvas.update()
    time.sleep(0.4)

    for step in path[1:]:
        draw_arrow(prev[0], prev[1], step[0], step[1])
        draw_knight(step[0], step[1], color="blue")
        prev = step
        canvas.update()
        time.sleep(0.1) #drawing speed
    
    # Draw end node in RED
    draw_knight(path[-1][0], path[-1][1], color="red")


def run_animation():
    path = generate_open_tour()
    animate(path)


threading.Thread(target=run_animation, daemon=True).start()
root.mainloop()
