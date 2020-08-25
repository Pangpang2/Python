from multiprocessing import Process
from multiprocessing import Pool
import os,time,random

def run_proc(name):
	print('Run child process %s (%s)' % (name, os.getpid()))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target = run_proc, args =('test',))
	print('Child process will start')
	p.start()
	p.join() #等待子进程结束后再继续往下运行，通常用于进程间的同步
	print('Child process end')

#Pool
#请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制
def long_time_task(name):
	print('Run task %s (%s)' %(name,os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %.2f seconds.' %(name, (end - start)))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args =(i,))
	print('Waiting for all subprocesses done')
	p.close() #调用close()之后就不能继续添加新的Process
	p.join()
	print("All subprocesses done.")

#subprocess
import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code', r)

a = 'abcdefg'
print(a[::-1])
