import matplotlib.pyplot as plt
import re


class EquationNotFoundError(ValueError):
    pass


class Equation:
    '''
    '''
    def __init__(self, oritext):
        self._oritext = oritext
        self._fetch_equation()
        pass

    def __str__(self):
        return self.matheq

    @property
    def oritext(self):
        return self._oritext

    @property
    def matheq(self):
        return self._matheq

    @classmethod
    def analysis(cls, equation: str):
        '''
        Analysis a equation and return a instence for class Equation
        :param equation: a str in .tex file like '\\begin{equation}...\\end{equation}'
        :return: a instance for class Equation.\n
        '''
        return cls(equation)

    def _fetch_equation(self):
        try:
            start_index = re.search(r'\\begin{equation}',
                                    self.oritext,
                                    flags=0).span()
        except AttributeError:
            raise EquationNotFoundError(
                r'can not found \begin{equation} in this str.')
        try:
            end_index = re.search(r'\\end{equation}', self.oritext,
                                  flags=0).span()
        except AttributeError:
            raise EquationNotFoundError(
                r'can not found \end{equation} in this str.')
        temp = self.oritext[start_index[1]:end_index[0]].strip()
        self._matheq = '$' + temp + '$'
        pass

    def show(self):
        '''
        show equation in LaTex code
        '''
        print(self)
        pass

    def displaymath(self):
        '''
        show equation in figure with Mathjax and matplotlib.pyplot
        '''
        ax = plt.subplot(111)
        ax.text(0, 0.5, self.matheq, fontsize=15, color="red")
        plt.axis('off')
        plt.show()
        pass


class Equations:
    '''
    '''
    def __init__(self):
        pass


teststr = r''' 
\end{enumerate}
\begin{equation}
    D = 2R \arcsin(\sqrt{\sin^2(\frac{\varphi_2-\varphi_1}{2})+\cos(\varphi_1)\cos(\varphi_2)\sin^2(\frac{\lambda_2-\lambda_1}{2})})
\end{equation}
123
'''

if __name__ == '__main__':
    a = Equation.analysis(teststr)
    a.show()
    a.displaymath()
