# import requests
# response = requests.get('https://httpbin.org/get')
# print(response.status_code) # 打印状态码
# print(response.text) # 打印响应内容
import requests

try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    response.raise_for_status()  # 检查请求是否成功
    data = response.json()
    print(data['title'])
    print(data['body'])
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
except KeyError as e:
    print(f"数据中缺少键: {e}")
