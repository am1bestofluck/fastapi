from flask import Flask

app = Flask("__main__")

@app.route("/<item>/")
def len_(item:str):
    return f"Got '{item}'<br>{len(item)=}"
