import time


def partition(data, head, tail, draw_data, pause):
    """
    Sorts the pivot into the middle of the array so that all elements to the left of it are less,
    and all elements to the right of it are greater.
    """

    border = head
    pivot = data[tail]

    # Visualize bars
    draw_data(data, get_bar_color(len(data), head, tail, border, border))
    time.sleep(pause)

    for j in range(head, tail):

        # Current element is less than the pivot, swap it with the border (move it up one)
        if data[j] < pivot:

            # Sets color of bars being swapped
            draw_data(data, get_bar_color(len(data), head, tail, border, j, True))
            time.sleep(pause)

            data[border], data[j] = data[j], data[border]
            border += 1

        draw_data(data, get_bar_color(len(data), head, tail, border, j))
        time.sleep(pause)

    draw_data(data, get_bar_color(len(data), head, tail, border, tail, True))
    time.sleep(pause)

    # Swap pivot with border
    data[border], data[tail] = data[tail], data[border]

    return border


def quick_sort(data, head, tail, draw_data, pause):
    """Splits array into two partitions and sorts each. Keeps doing that until array is sorted"""

    if head < tail:
        
        # Gets partition index from the partition function
        partn_index = partition(data, head, tail, draw_data, pause)

        # Calls quicksort on the left partition (elements less than pivot)
        quick_sort(data, head, partn_index - 1, draw_data, pause)

        # Calls quicksort on the right partition (elements greater than pivot)
        quick_sort(data, partn_index + 1, tail, draw_data, pause)


def get_bar_color(dataset_len, head, tail, border, curr_indx, is_swapping=False):
    """Sets the color of the bar based on certain criteria."""

    bar_color = []

    for i in range(dataset_len):

        # Color of current elements being used, and elements not being used (in that order).
        if head <= i <= tail:
            bar_color.append('gray')
        else:
            bar_color.append('white')

        # Set the tail to blue, border to red, and pointer to yellow.
        if i == tail:
            bar_color[i] = 'blue'
        elif i == border:
            bar_color[i] = 'red'
        elif i == curr_indx:
            bar_color[i] = 'yellow'

        # Set elements that are in the process of being swapped to green.
        if is_swapping:
            if i == border or i == curr_indx:
                bar_color[i] = 'green'

    return bar_color