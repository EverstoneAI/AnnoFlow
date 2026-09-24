FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
EXPOSE 7860
ENV PORT=7860
CMD ["python", "app.py"]
