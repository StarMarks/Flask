?
rt Flask,make_response

__author__ = 'zzw'

app = Flask(__name__)
app.config.from_object('config')

@app.route('/hello')
def hello():
    headers={
        'content-type': 'application/json',
        'location': 'http://www.baidu.com'
    }
    # response = make_response('<html></html>', 301)
    # response.headers = headers
    # return response
    return  '<html></html>',301,headers
    # return '<html></html>'

def helloo():
    return 'hello word!!666666'

# app.add_url_rule('/hello',view_func=hello)
if __name__ == '__main__':
    # 生产环境 nginx+uwsgi
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=66)
