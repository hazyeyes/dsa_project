from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    data = []
    steps = []

    if request.method == "POST":
        try:
            # Get the user input and convert it to a list of integers
            input_data = request.form["data"]
            data = list(map(int, input_data.split(",")))  
            steps = insertion_sort_steps(data)  # Get the steps for insertion sort
        except ValueError:
            error = "Invalid input. Please enter a valid comma-separated list of integers."

    return render_template("index.html", data=data, steps=steps, error=error)

def insertion_sort_steps(data):
    steps = []
    n = len(data)

    # Record the initial state
    steps.append([data.copy(), ["white"] * n])

    for i in range(1, n):
        key = data[i]
        j = i - 1
        colors = ["white"] * n
        colors[i] = "orange"  # Highlight the current element being considered

        prev_data = data.copy()

        # Shift elements greater than the key to the right
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            colors[j] = "yellow"  # Highlight the element being shifted
            j -= 1

        # Insert the key into its correct position
        data[j + 1] = key
        colors[j + 1] = "green"  # Highlight the inserted element

        # Record the state only if the data has changed
        if data != prev_data:
            steps.append([data.copy(), colors.copy()])

    # Final step with all elements in blue
    final_colors = ["blue"] * n
    steps.append([data.copy(), final_colors])

    # Add a duplicate of the final step to ensure completion
    steps.append([data.copy(), final_colors])

    # Remove identical consecutive steps to avoid redundancy
    unique_steps = []
    for step in steps:
        if not unique_steps or unique_steps[-1][0] != step[0]:
            unique_steps.append(step)

    return unique_steps

if __name__ == "__main__":
    app.run(debug=True)