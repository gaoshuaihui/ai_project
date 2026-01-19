import requests

# 目标接口地址
url = "https://jsonplaceholder.typicode.com/posts"

# 要提交的新帖子数据（符合接口要求的字段）
new_post = {
    "title": "我的测试帖子",  # 帖子标题
    "body": "这是用requests库提交的测试内容",  # 帖子正文
    "userId": 1  # 用户ID（接口要求必填字段）
}

try:
    # 发送POST请求提交数据（HTTPS请求会自动验证证书）
    response = requests.post(
        url=url,
        json=new_post,  # 自动将字典转为JSON格式，设置Content-Type: application/json
        timeout=10  # 设置超时时间，避免无限等待
    )

    # 检查请求是否成功（HTTP状态码201表示创建成功）
    response.raise_for_status()

    # 解析返回的JSON数据
    result = response.json()
    print(f"服务器返回的JSON数据：{result}")
    # 提取并打印新帖子的ID
    new_post_id = result.get("id")
    print(f"新帖子提交成功！返回的ID是：{new_post_id}")

except requests.exceptions.RequestException as e:
    # 捕获所有请求相关的异常（超时、连接失败、状态码错误等）
    print(f"提交帖子失败：{str(e)}")
    # 若有返回内容，打印详细信息
    if hasattr(e, 'response') and e.response is not None:
        print(f"服务器返回详情：{e.response.text}")