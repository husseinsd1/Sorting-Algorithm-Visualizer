from tkinter import ttk
from tkinter import *
import random
from SortingAlgoVisualizer.bubble_sort import bubble_sort
from SortingAlgoVisualizer.quick_sort import quick_sort
from SortingAlgoVisualizer.merge_sort import merge_sort

root = Tk()
root.maxsize(900, 600)
root.title('Sorting Algorithm Visualizer')
root.config(bg='black')

# Variables
selected_alg = StringVar()
data = []


def draw_data(dataset, bar_color):
    """Recieves a dataset, and draws the bars corresponding to each number in the dataset"""

    # Clears previous bar graph
    canvas.delete("all")

    # Set boundries for graphing area
    canvas_height = 380
    canvas_width = 600
    offset = 30
    spacing = 10

    # Width of a single bar
    x_width = canvas_width / (len(dataset) + 1)

    # Normalize data to scale bar size
    normalized_data = [i / max(dataset) for i in dataset]

    for i, height in enumerate(normalized_data):

        # Top left vertex of a bar
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 340

        # Bottom right vertex of a bar
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height

        # Draw the bar and display its value above it
        canvas.create_rectangle(x0, y0, x1, y1, fill=bar_color[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(dataset[i]))

    # Updates screen
    root.update_idletasks()


def generate():
    """Generates data set based on user specified constraints"""

    # Accesses the gloabal data array and clears it for new values to be generated
    global data
    data = []

    # Minimum, maximum, and size values of the data set. Checks for string inputs by user.
    min_val = int(min_entry.get())
    max_val = int(max_entry.get())
    size = int(size_entry.get())

    # Adds random numbers between min_val and max_val to data (the data set to be worked with)
    for _ in range(size):
        data.append(random.randrange(min_val, max_val + 1))

    # Calls draw data function on dataset to draw it onto canvas
    draw_data(data, ['red' for x in range(len(data))])


def start_algorithm():
    """Starts the sorting process on the data set."""
    
    global data

    # If data is empty, do nothing
    if not data:
        return

    # Applies the algorithm the user chooses
    if algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, draw_data, speed_scale.get())

    elif algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, draw_data, speed_scale.get())

    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, draw_data, speed_scale.get())

    # Set bars to all green after data has been sorting
    draw_data(data, ['green' for x in range(len(data))])


# Frame/Canvas creation
UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# UI widgets for row[0]
Label(UI_frame, text='Algorithm: ', bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)

algo_menu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

speed_scale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL,
                    label='Select Speed (s)')
speed_scale.grid(row=0, column=2, padx=5, pady=5)

Button(UI_frame, text='Start', command=start_algorithm, bg='green').grid(row=0, column=3, padx=5, pady=5)

# UI widgets for row[1]
size_entry = Scale(UI_frame, from_=3, to=30, resolution=1, orient=HORIZONTAL, label='Dataset Size')
size_entry.grid(row=1, column=0, padx=5, pady=5)

min_entry = Scale(UI_frame, from_=0, to=9, resolution=1, orient=HORIZONTAL, label='Min Value')
min_entry.grid(row=1, column=1, padx=5, pady=5)

max_entry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label='Max Value')
max_entry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text='Generate', command=generate, bg='red').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
