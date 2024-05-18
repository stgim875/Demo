from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RemoteCollaborate:
    def __init__(self, driver):
        self.driver = driver
        
        # 원격 협업 > 원격 협업 메인 화면
        self.collaborate_main = (
            AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/home_tv_title' and @text='원격 협업']")
        
        # 원격 협업 >  원격 협업 메인 화면 > 원격 협업 [찾기] 메뉴
        serch_menu_xpath = "//android.widget.ImageView[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/home_iv_search']"
        self.serch_menu = (AppiumBy.XPATH, serch_menu_xpath)
        
        # 원격 협업 > 원격 협업 리스트 화면
        self.collaborate_list = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/fragment_container")
        
        # 원격 협업 > 원격 협업 리스트 화면 > [취소] 버튼
        self.collaborate_cancel = (
            AppiumBy.XPATH, "//android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView")
        
        # 원격 협업 > [알림] 메뉴
        self.alarm_menu = (AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/home_iv_alarm']")
        
        # 원격 협업 > 원격 협업 [알림] 메뉴 > 알림 리스트
        self.alarm_list = (
            AppiumBy.XPATH, "//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup[2]")
        
        # 원격 협업 > 원격 협업 알림 > 알림 리스트 > [알림 해제]
        self.alarm_release = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_tv_toggle_subscribe")
        
        # 원격 협업 > 원격 협업 알림 > 알림 리스트 > [알림 수신]
        self.alarm_receive = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_tv_toggle_subscribe")
        
        # 원격 협업 > 원격 협업 알림 > 알림 리스트 > [이전] 버튼
        self.alarm_backbutton = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_iv_search")
        
        # 원격 협업 > [원격 협업 생성] 메뉴
        self.collaborate_create_menu = (
            AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/btn_create_reservation' and @text='원격 협업 생성']")
        
        # 원격 협업 > [원격 협업 생성] 메뉴 > 원격 협업 생성 메인 화면
        self.remote_collaborate_screen = (
            AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/home_tv_title' and @text='원격 협업 생성']")
        
        # 원격 협업 > [원격 협업 생성] 메뉴 > 원격 협업 생성 화면 >  [이전] 버튼
        self.create_backbutton = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_iv_back")
        
        # 원격 협업 > [오픈룸 생성] 메뉴
        self.openroom_btn = (
            AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/btn_create_open_room' and @text='오픈룸 생성']")
        
        # 원격 협업 > [오픈룸 생성] 메뉴 > 오픈룸 생성 메뉴 화면
        self.openroom_create_screen = (
            AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/home_tv_title' and @text='오픈룸 생성']")
        
        # 원격 협업 > [오픈룸 생성] 메뉴 > 오픈룸 생성 화면 > [이전] 버튼
        self.openroom_backbutton = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_iv_back")
        
        # [예약 목록] 메뉴
        self.reservation = (AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/home_iv_reservations']")
        
        # [예약 목록] 메뉴 > 예약 목록 메인 화면
        self.reservation_list = (
            AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/home_tv_title' and @text='예약 목록']")
        
        # [예약 목록] 메뉴 > 예약 목록 메인 화면 > 예약 목록 [찾기] 메뉴
        self.reservation_serch_menu = (AppiumBy.XPATH, serch_menu_xpath)
        
        # [최근 기록] 메뉴
        self.recent_records = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_iv_recent_records")
        
        # [최근 기록] 메뉴 > 최근 기록 메인 화면
        self.recent_records_list = (
            AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/home_tv_title' and @text='최근 기록']")
        
        # [최근 기록] 메뉴 > 최근 기록 메인 화면 > 최근 기록 [찾기] 메뉴
        self.recent_serch_menu = (AppiumBy.XPATH, serch_menu_xpath)
        
        # [최근 기록] 메뉴 > 최근 기록 메인 화면 > 최근 기록 [찾기] 메뉴 > 최근 기록 [검색 입력 필드]
        self.recent_serch_inputfield = (
            AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/cl_search_field_wrapper']")
        
        # [최근 기록] 메뉴 > 최근 기록 메인 화면 > 최근 기록 찾기 메뉴 > 최근 기록 [검색 입력 필드] > [취소]
        self.recent_cancel_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='취소']")
        
        # [멤버] 메뉴
        self.member_menu = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_iv_member")
        
        # [멤버] 메뉴 > 멤버 메인 화면
        self.member_menu_list = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/home_tv_title' and @text='멤버']")
        
        # [멤버] 메뉴 > 멤버 메인 화면 > 멤버 [찾기] 메뉴
        self.member_serch_menu = (AppiumBy.XPATH, serch_menu_xpath)
        
        # [멤버] 메뉴 > 멤버 메인 화면 > 멤버 찾기 메뉴 > 멤버 [검색 입력 필드]
        self.member_serch_inputfield = (
            AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/cl_search_field_wrapper']")
        
        # [멤버] 메뉴 > 멤버 메인 화면 > 멤버 찾기 메뉴 > 멤버 [검색 입력 필드] > [취소]
        self.member_cancel_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='취소']")
        
        # [환경 설정] 메뉴 
        self.preferences_menu = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_iv_settings")
        
        # [환경 설정] 메뉴 > 환경 설정 메인 화면
        self.preferences_main_scree = (
            AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/home_tv_title' and @text='환경 설정']")
        
    # [원격 협업] 메인 화면 확인하기
    def remote_collabrate_displayed(self):
        try:
            main_collaborate = WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element((self.collaborate_main), "원격 협업"))
            if main_collaborate:
                print("[원격 협업] 메인 화면이 존재합니다.")
            else:
                None
            return main_collaborate
        except NoSuchElementException:
            print("[원격 협업] 메인 화면을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 리스트를 새로고침하기
    def remote_collaborate_re_flash(self):
        try:
            collaborate_re_flash = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.collaborate_list)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(535, 825)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(532, 1453)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("원격 협업 정보가 갱신되었습니다..")
            return collaborate_re_flash
        except NoSuchElementException:
            print("원격 협업 리스트에서 새로고침을 하지 못했습니다.")
            return False
        
    # 원격 협업 리스트 화면 확인하기
    def remote_collaborate_list_displayed(self):
        try:
            collaborate_list = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_list)))
            if collaborate_list.is_displayed():
                print("원격 협업 리스트 화면이 존재합니다.")
            else:
                None
            return collaborate_list
        except NoSuchElementException:
            print("원격 협업 리스트 화면을 찾을 수 없습니다.")
            
    # 원격 협업 > [찾기] 버튼 확인하기
    def search_button_displayed(self):
        try:
            serch_menu_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.serch_menu)))
            if serch_menu_btn.is_displayed():
                print("원격 협업 >  [찾기] 버튼이 존재합니다.")
            else:
                None
            return serch_menu_btn
        except NoSuchElementException:
            print("원격 협업>  [찾기] 버튼을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 > [찾기] 버튼 터치하기
    def touch_collaborate_serch_button(self):
        try:
            serch_button_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.serch_menu)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(serch_button_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("원격 협업 >  [찾기] 버튼을 터치했습니다.")
            return serch_button_touch
        except NoSuchElementException:
            print("원격 협업 > [찾기] 버튼을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 > [찾기] 버튼 터치 > [취소] 버튼 확인하기
    def collaborate_cancel_button_displayed(self):
        try:
            collabo_cancel_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_cancel)))
            if collabo_cancel_btn.is_displayed():
                print("원격 협업 > 원격 협업 검색 리스트에 [취소] 버튼이 존재합니다.")
            else:
                None
            return collabo_cancel_btn
        except NoSuchElementException:
            print("원격 협업 > 원격 협업 검색 리스트에 [취소] 버튼을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 >  [찾기] 버튼 터치 > [취소] 버튼 터치하기
    def touch_collaborate_cancel_button(self):
        try:
            cancel_button_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.collaborate_cancel)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(cancel_button_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("원격 협업 >  원격 협업 > 원격 협업 검색 리스트에 [취소] 버튼을 터치했습니다.")
            return cancel_button_touch
        except NoSuchElementException:
            print("원격 협업 > 원격 협업 검색 리스트에 [취소] 버튼을 터치하지 못했습니다.")
            return False
        
    # 원격 협업 > 알림 메뉴 확인하기
    def alarm_menu_displayed(self):
        try:
            alarm_menu = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.alarm_menu)))
            if alarm_menu.is_displayed():
                print("원격 협업 > 알림 메뉴가 존재합니다.")
            else:
                None
            return alarm_menu.is_displayed
        except NoSuchElementException:
            print("원격 협업 알림 > 메뉴를 찾을 수 없습니다.")
            return False
        
    # 원격 협업 알림 메뉴 터치하기
    def touch_alarm_menu(self):
        try:
            alarm_menu_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.alarm_menu)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(alarm_menu_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("원격 협업 > 알림 메뉴를 터치했습니다.")
            return alarm_menu_touch
        except NoSuchElementException:
            print("원격 협업 > 알림 메뉴를 찾을 수 없습니다.")
            return False
            
    # 원격 협업 > 알림 리스트 확인하기
    def alarm_list_displayed(self):
        try:
            alarm_list = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.alarm_list)))
            if alarm_list.is_displayed():
                print("원격 협업 > 알림 리스트가 존재합니다.")
            else:
                None
            return alarm_list.is_displayed
        except NoSuchElementException:
            print("원격 협업 > 알림 리스트를 찾을 수 없습니다.")
        
    # 원격 협업 > 알림 리스트에서 알림 해제 버튼 확인하기
    def alarm_list_release_displayed(self):
        try:
            release_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.alarm_release)))
            if release_button.is_displayed():
                print("원격 협업 > 알림 리스트에서 [알림 해제] 버튼이 존재합니다.")
            else:
                None
            return release_button.is_displayed
        except NoSuchElementException:
            print("원격 협업 > 알림 리스트에서 [알림 해제] 버튼을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 알림 리스트에서 [알림 해제] 버튼 터치하기
    def touch_alarm_release_button(self):
        try:
            alarm_release_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.alarm_release)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(alarm_release_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("원격 협업 > 알림 리스트에서  [알림 해제] 버튼을 터치했습니다.")
            return alarm_release_touch
        except NoSuchElementException:
            print("원격 협업 > 알림 리스트에서 [알림 해제] 버튼을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 > 알림 리스트에서 [알림 수신] 버튼 확인하기
    def alarm_list_receive_displayed(self):
        try:
            receive_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.alarm_receive)))
            if receive_button.is_displayed():
                print("원격 협업 > 알림 리스트에서 [알림 수신] 버튼이 존재합니다.")
            else:
                None
            return receive_button.is_displayed
        except NoSuchElementException:
            print("원격 협업 > 알림 리스트에서 [알림 수신] 버튼을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 > 알림 리스트에서 [알림 수신] 버튼 터치하기
    def touch_alarm_receive_button(self):
        try:
            alarm_receive_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.alarm_receive)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(alarm_receive_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("원격 협업 > 알림 리스트에서 [알림 수신] 버튼을 터치했습니다.")
            return alarm_receive_touch
        except NoSuchElementException:
            print("원격 협업 > 알림 리스트에서 [알림 수신] 버튼을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 > 알림 메뉴에서 [이전] 버튼 확인하기
    def alarm_backbtn_displayed(self):
        try:
            alarm_back_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.alarm_backbutton)))
            if alarm_back_button.is_displayed():
                print("원격 협업 > 알림 메뉴에서 [이전] 버튼이 존재합니다.")
            else:
                None
            return alarm_back_button.is_displayed
        except NoSuchElementException:
            print("원격 협업 > 알림 리스트에서 [이전] 버튼을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 > 알림 메뉴에서 [이전] 버튼 터치하기
    def touch_alarm_back_button(self):
        try:
            touch_alarm_back = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.alarm_backbutton)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(touch_alarm_back)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("원격 협업 > 알림 메뉴에서 [이전] 버튼을 터치했습니다.")
            return touch_alarm_back
        except NoSuchElementException:
            print("원격 협업 > 알림 메뉴에서 [이전] 버튼을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 > [원격 협업 생성] 메뉴 확인하기
    def remote_collaborate_button_displayed(self):
        try:
            collaborate_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_create_menu)))
            if collaborate_btn.is_displayed():
                print("원격 협업 > [원격 협업 생성] 메뉴가 존재합니다.")
            else:
                None
            return collaborate_btn.is_displayed
        except NoSuchElementException:
            print("원격 협업 > [원격 협업 생성] 메뉴를 찾을 수 없습니다.")
            return False
        
    # 원격 협업 > [원격 협업 생성] 메뉴 터치하기
    def touch_remote_collaborate_button(self):
        try:
            touch_collaborate_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.collaborate_create_menu)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(touch_collaborate_btn)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("원격 협업 > [원격 협업 생성] 메뉴를 터치했습니다.")
            return touch_collaborate_btn
        except NoSuchElementException:
            print("원격 협업 > [원격 협업 생성] 메뉴를 찾을 수 없습니다.")
            return False
        
    # 원격 협업 생성 메뉴 > 원격 협업 생성 화면 확인
    def remote_collaborate_create_displayed(self):
        try:
            create_screen = WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element((self.remote_collaborate_screen), '원격 협업 생성'))
            if create_screen:
                print("원격 협업 생성 메뉴 > [원격 협업 생성] 화면이 존재합니다.")
            else:
                None
            return create_screen
        except NoSuchElementException:
            print("원격 협업 생성 > [원격 협업 생성] 화면을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 생성 메뉴 > 원격 협업 생성 화면에서 [이전] 버튼 확인
    def create_back_button_displayed(self):
        try:
            create_back_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.create_backbutton)))
            if create_back_button.is_displayed():
                print("원격 협업 생성 메뉴 > 원격 협업 생성 화면에 [이전] 버튼이 존재합니다.")
            else:
                None
            return create_back_button.is_displayed
        except NoSuchElementException:
            print("원격 협업 생성 메뉴 > 원격 협업 생성 화면에서 [이전] 버튼을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 생성 메뉴 > 원격 협업 생성 화면에서 [이전] 버튼 터치하기
    def touch_create_back_button(self):
        try:
            touch_create_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.create_backbutton)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(touch_create_btn )
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("원격 협업 생성 메뉴 > 원격 협업 생성 화면에서 [이전] 버튼을 터치했습니다.")
            return touch_create_btn
        except NoSuchElementException:
            print("원격 협업 생성 메뉴 > 원격 협업 생성 화면에서 [이전] 버튼을 찾을 수 없습니다.")
            return False
            
    # 원격 협업 > [오픈룸 생성] 메뉴 확인하기
    def openroom_create_button_displayed(self):
        try:
            openroom_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.openroom_btn)))
            if openroom_btn.is_displayed():
                print("원격 협업 > [오픈룸 생성] 메뉴가 존재합니다.")
            else:
                None
            return openroom_btn.is_displayed
        except NoSuchElementException:
            print("원격 협업 > [오픈룸 생성] 메뉴를 찾을 수 없습니다.")
            return False
        
    # 원격 협업 > [오픈룸 생성] 메뉴 터치하기
    def touch_open_room_button(self):
        try:
            touch_openroom_btn = WebDriverWait(self.driver,5).until(
                EC.element_to_be_clickable((self.openroom_btn)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(touch_openroom_btn)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("원격 협업 > [오픈룸 생성] 메뉴를 터치했습니다.")
            return touch_openroom_btn
        except NoSuchElementException:
            print("원격 협업 > [오픈룸 생성] 메뉴를 찾을 수 없습니다.")
            return False
        
    # 원격 협업 > 오픈룸 생성 메뉴 > 오픈룸 생성 화면 확인하기
    def openroom_create_screen_displayed(self):
        try:
            openroom_screen = WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element((self.openroom_create_screen), '오픈룸 생성'))
            if openroom_screen:
                print("오픈룸 생성 메뉴 > [오픈룸 생성] 화면이 존재합니다.")
            else:
                None
            return openroom_screen
        except NoSuchElementException:
            print("오픈룸 생성 메뉴 > [오픈룸 생성] 화면을 찾을 수 없습니다.")
            return False
        
    # 오픈룸 생성 메뉴 > 오픈룸 생성 화면에서 [이전] 버튼 확인하기
    def openroom_back_button_displayed(self):
        try:
            openroom_back_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.openroom_backbutton)))
            if openroom_back_button.is_displayed():
                print("오픈룸 생성 메뉴 > 오픈룸 생성 화면에 [이전] 버튼이 존재합니다.")
            else:
                None
            return openroom_back_button.is_displayed
        except NoSuchElementException:
            print("오픈룸 생성 > 오픈룸 생성 화면에서 [이전] 버튼을 찾을 수 없습니다.")
            return False
        
    # 오픈룸 생성 메뉴 > 오픈룸 생성 화면에서 [이전] 버튼 터치하기
    def touch_openroom_back_button(self):
        try:
            touch_openroom_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.openroom_backbutton)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(touch_openroom_btn)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("오픈룸 생성 > 오픈룸 생성 화면에서 [이전] 버튼을 터치했습니다.")
            return touch_openroom_btn
        except NoSuchElementException:
            print("오픈룸 생성 > 오픈룸 생성 화면에서 [이전] 버튼을 찾을 수 없습니다.")
            return False
        
    # Home 메뉴 > [예약 목록] 메뉴 확인하기
    def home_menu_reservation_displayed(self):
        try:
            reservation_menu = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.reservation)))
            if reservation_menu.is_displayed():
                print("Home 메뉴 > [예약 목록] 메뉴가 존재합니다.")
            else:
                None
            return reservation_menu.is_displayed
        except NoSuchElementException:
            print("Home 메뉴 > [예약 목록] 메뉴를 찾을 수 없습니다.")
            return False
        
    # Home 메뉴 > [예약 목록] 메뉴 터치하기
    def touch_home_reservation_menu(self):
        try:
            touch_reservation = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.reservation)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(touch_reservation)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("Home 메뉴 > [예약 목록] 메뉴를 터치했습니다.")
            return touch_reservation
        except NoSuchElementException:
            print("Home 메뉴 > [예약 목록] 메뉴를 터치하지 못했습니다.")
            return False
        
    # Home 메뉴 > [예약 목록] 메인 화면 확인하기
    def reservation_menu_displayed(self):
        try:
            main_recent = WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element((self.reservation_list), '예약 목록'))
            if main_recent:
                print("[예약 목록] 메인 화면이 존재합니다.")
            else:
                None
            return main_recent
        except NoSuchElementException:
            print("[예약 목록] 메인 화면을 찾을 수 없습니다.")
        
    # Home 메뉴 > [예약 목록] 메뉴 > 예약 목록 [찾기] 메뉴 확인하기
    def reservation_serch_menu_displayed(self):
        try:
            reservation_serch = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.reservation_serch_menu)))
            if reservation_serch.is_displayed():
                print("[예약 목록] 메뉴 > 예약 목록 [찾기] 메뉴가 존재합니다.")
            else:
                None
            return reservation_serch.is_displayed
        except NoSuchElementException:
            print("[예약 목록] 메뉴 > 예약 목록 [찾기] 메뉴를 찾을 수 없습니다.")
            return False
        
    # Home 메뉴 > [예약 목록] 메뉴 > 예약 목록 [찾기] 메뉴를 터치하기
    def touch_reservation_serch_menu(self):
        try:
            touch_reservation_serch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.reservation_serch_menu)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(touch_reservation_serch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("[예약 목록] 메뉴 > 예약 목록 [찾기] 메뉴를 터치했습니다.")
            return touch_reservation_serch
        except NoSuchElementException:
            print("[예약 목록] 메뉴 > 예약 목록 [찾기] 메뉴를 터치하지 못했습니다.")
            return False
        
    # Home 메뉴 > [예약 목록] 리스트를 새로고침하기
    def recservation_menu_re_flash(self):
        try:
            recent_re_flash = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.reservation_list)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(535, 825)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(532, 1453)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("[예약 목록] 정보가 갱신되었습니다.")
            return recent_re_flash
        except NoSuchElementException:
            print("[예약 목록] 리스트에서 새로고침을 하지 못했습니다.")
            return False
        
    # Home 메뉴 > [최근 기록] 메뉴 확인하기
    def home_menu_recentmenu_displayed(self):
        try:
            recent_menu = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.recent_records)))
            if recent_menu.is_displayed():
                print("Home 메뉴 > [최근 기록] 메뉴가 존재합니다.")
            else:
                None
            return recent_menu.is_displayed
        except NoSuchElementException:
            print("Home 메뉴 > [최근 기록] 메뉴를 찾을 수 없습니다.")
            return False
        
    # Home 메뉴 > [최근 기록] 메뉴 터치하기
    def touch_home_recent_menu(self):
        try:
            touch_recent = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.recent_records)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(touch_recent)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("Home 메뉴 > [최근 기록] 메뉴를 터치했습니다.")
            return touch_recent
        except NoSuchElementException:
            print("Home 메뉴 > [최근 기록] 메뉴를 터치하지 못했습니다.")
            return False
        
    # Home 메뉴 > [최근 기록] 메인 화면 확인하기
    def recent_menu_displayed(self):
        try:
            main_recent = WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element((self.recent_records_list), '최근 기록'))
            if main_recent:
                print("[최근 기록] 메인 화면이 존재합니다.")
            else:
                None
            return main_recent
        except NoSuchElementException:
            print("[최근 기록] 메인 화면을 찾을 수 없습니다.")
            
    # Home 메뉴 > [최근 기록] 리스트를 새로고침하기
    def recent_menu_re_flash(self):
        try:
            recent_re_flash = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.recent_records_list)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(535, 825)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(532, 1453)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("[최근 기록] 정보가 갱신되었습니다.")
            return recent_re_flash
        except NoSuchElementException:
            print("[최근 기록] 리스트에서 새로고침을 하지 못했습니다.")
            return False
        
    # Home 메뉴 > [최근 기록] 메뉴 > 최근 기록 [찾기] 메뉴 확인하기
    def recent_serch_menu_displayed(self):
        try:
            recent_serch = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.recent_serch_menu)))
            if recent_serch.is_displayed():
                print("[최근 기록] 메뉴 > 최근 기록 [찾기] 메뉴가 존재합니다.")
            else:
                None
            return recent_serch.is_displayed
        except NoSuchElementException:
            print("[최근 기록] 메뉴 > 최근 기록 [찾기] 메뉴를 찾을 수 없습니다.")
            return False
        
    # Home 메뉴 > [최근 기록] 메뉴 > 최근 기록 [찾기] 메뉴를 터치하기
    def touch_recent_serch_menu(self):
        try:
            touch_recent_serch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.recent_serch_menu)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(touch_recent_serch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("[최근 기록] 메뉴 > 최근 기록 [찾기] 메뉴를 터치했습니다.")
            return touch_recent_serch
        except NoSuchElementException:
            print("[최근 기록] 메뉴 > 최근 기록 [찾기] 메뉴를 터치하지 못했습니다.")
            return False
        
    # Home 메뉴 > [최근 기록] 메뉴 > 최근 기록 메인 화면 > 최근 기록 [검색 입력 필드] 확인하기
    def recent_serch_inputfield_displayed(self):
        try:
            recent_inputfield = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.recent_serch_inputfield)))
            if recent_inputfield.is_displayed():
                print("[최근 기록] 메뉴 > 최근 기록 검색 입력 필드가 존재합니다.")
            else:
                None
            return recent_inputfield.is_displayed
        except NoSuchElementException:
            print("[최근 기록] 메뉴 > 최근 기록 검색 입력 필드를 찾을 수 없습니다.")
            
    # Home 메뉴 > [최근 기록] 메뉴 > 최근 기록 메인 화면 > 최근 기록 검색 입력 필드에서 [취소] 메뉴 확인하기
    def recent_inputfield_cancel_displayed(self):
        try:
            recent_inputfield_cancel = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.recent_cancel_button)))
            if recent_inputfield_cancel.is_displayed():
                print("[최근 기록] 메뉴 > 최근 기록 검색 입력 필드에 [취소] 메뉴가 존재합니다.")
            else:
                None
            return recent_inputfield_cancel.is_displayed
        except NoSuchElementException:
            print("[최근 기록] 메뉴 > 최근 기록 검색 입력 필드에서 [취소] 메뉴를 찾을 수 없습니다.")
            return False
        
    # Home 메뉴 > [최근 기록] 메뉴 > 최근 기록 메인 화면 > 최근 기록 검색 입력 필드에서 [취소] 메뉴 터치하기
    def touch_recent_inputfield_cancel(self):
        try:
            touch_recent_cancel = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.recent_cancel_button)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(touch_recent_cancel)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("[최근 기록] 메뉴 > 최근 기록 검색 입력 필드에서 [취소] 메뉴를 터치했습니다.")
            return touch_recent_cancel
        except NoSuchElementException:
            print("[최근 기록] 메뉴 > 최근 기록 검색 입력 필드에서 [취소] 메뉴를 터치하지 못했습니다.")
            return False
        
    # Home 메뉴 > [멤버] 메뉴 확인하기
    def home_menu_membermenu_displayed(self):
        try:
            member_menu = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.member_menu)))
            if member_menu.is_displayed():
                print("Home 메뉴 > [멤버] 메뉴가 존재합니다.")
            else:
                None
            return member_menu.is_displayed
        except NoSuchElementException:
            print("Home 메뉴 > [멤버] 메뉴를 찾을 수 없습니다.")
        
    # Home 메뉴 > [멤버] 메뉴 터치하기
    def touch_member_menu(self):
        try:
            touch_member = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.member_menu)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(touch_member)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("Home 메뉴 > [멤버] 메뉴를 터치했습니다.")
            return touch_member
        except NoSuchElementException:
            print("Home 메뉴 > [멤버] 메뉴를 터치하지 못했습니다.")
            return False
        
    # [멤버] 메인 화면 확인하기
    def member_menu_displayed(self):
        try:
            main_member = WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element((self.member_menu_list), '멤버'))
            if main_member:
                print("[멤버] 메인 화면이 존재합니다.")
            else:
                None
            return main_member
        except NoSuchElementException:
            print("[멤버] 메인 화면을 찾을 수 없습니다.")
            return False
        
    # [멤버] 리스트를 새로고침하기
    def member_menu_re_flash(self):
        try:
            recent_re_flash = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.member_menu_list)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(535, 825)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(532, 1453)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("[멤버] 정보가 갱신되었습니다.")
            return recent_re_flash
        except NoSuchElementException:
            print("[멤버] 리스트에서 새로고침을 하지 못했습니다.")
            return False
        
    # [멤버] 메뉴 > 멤버 메인 화면 > 멤버 [찾기] 메뉴 확인하기
    def member_serch_menu_displayed(self):
        try:
            member_serch = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.member_serch_menu)))
            if member_serch.is_displayed():
                print("[멤버] 메뉴 > 멤버 메인 화면에서 멤버 [찾기] 메뉴가 존재합니다.")
            else:
                None
            return member_serch.is_displayed
        except NoSuchElementException:
            print("[멤버] 메뉴 > 멤버 메인 화면에서 멤버 [찾기] 메뉴를 찾을 수 없습니다.")
            return False
        
    # [멤버] 메뉴 > 멤버 메인 화면 > 멤버 [찾기] 메뉴 터치하기
    def touch_member_serch_button(self):
        try:
            touch_member_serch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.member_serch_menu)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(touch_member_serch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("Home 메뉴 > [멤버] 메뉴를 터치했습니다.")
            return touch_member_serch
        except NoSuchElementException:
            print("Home 메뉴 > [멤버] 메뉴를 터치하지 못했습니다.")
            return False
            
    # [멤버] 메뉴 > 멤버 메인 화면 > 멤버 [찾기] 메뉴 > 멤버 [검색 입력 필드] 확인하기
    def menber_serch_inputfield_displayed(self):
        try:
            member_serch_inputfield = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.member_serch_inputfield)))
            if member_serch_inputfield.is_displayed():
                print("[멤버] 메뉴 > 멤버 [찾기] 메뉴에서 멤버 [검색 입력 필드]가 존재합니다.")
            else:
                None
            return member_serch_inputfield.is_displayed
        except NoSuchElementException:
            print("[멤버] 메뉴 > 멤버 [찾기] 메뉴에서 멤버 [검색 입력 필드]를 찾을 수 없습니다.")
            return False
            
    # [멤버] 메뉴 > 멤버 메인 화면 > 멤버 [찾기] 메뉴 > 멤버 [검색 입력 필드] > [취소] 메뉴 확인하기
    def member_serch_inputfield_cancel_displayed(self):
        try:
            member_serch_cancel = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.member_cancel_button)))
            if member_serch_cancel.is_displayed():
                print("[멤버] 메뉴 > 멤버 [검색 입력 필드]에서 [취소] 버튼이 존재합니다.")
            else:
                None
            return member_serch_cancel.is_displayed
        except NoSuchElementException:
            print("[멤버] 메뉴 > 멤버 [검색 입력 필드]에서 [취소] 버튼을 찾을 수 없습니다.")
            return False
        
    # [멤버] 메뉴 > 멤버 메인 화면 > 멤버 [찾기] 메뉴 > 멤버 [검색 입력 필드] > [취소] 메뉴 터치하기
    def touch_member_inputfield_cancel(self):
        try:
            touch_member_cancel = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.member_cancel_button)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(touch_member_cancel)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("[멤버] 메뉴 > 멤버 검색 입력 필드에서 [취소]를 터치했습니다.")
            return touch_member_cancel
        except NoSuchElementException:
            print("[멤버] 메뉴 > 멤버 검색 입력 필드에서 [취소]를 터치하지 못했습니다.")
            return False
        
    # Home 메뉴 > [환경 설정] 메뉴 확인하기
    def home_menu_preferencesmenu_displayed(self):
        try:
            preferences_menu = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.preferences_menu)))
            if preferences_menu.is_displayed():
                print("Home 메뉴 > [환경 설정] 메뉴가 존재합니다.")
            else:
                None
            return preferences_menu.is_displayed
        except NoSuchElementException:
            print("Home 메뉴 > [환경 설정] 메뉴를 찾을 수 없습니다.")
            
    # Home 메뉴 > [환경 설정] 메뉴 터치하기
    def touch_preferences_menu(self):
        try:
            touch_preferences = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.preferences_menu)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(touch_preferences)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("Home 메뉴 > [환경 설정] 메뉴를 터치했습니다.")
            return touch_preferences
        except NoSuchElementException:
            print("Home 메뉴 > [환경 설정] 메뉴를 터치하지 못했습니다.")
            return False
        
    # [환경 설정] 메인 화면 확인하기
    def preferences_menu_displayed(self):
        try:
            main_preferences = WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element((self.preferences_main_scree), '환경 설정'))
            if main_preferences:
                print("[환경 설정] 메인 화면이 존재합니다.")
            else:
                None
            return main_preferences
        except NoSuchElementException:
            print("[환경 설정] 메인 화면을 찾을 수 없습니다.")
            return False