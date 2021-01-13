# 패키지 설치
# 파이썬에서 제공하는 기본 패키지를 제외하고
# 다른 사람들이 만들어 검증받은 다른 패키지를 가져다가 설치해서 사용
# google pypi 검색
# pip install beautifulsoup4   터미널에 입력 후 실행(설치)
# pip list (설치된 pip 확인)
# pip show beautifulsoup4
# pip install --upgrade beautifulsoup4
# pip uminstall beautifulsoup4 (삭제여부 확인 후 입력)

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
