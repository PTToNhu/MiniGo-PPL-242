# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decls.
    def visitDecls(self, ctx:MiniGoParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl.
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_decl.
    def visitType_decl(self, ctx:MiniGoParser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_decl.
    def visitArray_decl(self, ctx:MiniGoParser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#scalar_decl.
    def visitScalar_decl(self, ctx:MiniGoParser.Scalar_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_var_decl.
    def visitStruct_var_decl(self, ctx:MiniGoParser.Struct_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldnamelist.
    def visitFieldnamelist(self, ctx:MiniGoParser.FieldnamelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#datatype.
    def visitDatatype(self, ctx:MiniGoParser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitivetype.
    def visitPrimitivetype(self, ctx:MiniGoParser.PrimitivetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#compositetype.
    def visitCompositetype(self, ctx:MiniGoParser.CompositetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structtype.
    def visitStructtype(self, ctx:MiniGoParser.StructtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfacetype.
    def visitInterfacetype(self, ctx:MiniGoParser.InterfacetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arraytype.
    def visitArraytype(self, ctx:MiniGoParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimensions.
    def visitDimensions(self, ctx:MiniGoParser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodlist.
    def visitMethodlist(self, ctx:MiniGoParser.MethodlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func.
    def visitFunc(self, ctx:MiniGoParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramlist.
    def visitParamlist(self, ctx:MiniGoParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramprime.
    def visitParamprime(self, ctx:MiniGoParser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#body.
    def visitBody(self, ctx:MiniGoParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmtlist.
    def visitStmtlist(self, ctx:MiniGoParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignstmt.
    def visitAssignstmt(self, ctx:MiniGoParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#scalaassign.
    def visitScalaassign(self, ctx:MiniGoParser.ScalaassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldassign.
    def visitFieldassign(self, ctx:MiniGoParser.FieldassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayassign.
    def visitArrayassign(self, ctx:MiniGoParser.ArrayassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_instance.
    def visitStruct_instance(self, ctx:MiniGoParser.Struct_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldaccess.
    def visitFieldaccess(self, ctx:MiniGoParser.FieldaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayaccess.
    def visitArrayaccess(self, ctx:MiniGoParser.ArrayaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimensions_stmt.
    def visitDimensions_stmt(self, ctx:MiniGoParser.Dimensions_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnstmt.
    def visitReturnstmt(self, ctx:MiniGoParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method.
    def visitMethod(self, ctx:MiniGoParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifstmt.
    def visitIfstmt(self, ctx:MiniGoParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_clause.
    def visitIf_clause(self, ctx:MiniGoParser.If_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_clause.
    def visitElse_clause(self, ctx:MiniGoParser.Else_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseif_clauselist.
    def visitElseif_clauselist(self, ctx:MiniGoParser.Elseif_clauselistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseif_clause.
    def visitElseif_clause(self, ctx:MiniGoParser.Elseif_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forstmt.
    def visitForstmt(self, ctx:MiniGoParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forbasic.
    def visitForbasic(self, ctx:MiniGoParser.ForbasicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#foricu.
    def visitForicu(self, ctx:MiniGoParser.ForicuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#initialization_clause.
    def visitInitialization_clause(self, ctx:MiniGoParser.Initialization_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#condition_clause.
    def visitCondition_clause(self, ctx:MiniGoParser.Condition_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#update_clause.
    def visitUpdate_clause(self, ctx:MiniGoParser.Update_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forrange.
    def visitForrange(self, ctx:MiniGoParser.ForrangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakstmt.
    def visitBreakstmt(self, ctx:MiniGoParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continuestmt.
    def visitContinuestmt(self, ctx:MiniGoParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callstmt.
    def visitCallstmt(self, ctx:MiniGoParser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#subexpr.
    def visitSubexpr(self, ctx:MiniGoParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call.
    def visitCall(self, ctx:MiniGoParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_call.
    def visitStruct_call(self, ctx:MiniGoParser.Struct_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argumentlist.
    def visitArgumentlist(self, ctx:MiniGoParser.ArgumentlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argumentprime.
    def visitArgumentprime(self, ctx:MiniGoParser.ArgumentprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literals.
    def visitLiterals(self, ctx:MiniGoParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structliteral.
    def visitStructliteral(self, ctx:MiniGoParser.StructliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldvaluelist.
    def visitFieldvaluelist(self, ctx:MiniGoParser.FieldvaluelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldvalueprime.
    def visitFieldvalueprime(self, ctx:MiniGoParser.FieldvalueprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayliteral.
    def visitArrayliteral(self, ctx:MiniGoParser.ArrayliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elementlist.
    def visitElementlist(self, ctx:MiniGoParser.ElementlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#element.
    def visitElement(self, ctx:MiniGoParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_literals.
    def visitPrimitive_literals(self, ctx:MiniGoParser.Primitive_literalsContext):
        return self.visitChildren(ctx)



del MiniGoParser