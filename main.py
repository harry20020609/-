import eel
import jieba
import jieba.analyse as analyse

# 定义html文件所在文件夹名称
eel.init('web')
jieba.initialize()
analyse.set_idf_path("idf.txt")
jieba.load_userdict("user_dict.txt")


@eel.expose # 使用装饰器,类似flask里面对路由的定义
def py_fun1(a):#返回 各类名词
    content = analyse.extract_tags(a,topK=30,allowPOS=(['nr','ns']))
    return("/".join(content))

@eel.expose
def py_fun2(a):#返回 动词
    content = analyse.extract_tags(a,topK=20,allowPOS=(['v']))
    return("/".join(content))
    
@eel.expose
def py_fun3(a):#返回形容词
    content = analyse.extract_tags(a,topK=20,allowPOS=(['a','ad','an']))
    return("/".join(content))

@eel.expose
def py_fun4(a):#返回名词
    content = analyse.extract_tags(a,topK=20,allowPOS=(['nt','nz']))
    return("/".join(content))

# 启动的函数调用放在最后,port=0表示使用随机端口,size=(宽,高)
eel.start('main.html', port=0)