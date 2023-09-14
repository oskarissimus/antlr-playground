# Generated from antlr_playground/grammar/bds.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .bdsParser import bdsParser
else:
    from bdsParser import bdsParser

# This class defines a complete listener for a parse tree produced by bdsParser.
class bdsListener(ParseTreeListener):

    # Enter a parse tree produced by bdsParser#programUnit.
    def enterProgramUnit(self, ctx:bdsParser.ProgramUnitContext):
        pass

    # Exit a parse tree produced by bdsParser#programUnit.
    def exitProgramUnit(self, ctx:bdsParser.ProgramUnitContext):
        pass


    # Enter a parse tree produced by bdsParser#eol.
    def enterEol(self, ctx:bdsParser.EolContext):
        pass

    # Exit a parse tree produced by bdsParser#eol.
    def exitEol(self, ctx:bdsParser.EolContext):
        pass


    # Enter a parse tree produced by bdsParser#includeFile.
    def enterIncludeFile(self, ctx:bdsParser.IncludeFileContext):
        pass

    # Exit a parse tree produced by bdsParser#includeFile.
    def exitIncludeFile(self, ctx:bdsParser.IncludeFileContext):
        pass


    # Enter a parse tree produced by bdsParser#typeList.
    def enterTypeList(self, ctx:bdsParser.TypeListContext):
        pass

    # Exit a parse tree produced by bdsParser#typeList.
    def exitTypeList(self, ctx:bdsParser.TypeListContext):
        pass


    # Enter a parse tree produced by bdsParser#type.
    def enterType(self, ctx:bdsParser.TypeContext):
        pass

    # Exit a parse tree produced by bdsParser#type.
    def exitType(self, ctx:bdsParser.TypeContext):
        pass


    # Enter a parse tree produced by bdsParser#varDeclaration.
    def enterVarDeclaration(self, ctx:bdsParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by bdsParser#varDeclaration.
    def exitVarDeclaration(self, ctx:bdsParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by bdsParser#variableInit.
    def enterVariableInit(self, ctx:bdsParser.VariableInitContext):
        pass

    # Exit a parse tree produced by bdsParser#variableInit.
    def exitVariableInit(self, ctx:bdsParser.VariableInitContext):
        pass


    # Enter a parse tree produced by bdsParser#variableInitImplicit.
    def enterVariableInitImplicit(self, ctx:bdsParser.VariableInitImplicitContext):
        pass

    # Exit a parse tree produced by bdsParser#variableInitImplicit.
    def exitVariableInitImplicit(self, ctx:bdsParser.VariableInitImplicitContext):
        pass


    # Enter a parse tree produced by bdsParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:bdsParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by bdsParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:bdsParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by bdsParser#field.
    def enterField(self, ctx:bdsParser.FieldContext):
        pass

    # Exit a parse tree produced by bdsParser#field.
    def exitField(self, ctx:bdsParser.FieldContext):
        pass


    # Enter a parse tree produced by bdsParser#classDef.
    def enterClassDef(self, ctx:bdsParser.ClassDefContext):
        pass

    # Exit a parse tree produced by bdsParser#classDef.
    def exitClassDef(self, ctx:bdsParser.ClassDefContext):
        pass


    # Enter a parse tree produced by bdsParser#statement.
    def enterStatement(self, ctx:bdsParser.StatementContext):
        pass

    # Exit a parse tree produced by bdsParser#statement.
    def exitStatement(self, ctx:bdsParser.StatementContext):
        pass


    # Enter a parse tree produced by bdsParser#forInit.
    def enterForInit(self, ctx:bdsParser.ForInitContext):
        pass

    # Exit a parse tree produced by bdsParser#forInit.
    def exitForInit(self, ctx:bdsParser.ForInitContext):
        pass


    # Enter a parse tree produced by bdsParser#forCondition.
    def enterForCondition(self, ctx:bdsParser.ForConditionContext):
        pass

    # Exit a parse tree produced by bdsParser#forCondition.
    def exitForCondition(self, ctx:bdsParser.ForConditionContext):
        pass


    # Enter a parse tree produced by bdsParser#forEnd.
    def enterForEnd(self, ctx:bdsParser.ForEndContext):
        pass

    # Exit a parse tree produced by bdsParser#forEnd.
    def exitForEnd(self, ctx:bdsParser.ForEndContext):
        pass


    # Enter a parse tree produced by bdsParser#expression.
    def enterExpression(self, ctx:bdsParser.ExpressionContext):
        pass

    # Exit a parse tree produced by bdsParser#expression.
    def exitExpression(self, ctx:bdsParser.ExpressionContext):
        pass


    # Enter a parse tree produced by bdsParser#expressionList.
    def enterExpressionList(self, ctx:bdsParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by bdsParser#expressionList.
    def exitExpressionList(self, ctx:bdsParser.ExpressionListContext):
        pass



del bdsParser