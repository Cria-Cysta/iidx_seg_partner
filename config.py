import main
import serial

print("==============iidx串口助手==============")
print("ver 0.1 alpha")
print("================开始配置================")
add=str(input("请输入S tools api连接地址，若本地请填127.0.0.1："))
port=int(input("请输入连接端口："))
pswd=str(input("请输入密码："))

com=str(input("请输入待转发的端口（格式：comX）："))
baud=int(input("请输入端口波特率："))

if add is not None:
    if port is not None:
        if pswd is not None:
            try:
                print("尝试连接中……")
                detail=main.spice_connect(add,port,pswd)
            except ConnectionRefusedError:
                print("连接失败，请重启程序。")
                exit()
                

print("连接成功，已经连接到位于%s:%d的S tools api。"%(add,port))
ser=serial.Serial(com,baud)
ser.rtscts=1
ser.writeTimeout=0.1

print("数据转发至%s端口。"%(com))

i=1
while i == 1:
    try:
        texts=(main.ticker_get(detail))
        ser.write(texts.encode())
    except serial.serialutil.SerialTimeoutException:
        pass
    except ConnectionResetError:
        exit()
