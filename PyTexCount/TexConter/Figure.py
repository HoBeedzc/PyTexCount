import matplotlib.pyplot as plt
import re


class FigureNotFoundError(ValueError):
    pass


class Figure:
    '''
    '''
    def __init__(self, oritext):
        self._oritext = oritext
        pass

    @classmethod
    def analysis(cls, figure: str):
        '''
        Analysis a figure and return a instence for class Figure
        :param equation: a str in .tex file like '\\begin{Figure}...\\end{Figure}'
        :return: a instance for class Figure.\n
        '''
        return cls(figure)

    def _fetch_figure(self):
        try:
            start_index = re.search(r'\\begin{figure}', self.oritext,
                                    flags=0).span()
        except AttributeError:
            raise FigureNotFoundError(
                r'can not found \begin{figure} in this str.')
        try:
            end_index = re.search(r'\\end{figure}', self.oritext,
                                  flags=0).span()
        except AttributeError:
            raise FigureNotFoundError(
                r'can not found \end{figure} in this str.')
        temp = self.oritext[start_index[1]:end_index[0]].strip()
        pass
