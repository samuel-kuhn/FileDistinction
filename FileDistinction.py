import argparse, os
#Argparse
parser = argparse.ArgumentParser(prog="FileDistinction", description="This is a tool for finding all of the differences in two files.")

parser.add_argument("-f", "--full", help="extend the comparison to file properties", action="store_true", default=False)
parser.add_argument("file1", help="the first file", type=str)
parser.add_argument("file2", help="the second file", type=str)
args = parser.parse_args()

#Definitions
fn1 = args.file1.rsplit('/', 1)[-1].rsplit('\\', 1)[-1]
fn2 = args.file2.rsplit('/', 1)[-1].rsplit('\\', 1)[-1]

file1 = open(args.file1, "r")
file2 = open(args.file2, "r")

lines1 = [repr(x) for x in file1.readlines()]
lines2 = [repr(x) for x in file2.readlines()]

class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#methods
def colored(color, text):
    return(color + text + colors.ENDC)

def string_difference(str1, str2):
    if (len(str1) == len(str2)):
        colored_str1 = ""
        colored_str2 = ""
        for i in range(len(str1)):
            if (str1[i] == str2[i]):
                colored_str1 += str1[i]
                colored_str2 += str1[i]
            else:
                colored_str1 += colored(colors.RED, str1[i])
                colored_str2 += colored(colors.RED, str2[i])
        return([colored_str1, colored_str2])

    else:
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
                
        return([start + colored(colors.RED, diff1) + end, start + colored(colors.RED, diff2) + end])

def line_difference(lines1, lines2):
    differences1 = []
    differences2 = [] 
    lines = []
    if (len(lines1) == len(lines2)):
        #check for character differences
        for i in range(len(lines1)):
            if (lines1[i] != lines2[i]):
                str_diff = string_difference(lines1[i], lines2[i])
                differences1.append(str_diff[0])
                differences2.append(str_diff[1])
                lines.append(i+1)
        diffs_dict = {lines[i]: [differences1[i], differences2[i]] for i in range(len(lines))}

    else:
        return "error"
    return diffs_dict

#full check
if(args.full):
    #name check
    print(colored(colors.BLUE, "Name Check:"))
    if (fn1 == fn2):
        print("No difference found!")
    else:
        for string in string_difference(fn1, fn2):
            print(string)
    print()

    #size check
    print(colored(colors.BLUE, "File Size:"))
    fs1 = os.path.getsize(fn1)
    fs2 = os.path.getsize(fn2)
    if (fs1 == fs2):
        print(f"The files have the same size: {fs1} bytes")
    else:
        print(fn1 + f": {fs1} bytes")
        print(fn2 + f": {fs2} bytes")
    print()

#normal check
print(colored(colors.BLUE, "Content comparison"))

differences = line_difference(lines1, lines2)
if (differences == {}):
    print("The two files have the same content!")
else:
    if (len(lines1) == len(lines2)):
        for line in differences:
            print(colored(colors.HEADER, "Line " + str(line) + ":"))
            print(fn1 + ": " + differences[line][0])
            print(fn2 + ": " + differences[line][1] + "\n")


