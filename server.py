from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checker():
  return render_template('index.html', x=8, y=8)

@app.route('/4')
def fourbyfour():
  return render_template('index.html', x=4, y=4)

@app.route('/<int:x>/<int:y>')
def customize(x,y):
  return render_template('index.html', x=x, y=y)

if __name__=="__main__":
  app.run(debug=True)