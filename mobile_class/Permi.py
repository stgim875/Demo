from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Remote Mobile(AOS) 접근 권한 허용 안내 화면
class Permissions:
    def __init__(self, driver):
        self.driver = driver
        
        # 접근 권한 허용 다이얼 로그창
        self.permission_dialogs = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/mobile_permission_fragment")
        
        # 접근 권한 허용 다이얼 로그창 : [확인]
        self.confirmation = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/permission_btn_confirm")
        
        # 사진 촬영 및 동영상 다이얼 로그창
        dialog_display = "com.android.permissioncontroller:id/grant_dialog"
        self.picture_video = (AppiumBy.ID, dialog_display)
        
        # 사진 촬영 및 동영상 : [앱 사용 중에만 허용] 터치
        self.pictrecordapp_allow = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        
        # 기기의 위치 정보 액세스 허용 다이얼 로그창
        self.location_access = (
            AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.android.permissioncontroller:id/content_container']")
        
        # 기기의 위치 정보 액세스 : [앱 사용 중에만 허용] 터치
        self.locationaccess_allow = (
            AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']")
        
        # 오디오 녹음 허용 다이얼 로그창
        self.audio_recording = (AppiumBy.ID, dialog_display)
        
        # 오디오 녹음 : [앱 사용중에만 허용] 터치
        self.audiorecordapp_allow = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        
        # Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창
        self.devices_location = (AppiumBy.ID, dialog_display)
        
        # Remote에서 근처에 있는 기기 연결 및 상대적 위치 : [허용] 터치
        self.devicelocatapp_allow = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        
        # Remote에서 알림 보내도록 허용 다이얼 로그창
        self.notification_daillog = (AppiumBy.ID, dialog_display)
        
        # Remote에서 알림 보내도록 허용 다이얼 로그창 : [허용] 터치
        self.notification_allow = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']")
        
        # Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창
        self.music_audio = (AppiumBy.ID, dialog_display)
        
        # Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창 : [허용] 터치
        self.music_audio_allow = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']")
        
        # VIRNECT Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창
        self.pictvidmusaud = (AppiumBy.ID, dialog_display)
        
        # VIRNECT Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 : [허용] 터치
        self.pictvidmusaudapp_allow = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        
    # 접근 권한 허용 다이얼 로그창 확인하기
    def permission_dialogs_displayed(self):
        try:
            permission = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.permission_dialogs)))
            permission.is_displayed()
            print("접근 권한 허용 다이얼 로그창 출력되었습니다.")
            return True
        except TimeoutException:
            print("접근 권한 허용 다이얼 로그창 출력되지 않았습니다.")
            return False
        
    # 접근 권한 허용 다이얼 로그창에서 [확인] 버튼 확인하기
    def confirmation_permission_displayed(self):
        try:
            confirmation_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.confirmation)))
            confirmation_btn.is_displayed()
            print("접근 권한 허용 다이얼 로그창에 [확인] 버튼이 존재합니다.")
            return True
        except TimeoutException:
            print("접근 권한 허용 다이얼 로그창에 [확인] 버튼이 존재하지 않습니다.")
            return False
        
    # 접근 권한 허용 종류 다이얼 로그창에서 확인 터치하기
    def touch_permission_dialog(self):
        try:
            confirmation_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.confirmation)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(confirmation_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("접근 권한 허용 다이얼 로그창에서 [확인] 버튼을 터치했습니다.")
            return True
        except TimeoutException:
            print("접근 권한 허용 다이얼 로그창에서 [확인] 버튼 터치못했습니다.")
            return False
        
    # Remote에서 사진 촬영 및 동영상 녹화 허용 다이얼 로그창 확인하기
    def picture_recording_modal_displayed(self):
        try:
            picture_recording = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.picture_video)))
            picture_recording.is_displayed()
            print("사진 촬영 및 동영상 녹화 허용 다이얼 로그창이 존재합니다.")
            return True
        except TimeoutException:
            print("사진 촬영 및 동영상 녹화 허용 다이얼 로그창이 존재하지 않습니다.")
            return False
        
    # Remote에서 사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용 선택하기] 버튼 확인하기
    def picture_video_app_allow(self):
        try:
            pictvideo_appallow_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.pictrecordapp_allow)))
            pictvideo_appallow_btn.is_displayed()
            print("사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용 선택하기] 버튼이 존재합니다.")
            return True
        except TimeoutException:
            print("사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용 선택하기] 버튼이 존재하지 않습니다.")
            return False
            
    # Remote에서 사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용 선택하기] 터치하기
    def touch_picture_recording_displayed(self):
        try:
            recording_appallow_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.pictrecordapp_allow)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(recording_appallow_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용] 버튼을 터치했습니다.")
            return True
        except TimeoutException:
            print("사진 촬영 및 동영상 녹화 다이얼 로그창에서 [앱 사용 중에만 허용] 버튼 터치못했습니다.")
            return False
        
    # Remote에서 기기의 위치 정보에 액세스 허용 로그창 확인하기
    def devices_access_modal_displayed(self):
        try:
            devicess_access = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.location_access)))
            devicess_access.is_displayed()
            print("기기의 위치 정보 허용 다이얼 로그창이 존재합니다.")
            return True
        except TimeoutException:
            print("기기의 위치 정보 허용 다이얼 로그창이 존잿하지 않습니다.")
            return False
        
    # Remote에서 기기의 위치 정보 액세스 허용 다이얼 로그창에서 [앱 사용 중에만 허용] 버튼 확인하기
    def devices_access_appallow_displayed(self):
        try:
            location_access = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.locationaccess_allow)))
            location_access.is_displayed()
            print("기기의 위치 정보 액세스 허용 다이얼 로그창에 [앱 사용중에만 허용] 버튼이 존재합니다.")
            return True
        except TimeoutException:
            print("기기의 위치 정보 액세스 허용 다이얼 로그창에 [앱 사용중에만 허용] 버튼이 존재하지 않습니다.")
            return False
        
    # Remote에서 기기의 위치 정보 액세스 허용 다이얼 로그창에서 [앱 사용 중에만 허용] 버튼 터치하기
    def touch_location_access(self):
        try:
            location_access_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.locationaccess_allow)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(location_access_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("기기 위치 정보 액세스 허용 다이얼 로그창에서 [앱 사용 중에만 허용] 버튼을 터치했습니다.")
            return True
        except TimeoutException:
            print("기기 위치 정보 액세스 허용 다이얼 로그창에서 [앱 사용 중에만 허용] 버튼 터치못했습니다.")
            return False
        
    # Remote에서 오디오를 녹음 허용 다이얼 로그창 확인하기
    def audio_recording_modal_displayed(self):
        try:
            audio_recording  = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.audio_recording)))
            audio_recording.is_displayed()
            print("오디오 녹음 허용 다이얼 로그창이 존재합니다.")
            return True
        except TimeoutException:
            print("오디오 녹음 허용 다이얼 로그창이 존재하지 않습니다.")
            return False
        
    # Remote에서 오디오를 녹음 허용 다이얼 로그창에서 [앱 사용 중에만 허용] 버튼 확인하기
    def audio_recording_appallow_displayed(self):
        try:
            audiorecording_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.audiorecordapp_allow)))
            audiorecording_btn.is_displayed()
            print("오디오 녹음 허용 다이얼 로그창에서 [앱 사용중에만 허용] 버튼이 존재합니다.")
            return True
        except TimeoutException:
            print("오디오 녹음 허용 다이얼 로그창에서 [앱 사용중에만 허용] 버튼이 존재하지 않습니다.")
            return False
            
    # Remote에서 오디오를 녹음 허용 다이얼 로그창에서 [앱 사용중에만 허용] 버튼 터치하기
    def touch_audio_recording(self):
        try:
            audiorecording_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.audiorecordapp_allow )))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(audiorecording_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("오디오 녹음 허용 다이얼 로그창에서 [앱 사용 중에만 허용] 버튼을 터치했습니다.")
            return True
        except TimeoutException:
            print("오디오 녹음 허용 다이얼 로그창에서 [앱 사용 중에만 허용] 버튼 터치못했습니다.")
            return False
        
    # Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창 확인하기
    def devices_location_displayed(self):
            try:
                devices_location = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((self.devices_location)))
                devices_location.is_displayed()
                print("기기 연결 및 상대적 위치 파악 다이얼 로그창이 존재합니다.")
                return True
            except TimeoutException:
                print("기기 연결 및 상대적 위치 파악 다이얼 로그창이 존재하지 않습니다.")
                return False
            
    # Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창에서 [허용] 버튼 확인하기
    def devices_location_allow_displayed(self):
        try:
            deviceslocation_allow = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.devicelocatapp_allow)))
            deviceslocation_allow.is_displayed()
            print("기기 연결 및 상대적 위치 파악 다이얼 로그창에 [허용] 버튼이 존재합니다.")
            return True
        except TimeoutException:
            print("기기 연결 및 상대적 위치 파악 다이얼 로그창에 [허용] 버튼이 존재하지 않습니다.")
            return False
        
    # Remote에서 근처에 있는 기기 연결 및 상대적 위치 파악 다이얼 로그창에서 [허용] 버튼 터치하기
    def touch_devices_location_allow(self):
        try:
            deviceslocation_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.devicelocatapp_allow)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(deviceslocation_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("상대적 위치 파악 허용 다이얼 로그창에서 [허용] 버튼을 터치했습니다.")
            return True
        except TimeoutException:
            print("상대적 위치 파악 허용 다이얼 로그창에서 [허용] 버튼 터치못했습니다.")
            return False
        
    # Remote에서 알림 허용 다이얼 로그창 확인하기
    def notication_permission_displayed(self):
            try:
                noti_permission = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((self.notification_daillog)))
                noti_permission.is_displayed()
                print("Remote에서 알림 허용 다이얼 로그창이 존재합니다.")
                return True
            except TimeoutException:
                print("Remote에서 알림 허용 다이얼 로그창이 존재하지 않습니다.")
                return False
            
    # Remote에서 알림 허용 다이얼 로그창에서 [허용] 버튼 확인하기
    def notification_allow_displayed(self):
        try:
            noti_allow = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.notification_allow)))
            noti_allow.is_displayed()
            print("Remote에서 알림 허용 다이얼 로그창에 [허용] 버튼이 존재합니다.")
            return True
        except TimeoutException:
            print("Remote에서 알림 허용 다이얼 로그창에서 [허용] 버튼이 존재하지 않습니다.")
            return False
        
    # Remote에서 알림 허용 다이얼 로그창에서 [허용] 버튼 터치하기
    def touch_notification_allow(self):
        try:
            notification_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.notification_allow)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(notification_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("Remote에서 알림 허용 다이얼 로그창에서 [허용] 버튼을 터치했습니다.")
            return True
        except TimeoutException:
            print("Remote에서 알림 허용 다이얼 로그창에서 [허용] 버튼 터치못했습니다.")
            return False
        
    # Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창 확인하기
    def music_audio_displayed(self):
            try:
                music_audio = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((self.music_audio)))
                music_audio.is_displayed()
                print("Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창이 존재합니다.")
                return True
            except TimeoutException:
                print("Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창이 존재하지 않습니다.")
                return False
        
    # Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창에서 [허용] 버튼 확인하기
    def music_audio_allow_displayed(self):
        try:
            noti_allow = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.music_audio_allow)))
            noti_allow.is_displayed()
            print("Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창에 [허용] 버튼이 존재합니다.")
            return True
        except TimeoutException:
            print("Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창에 [허용] 버튼이 존재하지 않습니다.")
            return False
        
    # Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창에서 [허용] 버튼 터치하기
    def touch_music_audio_allow(self):
        try:
            music_audio_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.notification_allow)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(music_audio_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창에서 [허용] 버튼을 터치했습니다.")
            return True
        except TimeoutException:
            print("Remote에서 기기의 음악과 오디오 액세스 허용 다이얼 로그창에서 [허용] 버튼 터치못했습니다.")
            return False
        
    # Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창 확인하기
    def pictu_video_mus_audio_displayed(self):
        try:
            pict_vid_mus_aud = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.pictvidmusaud)))
            pict_vid_mus_aud.is_displayed()
            print("기기의 사진, 동영상, 음악, 오디오 액세스 허용 다이얼 로그창이 존재합니다.")
            return True
        except TimeoutException:
            print("기기의 사진, 동영상, 음악, 오디오 액세스 허용 다이얼 로그창이 존재하지 않습니다.")
            return False
        
    # Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창에서 [허용] 버튼 확인하기
    def picvidmusaud_allow_displayed(self):
        try:
            picvidmusaud_allow = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.pictvidmusaudapp_allow)))
            picvidmusaud_allow.is_displayed()
            print("기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창에 [허용] 버튼이 존재합니다.")
            return True
        except TimeoutException:
            print("기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창에서 [허용] 버튼이 존재하지 않습니다.")
            return False
        
    # Remote에서 기기의 사진, 동영상, 음악, 오디오 액세스 다이얼 로그창에서 [허용] 버튼 터치하기
    def touch_picvidmusaud_allow(self):
        try:
            picvidmusaud_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.pictvidmusaudapp_allow)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(picvidmusaud_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("기기의 사진 및 미디어 액세스 허용 다이얼 로그창에서 [허용] 버튼을 터치했습니다.")
            return True
        except TimeoutException:
            print("기기의 사진 및 미디어 액세스 허용 다이얼 로그창에서 [허용] 버튼 터치못했습니다.")
            return False