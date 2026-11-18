from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    stats = {
        "patients": 1250,
        "doctors": 85,
        "appointments": 320,
        "revenue": 125000
    }

    return render_template("dashboard.html", stats=stats)

if __name__ == "__ "__main__":
    app.run(debug=True)

    