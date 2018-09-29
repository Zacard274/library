# 图书管理系统
* init.py 启动文件
* config.py 配置文件
* fabfile.py 版本发布文件
* controller 处理
* structure 数据封装
* utils 工具库
* logs 日志
* sql 数据库文件
* orm 数据关系映射
* microservices 微服务nameko

| 一期工作目标 | 二期工作目标     |
| :------------- | :------------- |
| 完成基本功能、部署到aws上       | 拆分模块、模块间rpc调用       |
- [ ] flask 的使用（理解flask的框架）
- [ ] web后端基本框架设计
- [ ] 查找自己代码的不足，尝试重构代码
- [ ] 性能调优，迁移更多的功能到微服务上

**需要说明的是nameko需要先启动rabbitmq：
docker run -d --hostname my-rabbit --name some-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management**

:tada: *后续可以添加python docs工具sphinx、 sentry等工具*



Copyright (c) 2018 Copyright Holder All Rights Reserved.
