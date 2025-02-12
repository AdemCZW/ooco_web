# 使用官方的 Python 3.9 镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

#
COPY . .

CMD ["python", "app.py"]
