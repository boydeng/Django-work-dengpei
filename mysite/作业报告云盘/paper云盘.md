# 作业报告云盘-邓沛

## 一、github中仓库的建立与git操作
1. git建立初始仓库完成效果
   1. ![图1](./pic1/x0.png'x0')
2. git公钥产生
   
   ```
   代码：ssh-keygen
   ```
3. git公钥配置
    ```
    dengpei@LAPTOP-HV1G1FL4 MINGW64 ~
    $ cat ~/.ssh/id_rsa.pub
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDw9WLhwHSP8cOuEXe7OAA79cceJL7A4gns/NZH0rMwFYBRSt2fCTDAttMA2wX+NscPPS0BkDF7QRbxkt4oiuo4dJPnd/CkTeOLQtbEtUBEi+TOnw3IbdYZhJUkuENIm4BC2aVlbL1XviGXrJyUtQcJcLzG+cLmxRJnUGD2TMWO/Dt/pF3lIkQevty0MXpopVxeIh2FFxkzG+C4lKNNNbKIvMlun92txg2+3jFiFm+BxAROX5iFUjWGBt1Yq8dB9ybeQ1pidWIR2S44cb7HOqGzsALi5WGLoIROBBginYk06X1OurqwJK1w0K0ILO2Eo0597NN6rGdfrToppecsv6nKA5OVIj6bAAoc5dQ6NYWFe03Gga+Ln5ibTRJDWIQuHVhxbRMaXB0WzHsd4S8oArEkBw4QBZEwihgF1RlVuo0DiYqLVczcFpgAs1BJO1Lr966QsucITPpxHqIvlqziYfsx4PpQ4VH8dtL9nqPohJLIVUmCq5YRX0DN3FwUqz+Z1M0= dengpei@LAPTOP-HV1G1FL4

    dengpei@LAPTOP-HV1G1FL4 MINGW64 ~
    $ ls ~/.ssh/
    id_rsa  id_rsa.pub
    ```
    > 注：
    > 1. 由于操作失误，导致公钥生成重做了一次，则公钥重复了，导致git push时不能push到仓库。
    > 2. 解决方法：需首先重新建立公钥（github再建） 再限定为原来公钥路径
    > 3. 公钥再建：![图](./01.jpg '描述')
    > 4. 公钥路径更正:![图](./01.jpg '描述')
    ```
    更正代码：$ git push --set-upstream origin master
    ```
4. 仓库克隆
   ```
    代码：
    dengpei@LAPTOP-HV1G1FL4 MINGW64 ~/repos
    $ git clone git@github.com:boydeng/Django-work-dengpei.git
    ```
5. 切换到Django-work-dengpei，进行后面操作
   1. 效果图：![图1](./pic1/x0.png'x0')


## 二、项目创建初步



## 二、Django下mysite项目创建
1. git命令行中执行命令
    
    ```
    代码：
    ```

1. Django安装

    安装完成效果：![图1](./pic1/x0.png'x0')

2. Django项目初始化

    1. manage.py命令启动
    2. 网页火箭检查：![图1](./pic1/x0.png'x0')
    >注：若小火箭出现，则Django初始化成功
 3. polls app创建初步：

    1. git命令行执行代码：

    ```
    代码：
    ``` 
    2. 完成效果展示：![图2](./pic1/x1.png'x1')

## 三、vscode代码编写
>前面操作完成后，在vscode进行操作
1. 初始文件创建及配置
   1. 首先在仓库创建mysite文件夹，子目录下创建mysite、 news等文件夹，其次将sqlite3与pyc格式的文件加入gitignore，再通过通配符屏蔽这些格式的文件
   2. ![图2](./pic1/x1.png'x1')
2. 数据库建立及迁移，安装sqlite3
   1. 数据库建立：![图3](./pic1/x2.png'x2')
        1. 代码：
        ```
        ```
    2. 迁移：
        
        1. 代码：
        ```
        ```
    3. sqlite3安装成功：

        1. ![图1](./pic1/x0.png'x0')

3. 网络页面admin编写
    1. 先创建账号：
    2. 效果图：
        1. ![图4](./pic1/x3.png'x3')
        2. ![图4](./pic1/x3.png'x3')
4. news页面管理
    1. Reporter属性添加
    2. 按mysite/news/templates/news/year_archive.html样式创建文件，进行网页地址编写，网页效果预览，确定html网页样式 
    3. 在admin/news/artile/路径下添加文章，通过news文件夹下的artiles/int:year>/路径访问
5. 文件上传页面编写
    1. 增加文件上传的类HomeworkCreate，创建作业提交网页样式  
      
        1. 效果展示：
        ![图4](./pic1/x3.png'x3')



注解

> 1. 所有程序借助Django文档编写，若出现失误以文档为准。
> 2. Django文档链接：
    [Django文档](https://docs.djangoproject.com/en/3.1/ 'Django')