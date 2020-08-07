# About
'''
Author : Hobee
Date : 2020-08-07
Version : 1.0.0
contact me at : me@hobeedzc.cn
more info : https://github.com/HoBeedzc/PyTexCount
(c) copyright 1999-2020 Hobee. All rights reserved.
'''

# Third party libraries
import re
import sys

# global variables
Chinese_punctuation = '''  '''
English_punctuation = '''  '''
Alpha_string = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'''
Digit_string = '''1234567890'''
White_space = ''' \n\r\f\t\v'''


def read_tex(file):
    # open a tex file
    # return a string and ignore characters before '\begin{document}'
    with open(file, 'r', encoding='utf-8') as f:
        tex = f.read()
    return tex


def extract_body(tex):
    #
    #
    begin_index = re.search(r'\\begin{document}', tex, flags=0).span()
    end_index = re.search(r'\\end{document}', tex, flags=0).span()
    header = tex[:begin_index[0]]
    body = tex[begin_index[0]:end_index[1]]
    footer = tex[end_index[1]:]
    return header, body, footer


def remove_whitespace(doc):
    #
    #
    redoc = ''
    for i in doc:
        if i not in White_space or i == '\n':
            redoc += i
    return redoc


'''
def process_header(header):
    #
    # 
    return


def process_body(body):
    #
    # 去掉制表符和空格
    body = body.replace('\t','').replace(' ','')
    return body


def process_footer(footer):
    #
    #
    return
'''


def count_(tex):
    # input a string which read_tex() return
    # return a int that the number of Chinese characters it includes
    nex_tex = ''
    '''
    for i in tex:
        if i in '!@#$%^&*(){}[]|\\;:",<.>/?\n-_=+；：’“，。？！（）【】、 \t':
            pass
        elif i in Alpha_string:
            pass
        elif i in Digit_string:
            pass
        else:
            nex_tex += i
    '''
    f = open(r'testfile/content.txt', 'w')
    for i in tex:
        f.write(i)
        # f.write('\n')
    f.close()
    return len(nex_tex)


def count_packages(tex_pre):
    #
    #
    packages = []
    n = 0
    used_packages = re.findall(r'\\usepackage\[*.*\]*{.*}', tex_pre)
    for i in used_packages:
        packages.append(re.findall(r'{.*}', i)[0][1:-1])
        n += 1
    return packages, n


def main():
    # file_name = input('Enter a tex file path...')
    file_name = r'testfile/paper.tex'
    tex = read_tex(file_name)
    header, body, footer = extract_body(tex)
    header, body, footer = map(remove_whitespace, [header, body, footer])
    print('count:', end=' ')
    print(count_(body))
    print('used packages:', end=' ')
    print(count_packages(header))


if __name__ == '__main__':
    argvs = sys.argv
    print(argvs)
    main()
