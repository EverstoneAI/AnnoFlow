# AnnoFlowSmartLabel Pro · 四模态数据标注工具（魔搭创空间部署版）

自研的纯前端多模态数据标注工具，面向 AI 训练师与数据标注团队。支持图像 / 文本 / 音频 / 视频四模态统一管理，6 种格式导出。

**License：Apache License 2.0（开源 / 免费）**

## ✨ 核心能力

- 纯前端实现，零服务器依赖，可部署任意静态托管
- 内嵌分级练习体系与标注规范引导（入门 → 初级 → 中级 → 高级）
- 6 种标注格式导出：YOLO / VOC / COCO / JSON / 自定义结构化 / BIO（NER）
- 已实操 200+ 条标注并通过内部一致性自测
- API 对接阿里云百炼 DashScope（OpenAI 兼容模式），可调用 Qwen / DeepSeek 等模型做智能辅助标注（可选，用户自填 key）
- 内置示例素材（浏览器实时生成，无需联网即可体验）

## 🚀 本地预览

```bash
pip install -r requirements.txt
python app.py
# 浏览器打开 http://localhost:7860
```

或直接双击 `index.html` 也能在浏览器打开（纯前端，无需后端）。

## 📦 魔搭创空间部署

1. 在魔搭创建创空间（https://modelscope.cn/studios/create/）
   - **SDK 类型选「自定义」**（如有「前端」类型也可直接传 `index.html`）
   - 中文名：`AnnoFlowSmartLabel Pro · 四模态数据标注工具`
   - License：Apache License 2.0
   - 是否公开：公开
2. 创建后拿到 git 仓库地址，把本目录所有文件 push 上去：
   ```bash
   git clone <魔搭给的仓库地址>
   cd <仓库目录>
   # 把 app.py / index.html / requirements.txt / Dockerfile 复制进来
   git add .
   git commit -m "deploy AnnoFlowSmartLabel Pro"
   git push
   ```
3. 魔搭自动构建 + 部署，拿到 `modelscope.cn/studios/<owner>/<name>` 的在线地址

## 🛠 技术栈

- 前端：HTML / CSS / JavaScript 纯前端（单文件，零外部依赖）
- 部署：FastAPI 静态服务（自定义 Docker，端口读取 `PORT` 环境变量）
- 智能辅助：阿里云百炼 DashScope API（OpenAI 兼容模式）

## 👤 作者

何逸凡 · 浮石录团队 · fushilu921
