import redis
import flask
import services
from booking import Booking, Hotel
import datetime


r = redis.Redis(
    host='localhost',
    port=6379, 
    decode_responses=True
    )

app = flask.Flask(__name__)
booking = Booking(
    datetime.datetime(2023, 3, 1),
    datetime.datetime(2023, 3, 8)
)


@app.route("/")
def main_page():
    hotels: list[Hotel] = booking.get_info()
    return flask.render_template('index.html', hotels=hotels)


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8000,
        debug=True
    )

