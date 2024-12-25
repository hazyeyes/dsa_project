from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    data = []
    steps = []

    if request.method == "POST":
        try:
            # Get user input and convert it into a list of integers
            input_data = request.form["data"]
            data = list(map(int, input_data.split(",")))  
            steps = selection_sort_steps(data)  # Get the steps for selection sort visualization
        except ValueError:
            error = "Invalid input. Please enter a valid comma-separated list of integers."

    return render_template("index.html", data=data, steps=steps, error=error)

def selection_sort_steps(data):
    steps = []
    n = len(data)
    for i in range(n):
        min_idx = i
        colors = ["white"] * n
        colors[i] = "orange"  # Highlight the current index being processed
        
        swapped = False  # Flag to check if a swap is needed
        
        for j in range(i + 1, n):
            colors[j] = "yellow"  # Highlight the comparison index
            steps.append([data.copy(), colors.copy()])  # Record the state after comparison
            
            if data[j] < data[min_idx]:
                min_idx = j
                swapped = True  # Mark that a swap will be needed

        # Perform the swap if needed and record the state after swapping
        if swapped:
            data[i], data[min_idx] = data[min_idx], data[i]
            colors[i] = "green"  # Mark the current element as sorted
            steps.append([data.copy(), colors.copy()])

    # Final step to mark the entire list as sorted
    final_colors = ["blue"] * n
    steps.append([data.copy(), final_colors])  # Final state

    return steps

if __name__ == "__main__":
    app.run(debug=True)