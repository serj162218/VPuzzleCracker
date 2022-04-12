import re
def main():
    val = input("輸入要查詢的單詞")
    arr = re.findall(r'(\d[A-z])',val)
    for e in arr:
        print(e)
main()