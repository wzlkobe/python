#coding:GBK 字符设置

import psutil

config_cpu_count = 4                      #cpu数量配置
config_virtual_memory_total = 8          #内存，G为单位

msg = psutil.cpu_times()
print(msg)  #输出cpu的基本信息，以b为单位

cpu_count = psutil.cpu_count()
if cpu_count < config_cpu_count :
    print("你的CPU低于"+str(config_cpu_count)+"核，不适合电子证照系统的部署，请更换您的服务器！ ")
    quit()
else:
    print("CPU数量为" + str(cpu_count) + "核，符合电子证照系统的部署~")
    virtual_memory_total = psutil.virtual_memory().total
    virtual_memory_total /= 1024 * 1024 * 1024
    if (virtual_memory_total + 1) < config_virtual_memory_total :

        print("内存为低于"+str(config_virtual_memory_total)+"G，不符合电子证照系统的部署~")
        quit()
    else :
        print("内存为" + str(virtual_memory_total + 1) + "G，符合电子证照系统的部署~")
        print("\n")
        input = raw_input("请输入数字：1：开始配置；2.稍后配置；\n")
        if input == "1" :
            print("开始配置，接入配置代码")
        elif input == "2" :
            print("稍后配置，接入退出代码")
        else:
            print("无效的输入，接入退出代码")
