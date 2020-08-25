import re
import optparse
import os

def Main():
    parser = optparse.OptionParser("usage %prog -w <word> -f <file>")
    parser.add_option('-w', dest='word', type='string', help='specify a world to search for')
    parser.add_option('-f', dest='fname', type='string', help='specify a file to search')
    options, args = parser.parse_args()
    if (options.word == None) |(options.fname == None):
        print parser.usage
        exit(0)
    else:
        word = options.word
        fname = options.fname

    if os.path.isdir(fname):
        f_walk(fname, word)
        os.path.walk()
    else:
        lookup_file(fname, word)

def f_walk(top, word):
    try:
        names = os.listdir(top)
    except os.error:
        return

    for name in names:
        name = os.path.join(top, name)
        if os.path.isdir(name):
            f_walk(name, word)
        else:
            lookup_file(name, word)


def lookup_file(file_name, word):
    search_file = open(file_name)
    line_num = 0

    for line in search_file.readlines():
        line = line.strip('\n\r')
        line_num += 1
        search_result = re.search(word, line, re.M | re.I)
        if search_result:
            print  file_name + ' ' + str(line_num) + ':' + line

if __name__ == '__main__':
    Main()