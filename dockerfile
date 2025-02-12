# 使用官方的 Python 3.9 镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 文件到容器中
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制所有文件到容器中
COPY . .

# 设置容器的默认命令（根据你的项目进行修改）
CMD ["python", "app.py"]
