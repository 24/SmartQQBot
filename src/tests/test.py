import re
import random

a = re.compile("^\.r\s(\d*)d(\d+)(\s.*)?")

def is_call(key):
    result = re.findall(a, key)
    if result:
        return result[0]
    return None

result = is_call('.r d1')
print (result)
num, numrange, reason = result[0],int(result[1]),result[2]
if num:
    num = int(num)
else:
    num = 1
result = [random.randint(1,numrange) for x in range(num)]
reply_content = "因为："+reason+",投出了："
for num in result:
    reply_content += str(num)+"+"
reply_content = reply_content[:-1]+'='+str(sum(result))
print(reply_content)
