import re

a = re.compile("村饭")

def is_call(key):
    result = re.findall(a, key)
    if result:
        return result[0]
    return None

if is_call('撒旦法昂村 饭收到了咖啡机'):
    print(1)
