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
    redoc = doc.replace('\t', '    ').replace('    ', '')
    return redoc


def split_command(body):
    # F
    #
    body_list = body.split()
    command = []
    character = []
    for i in body_list:
        ans = re.findall(r'\\+[a-zA-Z]*(?:\{?.*\}?\[?.*\]?|\[?.*\]?\{?.*\}?)',
                         i, re.I)
        if ans == []:
            character.append(i)
        else:
            command.append(i)
    return ' '.join(command), ' '.join(character)


def count_body_character(tex):
    # input a string which read_tex() return
    # return a int that the number of Chinese characters it includes
    tex = re.sub(r'[,：:，、\$\(\)（）【】]', r' ', tex)
    tex = re.sub(r'[\s]+', r' ', tex)
    sennum = 0
    chanum = 0
    chinum = 0
    engnum = 0
    dignum = 0
    flag = 0
    for i in range(len(tex)):
        if tex[i] == '.' or i == '。':
            flag = 0
            sennum += 1
        elif tex[i] in Alpha_string:
            if flag == 1:
                pass
            else:
                engnum += 1
                flag = 1
        elif tex[i] in Digit_string:
            if flag == 2:
                pass
            else:
                dignum += 1
                flag = 2
        elif tex[i] == ' ':
            flag = 0
        else:
            flag = 0
            chinum += 1
    chanum = chinum + dignum + engnum
    return chanum, sennum, chinum, engnum, dignum


def count_body_command(tex):
    pass


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
    command, character = split_command(body)
    print('count:', end=' ')
    print(count_body_character(character))
    print('used packages:', end=' ')
    print(count_packages(header))
    with open(r'testfile/content.txt', 'w') as f:
        for i in re.findall(
                r'\\+[a-zA-Z]*(?:\{^\s*?\}\[^\s*?\]|\[^\s*?\]\{^\s*?\}|\{^\s*?\})?',
                command, re.I):
            f.write(i)
            f.write('\n')
        a = re.sub(r'\\+[a-zA-Z]*(?:\{^\s*?\}\[^\s*?\]|\[^\s*?\]\{^\s*?\})?',
                   ' ', command)
        f.write(re.sub(r'\s+', ' ', a))


if __name__ == '__main__':
    argvs = sys.argv
    print(argvs)
    main()
