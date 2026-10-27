import json
import requests


class SimpleWebInspector:
    """轻量级 HTTP 请求测试与数据抓包工具类"""

    def __init__(self, base_url=""):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept": "application/json, text/plain, */*",
            }
        )

    def inspect_request(self, method, endpoint, params=None, json_data=None):
        url = self.base_url + endpoint if self.base_url else endpoint
        print("\n" + "=" * 50)
        print(f"👉 [发送请求] {method.upper()} {url}")
        print("=" * 50)

        try:
            res = self.session.request(
                method=method, url=url, params=params, json=json_data, timeout=10
            )
            print(f"👈 [收到响应] 状态码: {res.status_code}")
            try:
                print(json.dumps(res.json(), indent=2, ensure_ascii=False))
            except Exception:
                print(res.text[:300])
            return res
        except Exception as e:
            print(f"❌ [请求异常] {e}")
            return None


if __name__ == "__main__":
    inspector = SimpleWebInspector()
    print("--- 正在测试 GET 接口 ---")
    inspector.inspect_request(
        "GET", "https://httpbin.org/get", params={"test_id": "1001"}
    )