import argparse, os
#Argparse
parser = argparse.ArgumentParser(prog="FileDistinction", description="This is a tool for finding all of the differences in two files.")

#group = parser.add_mutually_exclusive_group(required=False)
#group.add_argument("-a", "--all", help="use every special character in the entire ASCII Table (Default: %(default)s)",action="store_true", default=False)
#group.add_argument("-c", "--common", help="Use only special characters commonly used in passwords: _ . - ! @ * $ ? & %% (Source in Readme)", action="store_true", default=True)
#group.add_argument("-s", "--special-characters", help="use these specific characters as special characters (Example: --special-characters #!?-)", type=str, default='', dest='chars')

parser.add_argument("-f", "--full", help="extend the comparison to file properties", action="store_true", default=False)
parser.add_argument("file1", help="the first file", type=str)
parser.add_argument("file2", help="the second file", type=str)
args = parser.parse_args()

#Definitions
fn1 = args.file1.rsplit('/', 1)[-1].rsplit('\\', 1)[-1]
fn2 = args.file2.rsplit('/', 1)[-1].rsplit('\\', 1)[-1]

file1 = open(args.file1, "r")
file2 = open(args.file2, "r")


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colored(color, text):
    return(color + text + colors.ENDC)

def find_string_difference(str1, str2):
    start = end =  ""
    #start
    for i in range (min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            start += str1[i]
        else: 
            break
    #end
    for i in range (min(len(str1), len(str2))):
        if (str1[::-1][i] == str2[::-1][i]):
            end = str1[::-1][i] + end
        else:
            break
    
    diff1 = str1[len(start):len(str1)-len(end)]
    diff2 = str2[len(start):len(str2)-len(end)]
            
    return([start + colored(colors.FAIL, diff1) + end, start + colored(colors.FAIL, diff2) + end])

#full check
if(args.full):
    #name check
    print(colored(colors.OKBLUE, "Name Check:"))
    if (fn1 == fn2):
        print("No difference found!")
    else:
        for string in find_string_difference(fn1, fn2):
            print(string)
    print("")

    print(colored(colors.OKBLUE, "File Size:"))
    fs1 = os.path.getsize(fn1)
    fs2 = os.path.getsize(fn2)
    if (fs1 == fs2):
        print(f"The files have the same size: {fs1} bytes")
    else:
        print(fn1 + f": {fs1} bytes")
        print(fn2 + f": {fs2} bytes")
