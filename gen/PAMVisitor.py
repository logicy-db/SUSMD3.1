# Generated from .\source\PAM.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PAMParser import PAMParser
else:
    from PAMParser import PAMParser

# This class defines a complete generic visitor for a parse tree produced by PAMParser.

class PAMVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PAMParser#progr.
    def visitProgr(self, ctx:PAMParser.ProgrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PAMParser#series.
    def visitSeries(self, ctx:PAMParser.SeriesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PAMParser#stmt.
    def visitStmt(self, ctx:PAMParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PAMParser#input_stmt.
    def visitInput_stmt(self, ctx:PAMParser.Input_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PAMParser#output_stmt.
    def visitOutput_stmt(self, ctx:PAMParser.Output_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PAMParser#assign_stmt.
    def visitAssign_stmt(self, ctx:PAMParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PAMParser#cond_stmt.
    def visitCond_stmt(self, ctx:PAMParser.Cond_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PAMParser#loop.
    def visitLoop(self, ctx:PAMParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PAMParser#compar.
    def visitCompar(self, ctx:PAMParser.ComparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PAMParser#varlist.
    def visitVarlist(self, ctx:PAMParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PAMParser#expr.
    def visitExpr(self, ctx:PAMParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PAMParser#term.
    def visitTerm(self, ctx:PAMParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PAMParser#elem.
    def visitElem(self, ctx:PAMParser.ElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PAMParser#logical_expr.
    def visitLogical_expr(self, ctx:PAMParser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PAMParser#logical_term.
    def visitLogical_term(self, ctx:PAMParser.Logical_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PAMParser#logical_elem.
    def visitLogical_elem(self, ctx:PAMParser.Logical_elemContext):
        return self.visitChildren(ctx)



del PAMParser