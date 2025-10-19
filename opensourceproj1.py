import ast
import inspect
from urllib.request import url2pathname

class Proofread:
    def __init__(self, url):
        self.url = url
        pyc1 = list(self.url)[-2:]
        if str(pyc1) == '.py':
            self.pycheck = True
        else:
            self.pycheck = False

    def urlconvert(self):
        if self.pycheck is True:
            self.url = url2pathname(self.url, require_scheme=True)
        else:
            return ('Not Python file')
    
    def proofer(self):
        if self.pycheck is True:
            l = list(inspect.getsourcelines(self.url))
            lines = l[0]
            corrections = {ast.dump(ast.parse([i for i in lines])): ast.literal_eval(ast.parse([i for i in lines]))}
            for i in corrections.values():
                if i == set() or i == 'Error':
                    return lines.index(corrections.values[i])
        else:
            return ('Not Python file')
            

