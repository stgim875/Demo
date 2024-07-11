from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Remote Web 로그인 화면
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # 로그인 센터 화면
        self.login_center = (By.XPATH, "//div[@class='home-section']")
        
        # 아이디 입력 필드
        self.user_id_locator = (By.XPATH, "//div[@class='email-input el-input el-input--suffix']/input[@type='text' and @autocomplete='off' and @name='email']")
        
        # 패스워드 입력 필드
        self.user_pwd_locator = (By.XPATH, "//div[@class='password-input el-input el-input--suffix']/input[@type='password' and @autocomplete='off' and @name='password']")
        
        # 비활성화되어 있는 로그인 버튼
        self.disabled_login_button = (By.XPATH, "//div[@class='el-col el-col-24']/button[@disabled='disabled' and @type='button' and @class='el-button next-btn block-btn el-button--info is-disabled']")
        
        # 활성환된 로그인 버튼
        self.enabled_login_button = (
            By.XPATH, "//div[@class='el-col el-col-24']/button[@type='button' and @class='el-button next-btn block-btn el-button--info']")
        
        # Remote layout 화면
        self.remote_layout = (By.XPATH, "//section[@class='remote-layout']")
        
        # 중복 로그인 모달창
        self.duplicate_login_alert = (
            By.XPATH, "//div[@class='swal2-content']/div[@id='swal2-content' and @class='swal2-html-container' and @style='display: block;']")
        
        # 중복 로그인 모달창 > 원격 종료 버튼
        self.swal2_actions = (
            By.XPATH, "//div[@class='swal2-actions']/button[@class='swal2-confirm swal2-styled' and contains(text(), '원격종료')]")
        
    # Remote 로그인센터 화면 존재 확인하기
    def go_to_logincenter_displayed(self):
        try:
            login_center = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.login_center)))
            login_center.is_displayed()
            print("로그인 센터 화면이 존재합니다.")
            return True
        except TimeoutException:
            print("로그인 센터 화면이 존재하지 않습니다.")
            return False
        
    # 아이디 입력 필드 존재 확인하기
    def id_input_field_displayed(self):
        try:
            id_input_field = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.user_id_locator)))
            id_input_field.is_displayed()
            print("아이디 입력 필드가 존재합니다.")
            return True
        except TimeoutException:
            print("아이디 입력 필드가 존재하지 않습니다.")
            return False
        
    # 패스워드 입력 필드 존재 확인하기
    def pw_input_field_displayed(self):
        try:
            pw_input_field = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.user_pwd_locator)))
            pw_input_field.is_displayed()
            print("패스워드 입력 필드가 존재합니다.")
            return True
        except TimeoutException:
            print("패스워드 입력 필드가 존재하지 않습니다.")
            return False
        
    # 로그인 버튼 존재 확인하기
    def login_button_displayed(self):
        try:
            login_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.disabled_login_button)))
            login_button.is_displayed()
            print("로그인 버튼이 존재합니다.")
            return True
        except TimeoutException:
            print("로그인 버튼이 존재하지 않습니다.")
            return False
        
    # 아이디 입력하기
    def enter_username(self, username):
        try:
            user_id = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.user_id_locator))
            user_id.send_keys(username)
            print(f"아이디 '{username}'이 입력이 되었습니다.")
            return True
        except TimeoutException:
            print(f"아이디 '{username}'이 입력되지 않았습니다.")
            return False
        
    # 패스워드 입력하기
    def enter_password(self, password):
        try:
            user_pwd = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.user_pwd_locator))
            user_pwd.send_keys(password)
            print(f"패스워드 '{password}'가 입력되었습니다.")
            return True
        except TimeoutException:
            print(f"패스워드'{password}'가 입력되지 않았습니다.")
            return None
        
    # 로그인 버튼 클릭하기
    def click_login_button(self):
        try:
            login_button_click = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.enabled_login_button)))
            actions = ActionChains(self.driver)
            actions.move_to_element(login_button_click)
            actions.click(login_button_click)
            actions.perform()
            print("로그인 버튼을 클릭했습니다.")
            return True
        except TimeoutException:
            print("로그인 버튼을 클릭하지 못했습니다.")
            return None
        
    # # 로그인 결과 확인하기
    def remote_layout_result(self):
        try:
            remote_web_layout = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.remote_layout)))
            remote_web_layout.is_displayed()
            print("Remote web 화면으로 이동했습니다.")
            return True
        except TimeoutException:
            print("Remote web 화면으로 이동하지 못했습니다.")
            return False
        
    # 중복 로그인에 대한 예외 처리하기
    # 로그인 > 동일한 계정이 입력 되었을 경우 > 중복 로그인 모달창 출력 여부 확인하기
    def duplicate_login_displayed(self):
        try:
            duplicate_login = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.duplicate_login_alert)))
            duplicate_login.is_displayed()
            print("다른 장치에서 이미 로그인 중입니다. 계속 하시려면 상대방의 접속을 종료시켜주세요.")
            return True
        except TimeoutException:
            pass
        
    # 원격 종료 버튼 클릭하기
    def click_swal2_actions(self):
        try:
            swal2_actions_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.swal2_actions))
            actions = ActionChains(self.driver)
            actions.move_to_element(swal2_actions_btn)
            actions.click(swal2_actions_btn)
            actions.perform()
            print("원격 종료 버튼을 클릭했습니다.")
            return True
        except TimeoutException:
            pass