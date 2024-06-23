#python环境
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 将项目文件复制到工作目录
COPY . /app

# 安装所需的Python库
RUN pip install --no-cache-dir -r requirements.txt

# 安装Redis服务器
RUN apt-get update && apt-get install -y redis-server

# 下载NLTK数据集
RUN python -c "import nltk; nltk.download('punkt')"

# 暴露Django应用的端口
EXPOSE 8000

# 启动Redis服务器
CMD ["redis-server", "--daemonize", "yes"]


# 运行数据库迁移
RUN python manage.py migrate

# 启动Celery worker
CMD ["celery", "-A", "news_aggregator", "worker", "--loglevel=info"]


#安装angular以及node.js，有一些核心包： ng add @angular/material


# 启动Celery beat
CMD ["celery", "-A", "news_aggregator", "beat", "--loglevel=info"]

# 启动Django应用
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]