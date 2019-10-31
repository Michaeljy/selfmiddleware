
import settings
import importlib


def send_all(content):
    for module_path in settings.NOTIFY_LIST:
        module, class_name = module_path.rsplit('.',maxsplit=1)
        # module = 'notify.email'  class_name = 'Email'
        mod = importlib.import_module(module)  # mod就是模块名
        # from notify import email
        cls = getattr(mod,class_name)  # 利用反射 获取到模块中类的变量名
        obj = cls()
        obj.send(content)


