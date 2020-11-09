import tablib
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/json')
def convertToJson():
    return "Get JSON file"

@app.route('/api/excel', methods=['POST'])
def convertToExcel():
    firstname = request.values['name']
    print(firstname)
    return "Nothing"

# headers = ('first_name', 'last_name')
#
# data = [
#     ('John', 'Adams'),
#     ('George', 'Washington')
# ]
#
# data = tablib.Dataset(*data, headers=headers)
#
# print(data)

if __name__ == '__main__':
    app.run()


