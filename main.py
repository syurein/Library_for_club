from flask import Flask,render_template, request
import json
import os
app=Flask(__name__)
@app.route('/')
def get_html():
    with open('./index.html','r',encoding='utf-8') as f:
        text=f.read()
        print(f.read())
    return text

@app.route('/get_data')
def get_data():
    try:
        with open('./data.json','r',encoding='utf-8') as f:
            context=f.read()
        return context
    except FileNotFoundError:
        return '{}'

@app.route('/set_data',methods=["POST"])
def set_data():
  
    datas=json.loads(request.get_data())
    
    with open('./data.json','r',encoding='utf-8') as f:
        
        data=json.load(f)
        print(data[datas['title']]['status'])
        if data[datas['title']]:
            print(data[datas['title']]['status'])
            data[datas['title']]['status']=datas['status']

    with open('./data.json','w',encoding='utf-8') as f:
        json.dump(data,f,indent=2)
        print('success')
    return '{status:"success"}'

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=os.environ["PORT"])
