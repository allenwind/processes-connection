import time
import numpy as np
from multiprocessing.connection import Client

address = ("localhost", 8080)
authkey = b"qwerty"
client = Client(address, authkey=authkey)

while True:
    data = np.random.uniform(size=(1000, 1000)) # 模拟处理好的数据
    client.send(data) # 发送数据
    time.sleep(1)
