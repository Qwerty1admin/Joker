from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_tg():
    return redirect('https://t.me/JokerPrankedbot')

if __name__ == '__main__':
    app.run()
