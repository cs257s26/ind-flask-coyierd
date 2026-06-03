from flask import Flask

from ProductionCode import command_line

app = Flask(__name__)


@app.route("/year_count/<bird>/<year>")
def year_count(bird, year):
    """Routes a bird and year to find the total sightings of the bird that year"""
    year = int(year)
    return (
        "There were "
        + str(command_line.find_sightings_all_locations(bird, year))
        + f" sightings of the {bird} in {year}."
    )


@app.route("/year_stop_count/<bird>/<year>/<stop>")
def popular_stop(year):
    """Routes a bird, stop, and year to finding the sightings for a bird at a stop from a certain year"""
    year = int(year)
    return (
        "The most birds were seen at stop "
        + str(command_line.find_most_popular_stop(year))
        + " in "
        + f"{year}"
        + " out of all stops that year."
    )


app.run(port=845, host="0.0.0.0")
