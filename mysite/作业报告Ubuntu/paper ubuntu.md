# 作业报告Ubuntu-邓沛

## 一、virtualbox中配置lunix ubuntu虚拟机
![图1](./pic1/x0.png'x0')

## 二、网络桥接配置
1. 网卡1配置
   1. ![图2](./pic1/x1.png'x1')
2. 网卡2配置
   1. ![图3](./pic1/x2.png'x2')
## 三、联网安装包配置
1. ![图4](./pic1/x3.png'x3')
```
代码：sudo apt install net-tools
```

## 四、ip地址查询
1. 虚拟机IP地址查询
   1. ![图5](./pic1/x4.png'x4')
2. 主机IP地址查询
   1. ![图6](./pic1/x5.png'x5')
## 五、连接网络
1. 虚拟机尝试链接host主机
   1. ![图7](./pic1/x11.png'x11')
```
代码：ping 192.168.1.4
```

2. 主机尝试连接网络及网络连接成功
   1. ![图8](./pic1/x7.png'x7')
```
代码：ping 10.0.2.15
```
## 六、http开通及服务
1. guest主机使用github html范例样式
   1. ![图9](./pic1/x8.png'x8')
```
代码：git clone https://github.com/zxuqian/html-css-examples.git
```
2. guest主机开通http server服务
   1. ![图10](./pic1/x9.png'x9')
```
代码：python3 -m http.server --directory html-css-examples 8000
```
3. 连接访问效果
   1. ![图11](./pic1/x10.png'x10')

注解

> 无


