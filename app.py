import os
from fastapi import FastAPI, Response

app = FastAPI()

# 魔搭自定义部署会注入 PORT 环境变量；本地默认 7860
PORT = int(os.environ.get("PORT", 7860))


@app.get("/")
def index():
    with open("index.html", "r", encoding="utf-8") as f:
        return Response(content=f.read(), media_type="text/html; charset=utf-8")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=PORT)
