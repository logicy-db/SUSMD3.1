# Generated from .\source\IMP.g4 by ANTLR 4.9.2
from antlr4 import *
from gen.IMPParser import IMPParser
from gen.IMPVisitor import IMPVisitor
from antlr4.tree.Tree import TerminalNode
import operator


# Visitor for IMP language.
class CustomVisitor(IMPVisitor):
    variables = {}  # Storing the variable values
    data_values = []  # Storing data.txt values
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '<>': operator.ne,
        '=<': operator.le,
        '>=': operator.ge,
        '=': operator.eq,
        '<': operator.lt,
        '>': operator.gt,
        'NOT': operator.not_,
    }

    def __init__(self):
        # Reading data.txt on initializing
        read_data = open('source/data.txt', 'r').read()
        if read_data != '': 
            read_data = read_data.split(',')
            for val in read_data:
                self.data_values.append(int(val))

    # Visit a parse tree produced by IMPParser#input_stmt.
    def visitInput_stmt(self, ctx: IMPParser.Input_stmtContext):
        # input_stmt: 'read' varlist;
        varlist = self.visitChildren(ctx)  # visitVarlist

        for var in varlist:
            self.variables[var] = int(self.data_values[0])
            self.data_values.pop(0)

    # Visit a parse tree produced by IMPParser#output_stmt.
    def visitOutput_stmt(self, ctx: IMPParser.Output_stmtContext):
        varlist = self.visitChildren(ctx)

        for var in varlist:
            print(var + ": " + str(self.variables.get(var)))

    # Visit a parse tree produced by IMPParser#assign_stmt.
    def visitAssign_stmt(self, ctx: IMPParser.Assign_stmtContext):
        # assign_stmt : VARNAME ':=' (logical_expr|expr);
        self.variables[str(ctx.getChild(0))] = self.visit(ctx.getChild(2))

    # Visit a parse tree produced by IMPParser#cond_stmt.
    def visitCond_stmt(self, ctx: IMPParser.Cond_stmtContext):
        # cond_stmt : 'if' (logical_expr) 'then' series ('else' series)? 'fi';
        exeCond = self.visit(ctx.getChild(1))

        if exeCond:
            # if true do series
            return self.visit(ctx.getChild(3))
        else:
            if ctx.getChild(5) != None:
                return self.visit(ctx.getChild(5))

    # Visit a parse tree produced by IMPParser#loop.
    def visitLoop(self, ctx: IMPParser.LoopContext):
        # loop : 'while' (logical_expr) 'do' series 'end';
        while self.visit(ctx.getChild(1)):
            self.visit(ctx.getChild(3))

    # Visit a parse tree produced by IMPParser#compar.
    def visitCompar(self, ctx: IMPParser.ComparContext):
        # compar : expr RELATION expr;
        elem1 = self.visit(ctx.getChild(0))
        elem2 = self.visit(ctx.getChild(2))

        return self.ops[str(ctx.getChild(1))](elem1, elem2)

    # Visit a parse tree produced by IMPParser#expr.
    def visitExpr(self, ctx: IMPParser.ExprContext):
        # expr : term (WEAKOP term)*;
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)

        elem1 = self.visit(ctx.getChild(0))
        elem2 = self.visit(ctx.getChild(2))

        return round(self.ops[str(ctx.getChild(1))](elem1, elem2))

    # Visit a parse tree produced by IMPParser#term.
    def visitTerm(self, ctx: IMPParser.TermContext):
        # term : elem (STRONGOP elem)*;
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)

        elem1 = self.visit(ctx.getChild(0))
        elem2 = self.visit(ctx.getChild(2))

        return round(self.ops[str(ctx.getChild(1))](elem1, elem2))

    # Visit a parse tree produced by IMPParser#elem.
    def visitElem(self, ctx: IMPParser.ElemContext):
        # elem : NUMBER | VARNAME | '(' expr ')';
        if ctx.getChildCount() != 1:
            # if contains parenthesis
            return self.visit(ctx.getChild(1))  # visitExpr

        elem = str(ctx.getChild(0))

        if elem.isnumeric():
            return int(elem)

        return self.variables.get(elem)

    # Visit a parse tree produced by IMPParser#logical_expr.
    def visitLogical_expr(self, ctx: IMPParser.Logical_exprContext):
        # logical_expr :  logical_term (WEAKBOOL logical_term)*;
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)

        elem1 = self.visit(ctx.getChild(0))
        elem2 = self.visit(ctx.getChild(2))

        return elem1 or elem2

    # Visit a parse tree produced by IMPParser#logical_term.
    def visitLogical_term(self, ctx: IMPParser.Logical_termContext):
        # logical_term : logical_elem (STRONGBOOL logical_elem)*;
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)

        elem1 = self.visit(ctx.getChild(0))
        elem2 = self.visit(ctx.getChild(2))

        return elem1 and elem2

    # Visit a parse tree produced by IMPParser#logical_elem.
    def visitLogical_elem(self, ctx: IMPParser.Logical_elemContext):
        # logical_elem : (NEG)*? (compar|BOOL|VARNAME|'(' logical_expr ')');
        # NOT

        if str(ctx.getChild(0)) == 'NOT':
            notCounter = 0
            for i in range(0, ctx.getChildCount()):
                if str(ctx.getChild(i)) != 'NOT':
                    break
                else:
                    notCounter += 1

            if str(ctx.getChild(notCounter)) == '(': # next element after latest NOT
                # NOT with parenthesis
                elemPos = notCounter+1
            else:
                elemPos = notCounter

            if isinstance(ctx.getChild(elemPos), TerminalNode):
                # NOT terminal
                elem = str(ctx.getChild(elemPos))

                try:
                # Converting strings to True and False
                    if eval(elem) in (True, False):
                        return eval(elem) if notCounter % 2 == 0 else self.ops['NOT'](eval(elem))
                except:
                    # exception when trying convert VARNAMEs with eval()
                    # just continue to get value
                    pass

                # Returning variable
                return self.variables.get(elem) if notCounter % 2 == 0 else self.ops['NOT'](self.variables.get(elem))
            else:
                # NOT node
                return self.visit(ctx.getChild(elemPos)) if notCounter % 2 == 0 else self.ops['NOT'](self.visit(ctx.getChild(elemPos)))  # visitLogicalExpr

        # Parenthesis
        if str(ctx.getChild(0)) == '(':
            # (logical_expr)
            return self.visit(ctx.getChild(1))

        if not isinstance(ctx.getChild(0), TerminalNode):
            # compar handling
            elem = str(self.visitChildren(ctx))
        else:
            # Processing the single value that is BOOL, VARNAME
            elem = str(ctx.getChild(0))

        try:
            # Converting strings to True and False.
            if eval(elem) in (True, False):
                return eval(elem)
        except:
            # exception when trying convert VARNAMEs with eval()
            # just continue to get value
            pass

        # Getting the value of variable
        return self.variables.get(elem)


del IMPParser
