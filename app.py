from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/post')
def homePost():
    return render_template('homePost.html')

@app.route('/get')
def homeGet():
    return render_template('homeGet.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET':
        nome = request.args.get('nome')
        sesso = request.args.get('sesso')
        hobbies = request.args.getlist('hobbies')
        citta = request.args.get('citta')
        presentazione = request.args.get('presentazione')
    else: 
        nome = request.form['nome']
        sesso = request.form['sesso']
        hobbies = request.form.getlist('hobbies')
        citta = request.form['citta']
        presentazione = request.form['presentazione']

    return render_template('riepilogo.html', nome=nome, sesso=sesso, hobbies=hobbies, citta=citta, presentazione = presentazione)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)