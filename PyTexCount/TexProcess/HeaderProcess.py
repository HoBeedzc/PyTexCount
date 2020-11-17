from ..Tex import Tex

class HeaderProcess:
    '''
    '''
    def __init__(self,tex:Tex):
        self._tex = tex

    @property
    def header(self):
        return self._tex.header
