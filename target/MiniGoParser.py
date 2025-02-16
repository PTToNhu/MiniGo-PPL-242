# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u0262\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3\u009e\n\3\3\4\3\4\3\4\3\4\5\4\u00a4")
        buf.write("\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5\6\u00b0")
        buf.write("\n\6\3\7\3\7\5\7\u00b4\n\7\3\b\3\b\5\b\u00b8\n\b\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n\u00c3\n\n\3\n\3\n\3")
        buf.write("\n\3\n\5\n\u00c9\n\n\3\13\3\13\3\13\3\13\3\13\5\13\u00d0")
        buf.write("\n\13\3\13\3\13\3\13\3\13\5\13\u00d6\n\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5")
        buf.write("\r\u00e8\n\r\3\16\3\16\3\16\5\16\u00ed\n\16\3\17\3\17")
        buf.write("\3\20\3\20\5\20\u00f3\n\20\3\21\3\21\3\22\3\22\3\23\3")
        buf.write("\23\3\23\5\23\u00fc\n\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24\u0105\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\5\26\u0113\n\26\3\26\5\26")
        buf.write("\u0116\n\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u011f")
        buf.write("\n\26\3\26\5\26\u0122\n\26\5\26\u0124\n\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\5\27\u012c\n\27\3\27\3\27\3\30\3\30")
        buf.write("\5\30\u0132\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\5\31\u013e\n\31\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\5\33\u0148\n\33\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\5\34\u0153\n\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\5\35\u015b\n\35\3\36\3\36\3\36\3\36\3")
        buf.write("\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u017d\n$\3")
        buf.write("%\3%\5%\u0181\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\5(\u0194\n(\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("+\3+\3+\3+\5+\u01a1\n+\3,\3,\3,\3,\3,\3-\3-\3-\5-\u01ab")
        buf.write("\n-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\5\60\u01bb\n\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\5\66\u01d1\n\66\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\7\67\u01d9\n\67\f\67\16\67\u01dc\13\67\38\38\38\3")
        buf.write("8\38\38\78\u01e4\n8\f8\168\u01e7\138\39\39\39\39\39\3")
        buf.write("9\79\u01ef\n9\f9\169\u01f2\139\3:\3:\3:\3:\3:\3:\7:\u01fa")
        buf.write("\n:\f:\16:\u01fd\13:\3;\3;\3;\3;\3;\3;\7;\u0205\n;\f;")
        buf.write("\16;\u0208\13;\3<\3<\3<\5<\u020d\n<\3=\3=\3=\3=\3=\3=")
        buf.write("\3=\3=\5=\u0217\n=\3>\3>\3>\3>\3?\3?\5?\u021f\n?\3@\3")
        buf.write("@\3@\3@\3@\3A\3A\3A\3A\3A\3B\3B\5B\u022d\nB\3C\3C\3C\3")
        buf.write("C\3C\5C\u0234\nC\3D\3D\3D\5D\u0239\nD\3E\3E\3E\3E\3E\3")
        buf.write("F\3F\5F\u0242\nF\3G\3G\3G\3G\3G\3G\3G\3G\3G\5G\u024d\n")
        buf.write("G\3H\3H\3H\3I\3I\3I\3I\3I\3I\5I\u0258\nI\3I\3I\3J\3J\5")
        buf.write("J\u025e\nJ\3K\3K\3K\2\7lnprtL\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write("\u008c\u008e\u0090\u0092\u0094\2\f\4\288??\3\2\22\25\4")
        buf.write("\2::==\3\2).\4\2\3\3==\3\2 %\3\2\33\34\3\2\35\37\4\2\34")
        buf.write("\34((\4\2\4\4:<\2\u025c\2\u0096\3\2\2\2\4\u009d\3\2\2")
        buf.write("\2\6\u00a3\3\2\2\2\b\u00a7\3\2\2\2\n\u00af\3\2\2\2\f\u00b3")
        buf.write("\3\2\2\2\16\u00b7\3\2\2\2\20\u00b9\3\2\2\2\22\u00c8\3")
        buf.write("\2\2\2\24\u00d5\3\2\2\2\26\u00d7\3\2\2\2\30\u00e7\3\2")
        buf.write("\2\2\32\u00ec\3\2\2\2\34\u00ee\3\2\2\2\36\u00f2\3\2\2")
        buf.write("\2 \u00f4\3\2\2\2\"\u00f6\3\2\2\2$\u00f8\3\2\2\2&\u0104")
        buf.write("\3\2\2\2(\u0106\3\2\2\2*\u0123\3\2\2\2,\u0125\3\2\2\2")
        buf.write(".\u0131\3\2\2\2\60\u013d\3\2\2\2\62\u013f\3\2\2\2\64\u0147")
        buf.write("\3\2\2\2\66\u0152\3\2\2\28\u015a\3\2\2\2:\u015c\3\2\2")
        buf.write("\2<\u0160\3\2\2\2>\u0164\3\2\2\2@\u0168\3\2\2\2B\u016c")
        buf.write("\3\2\2\2D\u0170\3\2\2\2F\u017c\3\2\2\2H\u017e\3\2\2\2")
        buf.write("J\u0182\3\2\2\2L\u018b\3\2\2\2N\u0190\3\2\2\2P\u0195\3")
        buf.write("\2\2\2R\u0199\3\2\2\2T\u01a0\3\2\2\2V\u01a2\3\2\2\2X\u01aa")
        buf.write("\3\2\2\2Z\u01ac\3\2\2\2\\\u01b0\3\2\2\2^\u01ba\3\2\2\2")
        buf.write("`\u01bc\3\2\2\2b\u01bf\3\2\2\2d\u01c1\3\2\2\2f\u01ca\3")
        buf.write("\2\2\2h\u01cc\3\2\2\2j\u01d0\3\2\2\2l\u01d2\3\2\2\2n\u01dd")
        buf.write("\3\2\2\2p\u01e8\3\2\2\2r\u01f3\3\2\2\2t\u01fe\3\2\2\2")
        buf.write("v\u020c\3\2\2\2x\u0216\3\2\2\2z\u0218\3\2\2\2|\u021e\3")
        buf.write("\2\2\2~\u0220\3\2\2\2\u0080\u0225\3\2\2\2\u0082\u022c")
        buf.write("\3\2\2\2\u0084\u0233\3\2\2\2\u0086\u0238\3\2\2\2\u0088")
        buf.write("\u023a\3\2\2\2\u008a\u0241\3\2\2\2\u008c\u024c\3\2\2\2")
        buf.write("\u008e\u024e\3\2\2\2\u0090\u0251\3\2\2\2\u0092\u025d\3")
        buf.write("\2\2\2\u0094\u025f\3\2\2\2\u0096\u0097\5\4\3\2\u0097\u0098")
        buf.write("\7\2\2\3\u0098\3\3\2\2\2\u0099\u009a\5\6\4\2\u009a\u009b")
        buf.write("\5\4\3\2\u009b\u009e\3\2\2\2\u009c\u009e\3\2\2\2\u009d")
        buf.write("\u0099\3\2\2\2\u009d\u009c\3\2\2\2\u009e\5\3\2\2\2\u009f")
        buf.write("\u00a4\5\b\5\2\u00a0\u00a4\5\n\6\2\u00a1\u00a4\5\f\7\2")
        buf.write("\u00a2\u00a4\5\16\b\2\u00a3\u009f\3\2\2\2\u00a3\u00a0")
        buf.write("\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\u00a6\t\2\2\2\u00a6\7\3\2\2\2\u00a7")
        buf.write("\u00a8\7\r\2\2\u00a8\u00a9\7=\2\2\u00a9\u00aa\7/\2\2\u00aa")
        buf.write("\u00ab\5l\67\2\u00ab\t\3\2\2\2\u00ac\u00b0\5\22\n\2\u00ad")
        buf.write("\u00b0\5\20\t\2\u00ae\u00b0\5\24\13\2\u00af\u00ac\3\2")
        buf.write("\2\2\u00af\u00ad\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0\13")
        buf.write("\3\2\2\2\u00b1\u00b4\5\26\f\2\u00b2\u00b4\5(\25\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\r\3\2\2\2\u00b5")
        buf.write("\u00b8\5,\27\2\u00b6\u00b8\5J&\2\u00b7\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b6\3\2\2\2\u00b8\17\3\2\2\2\u00b9\u00ba\7\16\2\2\u00ba")
        buf.write("\u00bb\7=\2\2\u00bb\u00bc\5$\23\2\u00bc\21\3\2\2\2\u00bd")
        buf.write("\u00be\7\16\2\2\u00be\u00bf\7=\2\2\u00bf\u00c2\5\34\17")
        buf.write("\2\u00c0\u00c1\7/\2\2\u00c1\u00c3\5l\67\2\u00c2\u00c0")
        buf.write("\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c9\3\2\2\2\u00c4")
        buf.write("\u00c5\7\16\2\2\u00c5\u00c6\7=\2\2\u00c6\u00c7\7/\2\2")
        buf.write("\u00c7\u00c9\5l\67\2\u00c8\u00bd\3\2\2\2\u00c8\u00c4\3")
        buf.write("\2\2\2\u00c9\23\3\2\2\2\u00ca\u00cb\7\16\2\2\u00cb\u00cc")
        buf.write("\7=\2\2\u00cc\u00cf\5 \21\2\u00cd\u00ce\7)\2\2\u00ce\u00d0")
        buf.write("\5\u0088E\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write("\u00d6\3\2\2\2\u00d1\u00d2\7\16\2\2\u00d2\u00d3\7=\2\2")
        buf.write("\u00d3\u00d4\7)\2\2\u00d4\u00d6\5\u0088E\2\u00d5\u00ca")
        buf.write("\3\2\2\2\u00d5\u00d1\3\2\2\2\u00d6\25\3\2\2\2\u00d7\u00d8")
        buf.write("\7\n\2\2\u00d8\u00d9\7=\2\2\u00d9\u00da\7\13\2\2\u00da")
        buf.write("\u00db\7\65\2\2\u00db\u00dc\5\30\r\2\u00dc\u00dd\7\66")
        buf.write("\2\2\u00dd\27\3\2\2\2\u00de\u00df\7=\2\2\u00df\u00e0\5")
        buf.write("\32\16\2\u00e0\u00e1\t\2\2\2\u00e1\u00e2\5\30\r\2\u00e2")
        buf.write("\u00e8\3\2\2\2\u00e3\u00e4\7=\2\2\u00e4\u00e5\5\32\16")
        buf.write("\2\u00e5\u00e6\t\2\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00de")
        buf.write("\3\2\2\2\u00e7\u00e3\3\2\2\2\u00e8\31\3\2\2\2\u00e9\u00ed")
        buf.write("\5\34\17\2\u00ea\u00ed\5\36\20\2\u00eb\u00ed\5$\23\2\u00ec")
        buf.write("\u00e9\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2")
        buf.write("\u00ed\33\3\2\2\2\u00ee\u00ef\t\3\2\2\u00ef\35\3\2\2\2")
        buf.write("\u00f0\u00f3\5 \21\2\u00f1\u00f3\5\"\22\2\u00f2\u00f0")
        buf.write("\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3\37\3\2\2\2\u00f4\u00f5")
        buf.write("\7=\2\2\u00f5!\3\2\2\2\u00f6\u00f7\7=\2\2\u00f7#\3\2\2")
        buf.write("\2\u00f8\u00fb\5&\24\2\u00f9\u00fc\5\34\17\2\u00fa\u00fc")
        buf.write("\5\36\20\2\u00fb\u00f9\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc")
        buf.write("%\3\2\2\2\u00fd\u00fe\7\63\2\2\u00fe\u00ff\t\4\2\2\u00ff")
        buf.write("\u0100\7\64\2\2\u0100\u0105\5&\24\2\u0101\u0102\7\63\2")
        buf.write("\2\u0102\u0103\t\4\2\2\u0103\u0105\7\64\2\2\u0104\u00fd")
        buf.write("\3\2\2\2\u0104\u0101\3\2\2\2\u0105\'\3\2\2\2\u0106\u0107")
        buf.write("\7\n\2\2\u0107\u0108\7=\2\2\u0108\u0109\7\f\2\2\u0109")
        buf.write("\u010a\7\65\2\2\u010a\u010b\5*\26\2\u010b\u010c\7\66\2")
        buf.write("\2\u010c)\3\2\2\2\u010d\u010e\7=\2\2\u010e\u010f\7\61")
        buf.write("\2\2\u010f\u0110\5.\30\2\u0110\u0112\7\62\2\2\u0111\u0113")
        buf.write("\5\34\17\2\u0112\u0111\3\2\2\2\u0112\u0113\3\2\2\2\u0113")
        buf.write("\u0115\3\2\2\2\u0114\u0116\t\2\2\2\u0115\u0114\3\2\2\2")
        buf.write("\u0115\u0116\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\5")
        buf.write("*\26\2\u0118\u0124\3\2\2\2\u0119\u011a\7=\2\2\u011a\u011b")
        buf.write("\7\61\2\2\u011b\u011c\5.\30\2\u011c\u011e\7\62\2\2\u011d")
        buf.write("\u011f\5\34\17\2\u011e\u011d\3\2\2\2\u011e\u011f\3\2\2")
        buf.write("\2\u011f\u0121\3\2\2\2\u0120\u0122\t\2\2\2\u0121\u0120")
        buf.write("\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0124\3\2\2\2\u0123")
        buf.write("\u010d\3\2\2\2\u0123\u0119\3\2\2\2\u0124+\3\2\2\2\u0125")
        buf.write("\u0126\7\t\2\2\u0126\u0127\7=\2\2\u0127\u0128\7\61\2\2")
        buf.write("\u0128\u0129\5.\30\2\u0129\u012b\7\62\2\2\u012a\u012c")
        buf.write("\5\32\16\2\u012b\u012a\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("\u012d\3\2\2\2\u012d\u012e\5\62\32\2\u012e-\3\2\2\2\u012f")
        buf.write("\u0132\5\60\31\2\u0130\u0132\3\2\2\2\u0131\u012f\3\2\2")
        buf.write("\2\u0131\u0130\3\2\2\2\u0132/\3\2\2\2\u0133\u0134\7=\2")
        buf.write("\2\u0134\u0135\5\34\17\2\u0135\u0136\7\67\2\2\u0136\u0137")
        buf.write("\5\60\31\2\u0137\u013e\3\2\2\2\u0138\u0139\7=\2\2\u0139")
        buf.write("\u013a\7\67\2\2\u013a\u013e\5\60\31\2\u013b\u013c\7=\2")
        buf.write("\2\u013c\u013e\5\34\17\2\u013d\u0133\3\2\2\2\u013d\u0138")
        buf.write("\3\2\2\2\u013d\u013b\3\2\2\2\u013e\61\3\2\2\2\u013f\u0140")
        buf.write("\7\65\2\2\u0140\u0141\5\64\33\2\u0141\u0142\7\66\2\2\u0142")
        buf.write("\63\3\2\2\2\u0143\u0144\5\66\34\2\u0144\u0145\5\64\33")
        buf.write("\2\u0145\u0148\3\2\2\2\u0146\u0148\5\66\34\2\u0147\u0143")
        buf.write("\3\2\2\2\u0147\u0146\3\2\2\2\u0148\65\3\2\2\2\u0149\u0153")
        buf.write("\5H%\2\u014a\u0153\5\b\5\2\u014b\u0153\5\n\6\2\u014c\u0153")
        buf.write("\58\35\2\u014d\u0153\5N(\2\u014e\u0153\5X-\2\u014f\u0153")
        buf.write("\5j\66\2\u0150\u0153\5f\64\2\u0151\u0153\5h\65\2\u0152")
        buf.write("\u0149\3\2\2\2\u0152\u014a\3\2\2\2\u0152\u014b\3\2\2\2")
        buf.write("\u0152\u014c\3\2\2\2\u0152\u014d\3\2\2\2\u0152\u014e\3")
        buf.write("\2\2\2\u0152\u014f\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0151")
        buf.write("\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155\t\2\2\2\u0155")
        buf.write("\67\3\2\2\2\u0156\u015b\5:\36\2\u0157\u015b\5<\37\2\u0158")
        buf.write("\u015b\5> \2\u0159\u015b\5@!\2\u015a\u0156\3\2\2\2\u015a")
        buf.write("\u0157\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u0159\3\2\2\2")
        buf.write("\u015b9\3\2\2\2\u015c\u015d\7=\2\2\u015d\u015e\t\5\2\2")
        buf.write("\u015e\u015f\5l\67\2\u015f;\3\2\2\2\u0160\u0161\5B\"\2")
        buf.write("\u0161\u0162\t\5\2\2\u0162\u0163\5l\67\2\u0163=\3\2\2")
        buf.write("\2\u0164\u0165\5D#\2\u0165\u0166\t\5\2\2\u0166\u0167\5")
        buf.write("l\67\2\u0167?\3\2\2\2\u0168\u0169\7=\2\2\u0169\u016a\7")
        buf.write(")\2\2\u016a\u016b\5\u0088E\2\u016bA\3\2\2\2\u016c\u016d")
        buf.write("\7=\2\2\u016d\u016e\7\60\2\2\u016e\u016f\7=\2\2\u016f")
        buf.write("C\3\2\2\2\u0170\u0171\7=\2\2\u0171\u0172\5F$\2\u0172E")
        buf.write("\3\2\2\2\u0173\u0174\7\63\2\2\u0174\u0175\5l\67\2\u0175")
        buf.write("\u0176\7\64\2\2\u0176\u0177\5F$\2\u0177\u017d\3\2\2\2")
        buf.write("\u0178\u0179\7\63\2\2\u0179\u017a\5l\67\2\u017a\u017b")
        buf.write("\7\64\2\2\u017b\u017d\3\2\2\2\u017c\u0173\3\2\2\2\u017c")
        buf.write("\u0178\3\2\2\2\u017dG\3\2\2\2\u017e\u0180\7\b\2\2\u017f")
        buf.write("\u0181\5l\67\2\u0180\u017f\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181I\3\2\2\2\u0182\u0183\7\t\2\2\u0183\u0184\5L\'\2")
        buf.write("\u0184\u0185\7=\2\2\u0185\u0186\7\61\2\2\u0186\u0187\5")
        buf.write(".\30\2\u0187\u0188\7\62\2\2\u0188\u0189\5\32\16\2\u0189")
        buf.write("\u018a\5\62\32\2\u018aK\3\2\2\2\u018b\u018c\7\61\2\2\u018c")
        buf.write("\u018d\7=\2\2\u018d\u018e\5\36\20\2\u018e\u018f\7\62\2")
        buf.write("\2\u018fM\3\2\2\2\u0190\u0191\5P)\2\u0191\u0193\5T+\2")
        buf.write("\u0192\u0194\5R*\2\u0193\u0192\3\2\2\2\u0193\u0194\3\2")
        buf.write("\2\2\u0194O\3\2\2\2\u0195\u0196\7\5\2\2\u0196\u0197\5")
        buf.write("z>\2\u0197\u0198\5\62\32\2\u0198Q\3\2\2\2\u0199\u019a")
        buf.write("\7\6\2\2\u019a\u019b\5\62\32\2\u019bS\3\2\2\2\u019c\u019d")
        buf.write("\5V,\2\u019d\u019e\5T+\2\u019e\u01a1\3\2\2\2\u019f\u01a1")
        buf.write("\3\2\2\2\u01a0\u019c\3\2\2\2\u01a0\u019f\3\2\2\2\u01a1")
        buf.write("U\3\2\2\2\u01a2\u01a3\7\6\2\2\u01a3\u01a4\7\5\2\2\u01a4")
        buf.write("\u01a5\5z>\2\u01a5\u01a6\5\62\32\2\u01a6W\3\2\2\2\u01a7")
        buf.write("\u01ab\5Z.\2\u01a8\u01ab\5\\/\2\u01a9\u01ab\5d\63\2\u01aa")
        buf.write("\u01a7\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9\3\2\2\2")
        buf.write("\u01abY\3\2\2\2\u01ac\u01ad\7\7\2\2\u01ad\u01ae\5z>\2")
        buf.write("\u01ae\u01af\5\62\32\2\u01af[\3\2\2\2\u01b0\u01b1\7\7")
        buf.write("\2\2\u01b1\u01b2\5^\60\2\u01b2\u01b3\5`\61\2\u01b3\u01b4")
        buf.write("\5b\62\2\u01b4\u01b5\5\62\32\2\u01b5]\3\2\2\2\u01b6\u01b7")
        buf.write("\5:\36\2\u01b7\u01b8\78\2\2\u01b8\u01bb\3\2\2\2\u01b9")
        buf.write("\u01bb\5\22\n\2\u01ba\u01b6\3\2\2\2\u01ba\u01b9\3\2\2")
        buf.write("\2\u01bb_\3\2\2\2\u01bc\u01bd\5l\67\2\u01bd\u01be\78\2")
        buf.write("\2\u01bea\3\2\2\2\u01bf\u01c0\5:\36\2\u01c0c\3\2\2\2\u01c1")
        buf.write("\u01c2\7\7\2\2\u01c2\u01c3\t\6\2\2\u01c3\u01c4\7\67\2")
        buf.write("\2\u01c4\u01c5\7=\2\2\u01c5\u01c6\7)\2\2\u01c6\u01c7\7")
        buf.write("\21\2\2\u01c7\u01c8\5l\67\2\u01c8\u01c9\5\62\32\2\u01c9")
        buf.write("e\3\2\2\2\u01ca\u01cb\7\20\2\2\u01cbg\3\2\2\2\u01cc\u01cd")
        buf.write("\7\17\2\2\u01cdi\3\2\2\2\u01ce\u01d1\5~@\2\u01cf\u01d1")
        buf.write("\5\u0080A\2\u01d0\u01ce\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1")
        buf.write("k\3\2\2\2\u01d2\u01d3\b\67\1\2\u01d3\u01d4\5n8\2\u01d4")
        buf.write("\u01da\3\2\2\2\u01d5\u01d6\f\4\2\2\u01d6\u01d7\7\'\2\2")
        buf.write("\u01d7\u01d9\5n8\2\u01d8\u01d5\3\2\2\2\u01d9\u01dc\3\2")
        buf.write("\2\2\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01dbm\3")
        buf.write("\2\2\2\u01dc\u01da\3\2\2\2\u01dd\u01de\b8\1\2\u01de\u01df")
        buf.write("\5p9\2\u01df\u01e5\3\2\2\2\u01e0\u01e1\f\4\2\2\u01e1\u01e2")
        buf.write("\7&\2\2\u01e2\u01e4\5p9\2\u01e3\u01e0\3\2\2\2\u01e4\u01e7")
        buf.write("\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6")
        buf.write("o\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01e9\b9\1\2\u01e9")
        buf.write("\u01ea\5r:\2\u01ea\u01f0\3\2\2\2\u01eb\u01ec\f\4\2\2\u01ec")
        buf.write("\u01ed\t\7\2\2\u01ed\u01ef\5r:\2\u01ee\u01eb\3\2\2\2\u01ef")
        buf.write("\u01f2\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2")
        buf.write("\u01f1q\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f3\u01f4\b:\1\2")
        buf.write("\u01f4\u01f5\5t;\2\u01f5\u01fb\3\2\2\2\u01f6\u01f7\f\4")
        buf.write("\2\2\u01f7\u01f8\t\b\2\2\u01f8\u01fa\5t;\2\u01f9\u01f6")
        buf.write("\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb")
        buf.write("\u01fc\3\2\2\2\u01fcs\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe")
        buf.write("\u01ff\b;\1\2\u01ff\u0200\5v<\2\u0200\u0206\3\2\2\2\u0201")
        buf.write("\u0202\f\4\2\2\u0202\u0203\t\t\2\2\u0203\u0205\5v<\2\u0204")
        buf.write("\u0201\3\2\2\2\u0205\u0208\3\2\2\2\u0206\u0204\3\2\2\2")
        buf.write("\u0206\u0207\3\2\2\2\u0207u\3\2\2\2\u0208\u0206\3\2\2")
        buf.write("\2\u0209\u020a\t\n\2\2\u020a\u020d\5v<\2\u020b\u020d\5")
        buf.write("x=\2\u020c\u0209\3\2\2\2\u020c\u020b\3\2\2\2\u020dw\3")
        buf.write("\2\2\2\u020e\u0217\5\u0094K\2\u020f\u0217\5\u008eH\2\u0210")
        buf.write("\u0217\5\u0088E\2\u0211\u0217\5z>\2\u0212\u0217\7=\2\2")
        buf.write("\u0213\u0217\5B\"\2\u0214\u0217\5D#\2\u0215\u0217\5|?")
        buf.write("\2\u0216\u020e\3\2\2\2\u0216\u020f\3\2\2\2\u0216\u0210")
        buf.write("\3\2\2\2\u0216\u0211\3\2\2\2\u0216\u0212\3\2\2\2\u0216")
        buf.write("\u0213\3\2\2\2\u0216\u0214\3\2\2\2\u0216\u0215\3\2\2\2")
        buf.write("\u0217y\3\2\2\2\u0218\u0219\7\61\2\2\u0219\u021a\5l\67")
        buf.write("\2\u021a\u021b\7\62\2\2\u021b{\3\2\2\2\u021c\u021f\5~")
        buf.write("@\2\u021d\u021f\5\u0080A\2\u021e\u021c\3\2\2\2\u021e\u021d")
        buf.write("\3\2\2\2\u021f}\3\2\2\2\u0220\u0221\5B\"\2\u0221\u0222")
        buf.write("\7\61\2\2\u0222\u0223\5\u0082B\2\u0223\u0224\7\62\2\2")
        buf.write("\u0224\177\3\2\2\2\u0225\u0226\7=\2\2\u0226\u0227\7\61")
        buf.write("\2\2\u0227\u0228\5\u0082B\2\u0228\u0229\7\62\2\2\u0229")
        buf.write("\u0081\3\2\2\2\u022a\u022d\5\u0084C\2\u022b\u022d\3\2")
        buf.write("\2\2\u022c\u022a\3\2\2\2\u022c\u022b\3\2\2\2\u022d\u0083")
        buf.write("\3\2\2\2\u022e\u022f\5l\67\2\u022f\u0230\7\67\2\2\u0230")
        buf.write("\u0231\5\u0084C\2\u0231\u0234\3\2\2\2\u0232\u0234\5l\67")
        buf.write("\2\u0233\u022e\3\2\2\2\u0233\u0232\3\2\2\2\u0234\u0085")
        buf.write("\3\2\2\2\u0235\u0239\5\u0094K\2\u0236\u0239\5\u008eH\2")
        buf.write("\u0237\u0239\5\u0088E\2\u0238\u0235\3\2\2\2\u0238\u0236")
        buf.write("\3\2\2\2\u0238\u0237\3\2\2\2\u0239\u0087\3\2\2\2\u023a")
        buf.write("\u023b\5 \21\2\u023b\u023c\7\65\2\2\u023c\u023d\5\u008a")
        buf.write("F\2\u023d\u023e\7\66\2\2\u023e\u0089\3\2\2\2\u023f\u0242")
        buf.write("\5\u008cG\2\u0240\u0242\3\2\2\2\u0241\u023f\3\2\2\2\u0241")
        buf.write("\u0240\3\2\2\2\u0242\u008b\3\2\2\2\u0243\u0244\7=\2\2")
        buf.write("\u0244\u0245\79\2\2\u0245\u0246\5l\67\2\u0246\u0247\7")
        buf.write("\67\2\2\u0247\u0248\5\u008cG\2\u0248\u024d\3\2\2\2\u0249")
        buf.write("\u024a\7=\2\2\u024a\u024b\79\2\2\u024b\u024d\5l\67\2\u024c")
        buf.write("\u0243\3\2\2\2\u024c\u0249\3\2\2\2\u024d\u008d\3\2\2\2")
        buf.write("\u024e\u024f\5$\23\2\u024f\u0250\5\u0090I\2\u0250\u008f")
        buf.write("\3\2\2\2\u0251\u0257\7\65\2\2\u0252\u0253\5\u0092J\2\u0253")
        buf.write("\u0254\7\67\2\2\u0254\u0255\5\u0090I\2\u0255\u0258\3\2")
        buf.write("\2\2\u0256\u0258\5\u0092J\2\u0257\u0252\3\2\2\2\u0257")
        buf.write("\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u025a\7\66\2")
        buf.write("\2\u025a\u0091\3\2\2\2\u025b\u025e\5\u0090I\2\u025c\u025e")
        buf.write("\5l\67\2\u025d\u025b\3\2\2\2\u025d\u025c\3\2\2\2\u025e")
        buf.write("\u0093\3\2\2\2\u025f\u0260\t\13\2\2\u0260\u0095\3\2\2")
        buf.write("\2\61\u009d\u00a3\u00af\u00b3\u00b7\u00c2\u00c8\u00cf")
        buf.write("\u00d5\u00e7\u00ec\u00f2\u00fb\u0104\u0112\u0115\u011e")
        buf.write("\u0121\u0123\u012b\u0131\u013d\u0147\u0152\u015a\u017c")
        buf.write("\u0180\u0193\u01a0\u01aa\u01ba\u01d0\u01da\u01e5\u01f0")
        buf.write("\u01fb\u0206\u020c\u0216\u021e\u022c\u0233\u0238\u0241")
        buf.write("\u024c\u0257\u025d")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'_'", "<INVALID>", "'if'", "'else'", 
                     "'for'", "'return'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'const'", "'var'", "'continue'", "'break'", 
                     "'range'", "'int'", "'float'", "'string'", "'boolean'", 
                     "'nil'", "'true'", "'false'", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
                     "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'='", 
                     "'.'", "'('", "')'", "'['", "']'", "'{'", "'}'", "','", 
                     "';'", "':'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BOOLLIT", "IF", "ELSE", 
                      "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "INT", 
                      "FLOAT", "STRING", "BOOLEAN", "NIL", "TRUE", "FALSE", 
                      "COMMENT", "LINE_COMMENT", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQUAL", "N_EQUAL", "LESS", "L_EQUAL", "GREATER", 
                      "G_EQUAL", "AND", "OR", "NOT", "ASSIGNMENT", "ADDASS", 
                      "SUBASS", "MULASS", "DIVASS", "MODASS", "ASSIGN", 
                      "DOT", "LP", "RP", "LSB", "RSB", "LB", "RB", "COMMA", 
                      "SEMI", "COLON", "INTLIT", "FLOATLIT", "STRINGLIT", 
                      "ID", "WS", "NL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_decl = 2
    RULE_const_decl = 3
    RULE_var_decl = 4
    RULE_type_decl = 5
    RULE_func_decl = 6
    RULE_array_decl = 7
    RULE_scalar_decl = 8
    RULE_struct_var_decl = 9
    RULE_struct_decl = 10
    RULE_fieldnamelist = 11
    RULE_datatype = 12
    RULE_primitivetype = 13
    RULE_compositetype = 14
    RULE_structtype = 15
    RULE_interfacetype = 16
    RULE_arraytype = 17
    RULE_dimensions = 18
    RULE_interface_decl = 19
    RULE_methodlist = 20
    RULE_func = 21
    RULE_paramlist = 22
    RULE_paramprime = 23
    RULE_body = 24
    RULE_stmtlist = 25
    RULE_stmt = 26
    RULE_assignstmt = 27
    RULE_scalaassign = 28
    RULE_fieldassign = 29
    RULE_arrayassign = 30
    RULE_struct_instance = 31
    RULE_fieldaccess = 32
    RULE_arrayaccess = 33
    RULE_dimensions_stmt = 34
    RULE_returnstmt = 35
    RULE_method = 36
    RULE_receiver = 37
    RULE_ifstmt = 38
    RULE_if_clause = 39
    RULE_else_clause = 40
    RULE_elseif_clauselist = 41
    RULE_elseif_clause = 42
    RULE_forstmt = 43
    RULE_forbasic = 44
    RULE_foricu = 45
    RULE_initialization_clause = 46
    RULE_condition_clause = 47
    RULE_update_clause = 48
    RULE_forrange = 49
    RULE_breakstmt = 50
    RULE_continuestmt = 51
    RULE_callstmt = 52
    RULE_expr = 53
    RULE_expr1 = 54
    RULE_expr2 = 55
    RULE_expr3 = 56
    RULE_expr4 = 57
    RULE_expr5 = 58
    RULE_expr6 = 59
    RULE_subexpr = 60
    RULE_call = 61
    RULE_struct_call = 62
    RULE_func_call = 63
    RULE_argumentlist = 64
    RULE_argumentprime = 65
    RULE_literals = 66
    RULE_structliteral = 67
    RULE_fieldvaluelist = 68
    RULE_fieldvalueprime = 69
    RULE_arrayliteral = 70
    RULE_elementlist = 71
    RULE_element = 72
    RULE_primitive_literals = 73

    ruleNames =  [ "program", "decls", "decl", "const_decl", "var_decl", 
                   "type_decl", "func_decl", "array_decl", "scalar_decl", 
                   "struct_var_decl", "struct_decl", "fieldnamelist", "datatype", 
                   "primitivetype", "compositetype", "structtype", "interfacetype", 
                   "arraytype", "dimensions", "interface_decl", "methodlist", 
                   "func", "paramlist", "paramprime", "body", "stmtlist", 
                   "stmt", "assignstmt", "scalaassign", "fieldassign", "arrayassign", 
                   "struct_instance", "fieldaccess", "arrayaccess", "dimensions_stmt", 
                   "returnstmt", "method", "receiver", "ifstmt", "if_clause", 
                   "else_clause", "elseif_clauselist", "elseif_clause", 
                   "forstmt", "forbasic", "foricu", "initialization_clause", 
                   "condition_clause", "update_clause", "forrange", "breakstmt", 
                   "continuestmt", "callstmt", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "subexpr", "call", 
                   "struct_call", "func_call", "argumentlist", "argumentprime", 
                   "literals", "structliteral", "fieldvaluelist", "fieldvalueprime", 
                   "arrayliteral", "elementlist", "element", "primitive_literals" ]

    EOF = Token.EOF
    T__0=1
    BOOLLIT=2
    IF=3
    ELSE=4
    FOR=5
    RETURN=6
    FUNC=7
    TYPE=8
    STRUCT=9
    INTERFACE=10
    CONST=11
    VAR=12
    CONTINUE=13
    BREAK=14
    RANGE=15
    INT=16
    FLOAT=17
    STRING=18
    BOOLEAN=19
    NIL=20
    TRUE=21
    FALSE=22
    COMMENT=23
    LINE_COMMENT=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    MOD=29
    EQUAL=30
    N_EQUAL=31
    LESS=32
    L_EQUAL=33
    GREATER=34
    G_EQUAL=35
    AND=36
    OR=37
    NOT=38
    ASSIGNMENT=39
    ADDASS=40
    SUBASS=41
    MULASS=42
    DIVASS=43
    MODASS=44
    ASSIGN=45
    DOT=46
    LP=47
    RP=48
    LSB=49
    RSB=50
    LB=51
    RB=52
    COMMA=53
    SEMI=54
    COLON=55
    INTLIT=56
    FLOATLIT=57
    STRINGLIT=58
    ID=59
    WS=60
    NL=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    ERROR_CHAR=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decls(self):
            return self.getTypedRuleContext(MiniGoParser.DeclsContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.decls()
            self.state = 149
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(MiniGoParser.DeclsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = MiniGoParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.decl()
                self.state = 152
                self.decls()
                pass
            elif token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def type_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Type_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.CONST]:
                self.state = 157
                self.const_decl()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 158
                self.var_decl()
                pass
            elif token in [MiniGoParser.TYPE]:
                self.state = 159
                self.type_decl()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.state = 160
                self.func_decl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 163
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(MiniGoParser.CONST)
            self.state = 166
            self.match(MiniGoParser.ID)
            self.state = 167
            self.match(MiniGoParser.ASSIGN)
            self.state = 168
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Scalar_declContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declContext,0)


        def struct_var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_var_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.scalar_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.array_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                self.struct_var_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_decl" ):
                return visitor.visitType_decl(self)
            else:
                return visitor.visitChildren(self)




    def type_decl(self):

        localctx = MiniGoParser.Type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type_decl)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.struct_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.interface_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func(self):
            return self.getTypedRuleContext(MiniGoParser.FuncContext,0)


        def method(self):
            return self.getTypedRuleContext(MiniGoParser.MethodContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func_decl)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arraytype(self):
            return self.getTypedRuleContext(MiniGoParser.ArraytypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = MiniGoParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(MiniGoParser.VAR)
            self.state = 184
            self.match(MiniGoParser.ID)
            self.state = 185
            self.arraytype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def primitivetype(self):
            return self.getTypedRuleContext(MiniGoParser.PrimitivetypeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_scalar_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_decl" ):
                return visitor.visitScalar_decl(self)
            else:
                return visitor.visitChildren(self)




    def scalar_decl(self):

        localctx = MiniGoParser.Scalar_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_scalar_decl)
        self._la = 0 # Token type
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(MiniGoParser.VAR)
                self.state = 188
                self.match(MiniGoParser.ID)
                self.state = 189
                self.primitivetype()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 190
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 191
                    self.expr(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(MiniGoParser.VAR)
                self.state = 195
                self.match(MiniGoParser.ID)
                self.state = 196
                self.match(MiniGoParser.ASSIGN)
                self.state = 197
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def structtype(self):
            return self.getTypedRuleContext(MiniGoParser.StructtypeContext,0)


        def ASSIGNMENT(self):
            return self.getToken(MiniGoParser.ASSIGNMENT, 0)

        def structliteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructliteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_var_decl" ):
                return visitor.visitStruct_var_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_var_decl(self):

        localctx = MiniGoParser.Struct_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_struct_var_decl)
        self._la = 0 # Token type
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(MiniGoParser.VAR)
                self.state = 201
                self.match(MiniGoParser.ID)
                self.state = 202
                self.structtype()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGNMENT:
                    self.state = 203
                    self.match(MiniGoParser.ASSIGNMENT)
                    self.state = 204
                    self.structliteral()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.match(MiniGoParser.VAR)
                self.state = 208
                self.match(MiniGoParser.ID)
                self.state = 209
                self.match(MiniGoParser.ASSIGNMENT)
                self.state = 210
                self.structliteral()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def fieldnamelist(self):
            return self.getTypedRuleContext(MiniGoParser.FieldnamelistContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(MiniGoParser.TYPE)
            self.state = 214
            self.match(MiniGoParser.ID)
            self.state = 215
            self.match(MiniGoParser.STRUCT)
            self.state = 216
            self.match(MiniGoParser.LB)
            self.state = 217
            self.fieldnamelist()
            self.state = 218
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldnamelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def datatype(self):
            return self.getTypedRuleContext(MiniGoParser.DatatypeContext,0)


        def fieldnamelist(self):
            return self.getTypedRuleContext(MiniGoParser.FieldnamelistContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldnamelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldnamelist" ):
                return visitor.visitFieldnamelist(self)
            else:
                return visitor.visitChildren(self)




    def fieldnamelist(self):

        localctx = MiniGoParser.FieldnamelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_fieldnamelist)
        self._la = 0 # Token type
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(MiniGoParser.ID)
                self.state = 221
                self.datatype()
                self.state = 222
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                self.fieldnamelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.match(MiniGoParser.ID)
                self.state = 226
                self.datatype()
                self.state = 227
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatatypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitivetype(self):
            return self.getTypedRuleContext(MiniGoParser.PrimitivetypeContext,0)


        def compositetype(self):
            return self.getTypedRuleContext(MiniGoParser.CompositetypeContext,0)


        def arraytype(self):
            return self.getTypedRuleContext(MiniGoParser.ArraytypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_datatype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDatatype" ):
                return visitor.visitDatatype(self)
            else:
                return visitor.visitChildren(self)




    def datatype(self):

        localctx = MiniGoParser.DatatypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_datatype)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.STRING, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.primitivetype()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.compositetype()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 233
                self.arraytype()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitivetypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitivetype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitivetype" ):
                return visitor.visitPrimitivetype(self)
            else:
                return visitor.visitChildren(self)




    def primitivetype(self):

        localctx = MiniGoParser.PrimitivetypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_primitivetype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompositetypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structtype(self):
            return self.getTypedRuleContext(MiniGoParser.StructtypeContext,0)


        def interfacetype(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacetypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_compositetype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompositetype" ):
                return visitor.visitCompositetype(self)
            else:
                return visitor.visitChildren(self)




    def compositetype(self):

        localctx = MiniGoParser.CompositetypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_compositetype)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.structtype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.interfacetype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructtype" ):
                return visitor.visitStructtype(self)
            else:
                return visitor.visitChildren(self)




    def structtype(self):

        localctx = MiniGoParser.StructtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_structtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacetypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacetype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacetype" ):
                return visitor.visitInterfacetype(self)
            else:
                return visitor.visitChildren(self)




    def interfacetype(self):

        localctx = MiniGoParser.InterfacetypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_interfacetype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionsContext,0)


        def primitivetype(self):
            return self.getTypedRuleContext(MiniGoParser.PrimitivetypeContext,0)


        def compositetype(self):
            return self.getTypedRuleContext(MiniGoParser.CompositetypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = MiniGoParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.dimensions()
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.STRING, MiniGoParser.BOOLEAN]:
                self.state = 247
                self.primitivetype()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 248
                self.compositetype()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionsContext,0)


        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




    def dimensions(self):

        localctx = MiniGoParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_dimensions)
        self._la = 0 # Token type
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(MiniGoParser.LSB)
                self.state = 252
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.INTLIT or _la==MiniGoParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 253
                self.match(MiniGoParser.RSB)
                self.state = 254
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(MiniGoParser.LSB)
                self.state = 256
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.INTLIT or _la==MiniGoParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 257
                self.match(MiniGoParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def methodlist(self):
            return self.getTypedRuleContext(MiniGoParser.MethodlistContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(MiniGoParser.TYPE)
            self.state = 261
            self.match(MiniGoParser.ID)
            self.state = 262
            self.match(MiniGoParser.INTERFACE)
            self.state = 263
            self.match(MiniGoParser.LB)
            self.state = 264
            self.methodlist()
            self.state = 265
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def methodlist(self):
            return self.getTypedRuleContext(MiniGoParser.MethodlistContext,0)


        def primitivetype(self):
            return self.getTypedRuleContext(MiniGoParser.PrimitivetypeContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodlist" ):
                return visitor.visitMethodlist(self)
            else:
                return visitor.visitChildren(self)




    def methodlist(self):

        localctx = MiniGoParser.MethodlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_methodlist)
        self._la = 0 # Token type
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(MiniGoParser.ID)
                self.state = 268
                self.match(MiniGoParser.LP)
                self.state = 269
                self.paramlist()
                self.state = 270
                self.match(MiniGoParser.RP)
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.BOOLEAN))) != 0):
                    self.state = 271
                    self.primitivetype()


                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.SEMI or _la==MiniGoParser.NL:
                    self.state = 274
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 277
                self.methodlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.match(MiniGoParser.ID)
                self.state = 280
                self.match(MiniGoParser.LP)
                self.state = 281
                self.paramlist()
                self.state = 282
                self.match(MiniGoParser.RP)
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.BOOLEAN))) != 0):
                    self.state = 283
                    self.primitivetype()


                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.SEMI or _la==MiniGoParser.NL:
                    self.state = 286
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def body(self):
            return self.getTypedRuleContext(MiniGoParser.BodyContext,0)


        def datatype(self):
            return self.getTypedRuleContext(MiniGoParser.DatatypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = MiniGoParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(MiniGoParser.FUNC)
            self.state = 292
            self.match(MiniGoParser.ID)
            self.state = 293
            self.match(MiniGoParser.LP)
            self.state = 294
            self.paramlist()
            self.state = 295
            self.match(MiniGoParser.RP)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 296
                self.datatype()


            self.state = 299
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(MiniGoParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = MiniGoParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_paramlist)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.paramprime()
                pass
            elif token in [MiniGoParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def primitivetype(self):
            return self.getTypedRuleContext(MiniGoParser.PrimitivetypeContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def paramprime(self):
            return self.getTypedRuleContext(MiniGoParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = MiniGoParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_paramprime)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.match(MiniGoParser.ID)
                self.state = 306
                self.primitivetype()
                self.state = 307
                self.match(MiniGoParser.COMMA)
                self.state = 308
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.match(MiniGoParser.ID)
                self.state = 311
                self.match(MiniGoParser.COMMA)
                self.state = 312
                self.paramprime()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 313
                self.match(MiniGoParser.ID)
                self.state = 314
                self.primitivetype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(MiniGoParser.StmtlistContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MiniGoParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(MiniGoParser.LB)
            self.state = 318
            self.stmtlist()
            self.state = 319
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(MiniGoParser.StmtlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = MiniGoParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_stmtlist)
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.stmt()
                self.state = 322
                self.stmtlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def returnstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnstmtContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(MiniGoParser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ForstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(MiniGoParser.CallstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MiniGoParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(MiniGoParser.ContinuestmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 327
                self.returnstmt()
                pass

            elif la_ == 2:
                self.state = 328
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 329
                self.var_decl()
                pass

            elif la_ == 4:
                self.state = 330
                self.assignstmt()
                pass

            elif la_ == 5:
                self.state = 331
                self.ifstmt()
                pass

            elif la_ == 6:
                self.state = 332
                self.forstmt()
                pass

            elif la_ == 7:
                self.state = 333
                self.callstmt()
                pass

            elif la_ == 8:
                self.state = 334
                self.breakstmt()
                pass

            elif la_ == 9:
                self.state = 335
                self.continuestmt()
                pass


            self.state = 338
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalaassign(self):
            return self.getTypedRuleContext(MiniGoParser.ScalaassignContext,0)


        def fieldassign(self):
            return self.getTypedRuleContext(MiniGoParser.FieldassignContext,0)


        def arrayassign(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayassignContext,0)


        def struct_instance(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_instanceContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MiniGoParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 340
                self.scalaassign()
                pass

            elif la_ == 2:
                self.state = 341
                self.fieldassign()
                pass

            elif la_ == 3:
                self.state = 342
                self.arrayassign()
                pass

            elif la_ == 4:
                self.state = 343
                self.struct_instance()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalaassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def ASSIGNMENT(self):
            return self.getToken(MiniGoParser.ASSIGNMENT, 0)

        def ADDASS(self):
            return self.getToken(MiniGoParser.ADDASS, 0)

        def SUBASS(self):
            return self.getToken(MiniGoParser.SUBASS, 0)

        def MULASS(self):
            return self.getToken(MiniGoParser.MULASS, 0)

        def DIVASS(self):
            return self.getToken(MiniGoParser.DIVASS, 0)

        def MODASS(self):
            return self.getToken(MiniGoParser.MODASS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_scalaassign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalaassign" ):
                return visitor.visitScalaassign(self)
            else:
                return visitor.visitChildren(self)




    def scalaassign(self):

        localctx = MiniGoParser.ScalaassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_scalaassign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(MiniGoParser.ID)
            self.state = 347
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGNMENT) | (1 << MiniGoParser.ADDASS) | (1 << MiniGoParser.SUBASS) | (1 << MiniGoParser.MULASS) | (1 << MiniGoParser.DIVASS) | (1 << MiniGoParser.MODASS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 348
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldaccess(self):
            return self.getTypedRuleContext(MiniGoParser.FieldaccessContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def ASSIGNMENT(self):
            return self.getToken(MiniGoParser.ASSIGNMENT, 0)

        def ADDASS(self):
            return self.getToken(MiniGoParser.ADDASS, 0)

        def SUBASS(self):
            return self.getToken(MiniGoParser.SUBASS, 0)

        def MULASS(self):
            return self.getToken(MiniGoParser.MULASS, 0)

        def DIVASS(self):
            return self.getToken(MiniGoParser.DIVASS, 0)

        def MODASS(self):
            return self.getToken(MiniGoParser.MODASS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldassign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldassign" ):
                return visitor.visitFieldassign(self)
            else:
                return visitor.visitChildren(self)




    def fieldassign(self):

        localctx = MiniGoParser.FieldassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_fieldassign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.fieldaccess()
            self.state = 351
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGNMENT) | (1 << MiniGoParser.ADDASS) | (1 << MiniGoParser.SUBASS) | (1 << MiniGoParser.MULASS) | (1 << MiniGoParser.DIVASS) | (1 << MiniGoParser.MODASS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 352
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayaccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayaccessContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def ASSIGNMENT(self):
            return self.getToken(MiniGoParser.ASSIGNMENT, 0)

        def ADDASS(self):
            return self.getToken(MiniGoParser.ADDASS, 0)

        def SUBASS(self):
            return self.getToken(MiniGoParser.SUBASS, 0)

        def MULASS(self):
            return self.getToken(MiniGoParser.MULASS, 0)

        def DIVASS(self):
            return self.getToken(MiniGoParser.DIVASS, 0)

        def MODASS(self):
            return self.getToken(MiniGoParser.MODASS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayassign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayassign" ):
                return visitor.visitArrayassign(self)
            else:
                return visitor.visitChildren(self)




    def arrayassign(self):

        localctx = MiniGoParser.ArrayassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_arrayassign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.arrayaccess()
            self.state = 355
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGNMENT) | (1 << MiniGoParser.ADDASS) | (1 << MiniGoParser.SUBASS) | (1 << MiniGoParser.MULASS) | (1 << MiniGoParser.DIVASS) | (1 << MiniGoParser.MODASS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 356
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_instanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGNMENT(self):
            return self.getToken(MiniGoParser.ASSIGNMENT, 0)

        def structliteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructliteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_instance

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_instance" ):
                return visitor.visitStruct_instance(self)
            else:
                return visitor.visitChildren(self)




    def struct_instance(self):

        localctx = MiniGoParser.Struct_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_struct_instance)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(MiniGoParser.ID)
            self.state = 359
            self.match(MiniGoParser.ASSIGNMENT)
            self.state = 360
            self.structliteral()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldaccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldaccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldaccess" ):
                return visitor.visitFieldaccess(self)
            else:
                return visitor.visitChildren(self)




    def fieldaccess(self):

        localctx = MiniGoParser.FieldaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_fieldaccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(MiniGoParser.ID)
            self.state = 363
            self.match(MiniGoParser.DOT)
            self.state = 364
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayaccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def dimensions_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Dimensions_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayaccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayaccess" ):
                return visitor.visitArrayaccess(self)
            else:
                return visitor.visitChildren(self)




    def arrayaccess(self):

        localctx = MiniGoParser.ArrayaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arrayaccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(MiniGoParser.ID)
            self.state = 367
            self.dimensions_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimensions_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def dimensions_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Dimensions_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dimensions_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions_stmt" ):
                return visitor.visitDimensions_stmt(self)
            else:
                return visitor.visitChildren(self)




    def dimensions_stmt(self):

        localctx = MiniGoParser.Dimensions_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_dimensions_stmt)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.match(MiniGoParser.LSB)
                self.state = 370
                self.expr(0)
                self.state = 371
                self.match(MiniGoParser.RSB)
                self.state = 372
                self.dimensions_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.match(MiniGoParser.LSB)
                self.state = 375
                self.expr(0)
                self.state = 376
                self.match(MiniGoParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MiniGoParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(MiniGoParser.RETURN)
            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT) | (1 << MiniGoParser.ID))) != 0):
                self.state = 381
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def datatype(self):
            return self.getTypedRuleContext(MiniGoParser.DatatypeContext,0)


        def body(self):
            return self.getTypedRuleContext(MiniGoParser.BodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = MiniGoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MiniGoParser.FUNC)
            self.state = 385
            self.receiver()
            self.state = 386
            self.match(MiniGoParser.ID)
            self.state = 387
            self.match(MiniGoParser.LP)
            self.state = 388
            self.paramlist()
            self.state = 389
            self.match(MiniGoParser.RP)
            self.state = 390
            self.datatype()
            self.state = 391
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def compositetype(self):
            return self.getTypedRuleContext(MiniGoParser.CompositetypeContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(MiniGoParser.LP)
            self.state = 394
            self.match(MiniGoParser.ID)
            self.state = 395
            self.compositetype()
            self.state = 396
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_clause(self):
            return self.getTypedRuleContext(MiniGoParser.If_clauseContext,0)


        def elseif_clauselist(self):
            return self.getTypedRuleContext(MiniGoParser.Elseif_clauselistContext,0)


        def else_clause(self):
            return self.getTypedRuleContext(MiniGoParser.Else_clauseContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MiniGoParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.if_clause()
            self.state = 399
            self.elseif_clauselist()
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 400
                self.else_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def subexpr(self):
            return self.getTypedRuleContext(MiniGoParser.SubexprContext,0)


        def body(self):
            return self.getTypedRuleContext(MiniGoParser.BodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_clause" ):
                return visitor.visitIf_clause(self)
            else:
                return visitor.visitChildren(self)




    def if_clause(self):

        localctx = MiniGoParser.If_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_if_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(MiniGoParser.IF)
            self.state = 404
            self.subexpr()
            self.state = 405
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def body(self):
            return self.getTypedRuleContext(MiniGoParser.BodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_clause" ):
                return visitor.visitElse_clause(self)
            else:
                return visitor.visitChildren(self)




    def else_clause(self):

        localctx = MiniGoParser.Else_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_else_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(MiniGoParser.ELSE)
            self.state = 408
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_clauselistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_clause(self):
            return self.getTypedRuleContext(MiniGoParser.Elseif_clauseContext,0)


        def elseif_clauselist(self):
            return self.getTypedRuleContext(MiniGoParser.Elseif_clauselistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseif_clauselist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_clauselist" ):
                return visitor.visitElseif_clauselist(self)
            else:
                return visitor.visitChildren(self)




    def elseif_clauselist(self):

        localctx = MiniGoParser.Elseif_clauselistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_elseif_clauselist)
        try:
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                self.elseif_clause()
                self.state = 411
                self.elseif_clauselist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def subexpr(self):
            return self.getTypedRuleContext(MiniGoParser.SubexprContext,0)


        def body(self):
            return self.getTypedRuleContext(MiniGoParser.BodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseif_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_clause" ):
                return visitor.visitElseif_clause(self)
            else:
                return visitor.visitChildren(self)




    def elseif_clause(self):

        localctx = MiniGoParser.Elseif_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_elseif_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(MiniGoParser.ELSE)
            self.state = 417
            self.match(MiniGoParser.IF)
            self.state = 418
            self.subexpr()
            self.state = 419
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forbasic(self):
            return self.getTypedRuleContext(MiniGoParser.ForbasicContext,0)


        def foricu(self):
            return self.getTypedRuleContext(MiniGoParser.ForicuContext,0)


        def forrange(self):
            return self.getTypedRuleContext(MiniGoParser.ForrangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MiniGoParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 421
                self.forbasic()
                pass

            elif la_ == 2:
                self.state = 422
                self.foricu()
                pass

            elif la_ == 3:
                self.state = 423
                self.forrange()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForbasicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def subexpr(self):
            return self.getTypedRuleContext(MiniGoParser.SubexprContext,0)


        def body(self):
            return self.getTypedRuleContext(MiniGoParser.BodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forbasic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForbasic" ):
                return visitor.visitForbasic(self)
            else:
                return visitor.visitChildren(self)




    def forbasic(self):

        localctx = MiniGoParser.ForbasicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_forbasic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(MiniGoParser.FOR)
            self.state = 427
            self.subexpr()
            self.state = 428
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForicuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def initialization_clause(self):
            return self.getTypedRuleContext(MiniGoParser.Initialization_clauseContext,0)


        def condition_clause(self):
            return self.getTypedRuleContext(MiniGoParser.Condition_clauseContext,0)


        def update_clause(self):
            return self.getTypedRuleContext(MiniGoParser.Update_clauseContext,0)


        def body(self):
            return self.getTypedRuleContext(MiniGoParser.BodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_foricu

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForicu" ):
                return visitor.visitForicu(self)
            else:
                return visitor.visitChildren(self)




    def foricu(self):

        localctx = MiniGoParser.ForicuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_foricu)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(MiniGoParser.FOR)
            self.state = 431
            self.initialization_clause()
            self.state = 432
            self.condition_clause()
            self.state = 433
            self.update_clause()
            self.state = 434
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Initialization_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalaassign(self):
            return self.getTypedRuleContext(MiniGoParser.ScalaassignContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def scalar_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Scalar_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initialization_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization_clause" ):
                return visitor.visitInitialization_clause(self)
            else:
                return visitor.visitChildren(self)




    def initialization_clause(self):

        localctx = MiniGoParser.Initialization_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_initialization_clause)
        try:
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.scalaassign()
                self.state = 437
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.scalar_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_condition_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_clause" ):
                return visitor.visitCondition_clause(self)
            else:
                return visitor.visitChildren(self)




    def condition_clause(self):

        localctx = MiniGoParser.Condition_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_condition_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.expr(0)
            self.state = 443
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalaassign(self):
            return self.getTypedRuleContext(MiniGoParser.ScalaassignContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate_clause" ):
                return visitor.visitUpdate_clause(self)
            else:
                return visitor.visitChildren(self)




    def update_clause(self):

        localctx = MiniGoParser.Update_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_update_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.scalaassign()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForrangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def ASSIGNMENT(self):
            return self.getToken(MiniGoParser.ASSIGNMENT, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def body(self):
            return self.getTypedRuleContext(MiniGoParser.BodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forrange

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForrange" ):
                return visitor.visitForrange(self)
            else:
                return visitor.visitChildren(self)




    def forrange(self):

        localctx = MiniGoParser.ForrangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_forrange)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(MiniGoParser.FOR)
            self.state = 448
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__0 or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 449
            self.match(MiniGoParser.COMMA)
            self.state = 450
            self.match(MiniGoParser.ID)
            self.state = 451
            self.match(MiniGoParser.ASSIGNMENT)
            self.state = 452
            self.match(MiniGoParser.RANGE)
            self.state = 453
            self.expr(0)
            self.state = 454
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MiniGoParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MiniGoParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_call(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_callContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = MiniGoParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_callstmt)
        try:
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.struct_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 472
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 467
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 468
                    self.match(MiniGoParser.OR)
                    self.state = 469
                    self.expr1(0) 
                self.state = 474
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 483
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 478
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 479
                    self.match(MiniGoParser.AND)
                    self.state = 480
                    self.expr2(0) 
                self.state = 485
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def N_EQUAL(self):
            return self.getToken(MiniGoParser.N_EQUAL, 0)

        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def L_EQUAL(self):
            return self.getToken(MiniGoParser.L_EQUAL, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def G_EQUAL(self):
            return self.getToken(MiniGoParser.G_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 494
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 489
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 490
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.N_EQUAL) | (1 << MiniGoParser.LESS) | (1 << MiniGoParser.L_EQUAL) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.G_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 491
                    self.expr3(0) 
                self.state = 496
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 505
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 500
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 501
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 502
                    self.expr4(0) 
                self.state = 507
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 516
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 511
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 512
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 513
                    self.expr5() 
                self.state = 518
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 522
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 519
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 520
                self.expr5()
                pass
            elif token in [MiniGoParser.BOOLLIT, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 521
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_literals(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_literalsContext,0)


        def arrayliteral(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayliteralContext,0)


        def structliteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructliteralContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(MiniGoParser.SubexprContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def fieldaccess(self):
            return self.getTypedRuleContext(MiniGoParser.FieldaccessContext,0)


        def arrayaccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayaccessContext,0)


        def call(self):
            return self.getTypedRuleContext(MiniGoParser.CallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MiniGoParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_expr6)
        try:
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.primitive_literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
                self.arrayliteral()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 526
                self.structliteral()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 527
                self.subexpr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 528
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 529
                self.fieldaccess()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 530
                self.arrayaccess()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 531
                self.call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_subexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = MiniGoParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(MiniGoParser.LP)
            self.state = 535
            self.expr(0)
            self.state = 536
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_call(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_callContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = MiniGoParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_call)
        try:
            self.state = 540
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.struct_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldaccess(self):
            return self.getTypedRuleContext(MiniGoParser.FieldaccessContext,0)


        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def argumentlist(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentlistContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_call" ):
                return visitor.visitStruct_call(self)
            else:
                return visitor.visitChildren(self)




    def struct_call(self):

        localctx = MiniGoParser.Struct_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_struct_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.fieldaccess()
            self.state = 543
            self.match(MiniGoParser.LP)
            self.state = 544
            self.argumentlist()
            self.state = 545
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def argumentlist(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentlistContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(MiniGoParser.ID)
            self.state = 548
            self.match(MiniGoParser.LP)
            self.state = 549
            self.argumentlist()
            self.state = 550
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argumentprime(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argumentlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentlist" ):
                return visitor.visitArgumentlist(self)
            else:
                return visitor.visitChildren(self)




    def argumentlist(self):

        localctx = MiniGoParser.ArgumentlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_argumentlist)
        try:
            self.state = 554
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.BOOLLIT, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 552
                self.argumentprime()
                pass
            elif token in [MiniGoParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def argumentprime(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argumentprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentprime" ):
                return visitor.visitArgumentprime(self)
            else:
                return visitor.visitChildren(self)




    def argumentprime(self):

        localctx = MiniGoParser.ArgumentprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_argumentprime)
        try:
            self.state = 561
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 556
                self.expr(0)
                self.state = 557
                self.match(MiniGoParser.COMMA)
                self.state = 558
                self.argumentprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 560
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_literals(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_literalsContext,0)


        def arrayliteral(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayliteralContext,0)


        def structliteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructliteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = MiniGoParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_literals)
        try:
            self.state = 566
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.BOOLLIT, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 563
                self.primitive_literals()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 564
                self.arrayliteral()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 565
                self.structliteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structtype(self):
            return self.getTypedRuleContext(MiniGoParser.StructtypeContext,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def fieldvaluelist(self):
            return self.getTypedRuleContext(MiniGoParser.FieldvaluelistContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structliteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructliteral" ):
                return visitor.visitStructliteral(self)
            else:
                return visitor.visitChildren(self)




    def structliteral(self):

        localctx = MiniGoParser.StructliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_structliteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.structtype()
            self.state = 569
            self.match(MiniGoParser.LB)
            self.state = 570
            self.fieldvaluelist()
            self.state = 571
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldvaluelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldvalueprime(self):
            return self.getTypedRuleContext(MiniGoParser.FieldvalueprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldvaluelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldvaluelist" ):
                return visitor.visitFieldvaluelist(self)
            else:
                return visitor.visitChildren(self)




    def fieldvaluelist(self):

        localctx = MiniGoParser.FieldvaluelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_fieldvaluelist)
        try:
            self.state = 575
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 573
                self.fieldvalueprime()
                pass
            elif token in [MiniGoParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldvalueprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def fieldvalueprime(self):
            return self.getTypedRuleContext(MiniGoParser.FieldvalueprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldvalueprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldvalueprime" ):
                return visitor.visitFieldvalueprime(self)
            else:
                return visitor.visitChildren(self)




    def fieldvalueprime(self):

        localctx = MiniGoParser.FieldvalueprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_fieldvalueprime)
        try:
            self.state = 586
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 577
                self.match(MiniGoParser.ID)
                self.state = 578
                self.match(MiniGoParser.COLON)
                self.state = 579
                self.expr(0)
                self.state = 580
                self.match(MiniGoParser.COMMA)
                self.state = 581
                self.fieldvalueprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 583
                self.match(MiniGoParser.ID)
                self.state = 584
                self.match(MiniGoParser.COLON)
                self.state = 585
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arraytype(self):
            return self.getTypedRuleContext(MiniGoParser.ArraytypeContext,0)


        def elementlist(self):
            return self.getTypedRuleContext(MiniGoParser.ElementlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayliteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayliteral" ):
                return visitor.visitArrayliteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayliteral(self):

        localctx = MiniGoParser.ArrayliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_arrayliteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.arraytype()
            self.state = 589
            self.elementlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def element(self):
            return self.getTypedRuleContext(MiniGoParser.ElementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def elementlist(self):
            return self.getTypedRuleContext(MiniGoParser.ElementlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elementlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementlist" ):
                return visitor.visitElementlist(self)
            else:
                return visitor.visitChildren(self)




    def elementlist(self):

        localctx = MiniGoParser.ElementlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_elementlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.match(MiniGoParser.LB)
            self.state = 597
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 592
                self.element()
                self.state = 593
                self.match(MiniGoParser.COMMA)
                self.state = 594
                self.elementlist()
                pass

            elif la_ == 2:
                self.state = 596
                self.element()
                pass


            self.state = 599
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementlist(self):
            return self.getTypedRuleContext(MiniGoParser.ElementlistContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = MiniGoParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_element)
        try:
            self.state = 603
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 601
                self.elementlist()
                pass
            elif token in [MiniGoParser.BOOLLIT, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LP, MiniGoParser.LSB, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 602
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_literalsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MiniGoParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MiniGoParser.BOOLLIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_literals" ):
                return visitor.visitPrimitive_literals(self)
            else:
                return visitor.visitChildren(self)




    def primitive_literals(self):

        localctx = MiniGoParser.Primitive_literalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_primitive_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[53] = self.expr_sempred
        self._predicates[54] = self.expr1_sempred
        self._predicates[55] = self.expr2_sempred
        self._predicates[56] = self.expr3_sempred
        self._predicates[57] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




