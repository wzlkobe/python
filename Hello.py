#coding:GBK �ַ�����

import psutil

config_cpu_count = 4                      #cpu��������
config_virtual_memory_total = 8          #�ڴ棬GΪ��λ

msg = psutil.cpu_times()
print(msg)  #���cpu�Ļ�����Ϣ����bΪ��λ

cpu_count = psutil.cpu_count()
if cpu_count < config_cpu_count :
    print("���CPU����"+str(config_cpu_count)+"�ˣ����ʺϵ���֤��ϵͳ�Ĳ�����������ķ������� ")
    quit()
else:
    print("CPU����Ϊ" + str(cpu_count) + "�ˣ����ϵ���֤��ϵͳ�Ĳ���~")
    virtual_memory_total = psutil.virtual_memory().total
    virtual_memory_total /= 1024 * 1024 * 1024
    if (virtual_memory_total + 1) < config_virtual_memory_total :

        print("�ڴ�Ϊ����"+str(config_virtual_memory_total)+"G�������ϵ���֤��ϵͳ�Ĳ���~")
        quit()
    else :
        print("�ڴ�Ϊ" + str(virtual_memory_total + 1) + "G�����ϵ���֤��ϵͳ�Ĳ���~")
        print("\n")
        input = raw_input("���������֣�1����ʼ���ã�2.�Ժ����ã�\n")
        if input == "1" :
            print("��ʼ���ã��������ô���")
        elif input == "2" :
            print("�Ժ����ã������˳�����")
        else:
            print("��Ч�����룬�����˳�����")
