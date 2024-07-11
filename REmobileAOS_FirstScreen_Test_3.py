from appium import webdriver
from appium.options.android import UiAutomator2Options
from mobile_class.Permi import Permissions
from mobile_class.Login import RemoteLogin
from mobile_class.FirstScreen import RemoteCollaborate
from mobile_class.PreferencesMenu import RemotePreferences

import pytest
import time

@pytest.fixture(scope = "module")
def appium_driver():
    options = UiAutomator2Options().load_capabilities(
        {
            "deviceName": "T21G",
            "platformName": "Android",
            "platformVersion": "11",
            "automationName": "UiAutomator2",
            "app": "C:/appium_realwear/remote_realwear_21000025.apk",
            "newCommandTimeout": "3000",
            "noReset": "false",
            "appWaitActivity": "*"
        }
    )
    
    driver = webdriver.Remote('http://172.16.50.129:4444/wd/hub', options=options)
    yield driver
    driver.quit()

# Remote 접근 권한 허용
def test_permissions(appium_driver):
    dail_permission = Permissions(appium_driver)
    
    # 접근 권한 허용 다이얼 로그창 확인하기
    dail_permission.permission_dialogs_displayed()
    
    # 접근 권한 허용 다이얼 로그창에서 [확인] 버튼 확인하기
    dail_permission.confirmation_permission_displayed()
    
    # 접근 권한 허용 종류 다이얼 로그창에서 확인 터치하기
    dail_permission.touch_permission_dialog()
    
    # Remote에서 사진 촬영 및 동영상 녹화 허용 다이얼 로그창 확인하기
    dail_permission.picture_recording_modal_displayed()
    
    # Remote에서 사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용 선택하기] 버튼 확인하기
    dail_permission.picture_video_app_allow()
    
    # Remote에서 사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용 선택하기] 터치하기
    dail_permission.touch_picture_recording_displayed()
    
    # Remote에서 오디오를 녹음 허용 다이얼 로그창 확인하기
    dail_permission.audio_recording_modal_displayed()
    
    # Remote에서 오디오를 녹음 허용 다이얼 로그창에서 [앱 사용중에만 허용] 버튼 확인하기
    dail_permission.audio_recording_appallow_displayed()
    
    # Remote에서 오디오를 녹음 허용 다이얼 로그창에서 [앱 사용중에만 허용] 버튼 터치하기
    dail_permission.touch_audio_recording()
    
    # Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창 확인하기
    dail_permission.devices_location_displayed()
    
    # Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창에서 [허용] 버튼 확인하기
    dail_permission.devices_location_allow_displayed()
    
    # Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창에서 [허용] 버튼 터치하기
    dail_permission.touch_devices_location_allow()
    
    # Remote에서 알림 허용 다이얼 로그창 확인하기
    dail_permission.notication_permission_displayed()
    
    # Remote에서 알림 허용 다이얼 로그창에서 [허용] 버튼 확인하기
    dail_permission.notification_allow_displayed()
    
    # Remote에서 알림 허용 다이얼 로그창에서 [허용] 버튼 터치하기
    dail_permission.touch_notification_allow()
    
    # Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창 확인하기
    dail_permission.music_audio_displayed()
    
    # Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창에서 [허용] 버튼 확인하기
    dail_permission.music_audio_allow_displayed()
    
    # Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창에서 [허용] 버튼 터치하기
    dail_permission.touch_music_audio_allow()
    
    # Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창 확인하기
    dail_permission.pictu_video_mus_audio_displayed()
    
    # Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창에서 [허용] 버튼 확인하기
    dail_permission.picvidmusaud_allow_displayed()
    
    # Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창에서 [허용] 버튼 터치하기
    dail_permission.touch_picvidmusaud_allow()

