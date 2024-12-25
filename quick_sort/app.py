from flask import Flask, render_template, request

app = Flask(__name__)

def partition(array, low, high, steps):
    # Choose the middle element as the pivot
    mid = (low + high) // 2
    pivot = array[mid]
    
    # Move the pivot to the rightmost position
    array[mid], array[high] = array[high], array[mid]

    # Pointer for the greater element
    i = low - 1

    # Traverse through all elements
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found, swap it with the greater element pointed by i
            i += 1
            array[i], array[j] = array[j], array[i]

    # Swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]

    # Record the step with the current pivot position and array state
    steps.append(("Pivot: " + str(array[i + 1]), ", ".join(map(str, array))))
    return i + 1

def quickSort(array, low, high, steps):
    if low < high:
        # Find pivot element such that elements smaller than pivot are on the left,
        # elements greater than pivot are on the right
        pi = partition(array, low, high, steps)
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1, steps)
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high, steps)

def sort_and_visualize(data):
    steps = []
    arr = list(map(int, data.split(',')))
    quickSort(arr, 0, len(arr) - 1, steps)
    steps.append(("Final Sorted Array", ", ".join(map(str, arr))))
    return steps

@app.route('/', methods=['GET', 'POST'])
def index():
    steps = []
    error = None
    if request.method == 'POST':
        try:
            data = request.form['data']
            steps = sort_and_visualize(data)
        except Exception as e:
            error = str(e)
    return render_template('index.html', steps=steps, error=error)

if __name__ == '__main__':
    app.run(debug=True)
