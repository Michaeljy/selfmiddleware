
class Msg(object):
    def __init__(self):
        pass  # 发短信需要的前提准备工作

    def send(self,content):
        print('短信通知:%s'%content)
