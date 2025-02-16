import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {
            return 5;
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
            return foo()
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_variable_0(self):
        input = """var x int = 10;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_variable_1(self):
        input = """var y = "Hello";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_variable_2(self):
        input = """var z int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_const_0(self):
        input = """const Pi = 3.14;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_const_1(self):
        input = """const Greeting = "Hello, MiniGo!";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_const_2(self):
        input = """const MaxSize = 100 + 50;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_func_0(self):
        input = """func Add(x int, y int) int {
            return x + y
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_struct_0(self):
        input = """type Calculator struct {
            value int;
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_method_0(self):
        input = """func (c Calculator) Add(x int) int {
            c.value += x;
            return c.value;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_string_0(self):
        input = """func Add(){
            str1 := "Hello";
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_array_decl_0(self):
        input = 'var arr [5]int;'
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_array_decl_1(self):
        input = 'var multi_arr [2][5]int;'
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_struct_decl_0(self):
        input = """type Person struct {
            name string ;
            age int ;
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_method_1(self):
        input = """func (p Person) Greet() string {
            return "Hello, " + p.name;
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_interface(self):
        input = """type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset(a int)
            SayHello(name string);
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_221(self):
        input = """const a = "Hello, i am"
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_222(self):
        input = """func main(){p := Person{name: "Alice", age: 30};}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_223(self):
        input = """func main(){p := Person{};}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,2233))
    def test_224(self):
        input = """func main(){PutStringLn(p.name)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_225(self):
        input = """func main(){p.age:=31;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_226(self):
        input = """func main(){PutStringLn(p.Greet())
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_227(self):
        input = """func main(){a[2][3] := b[2]+1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_228(self):
        input = """func main(){person.name := "John";person.age := 30;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_229(self):
        input = """func main(){arr := [3]int{10, 20, 30}
        marr := [2][3]int{{1, 2, 3}, {4, 5, 6}}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_230(self):
        input = """
        type Shape interface {
            Area() float
            Perimeter(w, k int, z int) float
            Draw(name string, scale float) int
            Rotate(angle float, speed int) string
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))
    def test_231(self):
        input = """
        type Test interface {
            Add(x, y int, z);
        }
        """
        expect = "Error on line 3 col 28: )"
        self.assertTrue(TestParser.checkParser(input, expect, 231))