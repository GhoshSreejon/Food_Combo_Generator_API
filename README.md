<p align="center"> <img src="https://img.shields.io/badge/python-3.8+-blue?logo=python" alt="Python version"/> <img src="https://img.shields.io/badge/flask-%3E=2.0-green?logo=flask" alt="Flask"/> <img src="https://img.shields.io/badge/pandas-%3E=1.0-yellow?logo=pandas" alt="Pandas"/> </p> <h1 align="center">🍱 Food Combo Generator API</h1> <p align="center"><em> Hashira Round 2 Assignment — A simple Flask API that randomly generates balanced meal combos (main, side, drink) for multiple days based on calorie constraints. </em></p> <p align="center"> <b>API design • Data handling with pandas • JSON responses</b> </p>
🚀 Features
Random Combo Generation: 3 unique meal combos per day, calorie range: <b>550–800</b>.
No Duplicates: Each day's combos have no repeating dishes.
Taste Profiles: Calculates and includes each combo's taste profile.
Sorted Output: Returns data sorted by weekday.
📦 How It Works
Reads dish data from menu.csv.

Randomly selects items for combos, ensuring all constraints are met.

Exposes a POST endpoint at:

Code
/generate_combos_3_days
<details> <summary>Optional JSON Body</summary>
JSON
{
  "start_day": "Tuesday"
}
</details>

▶️ Usage

1. Clone the repo & add your menu.csv:

bash
git clone https://github.com/GhoshSreejon/Food_Combo_Generator_API.git
cd Food_Combo_Generator_API

2. Install dependencies:

bash
pip install flask pandas flask-cors

3. Run the API:

bash
python app.py

4. Test the endpoint:

bash
curl -X POST http://127.0.0.1:5000/generate_combos_3_days \
  -H "Content-Type: application/json" \
  -d '{"start_day":"Tuesday"}'
  
🧠 Built With
<b>Python</b> & <b>Flask</b> — API framework
<b>pandas</b> — Data handling
<b>flask-cors</b> — Cross-origin requests
<p align="center"> <b>Enjoy generating your balanced meal combos! 🍴</b> </p>
