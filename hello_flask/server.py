from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/')                           
def hello_world():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', times=3, color="lightblue")

@app.route('/play/<int:x>')
def num(x):
    return render_template('index.html', times=int(x), color="lightblue")

@app.route('/play/<int:x>/<color>')
def num_color(x, color):
    return render_template('index.html', times=int(x), color=color)
    
if __name__=="__main__":
    app.run(debug=True)

