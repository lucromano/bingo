import pandas as pd
import random
import itertools
from flask import Flask, render_template, request, url_for, jsonify

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/combinations', methods=['GET', 'POST'])
def combinations():
    if request.method == 'POST':
        data = request.get_json()
        # print(data)
        selected_numbers = data['selectedNumbers']
        total_numbers_to_draw = data['totalNumbersToDraw']
        min_value = data['min']
        max_value = data['max']

    # print(type(selected_numbers))
    # print(type(total_numbers_to_draw))
    # print(type(min_value))
    # print(type(max_value))

    # valid_combinations = set()
    # for combination in itertools.combinations(selected_numbers, total_numbers_to_draw):
    #     if min_value <= combination[-1] <= max_value:
    #         valid_combinations.add(combination)

        return render_template('combinations.html', nums=selected_numbers)
    else:
        return "Invalid"


app.run()