from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from web_class.privacy import PrivacyPage
from web_class.login import LoginPage
from web_class.header import HeaderArea

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
def test_login_page(browser):
    login_page = LoginPage(browser)
    
    # Remote 로그인센터 화면 존재 확인하기
    login_page.go_to_logincenter_displayed()
    
    # 아이디 입력 필드 존재 확인하기
    login_page.id_input_field_displayed()
    
    # 패스워드 입력 필드 존재 확인하기
    login_page.pw_input_field_displayed()
    
    # 로그인 버튼 존재 확인하기
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

# Remote_Web v2.10 화면 상단 Header 메뉴
def test_header_menu(browser):
    header_menu = HeaderArea(browser)
    
    # 워크스페이스 메뉴 확인하기
    header_menu.work_space_displayed()
    
    # 워크스페이스 메뉴를 두번 클릭하기
    header_menu.click_workspace_menu()
    
    # 영상 on/off 메뉴 확인하기
    header_menu.dis_on_off_displayed()
    
    # 영상 on/off 메뉴를 두번 클릭하기
    header_menu.click_display_on_off()
    
    # 마이크 on/off 메뉴 확인하기
    header_menu.mic_on_off_displayed()
    
    # 마이크 on/off 메뉴를 두번 클릭하기
    header_menu.click_mic_on_off()
    
    # 스피커 on/off 메뉴 확인하기
    header_menu.speaker_menu_displayed()
    
    # 스피커 on/off 메뉴를 두번 클릭하기
    header_menu.click_speaker_on_off_menu()
    
    # 알림 메뉴 확인하기
    header_menu.notification_menu_displayed()
    
    # 알림 메뉴를 한번 클릭하기
    header_menu.one_click_noti_menu()
    
    # 알림 메뉴 옵션 박스 메뉴 출력 확인하기
    header_menu.noti_menu_optionbox()
    
    # 알림 Push off > on > 버튼 두번 클릭하기
    header_menu.click_noti_push_on_off()
    
    # 알림 메뉴를 한번 더 클릭하여 알림 메뉴 닫기
    header_menu.re_click_noti_menu()
    
    # 나의 프로필 메뉴 확인하기
    header_menu.my_profile_menu_displayed()
    
    # 나의 프로필 메뉴를 클릭하기
    header_menu.click_myprofile_menu()
    
    # 나의 프로필 리스트 옵션 박스 메뉴 출력 확인하기
    header_menu.my_profile_list_displayed()
    
    # 나의 프로필 메뉴에서 워크스테이션 메뉴 확인하기
    header_menu.work_station_menu_displayed()
    
    # 나의 프로필 메뉴에서 대시보드 메뉴 확인하기
    header_menu.dash_board_menu_displyed()
    
    # 나의 프로필 메뉴에서 로컬 녹화 파일 메뉴 확인하기
    header_menu.local_file_menu_displayed()
    
    # 나의 프로필 메뉴에서 로그아웃 메뉴 확인하기
    header_menu.logout_menu_displayed()
    
    # 나의 프로필 메뉴에서 로그아웃 메뉴 선택하기
    header_menu.click_logout_menu()