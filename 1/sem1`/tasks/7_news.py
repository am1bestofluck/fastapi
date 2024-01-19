"""вывести новости через шаблон"""

from flask import render_template, Flask
from datetime import date,timedelta

app = Flask(__name__)
@app.route("/news/")
def get_news(page="news.html",):
    news_ = []
    estimate=10
    for i in range(estimate, 0, -1):
        news_.append(
            {"date": date.today() - timedelta(days=i),
             "name": f"entry#{5 - i}",
             "content": "lorem" * (estimate - i)})
    return render_template(page,news=news_)

if __name__ == '__main__':
    app.run()