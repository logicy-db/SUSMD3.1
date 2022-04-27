from antlr4 import *
from gen.IMPLexer import IMPLexer
from gen.IMPParser import IMPParser
from source.CustomIMPVisitor import CustomIMPVisitor
from antlr4.tree.Trees import Trees
import nltk

def main(filename):
    input_stream = FileStream(filename)
    lexer = IMPLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = IMPParser(stream)
    tree = parser.progr()
    CustomIMPVisitor().visit(tree)

    """
    Drawing the tree (for debugging)
    """
    # treeString = Trees.toStringTree(tree, None, parser)
    # tree = nltk.Tree.fromstring(treeString)
    # tree.draw()

if __name__ == '__main__':
    main('source/input.txt')