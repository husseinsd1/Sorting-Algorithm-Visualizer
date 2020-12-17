import time


def bubble_sort(data, draw_data, pause):
    """Implements the bubble sort algorithm on the given data array."""

    # Loops through all elements of the data array
    for _ in range(len(data) - 1):
        for j in range(len(data) - 1):

            # If the current element is greater than the one after it, swap them.
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

                # Colors the two elements being worked on green. Pauses for the time set by the scale.
                draw_data(data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(data))])
                time.sleep(pause)

    # Once all sorting is done, color all bars green.
    draw_data(data, ['green' for x in range(len(data))])

    return data