# Remote 로그인 화면에서 로그인
def test_remotelogin(appium_driver):
    remote_login = RemoteLogin(appium_driver)
    
    # Remote 로그인 화면 확인하기
    remote_login.login_screen_displayed()
    
    # Remote 로그인 화면에서 아이디 입력 필드 확인하기
    remote_login.id_inputfield_displayed()
    
    # Mobile 아이디 및 패스워드 정보
    user_id = 'user2'
    user_pw = 'Admin1324'
    
    # Remote 로그인 화면에서 아이디 입력하기
    remote_login.login_id_input(user_id)
    
    # Remote 로그인 화면에서 패스워드 입력 필드 확인하기
    remote_login.pw_inputfield_displayed()
    
    # Remote 로그인 화면에서 패스워드 입력하기
    remote_login.login_pw_input(user_pw)
    
    # Remote  로그인 화면에서 로그인 버튼 확인하기
    remote_login.loging_button_displayed()
    
    # Remote 로그인 화면에서 로그인 버튼 터치하기
    remote_login.touch_loging_button()
    
    # 워크스페이스 선택 모달창 확인하기
    remote_login.workspace_modal_displayed()
    
    # 워크스페이스 선택 모달창에서 My Workspace 선택하기
    remote_login.touch_my_workspace()

