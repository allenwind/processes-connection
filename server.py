from multiprocessing.connection import Listener

address = ("localhost", 8080)
authkey = b"qwerty" # 用来进行hmac认证，注意是bytes类型
server = Listener(address, authkey=authkey)
conn = server.accept() # 接受连接

while True:
    data = conn.recv() # 接收数据
    print(data.shape)
