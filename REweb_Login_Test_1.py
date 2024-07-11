from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from web_class.privacy import PrivacyPage
from web_class.login import LoginPage

import pytest

# Chrome WebDriver 옵션 설정 (필요에 따라 옵션 추가)
options = Options()
options.add_argument('--start-maximized')  # 브라우저가 최대화된 상태로 실행
options.add_argument("--use-fake-ui-for-media-stream")  # 구글 카메라 동의 팝업창 해제
options.add_argument("--disable-notifications") # 알림창 해제
options.add_experimental_option('excludeSwitches', ['disable-popup-blocking']) # 브라우저 팝업창 해제
# options.add_experimental_option("detach", True) # 브라우저를 닫지 않고 유지

# Desired Capabilities 설정
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['browserName'] = 'chrome'
capabilities['version'] = '126.0.6478.62'
capabilities['platform'] = 'WINDOWS'
capabilities['goog:chromeOptions'] = options.to_capabilities()

@pytest.fixture(scope="module")
def browser():
    # Selenium Grid URL
    grid_url = 'http://172.16.50.129:4444/wd/hub'
    
    # Remote WebDriver 초기화
    driver = webdriver.Remote(
        command_executor=grid_url,
        options=options
        )
    
    yield driver
    # 테스트 완료 후 드라이버 종료
    driver.quit()

# Remote_Web v2.10으로 이동하기
def test_privacy_page(browser):
    privacy_page = PrivacyPage(browser)
    
    # 개인 정보 보호 화면으로 이동
    privacy_page.go_to_privacy_page()
    
    # 비공개 페이지에서 고급 버튼 존재 확인
    privacy_page.advanced_button_displayed()
    
    # 비공개 페이지에서 고급 버튼 클릭
    privacy_page.click_advanced_button()
    
    # 비공개 페이지에서 (안전하지 않음) 링크 존재 확인
    privacy_page.unsafe_link_displayed()
    
    # 비공개 페이지에서 (안전하지 않음) 링크 클릭
    privacy_page.click_unsafe_link()

# Remote_Web v2.10 로그인 화면
def test_login(browser):
    login_page = LoginPage(browser)
    
    # Remote 로그인센터 화면 존재 확인
    login_page.go_to_login_displayed()
    
    # 아이디 입력 필드 존재 확인
    login_page.id_input_field_displayed()
    
    # 패스워드 입력 필드 존재 확인
    login_page.pw_input_field_displayed()
    
    # 로그인 버튼 존재 확인
    login_page.login_button_displayed()
    
    # 사용자 이름 및 비밀번호 입력
    login_id = 'user1'
    password = 'Admin1324'
    
    # 아이디 입력
    login_page.enter_username(login_id)
    
    # 패스워드 입력
    login_page.enter_password(password)
    
    # 로그인 버튼 클릭
    login_page.click_login_button()