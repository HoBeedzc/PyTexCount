import re


class Tex:
    '''
    '''
    def __init__(self, tex):
        self._tex = tex
        self._header, self._body, self._footer = self._extract_body()
        self._author = self._fetch_author()
        self._title = self._fetch_title()
        pass

    def __str__(self):
        return self._tex

    @property
    def tex(self):
        return self._tex

    @property
    def header(self):
        return self._header

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, new_body):
        self._body = new_body

    @property
    def footer(self):
        return self._footer

    @property
    def author(self):
        return self._author

    @property
    def title(self):
        return self._title

    @classmethod
    def open(cls, path, encoding='utf-8'):
        '''
        open a .tex file and reutrn a instance for class Tex.
        :param path: .tex file path
        :param encoding: Coding method of this .tex file
        :return: a instance for class Tex\n
        :sample: path = r'./sample.tex' encoding = 'utf-8'
        '''
        with open(path, 'r', encoding=encoding) as f:
            tex = f.read()
        return cls(tex)

    def _extract_body(self) -> str:
        begin_index = re.search(r'\\begin{document}', self.tex, flags=0).span()
        end_index = re.search(r'\\end{document}', self.tex, flags=0).span()
        header = self.tex[:begin_index[0]]
        body = self.tex[begin_index[0]:end_index[1]]
        footer = self.tex[end_index[1]:]
        return header, body, footer

    def _fetch_author(self):
        try:
            author = re.search(r'\\author{.*?}', self.header, flags=0).group(0)
            author = author[8:-1]
        except AttributeError:
            author = None
        return author

    def _fetch_title(self):
        try:
            title = re.search(r'\\title{.*?}', self.header, flags=0).group(0)
            title = title[7:-1]
        except AttributeError:
            title = None
        return title

    def show(self):
        '''
        Display .tex file contents
        '''
        print(self)

    def count(self):
        '''
        count charaters in the .tex file
        '''
        pass
