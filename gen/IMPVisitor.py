# Generated from .\source\IMP.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IMPParser import IMPParser
else:
    from IMPParser import IMPParser

# This class defines a complete generic visitor for a parse tree produced by IMPParser.

class IMPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IMPParser#progr.
    def visitProgr(self, ctx:IMPParser.ProgrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#series.
    def visitSeries(self, ctx:IMPParser.SeriesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#stmt.
    def visitStmt(self, ctx:IMPParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#assign_stmt.
    def visitAssign_stmt(self, ctx:IMPParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#cond_stmt.
    def visitCond_stmt(self, ctx:IMPParser.Cond_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#loop.
    def visitLoop(self, ctx:IMPParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#compar.
    def visitCompar(self, ctx:IMPParser.ComparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#expr.
    def visitExpr(self, ctx:IMPParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#term.
    def visitTerm(self, ctx:IMPParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#elem.
    def visitElem(self, ctx:IMPParser.ElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#logical_expr.
    def visitLogical_expr(self, ctx:IMPParser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#logical_term.
    def visitLogical_term(self, ctx:IMPParser.Logical_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IMPParser#logical_elem.
    def visitLogical_elem(self, ctx:IMPParser.Logical_elemContext):
        return self.visitChildren(ctx)



del IMPParser