# Remote Mobile 원격 협업 메인 화면
def test_remote_collaborate_main(appium_driver):
    remote_main = RemoteCollaborate(appium_driver)
    
    # 원격 협업 메인 화면 확인
    remote_main.remote_collabrate_displayed()
    
    # 원격 협업 리스트를 새로고침하기
    remote_main.remote_collaborate_re_flash
    
    # 원격 협업 리스트 화면 확인하기
    remote_main.remote_collaborate_list_displayed()
    
    # 원격 협업 > [찾기] 버튼 확인하기
    remote_main.search_button_displayed()
    
    # 3초동안 대기
    time.sleep(3)
    
    # 원격 협업 알림 메뉴 확인하기
    remote_main.alarm_menu_displayed()
    
    # 원격 협업 알림 메뉴 터치하기
    remote_main.touch_alarm_menu()
    
    # 원격 협업 알림 리스트 확인하기
    remote_main.alarm_list_displayed()
    
    # 원격 협업 알림 리스트에서 알림 해제 버튼 확인하기
    remote_main.alarm_list_release_displayed()
    
    # 원격 협업 알림 리스트에서 알림 해제 버튼 터치하기
    remote_main.touch_alarm_release_button()
    
    # 원격 협업 알림 리스트에서 알림 수신 버튼 확인하기
    remote_main.alarm_list_receive_displayed()
    
    # 원격 협업 알림 리스트에서 알림 수신 버튼 터치하기
    remote_main.touch_alarm_receive_button()
    
    # 원격 협업 > 알림 메뉴에서 [이전] 버튼 확인하기
    remote_main.alarm_backbtn_displayed()
    
    # 원격 협업 > 알림 메뉴에서 [이전] 버튼 터치하기
    remote_main.touch_alarm_back_button()
    
    # 원격 협업 > [원격 협업 생성] 메뉴 확인하기
    remote_main.remote_collaborate_button_displayed()
    
    # 원격 협업 > [원격 협업 생성] 메뉴 터치하기
    remote_main.touch_remote_collaborate_button()
    
    # 원격 협업 생성 메뉴 > 원격 협업 생성 화면 확인
    remote_main.remote_collaborate_create_displayed()
    
    # 원격 협업 생성 메뉴 > 원격 협업 생성 화면에서 [이전] 버튼 확인
    remote_main.create_back_button_displayed()
    
    # 원격 협업 생성 메뉴 > 원격 협업 생성 화면에서 [이전] 버튼 터치하기
    remote_main.touch_create_back_button()
    
    # 원격 협업 > [오픈룸 생성] 메뉴 확인하기
    remote_main.openroom_create_button_displayed()
    
    # 원격 협업 > [오픈룸 생성] 메뉴 터치하기
    remote_main.touch_open_room_button()
    
    # 원격 협업 > 오픈룸 생성 메뉴 > 오픈룸 생성 화면 확인하기
    remote_main.openroom_create_screen_displayed()
    
    # 오픈룸 생성 메뉴 > 오픈룸 생성 화면에서 [이전] 버튼 확인하기
    remote_main.openroom_back_button_displayed()
    
    # 오픈룸 생성 메뉴 > 오픈룸 생성 화면에서 [이전] 버튼 터치하기
    remote_main.touch_openroom_back_button()
    
    # Home 메뉴 > [예약 목록] 메뉴 확인하기
    remote_main.home_menu_reservation_displayed()
    
    # Home 메뉴 > [예약 목록] 메뉴 터치하기
    remote_main.touch_home_reservation_menu()
    
    # Home 메뉴 > [예약 목록] 메인 화면 확인하기
    remote_main.reservation_menu_displayed()
    
    # Home 메뉴 > [예약 목록] 메뉴 > 예약 목록 [찾기] 메뉴 확인하기
    remote_main.reservation_serch_menu_displayed()
    
    # Home 메뉴 > [예약 목록] 리스트를 새로고침하기
    remote_main.recservation_menu_re_flash()
    
    # Home 메뉴 > [최근 기록] 메뉴 확인하기
    remote_main.home_menu_recentmenu_displayed()
    
    # Home 메뉴 > [최근 기록] 메뉴 터치하기
    remote_main.touch_home_recent_menu()
    
    # [최근 기록] 메인 화면 확인하기
    remote_main.recent_menu_displayed()
    
    # [최근 기록] 리스트를 새로고침하기
    remote_main.recent_menu_re_flash()
    
    # [최근 기록] 메뉴 > 최근 기록 [찾기] 메뉴 확인하기
    remote_main.recent_serch_menu_displayed()
    
    # Home 메뉴 > [멤버] 메뉴 확인하기
    remote_main.home_menu_membermenu_displayed()
    
    # Home 메뉴 > [멤버] 메뉴 터치하기
    remote_main.touch_member_menu()
    
    # [멤버] 리스트를 새로고침하기
    remote_main.member_menu_re_flash()
    
    # [멤버] 메뉴 > 멤버 메인 화면 > 멤버 [찾기] 메뉴 확인하기
    remote_main.member_serch_menu_displayed()
    
    # [멤버] 메뉴 > 멤버 메인 화면 > 멤버 [찾기] 메뉴 터치하기
    remote_main.touch_member_serch_button()
    
    # [멤버] 메뉴 > 멤버 메인 화면 > 멤버 [찾기] 메뉴 > 멤버 [검색 입력 필드] 확인하기
    remote_main.menber_serch_inputfield_displayed()
    
    # [멤버] 메뉴 > 멤버 메인 화면 > 멤버 [찾기] 메뉴 > 멤버 [검색 입력 필드] > [취소] 메뉴 확인하기
    remote_main.member_serch_inputfield_cancel_displayed()
    
    # [멤버] 메뉴 > 멤버 메인 화면 > 멤버 [찾기] 메뉴 > 멤버 [검색 입력 필드] > [취소] 메뉴 터치하기
    remote_main.touch_member_inputfield_cancel()
    
    # Home 메뉴 > [환경 설정] 메뉴 확인하기
    remote_main.home_menu_preferencesmenu_displayed()
    
    # Home 메뉴 > [환경 설정] 메뉴 터치하기
    remote_main.touch_preferences_menu()
    
    # [환경 설정] 메인 화면 확인하기
    remote_main.preferences_menu_displayed()

# 환경 설정 메뉴 > 로그아웃
def test_preferences_logout(appium_driver):
    remote_logout = RemotePreferences(appium_driver)
    
    # [환경 설정] 메뉴에서 [로그아웃] 메뉴 확인하기
    remote_logout.preferences_logout_displayed()
    
    # 환경 설정] 메뉴에서 [로그아웃] 메뉴 터치하기
    remote_logout.touch_preferences_logout()