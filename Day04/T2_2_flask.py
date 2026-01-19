from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟数据库：使用列表存储用户数据
users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
]


# 获取所有用户
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# 获取单个用户
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = None
    for u in users:
        if int(u['id']) == user_id:
            user = u
            break

    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404


# 创建用户
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    if not new_user or 'name' not in new_user or 'email' not in new_user:
        return jsonify({'error': 'Invalid input'}), 400

    # 自动生成 ID
    new_user['id'] = max([u['id'] for u in users], default=0) + 1
    users.append(new_user)
    return jsonify(new_user), 201


# 更新用户
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = None
    for u in users:
        if int(u['id']) == user_id:
            user = u
            break

    if not user:
        return jsonify({'error': 'User not found'}), 404

    updated_data = request.get_json()
    user.update(updated_data)
    return jsonify(user)


# 删除用户
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = None
    for u in users:
        if u['id'] == user_id:
            user = u
            break

    if not user:
        return jsonify({'error': 'User not found'}), 404

    users = [u for u in users if u['id'] != user_id]
    return jsonify({'message': 'User deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


