# Import the dependencies.
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


#################################################
# Database Setup
#################################################




# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(bind=engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
@app.route("/")
def index():
    return(
        f"Welcome to SQLalchemy challenge!<br/>"
        f"here are the available routes:<br/>"
        f"/api/v1/static_Route <br/>"
        f"/api/v1/dynamic_Route"

    )


#################################################
# Flask Routes
#################################################