from socket import *
ADDR=("127.0.0.1",9422)
class FTPClient:
    def __init__(self, sockfd):
        self.sockfd=sockfd


    def do_list(self):
        self.sockfd.send(b"L")
        data=self.sockfd.recv(128).decode()
        if data=="YES":
            data=self.sockfd.recv(4096)
            print(data.decode())
        else:
            print("获取文件列表失败")





def main():
    s=socket()
    s.connect(ADDR)
    #实例化对象
    ftp=FTPClient(s)
    while True:
        print("==========命令选项===========")
        print("========== list  ===========")
        print("==========get file===========")
        print("==========put file===========")
        print("==========  quit  ===========")
        print("=============================")

        cmd=input("请输入命令：")
        if cmd=="list":
            ftp.do_list()
if __name__ == '__main__':
    main()

