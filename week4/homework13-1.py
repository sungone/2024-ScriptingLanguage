f = input("파일 이름을 입력하세요:")
infile = open(f , "r")
s = infile.read()
removeString = input("제거할 문자열을 입력 : ")
newS = s.replace(removeString , '')
infile.close()
outfile = open(f , "w")
print(newS , file=outfile , end = '')
print("완료")
outfile.close()
