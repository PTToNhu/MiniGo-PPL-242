import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_newline(self):
        """test new line"""
        self.assertTrue(TestLexer.checkLexeme("""var
                                              id
                                              int;""","var,id,;,int,;,<EOF>",106))
    def test_line_comment_0(self):
        """test line comment 0"""
        self.assertTrue(TestLexer.checkLexeme("//line comment\nint a;","int,a,;,<EOF>",107))
    def test_line_comment_1(self):
        """test line comment 1"""
        self.assertTrue(TestLexer.checkLexeme("//line comment\rint a;","int,a,;,<EOF>",124))
    def test_line_comment_2(self):
        """test line comment 2"""
        self.assertTrue(TestLexer.checkLexeme("//line comment\r\n","<EOF>",125))
    def test_multiline_comment_0(self):
        """test multi-line comment 0"""
        self.assertTrue(TestLexer.checkLexeme("/*comment\nabc*/","<EOF>",105))
    def test_multiline_comment_1(self):
        """test multi-line comment 1"""
        self.assertTrue(TestLexer.checkLexeme("/*comment\r\b\fabc*/","<EOF>",126))
    def test_multiline_comment_2(self):
        """test multi-line comment 2"""
        self.assertTrue(TestLexer.checkLexeme("/*comment\nint a;\nint a;*/int a;","int,a,;,<EOF>",127))
    def test_multiline_comment_3(self):
        """test multi-line comment 3"""
        self.assertTrue(TestLexer.checkLexeme("/*comment\nint a;*/int a;*/","int,a,;,*,/,<EOF>",128))
    def test_nested_comment(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("/* This is a /* nested \nmulti-line \ncomment. */ \n*/var abc int ;","var,abc,int,;,<EOF>",108))
    def test_identifier_0(self):
        """test identifiers 0"""
        self.assertTrue(TestLexer.checkLexeme("_abcA9_","_abcA9_,<EOF>",101))
    def test_identifier_1(self):
        """test identifiers 1"""
        self.assertTrue(TestLexer.checkLexeme("_abcA9_ -abcA9_","_abcA9_,-,abcA9_,<EOF>",129))
    def test_identifier_2(self):
        """test identifiers 2"""
        self.assertTrue(TestLexer.checkLexeme("_abcA9_ AbcA9","_abcA9_,AbcA9,<EOF>",130))
    def test_identifier_3(self):
        """test identifiers 3"""
        self.assertTrue(TestLexer.checkLexeme("_abcA9_ 9AbcA9","_abcA9_,9,AbcA9,<EOF>",131))
    def test_identifier_4(self):
        """test identifiers 4"""
        self.assertTrue(TestLexer.checkLexeme("_abcA9_ ?9AbcA9","_abcA9_,ErrorToken ?",132))
    def test_identifier_5(self):
        """test identifiers 5"""
        self.assertTrue(TestLexer.checkLexeme("1a","1,a,<EOF>",109))
    def test_identifier_6(self):
        """test identifiers 6"""
        self.assertTrue(TestLexer.checkLexeme("_ab+A9_","_ab,+,A9_,<EOF>",133))
    def test_identifier_7(self):
        """test identifiers 7"""
        self.assertTrue(TestLexer.checkLexeme("x","x,<EOF>",134))
    def test_identifier_8(self):
        """test identifiers 8"""
        self.assertTrue(TestLexer.checkLexeme("123variable","123,variable,<EOF>",135))
    def test_identifier_9(self):
        """test identifiers 9"""
        self.assertTrue(TestLexer.checkLexeme("userName","userName,<EOF>",136))
    def test_identifier_10(self):
        """test identifiers 10"""
        self.assertTrue(TestLexer.checkLexeme("count123","count123,<EOF>",137))
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("func abc ( ) ","func,abc,(,),<EOF>",104))
    def test_decimal_integer_0(self):
        """test decimal integer 0"""
        self.assertTrue(TestLexer.checkLexeme("10","10,<EOF>",110))
    def test_decimal_integer_1(self):
        """test decimal integer 1"""
        self.assertTrue(TestLexer.checkLexeme("01","0,1,<EOF>",138))
    def test_decimal_integer_2(self):
        """test decimal integer 2"""
        self.assertTrue(TestLexer.checkLexeme("019","0,19,<EOF>",139))
    def test_decimal_integer_3(self):
        """test decimal integer 3"""
        self.assertTrue(TestLexer.checkLexeme("0","0,<EOF>",140))
    def test_decimal_integer_4(self):
        """test decimal integer 4"""
        self.assertTrue(TestLexer.checkLexeme("42","42,<EOF>",111))
    def test_binary_integer_0(self):
        """test binary integer 0"""
        self.assertTrue(TestLexer.checkLexeme("0b1","0b1,<EOF>",113))
    def test_binary_integer_1(self):
        """test binary integer 1"""
        self.assertTrue(TestLexer.checkLexeme("0B147","0B1,47,<EOF>",112))
    def test_binary_integer_2(self):
        """test binary integer 2"""
        self.assertTrue(TestLexer.checkLexeme("0B101","0B101,<EOF>",141))
    def test_binary_integer_3(self):
        """test binary integer 3"""
        self.assertTrue(TestLexer.checkLexeme("0b001","0b001,<EOF>",142))
    def test_binary_integer_4(self):
        """test binary integer 4"""
        self.assertTrue(TestLexer.checkLexeme("0b0af","0b0,af,<EOF>",143))
    def test_hex_integer_0(self):
        """test hex integer 0"""
        self.assertTrue(TestLexer.checkLexeme("0x1a","0x1a,<EOF>",114))
    def test_hex_integer_1(self):
        """test hex integer 1"""
        self.assertTrue(TestLexer.checkLexeme("0x1g","0x1,g,<EOF>",115))
    def test_hex_integer_2(self):
        """test hex integer 2"""
        self.assertTrue(TestLexer.checkLexeme("0X1Abf","0X1Abf,<EOF>",144))
    def test_oct_integer_0(self):
        """test oct integer 0"""
        self.assertTrue(TestLexer.checkLexeme("0o18","0o1,8,<EOF>",145))
    def test_oct_integer_1(self):
        """test oct integer 1"""
        self.assertTrue(TestLexer.checkLexeme("0O17","0O17,<EOF>",146))
    def test_oct_integer_2(self):
        """test oct integer 2"""
        self.assertTrue(TestLexer.checkLexeme("0O12","0O12,<EOF>",147))
    def test_float_0(self):
        """test floating point"""
        self.assertTrue(TestLexer.checkLexeme("0.","0.,<EOF>",116))
    def test_float_1(self):
        """test floating point"""
        self.assertTrue(TestLexer.checkLexeme("0.0","0.0,<EOF>",117))
    def test_float_2(self):
        """test floating point"""
        self.assertTrue(TestLexer.checkLexeme("0.0e+1","0.0e+1,<EOF>",118))
    def test_float_3(self):
        """test floating point 2"""
        self.assertTrue(TestLexer.checkLexeme("3.14","3.14,<EOF>",148))
    def test_float_4(self):
        """test floating point 3"""
        self.assertTrue(TestLexer.checkLexeme("2.e10","2.,e10,<EOF>",149))
    def test_float_5(self):
        """test floating point 4"""
        self.assertTrue(TestLexer.checkLexeme("2.0Ea","2.0,Ea,<EOF>",150))
    def test_string_0(self):
        """test string 0"""
        self.assertTrue(TestLexer.checkLexeme('"abc"','"abc",<EOF>', 151))
    def test_string_1(self):
        """test string 1"""
        self.assertTrue(TestLexer.checkLexeme('"This is a string with a newline\n"','"This is a string with a newline\n\n",<EOF>', 152))
    def test_string_2(self):
        """test string 2"""
        self.assertTrue(TestLexer.checkLexeme('"123"','"123",<EOF>', 153))
    def test_string_3(self):
        """test string 3"""
        self.assertTrue(TestLexer.checkLexeme('"This is a string with a tab\t"','"This is a string with a tab\t\",<EOF>', 154))
    def test_string_4(self):
        """test string 4"""
        self.assertTrue(TestLexer.checkLexeme('"This\""', '"This\",Unclosed string: "', 155))
    def test_string_5(self):
        """test string 5"""
        self.assertTrue(TestLexer.checkLexeme('"This\\ "', 'Illegal escape in string: "This\ ', 156))
    def test_string_6(self):
        """test string 6"""
        self.assertTrue(TestLexer.checkLexeme('"ancjen\txyc"','"ancjen\txyc",<EOF>', 119))
    def test_string_7(self):
        """test string 7"""
        self.assertTrue(TestLexer.checkLexeme('"ancjen\"xyc"','\"ancjen",xyc,Unclosed string: "', 120))
    def test_string_8(self):
        """test string 8"""
        self.assertTrue(TestLexer.checkLexeme('"this is a \\\ double quote"','"this is a \\\ double quote",<EOF>', 123))
    def test_bool_0(self):
        """test bool 0"""
        self.assertTrue(TestLexer.checkLexeme("true","true,<EOF>", 157))
    def test_bool_1(self):
        """test bool 1"""
        self.assertTrue(TestLexer.checkLexeme("truE","truE,<EOF>", 121))
    def test_bool_2(self):
        """test bool 2"""
        self.assertTrue(TestLexer.checkLexeme("true ARE","true,ARE,<EOF>", 122))
    def test_bool_3(self):
        """test bool 2"""
        self.assertTrue(TestLexer.checkLexeme("FALSE","FALSE,<EOF>", 158))
    def test_nil(self):
        """test nil"""
        self.assertTrue(TestLexer.checkLexeme("nil","nil,<EOF>", 159))
    def test_array_type_0(self):
        """test array type 0"""
        self.assertTrue(TestLexer.checkLexeme("arr [5]int","arr,[,5,],int,<EOF>", 160))
    def test_array_type_1(self):
        """test array type 1"""
        self.assertTrue(TestLexer.checkLexeme("multi_arr [2][5]float","multi_arr,[,2,],[,5,],float,<EOF>", 161))
    def test_array_type_2(self):
        """test array type 2"""
        self.assertTrue(TestLexer.checkLexeme("multi_arr [2][con]float","multi_arr,[,2,],[,con,],float,<EOF>", 162))
    def test_add(self):
        """test add"""
        self.assertTrue(TestLexer.checkLexeme("return x + y","return,x,+,y,<EOF>", 163))
    def test_164(self):  
        input = '"hello \\"" world"'  
        expect = '"hello \\"",world,Unclosed string: "'  
        self.assertTrue(TestLexer.checkLexeme(input, expect, 164))
    def test_165(self):  
        input = '"This is a\q string with a newline"'  
        expect = 'Illegal escape in string: "This is a\q'  
        self.assertTrue(TestLexer.checkLexeme(input, expect, 165))
    def test_166(self):  
        input = 'func Add(x int, y int) int {\nreturn x + y;\n}'  
        expect = 'func,Add,(,x,int,,,y,int,),int,{,return,x,+,y,;,},<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 166))
    def test_167(self):  
        input = '"This is a string with a newline\n"'  
        expect = '"This is a string with a newline\n\n",<EOF>'  
        self.assertTrue(TestLexer.checkLexeme(input, expect, 167))
    def test_168(self):  
        input = 'type Calculator struct {\nvalue int;\n}'  
        expect = 'type,Calculator,struct,{,value,int,;,},<EOF>'  
        self.assertTrue(TestLexer.checkLexeme(input, expect, 168))
    def test_169(self):  
        input = """type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset()
            }"""
        expect = 'type,Calculator,interface,{,Add,(,x,,,y,int,),int,;,Subtract,(,a,,,b,float,,,c,int,),float,;,Reset,(,),;,},<EOF>'  
        self.assertTrue(TestLexer.checkLexeme(input, expect, 169))
    def test_170(self):  
        input = """func (p Person) Greet() string {
            return "Hello "+p.name
            }"""
        expect = 'func,(,p,Person,),Greet,(,),string,{,return,"Hello ",+,p,.,name,;,},<EOF>'  
        self.assertTrue(TestLexer.checkLexeme(input, expect, 170))
    def test_291(self):  
        input = """x := true 
        y := 20"""
        expect = "x,:=,true,;,y,:=,20,<EOF>"  
        self.assertTrue(TestLexer.checkLexeme(input, expect, 291))  

    def test_292(self):  
        input = """return 
        x + y"""
        expect = "return,;,x,+,y,<EOF>"  
        self.assertTrue(TestLexer.checkLexeme(input, expect, 292))  

    def test_293(self):  
        input = """if x > 0 {  \n return x  \n}"""  
        expect = "if,x,>,0,{,return,x,;,},<EOF>"  
        self.assertTrue(TestLexer.checkLexeme(input, expect, 293))  

    def test_294(self):  
        input = """func foo() {  y := 100
        return y}"""  
        expect = "func,foo,(,),{,y,:=,100,;,return,y,},<EOF>"  
        self.assertTrue(TestLexer.checkLexeme(input, expect, 294))  

    def test_295(self):  
        input = "arr := [3]int{1, \n 2, \n 3}"
        expect = "arr,:=,[,3,],int,{,1,,,2,,,3,},<EOF>"  
        self.assertTrue(TestLexer.checkLexeme(input, expect, 295))  

    def test_296(self):  
        input = 'myStruct:=Person{name: "Alice", \n age: 30}'
        expect = 'myStruct,:=,Person,{,name,:,"Alice",,,age,:,30,},<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 296))  

    def test_297(self):  
        input = "x := (a + b) \n * c "
        expect = "x,:=,(,a,+,b,),;,*,c,<EOF>"  
        self.assertTrue(TestLexer.checkLexeme(input, expect, 297))  

    def test_298(self):  
        input = "foo(1, \n 2, \n 3)"
        expect = "foo,(,1,,,2,,,3,),<EOF>"  
        self.assertTrue(TestLexer.checkLexeme(input, expect, 298))  

    def test_299(self):  
        input = "func main() {  \n a := 10  \n b := a + 5  \n c := b * 2  \n return c  \n}"
        expect = "func,main,(,),{,a,:=,10,;,b,:=,a,+,5,;,c,:=,b,*,2,;,return,c,;,},<EOF>"  
        self.assertTrue(TestLexer.checkLexeme(input, expect, 299))  

    def test_300(self):  
        input = """continue
                if x > 0 """
        expect = "continue,;,if,x,>,0,<EOF>"  
        self.assertTrue(TestLexer.checkLexeme(input, expect, 300))