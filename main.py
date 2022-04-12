import re

def main():
    val = input("輸入要查詢的單詞")
    reg = "^"
    for e in list(val):
        for j in list(e):
            if re.match(r'[A-z]', j):
                reg += j
            elif re.match(r'\d', j):
                reg += "[A-z]{"+j+"}"
    reg += "$"
    f = open('words.txt')
    b = open("ans.txt","w")
    b.write("")
    b = open("ans.txt","a")
    line = f.readline()
    while line:
        if re.match(rf"{reg}",line):
            print(line)
            b.write(line)
        line = f.readline()
    f.close()
main()
