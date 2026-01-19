import requests

# 目标接口地址
url = "https://jsonplaceholder.typicode.com/users"

try:
    # 发送GET请求获取用户列表
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # 检查HTTP请求是否成功

    # 解析返回的JSON数组
    users = response.json()
    # 提取所有用户的姓名并打印
    print("所有用户姓名：")
    for user in users:
        print(f"- {user['name']}")

except requests.exceptions.RequestException as e:
    print(f"获取用户失败：{str(e)}")