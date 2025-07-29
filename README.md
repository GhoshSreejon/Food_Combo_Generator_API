Hashira Round 2 Assignment:

A simple Flask API that generates random, balanced meal combos (main, side, drink) for multiple days.
Built as part of the Hashira round 2 assignment to explore API development, data handling with pandas, and JSON responses.

🚀 Features
Generates 3 unique combos per day with calorie range between 550–800.

Ensures no duplicate dishes within the same day's combos.

Automatically calculates the taste profile of each combo.

Returns data sorted in weekday order.

📦 How it works
Reads a menu.csv file containing dish data.

Picks random items for each combo while satisfying constraints.

Exposes a POST endpoint:

bash
Copy
Edit
/generate_combos_3_days
Optionally accepts:

json
Copy
Edit
{
  "start_day": "Tuesday"
}
to set the starting day.

▶️ Usage
Clone the repo & place your menu.csv in the same folder.

Install dependencies:

bash
Copy
Edit
pip install flask pandas flask-cors
Run:

bash
Copy
Edit
python app.py
Test with Postman or curl:

bash
Copy
Edit
curl -X POST http://127.0.0.1:5000/generate_combos_3_days -H "Content-Type: application/json" -d '{"start_day":"Tuesday"}'
🧠 Built with
Python & Flask

pandas for data handling

flask-cors to handle frontend requests
