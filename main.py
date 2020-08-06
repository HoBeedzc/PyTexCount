# About

# Third party libraries
import re

# global variables
Chinese_punctuation = '''  '''
English_punctuation = '''  '''
Alpha_string = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'''
Digit_string = '''1234567890'''


def read_tex(file):
    # open a tex file
    # return a string and ignore characters before '\begin{document}'
    with open(file, 'r', encoding='utf-8') as f:
        tex = f.read()
        index = re.search('begin{document}', tex, flags=0).span()
        return tex[:index[1]], tex[index[1]:]


def count_(tex):
    # input a string which read_tex() return
    # return a int that the number of Chinese characters it includes
    nex_tex = ''
    for i in tex:
        if i in '!@#$%^&*(){}[]|\\;:",<.>/?\n-_=+；：’“，。？！（）【】、 ':
            pass
        elif i in Alpha_string:
            pass
        elif i in Digit_string:
            pass
        else:
            nex_tex += i
    return len(nex_tex)


def count_packages(tex_pre):
    #
    #
    packages = []
    n = 0
    used_packages = re.findall('usepackage{[\S]*}', pre_tex)
    for i in used_packages:
        packages.append(i[11:-1])
        n += 1
    return packages, n


if __name__ == '__main__':
    file_name = input('Enter a tex file path...')
    pre_tex, tex = read_tex(file_name)
    print('count:', end=' ')
    print(count_(tex))
    print('used_packages:', end='')
    print(count_packages(pre_tex))
