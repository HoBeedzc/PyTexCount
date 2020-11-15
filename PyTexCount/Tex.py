class Tex:
    '''
    '''
    def __init__(self, tex):
        self._tex = tex
        pass

    @classmethod
    def open(cls, path, encoding='utf-8'):
        '''
        open a .tex file and reutrn a instance for class Tex.
        :param path: .tex file path
        :param encoding: Coding method of this .tex file
        :return: None\n
        :sample: path = r'./sample.tex' encoding = 'utf-8'
        '''
        with open(path, 'r', encoding=encoding) as f:
            tex = f.read()
        return cls(tex)

    def show(self):
        '''
        Display .tex file contents
        '''
        print(self)

    def __str__(self):
        return self._tex
