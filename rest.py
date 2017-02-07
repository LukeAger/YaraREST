from time import gmtime, strftime
from bottle import route, get, run, post, request


@post('/get')
def index():
    rulename = request.forms.get('rulename')
    f = open(rulename, 'rb')
    rule = f.read()
    f.close()
    return rule


@post('/put')
def index():
    recivedt = strftime('%Y-%m-%d %H:%M:%S', gmtime())
    rulename = request.forms.get('rulename')
    filename = request.forms.get('filename')
    hostname = request.forms.get('hostname')
    f = open("results.txt", "a")
    f.write("%s,%s,%s,%s\r\n" % (recivedt, hostname, rulename, filename))
    f.close()
    return ""


run(host='192.168.1.68', port=8080)