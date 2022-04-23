# Generated from .\source\IMP.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IMPParser import IMPParser
else:
    from IMPParser import IMPParser

# This class defines a complete listener for a parse tree produced by IMPParser.
class IMPListener(ParseTreeListener):

    # Enter a parse tree produced by IMPParser#progr.
    def enterProgr(self, ctx:IMPParser.ProgrContext):
        pass

    # Exit a parse tree produced by IMPParser#progr.
    def exitProgr(self, ctx:IMPParser.ProgrContext):
        pass


    # Enter a parse tree produced by IMPParser#series.
    def enterSeries(self, ctx:IMPParser.SeriesContext):
        pass

    # Exit a parse tree produced by IMPParser#series.
    def exitSeries(self, ctx:IMPParser.SeriesContext):
        pass


    # Enter a parse tree produced by IMPParser#stmt.
    def enterStmt(self, ctx:IMPParser.StmtContext):
        pass

    # Exit a parse tree produced by IMPParser#stmt.
    def exitStmt(self, ctx:IMPParser.StmtContext):
        pass


    # Enter a parse tree produced by IMPParser#assign_stmt.
    def enterAssign_stmt(self, ctx:IMPParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by IMPParser#assign_stmt.
    def exitAssign_stmt(self, ctx:IMPParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by IMPParser#cond_stmt.
    def enterCond_stmt(self, ctx:IMPParser.Cond_stmtContext):
        pass

    # Exit a parse tree produced by IMPParser#cond_stmt.
    def exitCond_stmt(self, ctx:IMPParser.Cond_stmtContext):
        pass


    # Enter a parse tree produced by IMPParser#loop.
    def enterLoop(self, ctx:IMPParser.LoopContext):
        pass

    # Exit a parse tree produced by IMPParser#loop.
    def exitLoop(self, ctx:IMPParser.LoopContext):
        pass


    # Enter a parse tree produced by IMPParser#compar.
    def enterCompar(self, ctx:IMPParser.ComparContext):
        pass

    # Exit a parse tree produced by IMPParser#compar.
    def exitCompar(self, ctx:IMPParser.ComparContext):
        pass


    # Enter a parse tree produced by IMPParser#expr.
    def enterExpr(self, ctx:IMPParser.ExprContext):
        pass

    # Exit a parse tree produced by IMPParser#expr.
    def exitExpr(self, ctx:IMPParser.ExprContext):
        pass


    # Enter a parse tree produced by IMPParser#term.
    def enterTerm(self, ctx:IMPParser.TermContext):
        pass

    # Exit a parse tree produced by IMPParser#term.
    def exitTerm(self, ctx:IMPParser.TermContext):
        pass


    # Enter a parse tree produced by IMPParser#elem.
    def enterElem(self, ctx:IMPParser.ElemContext):
        pass

    # Exit a parse tree produced by IMPParser#elem.
    def exitElem(self, ctx:IMPParser.ElemContext):
        pass


    # Enter a parse tree produced by IMPParser#logical_expr.
    def enterLogical_expr(self, ctx:IMPParser.Logical_exprContext):
        pass

    # Exit a parse tree produced by IMPParser#logical_expr.
    def exitLogical_expr(self, ctx:IMPParser.Logical_exprContext):
        pass


    # Enter a parse tree produced by IMPParser#logical_term.
    def enterLogical_term(self, ctx:IMPParser.Logical_termContext):
        pass

    # Exit a parse tree produced by IMPParser#logical_term.
    def exitLogical_term(self, ctx:IMPParser.Logical_termContext):
        pass


    # Enter a parse tree produced by IMPParser#logical_elem.
    def enterLogical_elem(self, ctx:IMPParser.Logical_elemContext):
        pass

    # Exit a parse tree produced by IMPParser#logical_elem.
    def exitLogical_elem(self, ctx:IMPParser.Logical_elemContext):
        pass



del IMPParser