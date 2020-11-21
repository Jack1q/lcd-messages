from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder='templates')

status = {
    'A' : False,
    'B' : False#,
    # 'C' : False,
    # 'D' : False
}

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/button/<string:letter>')
def button(letter):
    if letter in status:
        status[letter] = not status[letter]
    return render_template('index.html')

@app.route('/status')
def statuscheck():
    return jsonify(status)

if __name__ == '__main__':
    app.run(debug=True)


### CODE THIS INTO PI! ###
# import requests
# while True:
#     light_values = requests.get('R4ndoma$$l1nk.com/status').json()
#     for light in light_values:
#         led_switch = light_values[light] # should be true or false :P