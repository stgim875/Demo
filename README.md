## VIRNECT Remote(Web or Mobile) 리그레션 테스트 자동화

### 테스트 자동화 소개 
목적 : VIRNECT Remot에 대한 결함 수정 또는 신규 기능이 추가 되었을 경우, 기존 기능들이 올바르게 작동하는지 확인합니다. 예를 들어, 화상 회의 기능이 모든 플랫폼에서 정상적으로 작동하는지, 화질과 음질이 품질 표준에 부합하는지 확인합니다.

## 📱 Mobile Class 폴더 파일 소개

| 파일명 | 설명 |
|------|-----|
| **FirstScreen.py** | 앱 첫 진입 시 초기 화면 요소 확인 및 동작을 수행하는 페이지 객체 |
| **Login.py** | 모바일 로그인 화면 자동화 및 로그인 검증을 수행하는 페이지 객체 |
| **Permi.py** | 모바일 OS 권한 요청 팝업 허용/거부 처리 기능을 제공하는 페이지 객체 |
| **PreferencesMenu.py** | 앱 설정 메뉴의 UI 요소 조작 및 상태를 검증하는 페이지 객체 |

## 📌 Web Class 폴더 파일 소개

| 파일명 | 설명 |
|------|-----|
| **header.py** | Remote Web 화면 상단(Header) UI 요소 조작 및 표시 상태를 검증하는 페이지 객체 |
| **login.py** | Remote Web 로그인 화면에서 아이디/비밀번호 입력 및 로그인 동작을 수행하는 페이지 객체 |
| **privacy.py** | 개인정보 처리방침 관련 UI 요소 확인 및 이벤트 검증을 수행하는 페이지 객체 |

**[개발 언어 및 도구]**
- Python : 3.12.1  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
- Pytest: 8.3.4 <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=Pytest&logoColor=white">
- Selenium : 4.29.0  <img src="https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=Selenium&logoColor=white"/>
- Selenium Grid : 4.28.1 <img src="https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=Selenium&logoColor=white"/>
- Appium-Python-Client : v4.5.1 <img src="https://img.shields.io/badge/Appium-EE376D?style=for-the-badge&logo=Appium&logoColor=white">
- Github : <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">
- Jenkins : <img src="https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white">
- Salck : <img src="https://img.shields.io/badge/Slack-4A154B?style=flat-square&logo=Slack&logoColor=white"/>
- Jira : <img src="https://img.shields.io/badge/Jira-0052CC?style=flat-square&logo=Jira&logoColor=white"/>

### [VIRNECT Remote_Web UI 자동화]
#### <코드와 내용이 변경될 수 있습니다.>

https://github.com/stgim875/sample_code/assets/71519636/ebe4e978-8a2f-4f83-9392-dd2672286fa8

### [VIRNECT Remote_Mobile UI 자동화]
#### <코드와 내용이 변경될 수 있습니다.>

https://github.com/stgim875/Demo/assets/71519636/21803471-d29a-4634-a365-9185f1c72915

### [참고 자료]

[Selenium 공식 홈페이지]
https://www.selenium.dev 

[Appium 공식 홈페이지]
https://appium.io/docs/en/latest 

[우아한형제들 기술블로그]
https://techblog.woowahan.com/2658 

[라인 기술블로그]
https://engineering.linecorp.com/ko/blog/build-a-continuous-cicd-environment-based-on-data

[카카오페이 기술블로그]
https://tech.kakaopay.com/post/ifkakao2022-mobile-automation-test-monitoring/
