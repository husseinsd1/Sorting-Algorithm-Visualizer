import time


def merge_sort(data, draw_data, pause):
    """Uses functions below to merge sort given data"""
    merge_sort_alg(data, 0, len(data) - 1, draw_data, pause)


def merge_sort_alg(data, left, right, draw_data, pause):
    """Applies merge sort on left and right partitions"""

    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, draw_data, pause)
        merge_sort_alg(data, middle + 1, right, draw_data, pause)
        merge(data, left, middle, right, draw_data, pause)


def merge(data, left, middle, right, draw_data, pause):
    """Merges partitions on a given dataset"""
    
    # Visualizes data
    draw_data(data, get_bar_color(len(data), left, middle, right))
    time.sleep(pause)

    # Merges left and right partitions
    left_partition = data[left: middle + 1]
    right_partition = data[middle + 1: right + 1]

    left_index = right_index = 0

    # Splits the left and right partitions into more left right partitions
    for data_index in range(left, right + 1):
        if left_index < len(left_partition) and right_index < len(right_partition):

            if left_partition[left_index] <= right_partition[right_index]:
                data[data_index] = left_partition[left_index]
                left_index += 1
            else:
                data[data_index] = right_partition[right_index]
                right_index += 1

        elif left_index < len(left_partition):
            data[data_index] = left_partition[left_index]
            left_index += 1
        else:
            data[data_index] = right_partition[right_index]
            right_index += 1

    # If in the process of being merged, make green else white
    draw_data(data, ['green' if left <= x <= right else 'white' for x in range(len(data))])
    time.sleep(pause)


def get_bar_color(length, left, middle, right):
    """Sets the color of the bar based on certain criteria."""

    bar_color = []
    
    # Color of current 2 elements being used, and element not being used (in that order).
    for i in range(length):
        
        if left <= i <= right:
            if i <= middle:
                bar_color.append('yellow')
            else:
                bar_color.append('pink')

        else:
            bar_color.append('white')

    return bar_color
