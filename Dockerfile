# 使用官方 Python 作为基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置环境变量（防止 Python 生成 .pyc 文件）
ENV PYTHONUNBUFFERED=1

# 运行 Django 迁移和启动服务器
CMD ["sh", "-c", "python manage.py migrate && gunicorn oocoweb.wsgi:application --bind 0.0.0.0:8080"]
