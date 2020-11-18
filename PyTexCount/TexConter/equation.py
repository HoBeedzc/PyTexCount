import matplotlib.pyplot as plt


class Equation:
    '''
    '''
    def __init__(self, oritext):
        pass

    @classmethod
    def analysis(cls, equation: str) -> Equation:
        '''
        Analysis a equation and return a instence for class Equation
        :param equation: a str in .tex file like '\\begin{equation}...\\end{equation}'
        :return: a instance for class Equation.\n
        '''
        return cls(equation)
    
    def _fetch_equation(self):
        pass

    def display(self):
        pass


class Equations:
    '''
    '''
    def __init__(self):
        pass
