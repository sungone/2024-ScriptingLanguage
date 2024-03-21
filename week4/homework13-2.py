f = input("파일 이름을 입력하세요")
try:
    with open(f, "r") as infile:
        s = infile.read()
        print('문자', len(s), '개')
        print('단어', len(s.split()), '개')
        print('행', len(s.split('\n')), '개')
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")