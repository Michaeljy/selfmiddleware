# selfmiddleware


中间件可以对项目全局进行一个管控，自定义一个中间件，思路如下：
      
    基于一个需求：我想以多种方式发送同一个语句，与此同时，如果想禁用某一种方式，直接注释一条语句就好了。
    
    首先在notify文件夹中，把各个方式的类写好（email、msg、qq...), 这个类有一个__init__, 留作执行发送方式前，进行一些准备操作（配置环境，数据什么的），然后利用python崇尚的方法重写---鸭子类型，分别写一个send方法，执行相对应的功能。
    然后在settings文件中，把各个类的路径（字符串，精确到字符串）存到一个列表中。
    最后要记得，导包的话，就要把notify设置成包，这样就需要在notify中设置一个__init__文件夹，这样导notify模块时，就先执行该__init__里面的文件。
    文件里定义一个方法，然后把settings文件夹导过来，对里面的字符串进行拼接，这样通过导包及反射，就可以拿到各个类中对应的方法，然后执行即可
