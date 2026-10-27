import sys
import os
import unittest

# 将项目根目录加入环境变量
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import SimpleWebInspector

class TestWebInspector(unittest.TestCase):
    """针对 SimpleWebInspector 的基础单元测试"""

    def setUp(self):
        """每个测试用例运行前执行"""
        self.inspector = SimpleWebInspector()

    def test_get_request(self):
        """测试 GET 请求是否能正常返回状态码 200"""
        response = self.inspector.inspect_request(
            method="GET",
            endpoint="https://httpbin.org/get",
            params={"mode": "test"}
        )
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()