from flask import Flask,render_template
import json

app=Flask(__name__)
@app.route('/')
def get_html():
    with open('./index.html','r',encoding='utf-8') as f:
        text=f.read()
        print(f.read())
    return text


if __name__ == "__main__":
	app.run(debug=True)
