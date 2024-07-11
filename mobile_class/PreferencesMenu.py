from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Remote Mobile(AOS) 환경 설정 메뉴
class RemotePreferences:
    def __init__(self, driver):
        self.driver = driver
        
        # (환경 설정) 메뉴 
        self.preferences_menu = (
            AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/home_iv_settings")
        
        # (환경 설정) 메뉴 > 환경 설정 메인 화면
        self.preferences_main_scree = (
            AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/home_tv_title' and @text='환경 설정']")
        
        # (환경 설정) 메뉴 > 환경 설정 메인 화면 > 환경 설정 메인 리스트
        self.preferences_list_screen = (
            AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/fragment_container']")
        
        # (환경 설정) 메뉴 > 환경 설정 메인 화면 > 로그아웃
        self.logout = (
            AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/settings_logout_info' and @text='로그아웃']")
        
        # (환경 설정) 메뉴 > 환경 설정 메인 화면 > 로그아웃 (>) 버튼
        self.logout_button = (
            AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='com.virnect.remote.mobile2_onpremise_common:id/settings_iv_logout_arrow']")
        
    # (환경 설정) 메뉴 확인하기
    def preferences_displayed(self):
        try:
            preferences_menu = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.preferences_menu)))
            preferences_menu.is_displayed()
            print("Home 메뉴 > (환경 설정) 메뉴가 존재합니다.")
            return True
        except TimeoutException:
            print("Home 메뉴 > (환경 설정) 메뉴가 존재하지 않습니다.")
            return False
            
    # (환경 설정) 메뉴 터치하기
    def touch_preferences(self):
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
            print("Home 메뉴 > (환경 설정) 메뉴를 터치했습니다.")
            return True
        except TimeoutException:
            print("Home 메뉴 > (환경 설정) 메뉴를 터치못했습니다.")
            return False
        
    # (환경 설정) 메인 화면 확인하기
    def preferences_main_displayed(self):
        try:
            main_preferences = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.preferences_main_scree)))
            main_preferences.is_displayed()
            print("(환경 설정) 메인 화면이 존재합니다.")
            return True
        except TimeoutException:
            print("(환경 설정) 메인 화면을 찾을 수 없습니다.")
            return False
        
    # (환경 설정) 메뉴 >  [로그아웃] 메뉴 확인하기
    def preferences_logout_displayed(self):
        try:
            logout_menu = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.logout)))
            logout_menu.is_displayed()
            print("(환경 설정) 메뉴 >  [로그아웃] 메뉴가 존재합니다.")
            return True
        except TimeoutException:
            print("(환경 설정) 메뉴 > [로그아웃] 메뉴가 존재하지 않습니다.")
            return False
        
    # (환경 설정) 메뉴 > [로그아웃] 메뉴 터치하기
    def touch_preferences_logout(self):
        try:
            touch_logout = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.logout_button)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(touch_logout)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("(환경 설정) 메뉴 > [로그아웃] 메뉴를 터치했습니다.")
            return True
        except TimeoutException:
            print("(환경 설정) 메뉴 > [로그아웃] 메뉴를 터치못했습니다.")
            return False