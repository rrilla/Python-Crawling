# Python-Crawling

## 1. 라이브러리 설치
```
  pip install selenium
  pip install beautifulsoup4
  pip install PyMySQL
  pip install requests
  pip install fake-useragent # ramdon user-agent값 생성
```

## 2. Chrome Driver 설치
https://chromedriver.chromium.org/downloads

## 3. 에러
- ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
- 서버측에서 허용하지 않는 방식으로 접근하는 호출을 걸러냄.
```
from fake_useragent import UserAgent

ua = UserAgent()
url = "주소"
headers = {'User-Agent' : ua.random}

r = requests.get(url, headers=headers)
```
