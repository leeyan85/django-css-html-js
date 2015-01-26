测试： 
    1. cmd 进入命令行
    2. cd 3levelink,进入工程目录
    3. python manage.py runserver
    4. 访问 http://127.0.0.1:8000/app01/link


文件说明:

    配置文件：3levelink/3levelink/urls.py 配置URL访问
              3levelink/3levelink/settings.py 配置模板路径和静态文件路径

    模板文件： 3levelink/templates/index.html

    静态文件： 3levelink/statics/jquery-1.8.2.js
    
    数据文件:  3levelink/app01/area.py 包括省市县数据文件

    View文件： 3levelink/app01/line3level.py, 从 3levelink/app01/area.py 导入数据
    

    
           

           
           



      


