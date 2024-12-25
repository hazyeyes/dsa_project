from flask import Flask, render_template, request

app = Flask(__name__)

# Bubble Sort Algorithm with detailed steps tracking the colors of the elements
def bubble_sort(data):
    steps = []
    n = len(data)
    for i in range(n):
        colors = ['white'] * n  # Reset colors for each pass
        swapped = False  # Flag to track if any swap occurs
        
        for j in range(0, n-i-1):
            colors[j] = 'yellow'  # Highlight the current comparison index
            colors[j+1] = 'yellow'  # Highlight the next comparison index
            steps.append([data[:], colors[:]])  # Append the current step

            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]  # Swap the elements
                colors[j] = 'green'  # Mark the first swapped element as green
                colors[j+1] = 'green'  # Mark the second swapped element as green
                steps.append([data[:], colors[:]])  # Record the swap
                
                # After the swap, make them yellow since they are in correct order
                colors[j] = 'yellow'
                colors[j+1] = 'yellow'
                steps.append([data[:], colors[:]])  # Record the change to yellow
                
                swapped = True  # Indicate that a swap occurred

        colors[n-i-1] = 'green'  # Mark the last element as sorted
        steps.append([data[:], colors[:]])

        # If no elements were swapped in this pass, the list is already sorted
        if not swapped:
            break

    return steps

@app.route('/', methods=['GET', 'POST'])
def index():
    steps = []
    data = []
    error = None
    if request.method == 'POST':
        try:
            input_data = request.form['data']
            data = list(map(int, input_data.split(',')))  # Convert input to a list of integers
            if len(data) == 0:
                raise ValueError("Data list is empty.")
            steps = bubble_sort(data)  # Perform bubble sort and track steps
        except ValueError:
            error = "Please enter a valid comma-separated list of integers."  # Handle invalid input
    
    return render_template('index.html', steps=steps, data=data, error=error)

if __name__ == '__main__':
    app.run(debug=True)