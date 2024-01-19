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
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"

    )


#################################################
# Flask Routes
#################################################
@app.route("/api/v1.0/precipitation")
def precipitation():
    precipitation_result = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= "2016_08_23").all()
    session.close()
    precipitation_output = []
    for date, prcp in precipitation_result:
        prec_dict = {}
        prec_dict["date"] = prcp
        precipitation_output.append(prec_dict)

    return jsonify(precipitation_output)

@app.route("/api/v1.0/stations")
def station():
    station_list = session.query(Station.name).all()
    session.close()
    station_output = []
    for station in station_list:
        station_output.append(station.name)
    return jsonify(station_output)

@app.route("/api/v1.0/tobs")
def tobs():
    tobs_list = session.query(Measurement.tobs).filter(Measurement.station == "USC00519281").filter(Measurement.date >= "2016_08_23").all()
    session.close()
    tobs_output = []
    for tobs in tobs_list:
        tobs_output.append(tobs.tobs)
    return jsonify(tobs_output)



app.run()