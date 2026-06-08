from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def home():
    #passing data to html
    return render_template('home.html',name="Bashbytes")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run(debug=True)