#coding:utf-8
import os
import subprocess
import time
from ReplaceVariables import Config
class ST():
    def allrun(self):
        masterIP = '123.207.121.251'
        txt_name = time.strftime("%Y%m%d_%H%M%S")
        file_list = os.listdir(__dir__)
        jmx = []
        for i in file_list:
            if '.jmx' in i:
                jmx.append(i)
        with open(__dir__+'/result_'+txt_name+'.txt','w+') as f:
            for filename in jmx:
                print filename
                c = subprocess.Popen('scp %s/%s root@123.207.63.182:/data/jmetertest/jmetertest/jmx/' % (__dir__,filename),shell=True).wait()
                a = os.popen("ssh -t -t root@%s docker ps -a | grep jmeter-master | awk '{ print $1 }'"%masterIP).read()
                a = a.strip()
                #subprocess.Popen('ssh -t -t root@123.207.121.251 docker exec -it %s /bin/sh ./jmeter/jmetertest.sh %s' % (a,filename),shell=True).wait()
                v=os.popen('ssh -t -t root@%s docker exec -it %s /bin/sh ./jmeter/jmetertest.sh %s' % (masterIP,a,filename)).readlines()
                for i in v:
                    if 'Start JMeter Test' in i:
                        f.write(i.split(' ')[3]+'\n')
                    if "summary =" in i:
                        f.write(i)
                time.sleep(1)
                f.write('\n')
                print filename+'：已完成'
                print '-------------------'

    def mkdir(self,num):
        if os.path.exists('C:\Users\Administrator\Desktop\jmeter%d' % num):
            print u'已经存在'
            exit()
        else:
            os.makedirs('C:\Users\Administrator\Desktop\jmeter%d' % num)

    def change(self,num,Iteration,jmx):
        patt = re.compile(r"\>(.*?)\<", re.M)
        for filename in jmx:
            r_file = open(__dir__ + '\\basescript\jmeter\%s' % filename, 'r')
            w_file = open(__dir__ + '\\newscript\jmeter%s\%s' % (num, filename), 'w')
            b = r_file.readlines()
            c = []
            for i in range(len(b)):
                if '<stringProp name="ThreadGroup.num_threads">' in b[i]:
                    new = b[i].replace(patt.findall(b[i])[0], num)
                    c.append(new)
                    continue
                if '<stringProp name="LoopController.loops">' in b[i]:
                    new = b[i].replace(patt.findall(b[i])[0], Iteration)
                    c.append(new)
                    continue
                c.append(b[i])
            for i in c:
                w_file.write(i)
            r_file.close()
            w_file.close()


if __name__ =="__main__":
    st = ST()
    num = 800
    Iteration = '20'
    mkdir(num)
    file_list = os.listdir('C:\Users\Administrator\Desktop\jmeter')
    jmx = []
    for i in file_list:
        if '.jmx' in i:
            jmx.append(i)

    change(num,Iteration,jmx)