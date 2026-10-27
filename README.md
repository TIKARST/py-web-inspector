# py-web-inspector

基于 Python `requests` 的轻量级 HTTP 请求测试与数据抓取工具，专为网络安全测试、接口调试及轻量数据解析设计。

---

## 💡 功能亮点

* **轻量高效**：基于 Python 原生 `requests` 模块构建，快速发起 HTTP/HTTPS 请求。
* **模拟请求头**：预设常用浏览器 User-Agent，减少被目标站点误封禁的风险。
* **自动格式化解析**：自动对返回的 JSON 数据进行缩进打印，非 JSON 格式自动截取部分文本，方便快速排查。
* **结构化架构**：内置完整的使用示例 (`examples/`) 及单元测试 (`tests/`)，方便二次开发与扩展。

---

## 🛠️ 目录结构

```text
py-web-inspector/
├── examples/
│   └── post_demo.py     # POST 请求提交 JSON 数据示例
├── tests/
│   └── test_inspector.py# 单元测试代码
├── LICENSE              # 开源协议 (MIT)
├── README.md            # 项目说明文档
├── main.py              # 核心抓包测试类定义
└── requirements.txt     # 项目依赖声明