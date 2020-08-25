#Linux or Unix or Mac
import os
print('Process (%s) start....' %os.getpid())
pid = 0 #pid = fork()
if pid == 0:
	print('I am child process (%s) and my parent is %s.' %(os.getpid(), os.getppid()))
else:
	print('I (%s) just created a child process (%s).' %(os.getpid(),pid))

#Process (876) start...
#I (876) just created a child process (877).
#I am child process (877) and my parent is 876.

#windows
from multiprocessing import Process
import os

def run_proc(name):
	print('Run child process %s (%s)' %(name, os.getpid()))

if __name__ =='__main__':
	print('Parent process %s.' %os.getpid())
	p = Process(target = run_proc, args=('test'))
	print('Child process will start.')
	p.start()
	p.join() #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
	print('Child process end.')

#Pool
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task %s (%s)...' %(name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %.2f seconds.' %(name, (end - start)))

print('Parent process %s.' % os.getpid())
p = Pool(4)
for i in range(5):
	p.apply_async
