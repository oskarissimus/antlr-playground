# Generated from antlr_playground/grammar/bds.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,94,767,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,
        91,7,91,2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,7,
        97,2,98,7,98,2,99,7,99,2,100,7,100,2,101,7,101,1,0,1,0,1,1,1,1,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,
        5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,
        8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,
        14,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,
        19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,
        24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,
        28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,
        30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,
        32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,1,35,1,35,1,35,1,
        36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,
        38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,
        40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,
        42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,45,1,45,1,
        45,1,45,1,46,1,46,1,46,1,47,1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,
        50,1,51,1,51,1,52,1,52,1,53,1,53,1,54,1,54,1,55,1,55,1,56,1,56,1,
        56,1,57,1,57,1,57,1,58,1,58,1,58,1,59,1,59,1,59,1,60,1,60,1,61,1,
        61,1,62,1,62,1,63,1,63,1,64,1,64,1,64,1,65,1,65,1,65,1,66,1,66,1,
        67,1,67,1,67,1,68,1,68,1,68,1,69,1,69,1,69,1,69,1,69,1,70,1,70,1,
        70,1,70,1,71,1,71,1,71,1,71,1,71,1,72,1,72,1,72,1,72,1,73,1,73,1,
        73,1,73,1,73,1,73,1,73,1,73,1,73,1,74,1,74,1,74,1,75,1,75,1,75,1,
        76,1,76,1,76,1,77,1,77,1,77,1,78,1,78,1,78,1,79,1,79,1,79,1,80,1,
        80,1,80,5,80,544,8,80,10,80,12,80,547,9,80,1,80,1,80,4,80,551,8,
        80,11,80,12,80,552,1,80,1,80,4,80,557,8,80,11,80,12,80,558,3,80,
        561,8,80,1,81,1,81,1,81,1,81,1,81,1,81,1,81,1,81,3,81,571,8,81,1,
        82,1,82,1,82,1,82,3,82,577,8,82,1,83,1,83,3,83,581,8,83,1,83,4,83,
        584,8,83,11,83,12,83,585,1,84,1,84,1,84,1,84,3,84,592,8,84,1,85,
        1,85,1,86,4,86,597,8,86,11,86,12,86,598,1,86,1,86,5,86,603,8,86,
        10,86,12,86,606,9,86,1,86,3,86,609,8,86,1,86,1,86,4,86,613,8,86,
        11,86,12,86,614,1,86,3,86,618,8,86,1,86,4,86,621,8,86,11,86,12,86,
        622,1,86,1,86,4,86,627,8,86,11,86,12,86,628,3,86,631,8,86,1,87,1,
        87,5,87,635,8,87,10,87,12,87,638,9,87,1,88,1,88,1,88,1,88,1,88,1,
        89,1,89,1,89,1,89,1,89,1,89,1,89,1,89,1,89,3,89,654,8,89,1,90,1,
        90,1,91,1,91,1,92,1,92,1,92,1,92,5,92,664,8,92,10,92,12,92,667,9,
        92,1,92,1,92,1,93,1,93,5,93,673,8,93,10,93,12,93,676,9,93,1,93,1,
        93,1,94,1,94,1,94,1,94,1,94,1,94,4,94,686,8,94,11,94,12,94,687,1,
        94,1,94,1,95,1,95,1,95,1,95,1,95,4,95,697,8,95,11,95,12,95,698,1,
        95,1,95,1,96,1,96,1,96,1,96,1,96,1,96,4,96,709,8,96,11,96,12,96,
        710,1,96,1,96,1,96,1,97,1,97,1,97,1,97,5,97,720,8,97,10,97,12,97,
        723,9,97,1,97,1,97,1,97,1,97,1,97,1,98,1,98,1,98,1,98,5,98,734,8,
        98,10,98,12,98,737,9,98,1,98,1,98,1,99,1,99,5,99,743,8,99,10,99,
        12,99,746,9,99,1,99,1,99,1,100,1,100,5,100,752,8,100,10,100,12,100,
        755,9,100,1,101,1,101,1,101,1,101,1,101,1,101,1,101,3,101,764,8,
        101,1,101,1,101,1,721,0,102,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,
        20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,
        31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,
        42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,99,50,101,51,103,52,
        105,53,107,54,109,55,111,56,113,57,115,58,117,59,119,60,121,61,123,
        62,125,63,127,64,129,65,131,66,133,67,135,68,137,69,139,70,141,71,
        143,72,145,73,147,74,149,75,151,76,153,77,155,78,157,79,159,80,161,
        0,163,0,165,0,167,0,169,0,171,0,173,0,175,0,177,81,179,82,181,83,
        183,84,185,85,187,86,189,87,191,88,193,89,195,90,197,91,199,92,201,
        93,203,94,1,0,12,8,0,34,34,39,39,92,92,98,98,102,102,110,110,114,
        114,116,116,2,0,10,10,13,13,2,0,69,69,101,101,2,0,43,43,45,45,3,
        0,48,57,65,70,97,102,2,0,34,34,92,92,1,0,39,39,2,0,9,9,32,32,4,0,
        10,10,13,13,40,40,123,123,3,0,65,90,95,95,97,122,4,0,48,57,65,90,
        95,95,97,122,3,0,9,9,13,13,32,32,797,0,1,1,0,0,0,0,3,1,0,0,0,0,5,
        1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,
        0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,
        0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,
        0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,
        0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,
        0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,
        0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,
        0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,
        0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,
        0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,
        1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,
        0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,
        0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,
        133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,0,0,0,141,1,0,
        0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,149,1,0,0,0,0,151,
        1,0,0,0,0,153,1,0,0,0,0,155,1,0,0,0,0,157,1,0,0,0,0,159,1,0,0,0,
        0,177,1,0,0,0,0,179,1,0,0,0,0,181,1,0,0,0,0,183,1,0,0,0,0,185,1,
        0,0,0,0,187,1,0,0,0,0,189,1,0,0,0,0,191,1,0,0,0,0,193,1,0,0,0,0,
        195,1,0,0,0,0,197,1,0,0,0,0,199,1,0,0,0,0,201,1,0,0,0,0,203,1,0,
        0,0,1,205,1,0,0,0,3,207,1,0,0,0,5,209,1,0,0,0,7,217,1,0,0,0,9,219,
        1,0,0,0,11,224,1,0,0,0,13,228,1,0,0,0,15,233,1,0,0,0,17,240,1,0,
        0,0,19,245,1,0,0,0,21,247,1,0,0,0,23,249,1,0,0,0,25,251,1,0,0,0,
        27,253,1,0,0,0,29,255,1,0,0,0,31,258,1,0,0,0,33,260,1,0,0,0,35,262,
        1,0,0,0,37,268,1,0,0,0,39,276,1,0,0,0,41,282,1,0,0,0,43,293,1,0,
        0,0,45,304,1,0,0,0,47,313,1,0,0,0,49,319,1,0,0,0,51,324,1,0,0,0,
        53,330,1,0,0,0,55,338,1,0,0,0,57,346,1,0,0,0,59,352,1,0,0,0,61,356,
        1,0,0,0,63,362,1,0,0,0,65,370,1,0,0,0,67,376,1,0,0,0,69,380,1,0,
        0,0,71,382,1,0,0,0,73,385,1,0,0,0,75,390,1,0,0,0,77,395,1,0,0,0,
        79,402,1,0,0,0,81,407,1,0,0,0,83,414,1,0,0,0,85,419,1,0,0,0,87,427,
        1,0,0,0,89,433,1,0,0,0,91,435,1,0,0,0,93,439,1,0,0,0,95,442,1,0,
        0,0,97,445,1,0,0,0,99,447,1,0,0,0,101,449,1,0,0,0,103,451,1,0,0,
        0,105,453,1,0,0,0,107,455,1,0,0,0,109,457,1,0,0,0,111,459,1,0,0,
        0,113,461,1,0,0,0,115,464,1,0,0,0,117,467,1,0,0,0,119,470,1,0,0,
        0,121,473,1,0,0,0,123,475,1,0,0,0,125,477,1,0,0,0,127,479,1,0,0,
        0,129,481,1,0,0,0,131,484,1,0,0,0,133,487,1,0,0,0,135,489,1,0,0,
        0,137,492,1,0,0,0,139,495,1,0,0,0,141,500,1,0,0,0,143,504,1,0,0,
        0,145,509,1,0,0,0,147,513,1,0,0,0,149,522,1,0,0,0,151,525,1,0,0,
        0,153,528,1,0,0,0,155,531,1,0,0,0,157,534,1,0,0,0,159,537,1,0,0,
        0,161,560,1,0,0,0,163,562,1,0,0,0,165,572,1,0,0,0,167,578,1,0,0,
        0,169,591,1,0,0,0,171,593,1,0,0,0,173,630,1,0,0,0,175,636,1,0,0,
        0,177,639,1,0,0,0,179,653,1,0,0,0,181,655,1,0,0,0,183,657,1,0,0,
        0,185,659,1,0,0,0,187,670,1,0,0,0,189,679,1,0,0,0,191,691,1,0,0,
        0,193,702,1,0,0,0,195,715,1,0,0,0,197,729,1,0,0,0,199,740,1,0,0,
        0,201,749,1,0,0,0,203,763,1,0,0,0,205,206,5,59,0,0,206,2,1,0,0,0,
        207,208,5,10,0,0,208,4,1,0,0,0,209,210,5,105,0,0,210,211,5,110,0,
        0,211,212,5,99,0,0,212,213,5,108,0,0,213,214,5,117,0,0,214,215,5,
        100,0,0,215,216,5,101,0,0,216,6,1,0,0,0,217,218,5,44,0,0,218,8,1,
        0,0,0,219,220,5,98,0,0,220,221,5,111,0,0,221,222,5,111,0,0,222,223,
        5,108,0,0,223,10,1,0,0,0,224,225,5,105,0,0,225,226,5,110,0,0,226,
        227,5,116,0,0,227,12,1,0,0,0,228,229,5,114,0,0,229,230,5,101,0,0,
        230,231,5,97,0,0,231,232,5,108,0,0,232,14,1,0,0,0,233,234,5,115,
        0,0,234,235,5,116,0,0,235,236,5,114,0,0,236,237,5,105,0,0,237,238,
        5,110,0,0,238,239,5,103,0,0,239,16,1,0,0,0,240,241,5,118,0,0,241,
        242,5,111,0,0,242,243,5,105,0,0,243,244,5,100,0,0,244,18,1,0,0,0,
        245,246,5,91,0,0,246,20,1,0,0,0,247,248,5,93,0,0,248,22,1,0,0,0,
        249,250,5,123,0,0,250,24,1,0,0,0,251,252,5,125,0,0,252,26,1,0,0,
        0,253,254,5,61,0,0,254,28,1,0,0,0,255,256,5,58,0,0,256,257,5,61,
        0,0,257,30,1,0,0,0,258,259,5,40,0,0,259,32,1,0,0,0,260,261,5,41,
        0,0,261,34,1,0,0,0,262,263,5,99,0,0,263,264,5,108,0,0,264,265,5,
        97,0,0,265,266,5,115,0,0,266,267,5,115,0,0,267,36,1,0,0,0,268,269,
        5,101,0,0,269,270,5,120,0,0,270,271,5,116,0,0,271,272,5,101,0,0,
        272,273,5,110,0,0,273,274,5,100,0,0,274,275,5,115,0,0,275,38,1,0,
        0,0,276,277,5,98,0,0,277,278,5,114,0,0,278,279,5,101,0,0,279,280,
        5,97,0,0,280,281,5,107,0,0,281,40,1,0,0,0,282,283,5,98,0,0,283,284,
        5,114,0,0,284,285,5,101,0,0,285,286,5,97,0,0,286,287,5,107,0,0,287,
        288,5,112,0,0,288,289,5,111,0,0,289,290,5,105,0,0,290,291,5,110,
        0,0,291,292,5,116,0,0,292,42,1,0,0,0,293,294,5,99,0,0,294,295,5,
        104,0,0,295,296,5,101,0,0,296,297,5,99,0,0,297,298,5,107,0,0,298,
        299,5,112,0,0,299,300,5,111,0,0,300,301,5,105,0,0,301,302,5,110,
        0,0,302,303,5,116,0,0,303,44,1,0,0,0,304,305,5,99,0,0,305,306,5,
        111,0,0,306,307,5,110,0,0,307,308,5,116,0,0,308,309,5,105,0,0,309,
        310,5,110,0,0,310,311,5,117,0,0,311,312,5,101,0,0,312,46,1,0,0,0,
        313,314,5,100,0,0,314,315,5,101,0,0,315,316,5,98,0,0,316,317,5,117,
        0,0,317,318,5,103,0,0,318,48,1,0,0,0,319,320,5,101,0,0,320,321,5,
        120,0,0,321,322,5,105,0,0,322,323,5,116,0,0,323,50,1,0,0,0,324,325,
        5,112,0,0,325,326,5,114,0,0,326,327,5,105,0,0,327,328,5,110,0,0,
        328,329,5,116,0,0,329,52,1,0,0,0,330,331,5,112,0,0,331,332,5,114,
        0,0,332,333,5,105,0,0,333,334,5,110,0,0,334,335,5,116,0,0,335,336,
        5,108,0,0,336,337,5,110,0,0,337,54,1,0,0,0,338,339,5,119,0,0,339,
        340,5,97,0,0,340,341,5,114,0,0,341,342,5,110,0,0,342,343,5,105,0,
        0,343,344,5,110,0,0,344,345,5,103,0,0,345,56,1,0,0,0,346,347,5,101,
        0,0,347,348,5,114,0,0,348,349,5,114,0,0,349,350,5,111,0,0,350,351,
        5,114,0,0,351,58,1,0,0,0,352,353,5,116,0,0,353,354,5,114,0,0,354,
        355,5,121,0,0,355,60,1,0,0,0,356,357,5,99,0,0,357,358,5,97,0,0,358,
        359,5,116,0,0,359,360,5,99,0,0,360,361,5,104,0,0,361,62,1,0,0,0,
        362,363,5,102,0,0,363,364,5,105,0,0,364,365,5,110,0,0,365,366,5,
        97,0,0,366,367,5,108,0,0,367,368,5,108,0,0,368,369,5,121,0,0,369,
        64,1,0,0,0,370,371,5,116,0,0,371,372,5,104,0,0,372,373,5,114,0,0,
        373,374,5,111,0,0,374,375,5,119,0,0,375,66,1,0,0,0,376,377,5,102,
        0,0,377,378,5,111,0,0,378,379,5,114,0,0,379,68,1,0,0,0,380,381,5,
        58,0,0,381,70,1,0,0,0,382,383,5,105,0,0,383,384,5,102,0,0,384,72,
        1,0,0,0,385,386,5,101,0,0,386,387,5,108,0,0,387,388,5,115,0,0,388,
        389,5,101,0,0,389,74,1,0,0,0,390,391,5,107,0,0,391,392,5,105,0,0,
        392,393,5,108,0,0,393,394,5,108,0,0,394,76,1,0,0,0,395,396,5,114,
        0,0,396,397,5,101,0,0,397,398,5,116,0,0,398,399,5,117,0,0,399,400,
        5,114,0,0,400,401,5,110,0,0,401,78,1,0,0,0,402,403,5,119,0,0,403,
        404,5,97,0,0,404,405,5,105,0,0,405,406,5,116,0,0,406,80,1,0,0,0,
        407,408,5,115,0,0,408,409,5,119,0,0,409,410,5,105,0,0,410,411,5,
        116,0,0,411,412,5,99,0,0,412,413,5,104,0,0,413,82,1,0,0,0,414,415,
        5,99,0,0,415,416,5,97,0,0,416,417,5,115,0,0,417,418,5,101,0,0,418,
        84,1,0,0,0,419,420,5,100,0,0,420,421,5,101,0,0,421,422,5,102,0,0,
        422,423,5,97,0,0,423,424,5,117,0,0,424,425,5,108,0,0,425,426,5,116,
        0,0,426,86,1,0,0,0,427,428,5,119,0,0,428,429,5,104,0,0,429,430,5,
        105,0,0,430,431,5,108,0,0,431,432,5,101,0,0,432,88,1,0,0,0,433,434,
        5,46,0,0,434,90,1,0,0,0,435,436,5,110,0,0,436,437,5,101,0,0,437,
        438,5,119,0,0,438,92,1,0,0,0,439,440,5,43,0,0,440,441,5,43,0,0,441,
        94,1,0,0,0,442,443,5,45,0,0,443,444,5,45,0,0,444,96,1,0,0,0,445,
        446,5,126,0,0,446,98,1,0,0,0,447,448,5,33,0,0,448,100,1,0,0,0,449,
        450,5,42,0,0,450,102,1,0,0,0,451,452,5,47,0,0,452,104,1,0,0,0,453,
        454,5,37,0,0,454,106,1,0,0,0,455,456,5,43,0,0,456,108,1,0,0,0,457,
        458,5,45,0,0,458,110,1,0,0,0,459,460,5,60,0,0,460,112,1,0,0,0,461,
        462,5,60,0,0,462,463,5,61,0,0,463,114,1,0,0,0,464,465,5,61,0,0,465,
        466,5,61,0,0,466,116,1,0,0,0,467,468,5,33,0,0,468,469,5,61,0,0,469,
        118,1,0,0,0,470,471,5,62,0,0,471,472,5,61,0,0,472,120,1,0,0,0,473,
        474,5,62,0,0,474,122,1,0,0,0,475,476,5,38,0,0,476,124,1,0,0,0,477,
        478,5,124,0,0,478,126,1,0,0,0,479,480,5,94,0,0,480,128,1,0,0,0,481,
        482,5,38,0,0,482,483,5,38,0,0,483,130,1,0,0,0,484,485,5,124,0,0,
        485,486,5,124,0,0,486,132,1,0,0,0,487,488,5,63,0,0,488,134,1,0,0,
        0,489,490,5,60,0,0,490,491,5,45,0,0,491,136,1,0,0,0,492,493,5,61,
        0,0,493,494,5,62,0,0,494,138,1,0,0,0,495,496,5,116,0,0,496,497,5,
        97,0,0,497,498,5,115,0,0,498,499,5,107,0,0,499,140,1,0,0,0,500,501,
        5,100,0,0,501,502,5,101,0,0,502,503,5,112,0,0,503,142,1,0,0,0,504,
        505,5,103,0,0,505,506,5,111,0,0,506,507,5,97,0,0,507,508,5,108,0,
        0,508,144,1,0,0,0,509,510,5,112,0,0,510,511,5,97,0,0,511,512,5,114,
        0,0,512,146,1,0,0,0,513,514,5,112,0,0,514,515,5,97,0,0,515,516,5,
        114,0,0,516,517,5,97,0,0,517,518,5,108,0,0,518,519,5,108,0,0,519,
        520,5,101,0,0,520,521,5,108,0,0,521,148,1,0,0,0,522,523,5,124,0,
        0,523,524,5,61,0,0,524,150,1,0,0,0,525,526,5,38,0,0,526,527,5,61,
        0,0,527,152,1,0,0,0,528,529,5,47,0,0,529,530,5,61,0,0,530,154,1,
        0,0,0,531,532,5,42,0,0,532,533,5,61,0,0,533,156,1,0,0,0,534,535,
        5,45,0,0,535,536,5,61,0,0,536,158,1,0,0,0,537,538,5,43,0,0,538,539,
        5,61,0,0,539,160,1,0,0,0,540,561,5,48,0,0,541,545,2,49,57,0,542,
        544,2,48,57,0,543,542,1,0,0,0,544,547,1,0,0,0,545,543,1,0,0,0,545,
        546,1,0,0,0,546,561,1,0,0,0,547,545,1,0,0,0,548,550,5,48,0,0,549,
        551,2,48,55,0,550,549,1,0,0,0,551,552,1,0,0,0,552,550,1,0,0,0,552,
        553,1,0,0,0,553,561,1,0,0,0,554,556,3,169,84,0,555,557,3,171,85,
        0,556,555,1,0,0,0,557,558,1,0,0,0,558,556,1,0,0,0,558,559,1,0,0,
        0,559,561,1,0,0,0,560,540,1,0,0,0,560,541,1,0,0,0,560,548,1,0,0,
        0,560,554,1,0,0,0,561,162,1,0,0,0,562,570,5,92,0,0,563,571,7,0,0,
        0,564,565,2,48,51,0,565,566,2,48,55,0,566,571,2,48,55,0,567,568,
        2,48,55,0,568,571,2,48,55,0,569,571,2,48,55,0,570,563,1,0,0,0,570,
        564,1,0,0,0,570,567,1,0,0,0,570,569,1,0,0,0,571,164,1,0,0,0,572,
        576,5,92,0,0,573,577,7,1,0,0,574,575,5,13,0,0,575,577,5,10,0,0,576,
        573,1,0,0,0,576,574,1,0,0,0,577,166,1,0,0,0,578,580,7,2,0,0,579,
        581,7,3,0,0,580,579,1,0,0,0,580,581,1,0,0,0,581,583,1,0,0,0,582,
        584,2,48,57,0,583,582,1,0,0,0,584,585,1,0,0,0,585,583,1,0,0,0,585,
        586,1,0,0,0,586,168,1,0,0,0,587,588,5,48,0,0,588,592,5,120,0,0,589,
        590,5,48,0,0,590,592,5,88,0,0,591,587,1,0,0,0,591,589,1,0,0,0,592,
        170,1,0,0,0,593,594,7,4,0,0,594,172,1,0,0,0,595,597,2,48,57,0,596,
        595,1,0,0,0,597,598,1,0,0,0,598,596,1,0,0,0,598,599,1,0,0,0,599,
        600,1,0,0,0,600,604,5,46,0,0,601,603,2,48,57,0,602,601,1,0,0,0,603,
        606,1,0,0,0,604,602,1,0,0,0,604,605,1,0,0,0,605,608,1,0,0,0,606,
        604,1,0,0,0,607,609,3,167,83,0,608,607,1,0,0,0,608,609,1,0,0,0,609,
        631,1,0,0,0,610,612,5,46,0,0,611,613,2,48,57,0,612,611,1,0,0,0,613,
        614,1,0,0,0,614,612,1,0,0,0,614,615,1,0,0,0,615,617,1,0,0,0,616,
        618,3,167,83,0,617,616,1,0,0,0,617,618,1,0,0,0,618,631,1,0,0,0,619,
        621,2,48,57,0,620,619,1,0,0,0,621,622,1,0,0,0,622,620,1,0,0,0,622,
        623,1,0,0,0,623,624,1,0,0,0,624,631,3,167,83,0,625,627,2,48,57,0,
        626,625,1,0,0,0,627,628,1,0,0,0,628,626,1,0,0,0,628,629,1,0,0,0,
        629,631,1,0,0,0,630,596,1,0,0,0,630,610,1,0,0,0,630,620,1,0,0,0,
        630,626,1,0,0,0,631,174,1,0,0,0,632,635,3,165,82,0,633,635,8,1,0,
        0,634,632,1,0,0,0,634,633,1,0,0,0,635,638,1,0,0,0,636,634,1,0,0,
        0,636,637,1,0,0,0,637,176,1,0,0,0,638,636,1,0,0,0,639,640,5,110,
        0,0,640,641,5,117,0,0,641,642,5,108,0,0,642,643,5,108,0,0,643,178,
        1,0,0,0,644,645,5,116,0,0,645,646,5,114,0,0,646,647,5,117,0,0,647,
        654,5,101,0,0,648,649,5,102,0,0,649,650,5,97,0,0,650,651,5,108,0,
        0,651,652,5,115,0,0,652,654,5,101,0,0,653,644,1,0,0,0,653,648,1,
        0,0,0,654,180,1,0,0,0,655,656,3,161,80,0,656,182,1,0,0,0,657,658,
        3,173,86,0,658,184,1,0,0,0,659,665,5,34,0,0,660,664,8,5,0,0,661,
        662,5,92,0,0,662,664,9,0,0,0,663,660,1,0,0,0,663,661,1,0,0,0,664,
        667,1,0,0,0,665,663,1,0,0,0,665,666,1,0,0,0,666,668,1,0,0,0,667,
        665,1,0,0,0,668,669,5,34,0,0,669,186,1,0,0,0,670,674,5,39,0,0,671,
        673,8,6,0,0,672,671,1,0,0,0,673,676,1,0,0,0,674,672,1,0,0,0,674,
        675,1,0,0,0,675,677,1,0,0,0,676,674,1,0,0,0,677,678,5,39,0,0,678,
        188,1,0,0,0,679,680,5,104,0,0,680,681,5,101,0,0,681,682,5,108,0,
        0,682,683,5,112,0,0,683,685,1,0,0,0,684,686,7,7,0,0,685,684,1,0,
        0,0,686,687,1,0,0,0,687,685,1,0,0,0,687,688,1,0,0,0,688,689,1,0,
        0,0,689,690,3,175,87,0,690,190,1,0,0,0,691,692,5,115,0,0,692,693,
        5,121,0,0,693,694,5,115,0,0,694,696,1,0,0,0,695,697,7,7,0,0,696,
        695,1,0,0,0,697,698,1,0,0,0,698,696,1,0,0,0,698,699,1,0,0,0,699,
        700,1,0,0,0,700,701,3,175,87,0,701,192,1,0,0,0,702,703,5,116,0,0,
        703,704,5,97,0,0,704,705,5,115,0,0,705,706,5,107,0,0,706,708,1,0,
        0,0,707,709,7,7,0,0,708,707,1,0,0,0,709,710,1,0,0,0,710,708,1,0,
        0,0,710,711,1,0,0,0,711,712,1,0,0,0,712,713,8,8,0,0,713,714,3,175,
        87,0,714,194,1,0,0,0,715,716,5,47,0,0,716,717,5,42,0,0,717,721,1,
        0,0,0,718,720,9,0,0,0,719,718,1,0,0,0,720,723,1,0,0,0,721,722,1,
        0,0,0,721,719,1,0,0,0,722,724,1,0,0,0,723,721,1,0,0,0,724,725,5,
        42,0,0,725,726,5,47,0,0,726,727,1,0,0,0,727,728,6,97,0,0,728,196,
        1,0,0,0,729,730,5,47,0,0,730,731,5,47,0,0,731,735,1,0,0,0,732,734,
        8,1,0,0,733,732,1,0,0,0,734,737,1,0,0,0,735,733,1,0,0,0,735,736,
        1,0,0,0,736,738,1,0,0,0,737,735,1,0,0,0,738,739,6,98,0,0,739,198,
        1,0,0,0,740,744,5,35,0,0,741,743,8,1,0,0,742,741,1,0,0,0,743,746,
        1,0,0,0,744,742,1,0,0,0,744,745,1,0,0,0,745,747,1,0,0,0,746,744,
        1,0,0,0,747,748,6,99,0,0,748,200,1,0,0,0,749,753,7,9,0,0,750,752,
        7,10,0,0,751,750,1,0,0,0,752,755,1,0,0,0,753,751,1,0,0,0,753,754,
        1,0,0,0,754,202,1,0,0,0,755,753,1,0,0,0,756,764,7,11,0,0,757,758,
        5,92,0,0,758,764,5,10,0,0,759,760,5,92,0,0,760,761,5,13,0,0,761,
        764,5,10,0,0,762,764,5,12,0,0,763,756,1,0,0,0,763,757,1,0,0,0,763,
        759,1,0,0,0,763,762,1,0,0,0,764,765,1,0,0,0,765,766,6,101,0,0,766,
        204,1,0,0,0,32,0,545,552,558,560,570,576,580,585,591,598,604,608,
        614,617,622,628,630,634,636,653,663,665,674,687,698,710,721,735,
        744,753,763,1,6,0,0
    ]

class bdsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    T__50 = 51
    T__51 = 52
    T__52 = 53
    T__53 = 54
    T__54 = 55
    T__55 = 56
    T__56 = 57
    T__57 = 58
    T__58 = 59
    T__59 = 60
    T__60 = 61
    T__61 = 62
    T__62 = 63
    T__63 = 64
    T__64 = 65
    T__65 = 66
    T__66 = 67
    T__67 = 68
    T__68 = 69
    T__69 = 70
    T__70 = 71
    T__71 = 72
    T__72 = 73
    T__73 = 74
    T__74 = 75
    T__75 = 76
    T__76 = 77
    T__77 = 78
    T__78 = 79
    T__79 = 80
    NULL_LITERAL = 81
    BOOL_LITERAL = 82
    INT_LITERAL = 83
    REAL_LITERAL = 84
    STRING_LITERAL = 85
    STRING_LITERAL_SINGLE = 86
    HELP_LITERAL = 87
    SYS_LITERAL = 88
    TASK_LITERAL = 89
    COMMENT = 90
    COMMENT_LINE = 91
    COMMENT_LINE_HASH = 92
    ID = 93
    WS = 94

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'\\n'", "'include'", "','", "'bool'", "'int'", "'real'", 
            "'string'", "'void'", "'['", "']'", "'{'", "'}'", "'='", "':='", 
            "'('", "')'", "'class'", "'extends'", "'break'", "'breakpoint'", 
            "'checkpoint'", "'continue'", "'debug'", "'exit'", "'print'", 
            "'println'", "'warning'", "'error'", "'try'", "'catch'", "'finally'", 
            "'throw'", "'for'", "':'", "'if'", "'else'", "'kill'", "'return'", 
            "'wait'", "'switch'", "'case'", "'default'", "'while'", "'.'", 
            "'new'", "'++'", "'--'", "'~'", "'!'", "'*'", "'/'", "'%'", 
            "'+'", "'-'", "'<'", "'<='", "'=='", "'!='", "'>='", "'>'", 
            "'&'", "'|'", "'^'", "'&&'", "'||'", "'?'", "'<-'", "'=>'", 
            "'task'", "'dep'", "'goal'", "'par'", "'parallel'", "'|='", 
            "'&='", "'/='", "'*='", "'-='", "'+='", "'null'" ]

    symbolicNames = [ "<INVALID>",
            "NULL_LITERAL", "BOOL_LITERAL", "INT_LITERAL", "REAL_LITERAL", 
            "STRING_LITERAL", "STRING_LITERAL_SINGLE", "HELP_LITERAL", "SYS_LITERAL", 
            "TASK_LITERAL", "COMMENT", "COMMENT_LINE", "COMMENT_LINE_HASH", 
            "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "T__44", "T__45", "T__46", "T__47", "T__48", "T__49", 
                  "T__50", "T__51", "T__52", "T__53", "T__54", "T__55", 
                  "T__56", "T__57", "T__58", "T__59", "T__60", "T__61", 
                  "T__62", "T__63", "T__64", "T__65", "T__66", "T__67", 
                  "T__68", "T__69", "T__70", "T__71", "T__72", "T__73", 
                  "T__74", "T__75", "T__76", "T__77", "T__78", "T__79", 
                  "IntegerNumber", "EscapeSequence", "EscapedNewLine", "Exponent", 
                  "HexPrefix", "HexDigit", "NonIntegerNumber", "SysMultiLine", 
                  "NULL_LITERAL", "BOOL_LITERAL", "INT_LITERAL", "REAL_LITERAL", 
                  "STRING_LITERAL", "STRING_LITERAL_SINGLE", "HELP_LITERAL", 
                  "SYS_LITERAL", "TASK_LITERAL", "COMMENT", "COMMENT_LINE", 
                  "COMMENT_LINE_HASH", "ID", "WS" ]

    grammarFileName = "bds.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


