from appium import webdriver
from appium.options.android import UiAutomator2Options
from mobile_class.Permi import Permissions

import pytest
import time

@pytest.fixture(scope = "module")
def appium_driver():
    options = UiAutomator2Options().load_capabilities(
        {
            "deviceName": "Galaxy S22",
            "platformName": "Android",
            "platformVersion": "14",
            "automationName": "UiAutomator2",
            "app": "C:/appium_application/remote_mobile.apk",
            "newCommandTimeout": "3000",
            "noReset": "false",
            "appWaitActivity": "*"
        }
    )
    
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    yield driver
    driver.quit()
    
# Remote 접근 권한 허용
def test_permissions(appium_driver):
    dail_permission = Permissions(appium_driver)
    
    # 접근 권한 허용 다이얼 로그창 확인
    dail_permission.permission_dialogs_displayed()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # 접근 권한 허용 다이얼 로그창에서 [확인] 버튼 확인
    dail_permission.confirmation_permission_displayed()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # 접근 권한 허용 종류 다이얼 로그창에서 확인 터치하기
    dail_permission.touch_permission_dialog()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 사진 촬영 및 동영상 녹화 허용 다이얼 로그창 확인
    dail_permission.picture_recording_modal_displayed()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용 선택하기] 버튼 확인
    dail_permission.picture_video_app_allow()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용 선택하기] 터치하기
    dail_permission.touch_picture_recording_displayed()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 오디오를 녹음 허용 다이얼 로그창 확인
    dail_permission.audio_recording_modal_displayed()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 오디오를 녹음 허용 다이얼 로그창에서 [앱 사용중에만 허용] 버튼 확인
    dail_permission.audio_recording_appallow_displayed()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 오디오를 녹음 허용 다이얼 로그창에서 [앱 사용중에만 허용] 버튼 터치하기
    dail_permission.touch_audio_recording()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창 확인
    dail_permission.devices_location_displayed()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창에서 [허용] 버튼 확인
    dail_permission.devices_location_allow_displayed()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창에서 [허용] 버튼 터치하기
    dail_permission.touch_devices_location_allow()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 알림 허용 다이얼 로그창 확인
    dail_permission.notication_permission_displayed()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 알림 허용 다이얼 로그창에서 [허용] 버튼 확인
    dail_permission.notification_allow_displayed()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 알림 허용 다이얼 로그창에서 [허용] 버튼 터치하기
    dail_permission.touch_notification_allow()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창 확인
    dail_permission.music_audio_displayed()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창에서 [허용] 버튼 확인
    dail_permission.music_audio_allow_displayed()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창에서 [허용] 버튼 터치하기
    dail_permission.touch_music_audio_allow()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창 확인
    dail_permission.pictu_video_mus_audio_displayed()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창에서 [허용] 버튼 확인
    dail_permission.picvidmusaud_allow_displayed()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창에서 [허용] 버튼 터치하기
    dail_permission.touch_picvidmusaud_allow()
    
    # 3초간 암묵적 대기
    appium_driver.implicitly_wait(time_to_wait=3)
    
    # 3초동안 대기
    time.sleep(3)