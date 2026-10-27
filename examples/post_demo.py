import sys
import os

# 将项目根目录加入环境变量，方便导入 main.py 中的类
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import SimpleWebInspector

if __name__ == "__main__":
    print("=== 正在运行示例：使用自定义 Inspector 发送 POST 请求 ===")
    
    # 初始化抓包测试器
    inspector = SimpleWebInspector()

    # 测试 POST 请求与 JSON 载荷提交
    inspector.inspect_request(
        method="POST",
        endpoint="https://httpbin.org/post",
        json_data={
            "tool_name": "py-web-inspector",
            "action": "security_test",
            "status": "active"
        }
    )