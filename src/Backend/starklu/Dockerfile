# 基础镜像
FROM python:3.8-slim-buster

# 设置工作目录
WORKDIR /app

# 将应用程序添加到容器中
COPY . .

# 安装应用程序所需的依赖项
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 5000

# 启动应用程序
CMD [ "python", "Server.py" ]
