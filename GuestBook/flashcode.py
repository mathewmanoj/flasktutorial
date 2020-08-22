from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return'<h1> Hello there !</h1>'
    
     
@app.route('/home/',methods=['GET','POST'])
def home():
      links =['https://www.youtube.com','https://www.bing.com','https://www.python.org']
      return render_template('e.html',links=links)
#      return render_template('e.html',myvar ='Flask Variable pass to hmtl ')
#      return'<h1> Hello there111 !</h1>'
    

if __name__ == '__main__':
    app.run(debug=True)