from ..Tex import Tex


class HeaderProcess:
    '''
    '''
    def __init__(self, tex: Tex):
        self._tex = tex

    @property
    def header(self):
        return self._tex.header


'''
待完成需求：
提取使用到的第三方库 以及相关参数
'''
