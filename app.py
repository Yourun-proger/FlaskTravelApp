from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html",
                           tours=data.tours,
                           title=data.title,
                           subtitle=data.subtitle,
                           departures=data.departures)


@app.route("/departures/<departure>/")
def departures(departure):
    count = 0
    prices = []
    nignts = []
    smr = {}
    for key, tour in data.tours.items():
        if tour["departure"] == departure:
            smr[key] = tour
            count += 1
    for tr in smr.values():
        prices.append(tr["price"])
        nignts.append(tr["nights"])
    return render_template("departure.html",
                           departures=data.departures,
                           departure=departure,
                           max_money=max(prices),
                           min_money=min(prices),
                           max_nights=max(nignts),
                           min_nights=min(nignts),
                           smr=smr,
                           count=count)


@app.route("/tours/<int:id>/")
def tours(id):
    return render_template("tour.html", tour=data.tours[id], id=id, departures=data.departures)


@app.errorhandler(500)
def render_server_error(error):
    page = "<h1>500 error</h1><br><h2>Из-за некорректого ввода произошла ошибка на сервере...</h2>"
    return page


@app.errorhandler(404)
def render_not_found(error):
    page = "<h1>404 error</h1><br><h2>Сайт не нашёл тура или направления...</h2>"
    return page


if __name__ == '__main__':
    app.run()
