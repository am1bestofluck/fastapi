"""выводим фласком hello world"""

from flask import Flask

app = Flask("__main__")


@app.route("/")
def static_string(item: str | None = None):
    if item is None:
        item = "Hello world!"
    return item


if __name__ == '__main__':
    # static_string(item="Hello_world")
    app.run()
