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
            data = list(map(int, input_data.split(",")))  # Convert input to a list of integers
            steps = merge_sort_steps(data)  # Get the steps for merge sort
        except ValueError:
            error = "Invalid input. Please enter a valid comma-separated list of integers."

    return render_template("index.html", data=data, steps=steps, error=error)

def merge_sort_steps(data):
    steps = []  # Holds the steps for visualization

    # Merge Sort function that also records the steps
    def merge_sort(arr):
        n = len(arr)
        if n <= 1:
            return arr

        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        # Record the split step (e.g., [10, 20], [4, 3])
        steps.append(("Split Data", f"[{', '.join(map(str, left))}]   [{', '.join(map(str, right))}]"))

        # Recursively sort both halves
        left_sorted = merge_sort(left)
        right_sorted = merge_sort(right)

        # Merge the sorted halves and capture the merge step
        merged = merge(left_sorted, right_sorted)
        steps.append(("Merge Data", f"[{', '.join(map(str, left_sorted))}]  [{', '.join(map(str, right_sorted))}]"))
        steps.append(("Merged Data", f"[{', '.join(map(str, merged))}]"))
        return merged

    # Merge function to combine two sorted arrays
    def merge(left, right):
        result = []
        i = j = 0

        # Merge elements from left and right arrays
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # Capture the initial array
    steps.append(("Initial Data", f"[{', '.join(map(str, data))}]"))
    sorted_data = merge_sort(data)
    # Capture the final sorted array
    steps.append(("Final Sequence", f"[{', '.join(map(str, sorted_data))}]"))
    
    return steps

if __name__ == "__main__":
    app.run(debug=True)
