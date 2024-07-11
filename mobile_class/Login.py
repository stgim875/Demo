from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Remote Mobile(AOS) 로그인 화면
class RemoteLogin:
    def __init__(self, driver):
        self.driver = driver
        
        # 로그인 화면
        self.login_screen = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/fragment_container")
        
        # Remote 로그인 > 아이디 입력 필드
        self.login_field = (AppiumBy.CLASS_NAME, "android.widget.AutoCompleteTextView")
        
        # Remote 로그인 화면 > 비밀번호 필드
        self.paaword_field = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/login_input_et_pwd")
        
        # Remote 로그인 화면 > 로그인 버튼
        self.login_button = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/login_btn_login")
        
        # 워크스페이스 모달창
        self.workspace_modal = (
            AppiumBy.XPATH, "//android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup")
        
        # 워크스페이스 모달창 > Myworkspace
        self.my_workspace = (AppiumBy.ID, "com.virnect.remote.mobile2_onpremise_common:id/rc_item_tv_title")
        
    # Remote 로그인 화면 확인
    def login_screen_displayed(self):
        try:
            login_screen = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.login_screen)))
            login_screen.is_displayed()
            print("Remote 로그인 화면이 존재합니다.")
            return True
        except TimeoutException:
            print("Remote 로그인 화면이 존재하지 않습니다.")
            return False
        
    # Remote 로그인 화면에서 아이디 입력 필드 확인
    def id_inputfield_displayed(self):
        try:
            id_inputfield = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.login_field)))
            id_inputfield.is_displayed()
            print("Remote 로그인 화면에서 아이디 입력 필드가 존재합니다.")
            return True
        except TimeoutException:
            print("Remote 로그인 화면에서 아이디 입력 필드가 존재하지 않습니다.")
            return False
            
    # Remote 로그인 화면에서 아이디 입력하기
    def login_id_input(self, userid):
        try:
            id_input = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.login_field)))
            id_input.send_keys(userid)
            print(f"아이디 {userid}가 입력되었습니다.")
            return True
        except TimeoutException:
            print(f"아이디 {userid}가 입력되지 않았습니다.")
            return False
        
    # Remote 로그인 화면에서 패스워드 입력 필드 확인
    def pw_inputfield_displayed(self):
        try:
            password_inputfield = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.paaword_field)))
            password_inputfield.is_displayed()
            print("Remote 로그인 화면에서 패스워드 입력 필드가 존재합니다.")
            return True
        except TimeoutException:
            print("Remote 로그인 화면에서 패스워드 입력 필드가 존재하지 않습니다.")
            return False
        
    # Remote 로그인 화면에서 패스워드 입력하기
    def login_pw_input(self, userpw):
        try:
            pw_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.paaword_field)))
            pw_input.send_keys(userpw)
            print(f"패스워드 {userpw}가 입력되었습니다.")
            return True
        except TimeoutException:
            print(f"패스워드 {userpw}가 입력되지 않았습니다.")
            return False
        
    # Remote  로그인 화면에서 로그인 버튼 확인
    def loging_button_displayed(self):
        try:
            login_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.login_button)))
            login_button.is_displayed()
            print("Remote 로그인 화면에서 [로그인] 버튼이 존재합니다.")
            return True
        except TimeoutException:
            print("Remote 로그인 화면에서 [로그인] 버튼이 존재하지 않습니다.")
            return False
        
    # Remote 로그인 화면에서 로그인 버튼 터치하기
    def touch_loging_button(self):
        try:
            login_button_touch = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.login_button)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(login_button_touch)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("Remote 로그인 화면에서 [로그인] 버튼을 터치했습니다.")
            return True
        except TimeoutException:
            print("Remote 로그인 화면에서 [로그인] 버튼 터치못했습니다.")
            return False
            
    # 워크스페이스 선택 모달창 확인
    def workspace_modal_displayed(self):
        try:
            workspace_modal = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.workspace_modal)))
            workspace_modal.is_displayed()
            print("워크스페이스 모달창이 존재합니다.")
            return True
        except TimeoutException:
            print("워크스페이스 모달창이 존재하지 않습니다.")
            return False
    
    # 워크스페이스 선택 모달창에서 My Workspace 선택하기
    def touch_my_workspace(self):
        try:
            my_workspace = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.my_workspace)))
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to(my_workspace)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            print("워크스페이스 모달창에서 [My Workspace]를 터치했습니다.")
            return True
        except TimeoutException:
            print("워크스페이스 모달창에서 [My Workspace]를 터치못했습니다.")
            return False