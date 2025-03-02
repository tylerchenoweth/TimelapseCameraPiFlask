import time

def update_display(counter):
    """Prints 8 lines, then moves the cursor up to overwrite them."""
    for i in range(1, 9):
        print(f"Line {i}: Update {counter}")

    # Move cursor up 8 lines to overwrite
    for _ in range(8):
        print("\033[F\033[K", end="")  # Move up and clear line

counter = 1
while True:
    update_display(counter)
    counter += 1
    time.sleep(5)  # Wait 5 seconds before updating again
