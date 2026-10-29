from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Temperature Converter</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <h2>Temperature Converter Application</h2>
    <form method="post">
        <!-- Input 1: Temperature value -->
        <input name="val1" type="number" step="any" placeholder="Enter Temperature" required>
        
        <!-- Dropdown Menu for Push 1 & Push 2 Features -->
        <select name="action">
            <option value="c_to_f">Celsius to Fahrenheit (Push 1)</option>
        </select>
        <button type="submit">Submit</button>
    </form>
    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            # val1 represents the temperature to convert
            temp = float(request.form.get("val1", 0))
            action = request.form["action"]

            if action == "c_to_f":
                converted = (temp * 9 / 5) + 32
                result = f"{temp}°C = {converted:.2f}°F"

            else:
                result = "Invalid operation"
        except (ValueError, KeyError):
            result = "Invalid input"

    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
