import re

def read_tex(file):
    # open a tex file
    # return a string and ignore characters before '\begin{document}'
    with open(file,'r',encoding = 'utf-8') as f:
        tex = f.read()
        index = re.search('begin{document}', tex, flags=0).span()
        return tex[index[1]:]

def count_(tex):
    # input a string which read_tex() return
    # return a int that the number of Chinese characters it includes
    nex_tex = ''
    for i in tex:
        if i in '!@#$%^&*(){}[]|\\;:",<.>/?\n-_=+；：’“，。？！（）【】、 ':
            pass
        elif i in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm':
            pass
        elif i.isdigit():
            pass
        else:
            nex_tex += i
    return len(nex_tex)

if __name__ == '__main__':
    file_name = ''
    print('count:')
    print(count_(read_tex(file_name)))
