from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Home.html")
if __name__ == "__main__":
    app.run()

@app.route("/About")
def about():
    return render_template("About.html")

@app.route("/About/James")
def jimmy():
    return render_template("About/James.html")

@app.route("/About/Patrick")
def patrick():
    return render_template("About/Patrick.html")

@app.route("/Alabama")
def alabama():
    return render_template("Alabama.html")

@app.route("/Alaska")
def alaska():
    return render_template("Alaska.html")

@app.route("/Arizona")
def arizona():
    return render_template("Arizona.html")    

@app.route("/Arkansas")
def arkansas():
    return render_template("Arkansas.html")

@app.route("/California")
def california():
    return render_template("California.html")

@app.route("/Colorado")
def colorado():
    return render_template("Colorado.html")

@app.route("/Connecticut")
def connecticut():
    return render_template("Connecticut.html")    

@app.route("/Delaware")
def delaware():
    return render_template("Delaware.html")     

@app.route("/Florida")
def florida():
    return render_template("Florida.html")     

@app.route("/Georgia")
def georgia():
    return render_template("Georgia.html") 

@app.route("/Hawaii")
def hawaii():
    return render_template("Hawaii.html") 

@app.route("/Idaho")
def idaho():
    return render_template("Idaho.html") 

@app.route("/Illinois")
def illinois():
    return render_template("Illinois.html") 

@app.route("/Indiana")
def indiana():
    return render_template("Indiana.html") 

@app.route("/Iowa")
def iowa():
    return render_template("Iowa.html") 

@app.route("/Kansas")
def kansas():
    return render_template("Kansas.html") 

@app.route("/Kentucky")
def kentucky():
    return render_template("Kentucky.html") 

@app.route("/Louisiana")
def louisiana():
    return render_template("Louisiana.html") 

@app.route("/Maine")
def maine():
    return render_template("Maine.html") 

@app.route("/Maryland")
def maryland():
    return render_template("Maryland.html")     

@app.route("/Massachusetts")
def massachusetts():
    return render_template("Massachusetts.html") 

@app.route("/Michigan")
def michigan():
    return render_template("Michigan.html")

@app.route("/Minnesota")
def minnesota():
    return render_template("Minnesota.html")

@app.route("/Mississippi")
def mississippi():
    return render_template("Mississippi.html")

@app.route("/Missouri")
def missouri():
    return render_template("Missouri.html")

@app.route("/Montana")
def montana():
    return render_template("Montana.html")

@app.route("/Nebraska")
def nebraska():
    return render_template("Nebraska.html")

@app.route("/Nevada")
def nevada():
    return render_template("Nevada.html")

@app.route("/NewHampshire")
def newhampshire():
    return render_template("NewHampshire.html")

@app.route("/NewJersey")
def newjersey():
    return render_template("NewJersey.html")

@app.route("/NewMexico")
def newmexico():
    return render_template("NewMexico.html")

@app.route("/NewYork")
def newyork():
    return render_template("NewYork.html")

@app.route("/NorthCarolina")
def northcarolina():
    return render_template("NorthCarolina.html")

@app.route("/NorthDakota")
def northdakota():
    return render_template("NorthDakota.html")

@app.route("/Ohio")
def ohio():
    return render_template("Ohio.html")

@app.route("/Oklahoma")
def oklahoma():
    return render_template("Oklahoma.html")

@app.route("/Oregon")
def oregon():
    return render_template("Oregon.html")

@app.route("/Pennsylvania")
def pennsylvania():
    return render_template("Pennsylvania.html")

@app.route("/RhodeIsland")
def rhodeisland():
    return render_template("RhodeIsland.html")

@app.route("/SouthCarolina")
def southcarolina():
    return render_template("SouthCarolina.html")

@app.route("/SouthDakota")
def southdakota():
    return render_template("SouthDakota.html")

@app.route("/Tennessee")
def tennessee():
    return render_template("Tennessee.html")

@app.route("/Texas")
def texas():
    return render_template("Texas.html")

@app.route("/Utah")
def utah():
    return render_template("Utah.html")

@app.route("/Vermont")
def vermont():
    return render_template("Vermont.html")

@app.route("/Virginia")
def virginia():
    return render_template("Virginia.html")

@app.route("/Washington")
def washington():
    return render_template("Washington.html")


@app.route("/WestVirginia")
def westvirinia():
    return render_template("WestVirginia.html")

@app.route("/Wisconsin")
def wisconsin():
    return render_template("Wisconsin.html")

@app.route("/Wyoming")
def wyoming():
    return render_template("Wyoming.html")
































