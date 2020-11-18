from ..Tex import Tex
import re


class BodyProcess:
    '''
    '''
    def __init__(self, tex: Tex):
        self._tex = tex
        pass

    @property
    def body(self):
        return self._tex.body

    @body.setter
    def body(self, new_body):
        self._tex.body = new_body

    def _fetch_equation(self):
        pass

    def _fetch_fingure(self):
        pass

    def _fetch_table(self):
        pass

    def _remove_whitespace(self):
        self.body = self.body.replace('\t', ' ').replace('\n', ' ')
        pass

    def _remove_punctuation(self):
        self.body = re.sub(r'[,：:，、\$\(\)（）【】]', r' ', self.body)
        self.body = re.sub(r' +', r' ', self.body)
        pass


def body_process(self: Tex):
    '''
    '''
    bp = BodyProcess(self)
    bp._fetch_equation()
    bp._fetch_fingure()
    bp._fetch_table()
    bp._remove_whitespace()
    bp._remove_punctuation()
    pass


'''
待完成需求：
提取章节树 -> 生产json文件

'''
