from flask import Flask, jsonify, request


app = Flask(__name__)

toDolist = [
    {
        'title': 'hello',
    },
    {
        'title': 'flask',
    }
]


@app.route('/')
def home():
    return "hello"


# Get All Todo List
@app.route('/allList')
def getAllToDoList():
    print(toDolist)
    return jsonify(toDolist)


@app.route('/addNewList', methods=['POST'])
def addNewList():
    request_data = request.get_json()
    new_data = {
        'title': request_data['title'].lower()
    }
    toDolist.append(new_data)
    return jsonify(toDolist)


@app.route('/delete/<string:title>', methods=['DELETE'])
def deleteOneItem(title):
    msg: any
    for list in toDolist:
        if list['title'] == title.lower():
            delete_item = {'title': title.lower()}
            toDolist.remove(delete_item)
            msg = title + ' Deleted Successful'
        else:
            msg = title + ' Not Found'
    return jsonify({
        'msg': msg,
        'status': 200
    })


@app.route('/deleteAll', methods=['DELETE'])
def deleteAll():
    toDolist.clear()
    return 'Deleted'


@app.route('/update/<string:title>', methods=['PATCH'])
def updateItem(title):
    msg: any
    request_data = request.get_json()
    newTitle = request_data['title'].lower()
    print("newTitle", newTitle)

    for list in toDolist:
        if list['title'] == title.lower():
            newValue = {'title': newTitle}

            toDolist.remove(list)
            toDolist.append(newValue)

            msg = title + ' Updated to ' + newTitle
        else:
            print('Not Found', list)
            msg = title + ' Not Found'
    return ({
        'msg': msg,
        'status': 200,
    })


if __name__ == '__main__':
    app.run(port=5000)
