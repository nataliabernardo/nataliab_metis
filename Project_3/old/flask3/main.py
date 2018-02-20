from flask import Flask, request, render_template
from py_muffins_cupcakes import muffin_or_cupcake

app = Flask(__name__)

@app.route('/')
def entry_page():
    return render_template('index.html')

@app.route('/predict_recipe/', methods=['GET', 'POST'])
def render_message():

    flour_cups = request.form['flour_cups']
    try:
        flour_cups_float = float(flour_cups)
    except:
        message = "The amount of flour must be in cups."
        return render_template('index.html',
                               message=message)

    milk_cups = request.form['milk_cups']
    try:
        milk_cups_float = float(milk_cups)
    except:
        message = "The amount of milk must be in cups."
        return render_template('index.html',
                               message=message)

    sugar_cups = request.form['sugar_cups']
    try:
        sugar_cups_float = float(sugar_cups)
    except:
        message = "The amount of sugar must be in cups."
        return render_template('index.html',
                               message=message)

    butter_cups = request.form['butter_cups']
    try:
        butter_cups_float = float(butter_cups)
    except:
        message = "The amount of butter must be in cups."
        return render_template('index.html',
                               message=message)

    eggs_num = request.form['eggs_num']
    try:
        eggs_num_float = float(eggs_num)
    except:
        message = "You must enter a number of eggs."
        return render_template('index.html',
                               message=message)

    bp_tsp = request.form['bp_tsp']
    try:
        bp_tsp_float = float(bp_tsp)
    except:
        message = "The amount of baking powder must be in teaspoons."
        return render_template('index.html',
                               message=message)

    vanilla_tsp = request.form['vanilla_tsp']
    try:
        vanilla_tsp_float = float(vanilla_tsp)
    except:
        message = "The amount of vanilla must be in teaspoons."
        return render_template('index.html',
                               message=message)

    salt_tsp = request.form['salt_tsp']
    try:
        salt_tsp_float = float(salt_tsp)
    except:
        message = "The amount of salt must be in teaspoons."
        return render_template('index.html',
                               message=message)

    message = muffin_or_cupcake(flour_cups_float,
                            milk_cups_float,
                            sugar_cups_float,
                            butter_cups_float,
                            eggs_num_float,
                            bp_tsp_float,
                            vanilla_tsp_float,
                            salt_tsp_float)

    return render_template('index.html',
                           message=message)


if __name__ == '__main__':
    app.run(debug=True)