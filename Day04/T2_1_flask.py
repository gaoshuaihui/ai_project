from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        if not username or not email:
            return jsonify({'error': '用户名和邮箱不能为空'}), 400
        return jsonify({
            'message': f'用户 {username} 注册成功',
            'user_info': {
                'username': username,
                'email': email
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

