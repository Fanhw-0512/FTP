from socket import *
from threading import Thread
import sys,os
import time
#全局变量
HOST="0.0.0.0"
PORT=9422
ADDR=(HOST,PORT)
FTP="/home/tarena/FHW/File/"
class FTPServer(Thread):
    def __init__(self, connfd):
        super().__init__()
        self.connfd=connfd
    def do_list(self):
        file_list=os.listdir(FTP)
        if not file_list:
            self.connfd.send(b"NO")
            return
        else:
            self.connfd.send(b"YES")
            time.sleep(0.1)
            data="\n".join(file_list)




    def run(self):
        while True:
            data = self.connfd.recv(1024)
            print(data)

def main():
    #创建套接字
    sock=socket()
    sock.bind(ADDR)
    sock.listen(3)
    print("Listen to the port 9422")
    #循环连接客户端
    while True:
        try:
            connfd,addr=sock.accept()
            print("客户端地址：",addr)
        except:
            sys.exit("服务退出")

        t=FTPServer(connfd)
        t.setDaemon(True)
        t.start()
if __name__ == '__main__':
         main()
