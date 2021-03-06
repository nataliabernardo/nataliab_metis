from flask import Flask, request, render_template


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60


@app.route('/')
def entry_page():
    return render_template('index.html')


@app.route('/calculate/', methods=['GET', 'POST'])
def calculate():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
