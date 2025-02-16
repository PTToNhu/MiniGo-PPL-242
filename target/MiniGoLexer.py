# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01ef\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\3\3\3\5\3\u009a\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\7\30\u0116\n")
        buf.write("\30\f\30\16\30\u0119\13\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\31\3\31\3\31\3\31\7\31\u0124\n\31\f\31\16\31\u0127\13")
        buf.write("\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3")
        buf.write("#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\39\39\39\39\59\u0179\n")
        buf.write("9\3:\3:\3:\7:\u017e\n:\f:\16:\u0181\13:\5:\u0183\n:\3")
        buf.write(";\3;\3;\6;\u0188\n;\r;\16;\u0189\3<\3<\3<\6<\u018f\n<")
        buf.write("\r<\16<\u0190\3=\3=\3=\6=\u0196\n=\r=\16=\u0197\3>\3>")
        buf.write("\3>\5>\u019d\n>\3>\3>\3>\3>\5>\u01a3\n>\5>\u01a5\n>\3")
        buf.write("?\6?\u01a8\n?\r?\16?\u01a9\3@\3@\5@\u01ae\n@\3@\6@\u01b1")
        buf.write("\n@\r@\16@\u01b2\3A\3A\7A\u01b7\nA\fA\16A\u01ba\13A\3")
        buf.write("A\3A\3B\3B\5B\u01c0\nB\3C\3C\3C\3D\3D\7D\u01c7\nD\fD\16")
        buf.write("D\u01ca\13D\3E\6E\u01cd\nE\rE\16E\u01ce\3E\3E\3F\3F\3")
        buf.write("G\3G\7G\u01d7\nG\fG\16G\u01da\13G\3G\3G\3H\3H\7H\u01e0")
        buf.write("\nH\fH\16H\u01e3\13H\3H\3H\3H\3I\3I\3I\5I\u01eb\nI\3J")
        buf.write("\3J\3J\3\u0117\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o9q:s\2u\2w\2y\2{;}\2\177\2\u0081<\u0083\2\u0085")
        buf.write("\2\u0087=\u0089>\u008b?\u008d@\u008fA\u0091\2\u0093B\3")
        buf.write("\2\22\4\2\f\f\17\17\3\2\63;\3\2\62;\4\2DDdd\3\2\62\63")
        buf.write("\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--//\4")
        buf.write("\2$$^^\7\2$$^^ppttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2\13")
        buf.write("\13\16\17\"\"\2\u01fe\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2{\3\2\2\2\2\u0081\3\2")
        buf.write("\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2")
        buf.write("\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0093\3\2\2\2\3\u0095")
        buf.write("\3\2\2\2\5\u0099\3\2\2\2\7\u009b\3\2\2\2\t\u009e\3\2\2")
        buf.write("\2\13\u00a3\3\2\2\2\r\u00a7\3\2\2\2\17\u00ae\3\2\2\2\21")
        buf.write("\u00b3\3\2\2\2\23\u00b8\3\2\2\2\25\u00bf\3\2\2\2\27\u00c9")
        buf.write("\3\2\2\2\31\u00cf\3\2\2\2\33\u00d3\3\2\2\2\35\u00dc\3")
        buf.write("\2\2\2\37\u00e2\3\2\2\2!\u00e8\3\2\2\2#\u00ec\3\2\2\2")
        buf.write("%\u00f2\3\2\2\2\'\u00f9\3\2\2\2)\u0101\3\2\2\2+\u0105")
        buf.write("\3\2\2\2-\u010a\3\2\2\2/\u0110\3\2\2\2\61\u011f\3\2\2")
        buf.write("\2\63\u012a\3\2\2\2\65\u012c\3\2\2\2\67\u012e\3\2\2\2")
        buf.write("9\u0130\3\2\2\2;\u0132\3\2\2\2=\u0134\3\2\2\2?\u0137\3")
        buf.write("\2\2\2A\u013a\3\2\2\2C\u013c\3\2\2\2E\u013f\3\2\2\2G\u0141")
        buf.write("\3\2\2\2I\u0144\3\2\2\2K\u0147\3\2\2\2M\u014a\3\2\2\2")
        buf.write("O\u014c\3\2\2\2Q\u014f\3\2\2\2S\u0152\3\2\2\2U\u0155\3")
        buf.write("\2\2\2W\u0158\3\2\2\2Y\u015b\3\2\2\2[\u015e\3\2\2\2]\u0160")
        buf.write("\3\2\2\2_\u0162\3\2\2\2a\u0164\3\2\2\2c\u0166\3\2\2\2")
        buf.write("e\u0168\3\2\2\2g\u016a\3\2\2\2i\u016c\3\2\2\2k\u016e\3")
        buf.write("\2\2\2m\u0170\3\2\2\2o\u0172\3\2\2\2q\u0178\3\2\2\2s\u0182")
        buf.write("\3\2\2\2u\u0184\3\2\2\2w\u018b\3\2\2\2y\u0192\3\2\2\2")
        buf.write("{\u01a4\3\2\2\2}\u01a7\3\2\2\2\177\u01ab\3\2\2\2\u0081")
        buf.write("\u01b4\3\2\2\2\u0083\u01bf\3\2\2\2\u0085\u01c1\3\2\2\2")
        buf.write("\u0087\u01c4\3\2\2\2\u0089\u01cc\3\2\2\2\u008b\u01d2\3")
        buf.write("\2\2\2\u008d\u01d4\3\2\2\2\u008f\u01dd\3\2\2\2\u0091\u01ea")
        buf.write("\3\2\2\2\u0093\u01ec\3\2\2\2\u0095\u0096\7a\2\2\u0096")
        buf.write("\4\3\2\2\2\u0097\u009a\5+\26\2\u0098\u009a\5-\27\2\u0099")
        buf.write("\u0097\3\2\2\2\u0099\u0098\3\2\2\2\u009a\6\3\2\2\2\u009b")
        buf.write("\u009c\7k\2\2\u009c\u009d\7h\2\2\u009d\b\3\2\2\2\u009e")
        buf.write("\u009f\7g\2\2\u009f\u00a0\7n\2\2\u00a0\u00a1\7u\2\2\u00a1")
        buf.write("\u00a2\7g\2\2\u00a2\n\3\2\2\2\u00a3\u00a4\7h\2\2\u00a4")
        buf.write("\u00a5\7q\2\2\u00a5\u00a6\7t\2\2\u00a6\f\3\2\2\2\u00a7")
        buf.write("\u00a8\7t\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7v\2\2\u00aa")
        buf.write("\u00ab\7w\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad\7p\2\2\u00ad")
        buf.write("\16\3\2\2\2\u00ae\u00af\7h\2\2\u00af\u00b0\7w\2\2\u00b0")
        buf.write("\u00b1\7p\2\2\u00b1\u00b2\7e\2\2\u00b2\20\3\2\2\2\u00b3")
        buf.write("\u00b4\7v\2\2\u00b4\u00b5\7{\2\2\u00b5\u00b6\7r\2\2\u00b6")
        buf.write("\u00b7\7g\2\2\u00b7\22\3\2\2\2\u00b8\u00b9\7u\2\2\u00b9")
        buf.write("\u00ba\7v\2\2\u00ba\u00bb\7t\2\2\u00bb\u00bc\7w\2\2\u00bc")
        buf.write("\u00bd\7e\2\2\u00bd\u00be\7v\2\2\u00be\24\3\2\2\2\u00bf")
        buf.write("\u00c0\7k\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7v\2\2\u00c2")
        buf.write("\u00c3\7g\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7h\2\2\u00c5")
        buf.write("\u00c6\7c\2\2\u00c6\u00c7\7e\2\2\u00c7\u00c8\7g\2\2\u00c8")
        buf.write("\26\3\2\2\2\u00c9\u00ca\7e\2\2\u00ca\u00cb\7q\2\2\u00cb")
        buf.write("\u00cc\7p\2\2\u00cc\u00cd\7u\2\2\u00cd\u00ce\7v\2\2\u00ce")
        buf.write("\30\3\2\2\2\u00cf\u00d0\7x\2\2\u00d0\u00d1\7c\2\2\u00d1")
        buf.write("\u00d2\7t\2\2\u00d2\32\3\2\2\2\u00d3\u00d4\7e\2\2\u00d4")
        buf.write("\u00d5\7q\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7\7v\2\2\u00d7")
        buf.write("\u00d8\7k\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da\7w\2\2\u00da")
        buf.write("\u00db\7g\2\2\u00db\34\3\2\2\2\u00dc\u00dd\7d\2\2\u00dd")
        buf.write("\u00de\7t\2\2\u00de\u00df\7g\2\2\u00df\u00e0\7c\2\2\u00e0")
        buf.write("\u00e1\7m\2\2\u00e1\36\3\2\2\2\u00e2\u00e3\7t\2\2\u00e3")
        buf.write("\u00e4\7c\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7i\2\2\u00e6")
        buf.write("\u00e7\7g\2\2\u00e7 \3\2\2\2\u00e8\u00e9\7k\2\2\u00e9")
        buf.write("\u00ea\7p\2\2\u00ea\u00eb\7v\2\2\u00eb\"\3\2\2\2\u00ec")
        buf.write("\u00ed\7h\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef\7q\2\2\u00ef")
        buf.write("\u00f0\7c\2\2\u00f0\u00f1\7v\2\2\u00f1$\3\2\2\2\u00f2")
        buf.write("\u00f3\7u\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5\7t\2\2\u00f5")
        buf.write("\u00f6\7k\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8\7i\2\2\u00f8")
        buf.write("&\3\2\2\2\u00f9\u00fa\7d\2\2\u00fa\u00fb\7q\2\2\u00fb")
        buf.write("\u00fc\7q\2\2\u00fc\u00fd\7n\2\2\u00fd\u00fe\7g\2\2\u00fe")
        buf.write("\u00ff\7c\2\2\u00ff\u0100\7p\2\2\u0100(\3\2\2\2\u0101")
        buf.write("\u0102\7p\2\2\u0102\u0103\7k\2\2\u0103\u0104\7n\2\2\u0104")
        buf.write("*\3\2\2\2\u0105\u0106\7v\2\2\u0106\u0107\7t\2\2\u0107")
        buf.write("\u0108\7w\2\2\u0108\u0109\7g\2\2\u0109,\3\2\2\2\u010a")
        buf.write("\u010b\7h\2\2\u010b\u010c\7c\2\2\u010c\u010d\7n\2\2\u010d")
        buf.write("\u010e\7u\2\2\u010e\u010f\7g\2\2\u010f.\3\2\2\2\u0110")
        buf.write("\u0111\7\61\2\2\u0111\u0112\7,\2\2\u0112\u0117\3\2\2\2")
        buf.write("\u0113\u0116\5/\30\2\u0114\u0116\13\2\2\2\u0115\u0113")
        buf.write("\3\2\2\2\u0115\u0114\3\2\2\2\u0116\u0119\3\2\2\2\u0117")
        buf.write("\u0118\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u011a\3\2\2\2")
        buf.write("\u0119\u0117\3\2\2\2\u011a\u011b\7,\2\2\u011b\u011c\7")
        buf.write("\61\2\2\u011c\u011d\3\2\2\2\u011d\u011e\b\30\2\2\u011e")
        buf.write("\60\3\2\2\2\u011f\u0120\7\61\2\2\u0120\u0121\7\61\2\2")
        buf.write("\u0121\u0125\3\2\2\2\u0122\u0124\n\2\2\2\u0123\u0122\3")
        buf.write("\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126")
        buf.write("\3\2\2\2\u0126\u0128\3\2\2\2\u0127\u0125\3\2\2\2\u0128")
        buf.write("\u0129\b\31\2\2\u0129\62\3\2\2\2\u012a\u012b\7-\2\2\u012b")
        buf.write("\64\3\2\2\2\u012c\u012d\7/\2\2\u012d\66\3\2\2\2\u012e")
        buf.write("\u012f\7,\2\2\u012f8\3\2\2\2\u0130\u0131\7\61\2\2\u0131")
        buf.write(":\3\2\2\2\u0132\u0133\7\'\2\2\u0133<\3\2\2\2\u0134\u0135")
        buf.write("\7?\2\2\u0135\u0136\7?\2\2\u0136>\3\2\2\2\u0137\u0138")
        buf.write("\7#\2\2\u0138\u0139\7?\2\2\u0139@\3\2\2\2\u013a\u013b")
        buf.write("\7>\2\2\u013bB\3\2\2\2\u013c\u013d\7>\2\2\u013d\u013e")
        buf.write("\7?\2\2\u013eD\3\2\2\2\u013f\u0140\7@\2\2\u0140F\3\2\2")
        buf.write("\2\u0141\u0142\7@\2\2\u0142\u0143\7?\2\2\u0143H\3\2\2")
        buf.write("\2\u0144\u0145\7(\2\2\u0145\u0146\7(\2\2\u0146J\3\2\2")
        buf.write("\2\u0147\u0148\7~\2\2\u0148\u0149\7~\2\2\u0149L\3\2\2")
        buf.write("\2\u014a\u014b\7#\2\2\u014bN\3\2\2\2\u014c\u014d\7<\2")
        buf.write("\2\u014d\u014e\7?\2\2\u014eP\3\2\2\2\u014f\u0150\7-\2")
        buf.write("\2\u0150\u0151\7?\2\2\u0151R\3\2\2\2\u0152\u0153\7/\2")
        buf.write("\2\u0153\u0154\7?\2\2\u0154T\3\2\2\2\u0155\u0156\7,\2")
        buf.write("\2\u0156\u0157\7?\2\2\u0157V\3\2\2\2\u0158\u0159\7\61")
        buf.write("\2\2\u0159\u015a\7?\2\2\u015aX\3\2\2\2\u015b\u015c\7\'")
        buf.write("\2\2\u015c\u015d\7?\2\2\u015dZ\3\2\2\2\u015e\u015f\7?")
        buf.write("\2\2\u015f\\\3\2\2\2\u0160\u0161\7\60\2\2\u0161^\3\2\2")
        buf.write("\2\u0162\u0163\7*\2\2\u0163`\3\2\2\2\u0164\u0165\7+\2")
        buf.write("\2\u0165b\3\2\2\2\u0166\u0167\7]\2\2\u0167d\3\2\2\2\u0168")
        buf.write("\u0169\7_\2\2\u0169f\3\2\2\2\u016a\u016b\7}\2\2\u016b")
        buf.write("h\3\2\2\2\u016c\u016d\7\177\2\2\u016dj\3\2\2\2\u016e\u016f")
        buf.write("\7.\2\2\u016fl\3\2\2\2\u0170\u0171\7=\2\2\u0171n\3\2\2")
        buf.write("\2\u0172\u0173\7<\2\2\u0173p\3\2\2\2\u0174\u0179\5s:\2")
        buf.write("\u0175\u0179\5u;\2\u0176\u0179\5w<\2\u0177\u0179\5y=\2")
        buf.write("\u0178\u0174\3\2\2\2\u0178\u0175\3\2\2\2\u0178\u0176\3")
        buf.write("\2\2\2\u0178\u0177\3\2\2\2\u0179r\3\2\2\2\u017a\u0183")
        buf.write("\7\62\2\2\u017b\u017f\t\3\2\2\u017c\u017e\t\4\2\2\u017d")
        buf.write("\u017c\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3")
        buf.write("\2\2\2\u0182\u017a\3\2\2\2\u0182\u017b\3\2\2\2\u0183t")
        buf.write("\3\2\2\2\u0184\u0185\7\62\2\2\u0185\u0187\t\5\2\2\u0186")
        buf.write("\u0188\t\6\2\2\u0187\u0186\3\2\2\2\u0188\u0189\3\2\2\2")
        buf.write("\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018av\3\2\2")
        buf.write("\2\u018b\u018c\7\62\2\2\u018c\u018e\t\7\2\2\u018d\u018f")
        buf.write("\t\b\2\2\u018e\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191x\3\2\2\2\u0192")
        buf.write("\u0193\7\62\2\2\u0193\u0195\t\t\2\2\u0194\u0196\t\n\2")
        buf.write("\2\u0195\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0195")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198z\3\2\2\2\u0199\u019a")
        buf.write("\5}?\2\u019a\u019c\5]/\2\u019b\u019d\5}?\2\u019c\u019b")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u01a5\3\2\2\2\u019e")
        buf.write("\u019f\5}?\2\u019f\u01a0\5]/\2\u01a0\u01a2\5}?\2\u01a1")
        buf.write("\u01a3\5\177@\2\u01a2\u01a1\3\2\2\2\u01a2\u01a3\3\2\2")
        buf.write("\2\u01a3\u01a5\3\2\2\2\u01a4\u0199\3\2\2\2\u01a4\u019e")
        buf.write("\3\2\2\2\u01a5|\3\2\2\2\u01a6\u01a8\t\4\2\2\u01a7\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa~\3\2\2\2\u01ab\u01ad\t\13\2\2\u01ac")
        buf.write("\u01ae\t\f\2\2\u01ad\u01ac\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01ae\u01b0\3\2\2\2\u01af\u01b1\t\4\2\2\u01b0\u01af\3")
        buf.write("\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3")
        buf.write("\3\2\2\2\u01b3\u0080\3\2\2\2\u01b4\u01b8\7$\2\2\u01b5")
        buf.write("\u01b7\5\u0083B\2\u01b6\u01b5\3\2\2\2\u01b7\u01ba\3\2")
        buf.write("\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bb")
        buf.write("\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb\u01bc\7$\2\2\u01bc")
        buf.write("\u0082\3\2\2\2\u01bd\u01c0\n\r\2\2\u01be\u01c0\5\u0085")
        buf.write("C\2\u01bf\u01bd\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0\u0084")
        buf.write("\3\2\2\2\u01c1\u01c2\7^\2\2\u01c2\u01c3\t\16\2\2\u01c3")
        buf.write("\u0086\3\2\2\2\u01c4\u01c8\t\17\2\2\u01c5\u01c7\t\20\2")
        buf.write("\2\u01c6\u01c5\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6")
        buf.write("\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u0088\3\2\2\2\u01ca")
        buf.write("\u01c8\3\2\2\2\u01cb\u01cd\t\21\2\2\u01cc\u01cb\3\2\2")
        buf.write("\2\u01cd\u01ce\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\bE\2\2\u01d1")
        buf.write("\u008a\3\2\2\2\u01d2\u01d3\7\f\2\2\u01d3\u008c\3\2\2\2")
        buf.write("\u01d4\u01d8\7$\2\2\u01d5\u01d7\5\u0083B\2\u01d6\u01d5")
        buf.write("\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8")
        buf.write("\u01d9\3\2\2\2\u01d9\u01db\3\2\2\2\u01da\u01d8\3\2\2\2")
        buf.write("\u01db\u01dc\bG\3\2\u01dc\u008e\3\2\2\2\u01dd\u01e1\7")
        buf.write("$\2\2\u01de\u01e0\5\u0083B\2\u01df\u01de\3\2\2\2\u01e0")
        buf.write("\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2")
        buf.write("\u01e2\u01e4\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4\u01e5\5")
        buf.write("\u0091I\2\u01e5\u01e6\bH\4\2\u01e6\u0090\3\2\2\2\u01e7")
        buf.write("\u01e8\7^\2\2\u01e8\u01eb\n\16\2\2\u01e9\u01eb\7^\2\2")
        buf.write("\u01ea\u01e7\3\2\2\2\u01ea\u01e9\3\2\2\2\u01eb\u0092\3")
        buf.write("\2\2\2\u01ec\u01ed\13\2\2\2\u01ed\u01ee\bJ\5\2\u01ee\u0094")
        buf.write("\3\2\2\2\32\2\u0099\u0115\u0117\u0125\u0178\u017f\u0182")
        buf.write("\u0189\u0190\u0197\u019c\u01a2\u01a4\u01a9\u01ad\u01b2")
        buf.write("\u01b8\u01bf\u01c8\u01ce\u01d8\u01e1\u01ea\6\b\2\2\3G")
        buf.write("\2\3H\3\3J\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    BOOLLIT = 2
    IF = 3
    ELSE = 4
    FOR = 5
    RETURN = 6
    FUNC = 7
    TYPE = 8
    STRUCT = 9
    INTERFACE = 10
    CONST = 11
    VAR = 12
    CONTINUE = 13
    BREAK = 14
    RANGE = 15
    INT = 16
    FLOAT = 17
    STRING = 18
    BOOLEAN = 19
    NIL = 20
    TRUE = 21
    FALSE = 22
    COMMENT = 23
    LINE_COMMENT = 24
    ADD = 25
    SUB = 26
    MUL = 27
    DIV = 28
    MOD = 29
    EQUAL = 30
    N_EQUAL = 31
    LESS = 32
    L_EQUAL = 33
    GREATER = 34
    G_EQUAL = 35
    AND = 36
    OR = 37
    NOT = 38
    ASSIGNMENT = 39
    ADDASS = 40
    SUBASS = 41
    MULASS = 42
    DIVASS = 43
    MODASS = 44
    ASSIGN = 45
    DOT = 46
    LP = 47
    RP = 48
    LSB = 49
    RSB = 50
    LB = 51
    RB = 52
    COMMA = 53
    SEMI = 54
    COLON = 55
    INTLIT = 56
    FLOATLIT = 57
    STRINGLIT = 58
    ID = 59
    WS = 60
    NL = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'_'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'const'", "'var'", "'continue'", 
            "'break'", "'range'", "'int'", "'float'", "'string'", "'boolean'", 
            "'nil'", "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
            "'!'", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'='", 
            "'.'", "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "';'", 
            "':'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLLIT", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
            "INTERFACE", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "INT", 
            "FLOAT", "STRING", "BOOLEAN", "NIL", "TRUE", "FALSE", "COMMENT", 
            "LINE_COMMENT", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
            "N_EQUAL", "LESS", "L_EQUAL", "GREATER", "G_EQUAL", "AND", "OR", 
            "NOT", "ASSIGNMENT", "ADDASS", "SUBASS", "MULASS", "DIVASS", 
            "MODASS", "ASSIGN", "DOT", "LP", "RP", "LSB", "RSB", "LB", "RB", 
            "COMMA", "SEMI", "COLON", "INTLIT", "FLOATLIT", "STRINGLIT", 
            "ID", "WS", "NL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "BOOLLIT", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                  "TYPE", "STRUCT", "INTERFACE", "CONST", "VAR", "CONTINUE", 
                  "BREAK", "RANGE", "INT", "FLOAT", "STRING", "BOOLEAN", 
                  "NIL", "TRUE", "FALSE", "COMMENT", "LINE_COMMENT", "ADD", 
                  "SUB", "MUL", "DIV", "MOD", "EQUAL", "N_EQUAL", "LESS", 
                  "L_EQUAL", "GREATER", "G_EQUAL", "AND", "OR", "NOT", "ASSIGNMENT", 
                  "ADDASS", "SUBASS", "MULASS", "DIVASS", "MODASS", "ASSIGN", 
                  "DOT", "LP", "RP", "LSB", "RSB", "LB", "RB", "COMMA", 
                  "SEMI", "COLON", "INTLIT", "DEC", "BIN", "OCT", "HEX", 
                  "FLOATLIT", "INTPART", "EXPPART", "STRINGLIT", "STR_CHAR", 
                  "ESC", "ID", "WS", "NL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ESC_ILLEGAL", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type

        if not hasattr(self, "prev_token"):
            self.prev_token = None  

        if tk == self.UNCLOSE_STRING:       
            result = super().emit()
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit()
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            result = super().emit()
            raise ErrorToken(result.text)
        elif tk == self.NL:
            if self.prev_token in {
                self.RETURN, self.CONTINUE, self.BREAK,
                self.FLOATLIT, self.STRINGLIT, self.BOOLLIT, self.INTLIT,
                self.FLOAT, self.STRING,self.BOOLEAN, self.INT,
                self.RP, self.RB, self.RSB,self.ID
            }:
                self.type = self.SEMI
                self.text = ';'
                result = super().emit()
            else:
                return self.nextToken()
        else:
            result = super().emit()

        self.prev_token = result.type 
        return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            actions[72] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise UncloseString(self.text[:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise IllegalEscape(self.text[:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


