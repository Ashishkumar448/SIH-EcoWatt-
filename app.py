from flask import Flask, render_template, request, jsonify
from randomtip import get_tip
from algo import get_m_avg
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", tip = get_tip())


        
@app.route('/tips')
def tips():
    return render_template('tips.html')


@app.route('/maintenance')
def maintenance():
    return render_template("maintenance.html")


@app.route('/appliances')
def appl():
    return render_template('appl.html')

@app.route('/analytics')
def analytics():
    m_avg = float(get_m_avg())
    m_saved = 20 - m_avg
    p_s = m_saved/20 * 100
    if m_saved > 0:
        return render_template("Analytics.html", m_avg = str(m_avg), m_s_w = str(m_saved), s_w = "Saved", p_s_w = "Saved", p_sw = str(p_s) + "%", color = "#18de40")
    elif m_saved < 0:
        return render_template("Analytics.html", m_avg = str(m_avg), m_s_w = str(-m_saved),  s_w = "Wasted", p_s_w = "Wasted", p_sw = str(-p_s) + "%", color = "#FF0000")
    else:
        return render_template("Analytics.html", m_avg = str(m_avg), m_waste = 0,  m_saved = 0, color = "#006ED3")

@app.route('/save-appliances', methods=['POST'])
def save_appliances():
    data = request.json
    csv_file = 'appl.csv'
    file_exists = os.path.isfile(csv_file)

    try:
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)


            if not file_exists:
                writer.writerow(['Appliance Name', 'Usage Time (hours)', 'Wattage (W)'])

            for item in data:
                writer.writerow([item['name'], item['usageTime'], item['wattage']])

        return jsonify({'message': 'Appliances saved successfully!'}), 200
    except Exception as e:
        print(f"Error saving appliances: {e}")
        return jsonify({'message': 'Failed to save appliances.'}), 500
    
@app.route('/standardusage')
def stdus():
    return render_template('stdus.html')


@app.route('/energycalculator')
def cal():
    return render_template('cal.html')
    
 
if __name__ == "__main__":
    app.run(debug=True)
