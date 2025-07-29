from flask import Flask, request, jsonify
import pandas as pd
import random
from collections import Counter, OrderedDict
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

# menu.csv
menu_df = pd.read_csv("menu.csv")

# Separate by category
mains = menu_df[menu_df['category'] == 'main'].to_dict('records')
sides = menu_df[menu_df['category'] == 'side'].to_dict('records')
drinks = menu_df[menu_df['category'] == 'drink'].to_dict('records')

# Weekdays
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def generate_combos_for_day():
    combos = []
    used_dishes = set()
    tries = 0

    while len(combos) < 3 and tries < 1000:
        tries += 1
        main = random.choice(mains)
        side = random.choice(sides)
        drink = random.choice(drinks)

        # Ensure unique items in combo
        dish_names = {main['item_name'], side['item_name'], drink['item_name']}
        if len(dish_names) < 3:
            continue

        # Dont reuse dishes in same days combos
        if dish_names & used_dishes:
            continue

        total_cals = main['calories'] + side['calories'] + drink['calories']
        if 550 <= total_cals <= 800:
            used_dishes.update(dish_names)

            items = [
                {'name': main['item_name'], 'calories': main['calories'], 'taste': main['taste_profile'], 'type': 'main'},
                {'name': side['item_name'], 'calories': side['calories'], 'taste': side['taste_profile'], 'type': 'side'},
                {'name': drink['item_name'], 'calories': drink['calories'], 'taste': drink['taste_profile'], 'type': 'drink'}
            ]

            
            tastes = [i['taste'] for i in items]
            taste_counts = Counter(tastes)
            top_taste, top_count = taste_counts.most_common(1)[0]
            taste_profile = top_taste if top_count >= 2 else 'mix'

            combos.append({
                'combo_name': f'Combo {len(combos)+1}',
                'items': items,
                'taste_profile': taste_profile,
                'total_calories': total_cals
            })

    return combos

@app.route('/generate_combos_3_days', methods=['POST'])
def generate_combos_3_days():
    data = request.get_json()
    start_day = data.get('start_day', 'Monday')  # default to Monday

    if start_day not in week_days:
        return jsonify({"error": "Invalid start_day"}), 400

    start_idx = week_days.index(start_day)
    days = [week_days[(start_idx + i) % 7] for i in range(3)]

    
    output = {}
    for day in days:
        output[day] = generate_combos_for_day()

    
    weekday_order = {day: idx for idx, day in enumerate(week_days)}
    ordered_response = OrderedDict(sorted(output.items(), key=lambda x: weekday_order[x[0]]))

    return jsonify(ordered_response)

if __name__ == '__main__':
    app.run(debug=True)
