from flask import Flask, render_template


#create flask instance
app = Flask(__name__)

app.config['DEBUG'] = True

#create a route decorator)
@app.route('/')

#def index():
#   return "<h1>Hello World </h1>"


# safe
# capitalize
# lower
# upper
# title
# trim == delete spaces
# striptags == delete tags


def index():
    first_name = "Omar"
    stuff = "This is bold Text"

    favourite_pizza = ["pepperoni","Cheese", "Mushrooms"]


    return render_template("index.html",
     first_name=first_name,
     stuff=stuff,
     favourite_pizza=favourite_pizza)

#localhost:5000/user/omar
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)




#Create custom Eror pages

#Invalid url
@app.errorhandler(404) 
def page_not_found(e):
    return render_template("404.html"),404


#Internal server eror A7a
@app.errorhandler(500) 
def page_not_found(e):
    return render_template("500.html"),500



if __name__ == '__main__':
   app.run(debug=True)  # تأكد من أن debug=True
