from flask import Flask, jsonify, request
app = Flask(__name__)
items = []

@app.route('/items', methods=['GET'])
def home():
    """

    home page

    """

    return jsonify({
        'message': 'Welcome to my first API!',
        'available_routes': {
            'GET /': 'This welcome message',
            'GET /items': 'Get all items',
            'GET /items/<id>': 'Get a single item by ID',
            'POST /items': 'Create a new item'
        }
    })

def get_items():
    """
    Returns all items in our list
    """
    return jsonify({'items': items})

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """
    Returns a single item by its ID
    """
    
    if item_id < 0 or item_id >= len(items):
        return jsonify({'error': 'Item not found'}), 404
    
    return jsonify({'item': items[item_id]})


@app.route('/items', methods=['POST'])
def create_item():
    """
    Creates a new item from the POST request data
    """
    data = request.get_json()
    
   
    if 'name' not in data:
        return jsonify({'error': 'Name field is required'}), 400
    
    
    new_item = {
        'id': len(items),
        'name': data['name']
    }
    
   
    items.append(new_item)
    
    
    return jsonify({'item': new_item}), 201

# This is here just to ensure the server only runs if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)