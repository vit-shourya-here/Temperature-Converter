from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Temperature Converter V1</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <h2>Temperature Converter Application (Push 1)</h2>
    <form method="post">
        <!-- Input 1 -->
        <input name="val1" type="number" step="any" placeholder="Enter Temperature" required>
        
        <!-- Dropdown Menu containing only Push 1 Feature -->
        <select name="action">
            <option value="c_to_f">Celsius to Fahrenheit</option>
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
            temp = float(request.form.get("val1", 0))
            action = request.form["action"]

            # Push 1: Celsius to Fahrenheit
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
