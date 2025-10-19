Originally created for the Major League Hacking Open Source Hackfest 2025, this tool is designed specifically for Python open source files. While researching ways to identify every single element in such a file, two ways stood out to me; the inspect module to isolate every line of source code as a string, and abstract syntax trees to identify every element or attribute of that string. With more time, I look forward into being able to both automate this as well as turn it into a localization tool for other languages. Additionally, I hope to be able to resolve issues such as expected function indentations that make it difficult for lines of code to be parsed before packaging this file. I learned quite a bit about the importance of nodes and children nodes, as well as the importance of randomness versus order, which are reflected in the usage of the ast.dump command rather than ast.walk. An additional challenge is making this accessible for users, as currently one would have to navigate to this link, download the program, and then manually make commands. Overall, this was a very illuminating project for me, although the lack of proper documentation on AST command usage was definitely an obstacle within the short period of time I had to implement it.


Resources used:

  https://docs.python.org/3/library/urllib.request.html
  
  https://docs.python.org/3/library/ast.html
  
  https://stackoverflow.com/questions/15197673/using-pythons-eval-vs-ast-literal-eval
  
  https://greentreesnakes.readthedocs.io/en/latest/
  
  https://docs.python.org/3/library/inspect.html#
  
  https://docs.python.org/3/library/functions.html#dir
