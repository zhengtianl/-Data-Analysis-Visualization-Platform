# 基于Node.js的官方镜像
FROM node:14-alpine

# 在容器中创建一个工作目录
WORKDIR /app

# 将本地的 package.json 和 package-lock.json 复制到容器中
COPY package*.json ./

# 安装项目依赖
RUN npm install

# 复制本地的前端文件到容器中
COPY . .

# 构建前端项目
RUN npm run build

# 暴露容器内的端口（如果前端应用使用了特定的端口，请相应修改）
EXPOSE 3000

# 启动前端应用
CMD ["npm", "run", "start"]
