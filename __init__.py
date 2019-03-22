from flask import Flask, render_template,Markup
import sys

app = Flask(__name__)

@app.route("/")
def index():


    with open('/var/www/EU/EU/results.txt', 'r') as f:
        lines = f.read().splitlines()
        latest_value = lines[-1]

    latest_value=latest_value.split(',')
    legend = 'Signatures'
    labels = []
    values = []
    with open('/var/www/EU/EU/results.txt', 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        line = line.split(',')
        if len(values) > 0:
            if line[1] != values[-1]:
                labels.append(line[0])
                values.append(line[1])
        else:
            labels.append(line[0])
            values.append(line[1])
    return render_template('index.html',value=latest_value, values=values, labels=labels, legend=legend)

@app.route("/full_chart")
def chart():
    legend = 'Signatures'
    labels = []
    values = []
    with open('/var/www/EU/EU/results.txt', 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        line = line.split(',')
        labels.append(line[0])
        values.append(line[1])
    return render_template('chart.html', values=values, labels=labels, legend=legend)


if __name__ == "__main__":
    app.run(debug=True)