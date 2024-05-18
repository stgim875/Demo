from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from web_class.privacy import PrivacyPage
from web_class.login import LoginPage
from web_class.header import HeaderArea

import pytest

options = Options()
options.add_argument("--use-fake-ui-for-media-stream")  # 구글 카메라 동의 팝업창 해제
options.add_argument('--start-maximized')  # 브라우저가 최대화된 상태로 실행
# options.add_experimental_option("detach", True) # 브라우저를 닫지 않고 유지

@pytest.fixture(scope = "module")
def browser():
    # 크롬 드라이버의 절대 경로 설정
    CHROME_DRIVER_PATH = ("C:\\chromedriver-win64\\chromedriver.exe")
    service = Service(CHROME_DRIVER_PATH)
    # Chrome WebDriver 초기화
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit
    
# Remote_Web v2.10으로 이동하기
def test_privacy_page(browser):
    privacy_page = PrivacyPage(browser)
    
    # 개인 정보 보호 화면으로 이동
    privacy_page.go_to_privacy_page()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 비공개 페이지에서 고급 버튼 존재 확인
    privacy_page.advanced_button_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 비공개 페이지에서 고급 버튼 클릭
    privacy_page.click_advanced_button()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 비공개 페이지에서 (안전하지 않음) 링크 존재 확인
    privacy_page.unsafe_link_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 비공개 페이지에서 (안전하지 않음) 링크 클릭
    privacy_page.click_unsafe_link()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
# Remote_Web v2.10 로그인 화면
def test_login_page(browser):
    login_page = LoginPage(browser)
    
    # Remote 로그인센터 화면 존재 확인
    login_page.go_to_login_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 아이디 입력 필드 존재 확인
    login_page.id_input_field_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 패스워드 입력 필드 존재 확인
    login_page.pw_input_field_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 로그인 버튼 존재 확인
    login_page.login_button_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 사용자 이름 및 비밀번호 입력 테스트
    login_id = 'user1'
    password = 'Admin1324'
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 아이디 입력
    user_id_input = login_page.enter_username(login_id)
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 아이디와 입력된 값 비교
    user_id_input and login_page.compare_username(user_id_input.get_attribute("value"), login_id)
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 패스워드 입력
    user_password_input = login_page.enter_password(password)
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 아이디와 입력된 값 비교
    user_password_input and login_page.compare_password(user_password_input.get_attribute("value"), password)
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 로그인 버튼 클릭
    login_page.click_login_button()
    
# Remote_Web v2.10 화면 상단 Header 메뉴
def test_header_menu(browser):
    header_menu = HeaderArea(browser)
    
    # 워크스페이스 메뉴 확인하기
    header_menu.work_space_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 워크스페이스 메뉴를 두번 클릭하기
    header_menu.click_workspace_menu()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 영상 on/off 메뉴 확인하기
    header_menu.dis_on_off_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 영상 on/off 메뉴를 두번 클릭하기
    header_menu.click_display_on_off()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 마이크 on/off 메뉴 확인하기
    header_menu.mic_on_off_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 마이크 on/off 메뉴를 두번 클릭하기
    header_menu.click_mic_on_off()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 스피커 on/off 메뉴 확인하기
    header_menu.speaker_menu_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 스피커 on/off 메뉴를 두번 클릭하기
    header_menu.click_speaker_on_off_menu()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 알림 메뉴 확인하기
    header_menu.notification_menu_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 알림 메뉴를 한번 클릭하기
    header_menu.one_click_noti_menu()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 알림 메뉴 옵션 박스 메뉴 출력 확인하기
    header_menu.noti_menu_optionbox()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 알림 Push off > on > 버튼 두번 클릭하기
    header_menu.click_noti_push_on_off()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 알림 메뉴를 한번 더 클릭하여 알림 메뉴 닫기
    header_menu.re_click_noti_menu()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 메뉴 확인하기
    header_menu.my_profile_menu_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 메뉴를 클릭하기
    header_menu.click_myprofile_menu()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 리스트 옵션 박스 메뉴 출력 확인하기
    header_menu.my_profile_list_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 메뉴에서 워크스테이션 메뉴 확인하기
    header_menu.work_station_menu_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 메뉴에서 대시보드 메뉴 확인하기
    header_menu.dash_board_menu_displyed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 메뉴에서 로컬 녹화 파일 메뉴 확인하기
    header_menu.local_file_menu_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 메뉴에서 로그아웃 메뉴 확인하기
    header_menu.logout_menu_displayed()
    
    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 메뉴에서 로그아웃 메뉴 선택하기
    header_menu.click_logout_menu()
    