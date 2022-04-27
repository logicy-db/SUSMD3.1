# Generated from .\source\IMP.g4 by ANTLR 4.9.2
from antlr4 import *
from gen.IMPVisitor import IMPVisitor
from antlr4.tree.Tree import TerminalNode
from gen.IMPParser import IMPParser

# This class defines a complete generic visitor for a parse tree produced by IMPParser.

class CustomIMPVisitor(ParseTreeVisitor):
    AM_CODE = []
    ops = {
        '+': 'ADD',
        '-': 'SUB',
        '*': 'MULT',
        '/': 'DIV',
        '<>': ['EQ', 'NEG'],
        '=<': 'LE',
        '>=': ['LE', 'NEG', 'EQ', 'OR'],
        '=': 'EQ',
        '<': ['EQ', 'NEG', 'LE', 'AND'],
        '>': ['LE', 'NEG'],
    }

    # Get AM command
    def createCommand(self, elem1, elem2, operator):
        operator = str(operator)

        if operator in ['>=', '<']:
            return ' : '.join([
                elem1,
                elem2,
                self.ops[operator][0],
                self.ops[operator][1],
                elem1,
                elem2,
                self.ops[operator][2],
                self.ops[operator][3]
            ])

        if operator in ['<>', '>']:
            return ' : '.join([
                elem1,
                elem2,
                self.ops[operator][0],
                self.ops[operator][1]
            ])

        return ' : '.join([
            elem1,
            elem2,
            self.ops[operator]
        ])

    # Get appropriate PUSH or FETCH command based on the terminal
    def pushFetchBool(self, elem):
        elem = str(elem)
        if elem in ('false', 'true'):
            return eval(elem.capitalize())
        return "PUSH(%s)" % elem if elem.isnumeric() else "FETCH(%s)" % elem

    # Visit a parse tree produced by IMPParser#progr.
    def visitProgr(self, ctx: IMPParser.ProgrContext):
        self.visitChildren(ctx)
        print(' '.join(self.AM_CODE))

    # Visit a parse tree produced by IMPParser#series.
    def visitSeries(self, ctx: IMPParser.SeriesContext):
        from gen.IMPParser import IMPParser

        program = []
        for i in range(ctx.getChildCount()):
            if not isinstance(ctx.getChild(i), TerminalNode):
                program.append(self.visit(ctx.getChild(i)))
            else:
                program.append(str(ctx.getChild(i)))

        program = ' '.join(program)
        if isinstance(ctx.parentCtx, IMPParser.ProgrContext):
            self.AM_CODE.append(program)

        return program

    # Visit a parse tree produced by IMPParser#stmt.
    def visitStmt(self, ctx: IMPParser.StmtContext):
        if isinstance(ctx.getChild(0), TerminalNode):
            return str(ctx.getChild(0))

        return self.visitChildren(ctx)

    # Visit a parse tree produced by IMPParser#assign_stmt.
    def visitAssign_stmt(self, ctx: IMPParser.Assign_stmtContext):
        return "%s : STORE(%s)" % (
            self.visit(ctx.getChild(2)),
            ctx.getChild(0),
        )

    # Visit a parse tree produced by IMPParser#cond_stmt.
    def visitCond_stmt(self, ctx: IMPParser.Cond_stmtContext):
        # cond_stmt : 'if' (logical_expr) 'then' series ('else' series)? 'fi';
        return "%s : BRANCH(%s, %s)" % (
            self.visit(ctx.getChild(1)),
            self.visit(ctx.getChild(3)),
            self.visit(ctx.getChild(5))
        )

    # Visit a parse tree produced by IMPParser#loop.
    def visitLoop(self, ctx: IMPParser.LoopContext):
        return "LOOP (%s, %s)" % (
            self.visit(ctx.getChild(1)),
            self.visit(ctx.getChild(3)),
        )

    # Visit a parse tree produced by IMPParser#compar.
    def visitCompar(self, ctx: IMPParser.ComparContext):
        return self.createCommand(
            self.visit(ctx.getChild(0)),
            self.visit(ctx.getChild(2)),
            ctx.getChild(1)
        )

    # Visit a parse tree produced by IMPParser#expr.
    def visitExpr(self, ctx: IMPParser.ExprContext):
        if ctx.getChildCount() == 3:
            return self.createCommand(
                self.visit(ctx.getChild(0)),
                self.visit(ctx.getChild(2)),
                ctx.getChild(1)
            )

        return self.visitChildren(ctx)

    # Visit a parse tree produced by IMPParser#term.
    def visitTerm(self, ctx: IMPParser.TermContext):
        if ctx.getChildCount() == 3:
            return self.createCommand(
                self.visit(ctx.getChild(0)),
                self.visit(ctx.getChild(2)),
                ctx.getChild(1)
            )

        return self.visitChildren(ctx)

    # Visit a parse tree produced by IMPParser#elem.
    def visitElem(self, ctx: IMPParser.ElemContext):
        if ctx.getChildCount() != 1:
            # if contains parenthesis
            return self.visit(ctx.getChild(1))  # visitExpr

        return self.pushFetchBool(ctx.getChild(0))

    # Visit a parse tree produced by IMPParser#logical_expr.
    def visitLogical_expr(self, ctx: IMPParser.Logical_exprContext):
        if ctx.getChildCount() == 3:
            return self.createCommand(
                self.visit(ctx.getChild(0)),
                self.visit(ctx.getChild(2)),
                ctx.getChild(1)
            )

        return self.visitChildren(ctx)

    # Visit a parse tree produced by IMPParser#logical_term.
    def visitLogical_term(self, ctx: IMPParser.Logical_termContext):
        if ctx.getChildCount() == 3:
            return self.createCommand(
                self.visit(ctx.getChild(0)),
                self.visit(ctx.getChild(2)),
                ctx.getChild(1)
            )

        return self.visitChildren(ctx)

    # Visit a parse tree produced by IMPParser#logical_elem.
    def visitLogical_elem(self, ctx: IMPParser.Logical_elemContext):
        if str(ctx.getChild(0)) == 'NOT':
            return "%s : NOT" % self.visitChildren(ctx)

        # Parenthesis
        if str(ctx.getChild(0)) == '(':
            # (logical_expr)
            return "(%s)" % self.visitChildren(ctx)

        if not isinstance(ctx.getChild(0), TerminalNode):
            # compar handling
            elem = self.visitChildren(ctx)
        else:
            # Processing the single value that is BOOL, VARNAME
            elem = self.pushFetchBool(ctx.getChild(0))

        return elem


del IMPParser
