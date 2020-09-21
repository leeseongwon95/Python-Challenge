import requests
from flask import Flask, render_template, request


base_url = "http://hn.algolia.com/api/v1"
new = f"{base_url}/search_by_date?tags=story"
popular = f"{base_url}/search?tags=story"
news_db, comment_db = {}, {}

app = Flask("DayNine")


def make_detail_url(id):
    return f"{base_url}/items/{id}"


@app.route("/")
def index():
    order_by = request.args.get("order_by", default="popular")

    try:
        if order_by not in news_db.keys():
            if order_by == "popular":
                response = requests.get(popular)

            elif order_by == "new":
                response = requests.get(new)

            news = response.json()["hits"]
            news_db[order_by] = news
            print(news_db[order_by])
        else:
            news = news_db[order_by]

        return render_template("index.html", order_by=order_by, news=news)
    except Exception:
        error = f"Can't get {order_by} news."

        return render_template("index.html", order_by=order_by, error=error)


@app.route("/<news_id>")
def detail(news_id):
    print(news_id)
    try:
        print(news_id)
        if news_id not in comment_db.keys():
            detail_url = make_detail_url(news_id)
            response = requests.get(detail_url)
            data = response.json()
            comment_db[news_id] = data

        else:
            data = comment_db[news_id]

        return render_template("detail.html", news_id=news_id, data=data)

    except Exception:
        error = f"Can't get detail information."

    return render_template("detail.html", news_id=news_id, error=error)


app.run(host="0.0.0.0")
