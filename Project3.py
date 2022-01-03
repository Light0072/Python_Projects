from flask import Flask, render_template

app = Flask(__name__,template_folder="/Users/a2/PycharmProject/MCS275")

@app.route("/")
def index():
    return render_template('Project3.html')

if __name__ == '__main__':
    app.run(debug=True)
