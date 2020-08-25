import threading
import time

tlock = threading.Lock()

def timer(name, delay, repeat):
    print 'Timer: ' + name + ' Started'
    tlock.acquire()
    print name + " has acquired the lock"
    while repeat > 0:
        time.sleep(delay)
        print name + ':' + str(time.ctime(time.time()))
        repeat -= 1
    print name + " is releasing the lock"
    tlock.release()
    print 'Timer: ' + name + ' Completed'

def Main():
    t1 = threading.Thread(target=timer, args=('Time1', 1, 5))
    t2 = threading.Thread(target=timer, args=('Time2', 2, 5))
    t1.start()
    t2.start()

    print "Main Complete"

# class AsyncWrite(Thread):
#     def __init__(self, text, out):
#         Thread.__init__(self)
#         self.text = text
#         self.out = out
#
#     def run(self):
#         f = open(self.out, 'a')
#         f.write(self.text + '\n')
#         f.close()
#         time.sleep(2)
#         print "Finished Background file write to " + self.out
#
# def Main():
#     message = raw_input("Enter a string to store:")
#     background = AsyncWrite(message, 'out.txt')
#     background.start()
#     print "The program can continue to run while it write in another thread"
#     print 100+400
#
#     background.join()
#     print "Waited until thread was complete"

if __name__ == '__main__':
    Main()