from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# # Remote Web PrivacyPage 화면
class PrivacyPage:
    def __init__(self, driver):
        self.driver = driver
        
        # Remote Web 주소
        self.remote_url = ''
        
        # 비공개 페이지 > [고급] 버튼
        self.advanced_button = (By.XPATH, "//body[@class='ssl']/div[@class='interstitial-wrapper']/div[@class='nav-wrapper']/button[@id='details-button' and @class='secondary-button small-link' and contains(text(), '고급')]")
        
        # 비공개 페이지 > [고급] 버튼 > (안전하지 않음) 링크
        self.unsafe_link = (By.XPATH, "//a[@id='proceed-link' and @class='small-link']")
        
    # 개인 정보 보호 화면으로 이동하기
    def go_to_privacy_page(self):
        self.driver.get(self.remote_url)
        
    # 비공개 페이지에서 고급 버튼 존재 확인하기
    def advanced_button_displayed(self):
        try:
            advanced_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.advanced_button)))
            advanced_button.is_displayed()
            print("고급 버튼이 존재합니다.")
            return True
        except TimeoutException:
            print("고급 버튼이 존재하지 않습니다.")
            return False
        
    # 비공개 페이지에서 고급 버튼 클릭하기
    def click_advanced_button(self):
        try:
            advanced_button_click = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.advanced_button)))
            actions = ActionChains(self.driver)
            actions.move_to_element(advanced_button_click)
            actions.click(advanced_button_click)
            actions.perform()
            print("비공개 페이지에서 [고급] 버튼을 클릭했습니다.")
            return True
        except TimeoutException:
            print("비공개 페이지에서 [고급] 버튼을 클릭하지 못했습니다.")
            return False
    
    # 비공개 페이지에서 (안전하지 않음) 링크 존재 확인하기
    def unsafe_link_displayed(self):
        try:
            unsafe_link = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.unsafe_link)))
            unsafe_link.is_displayed()
            print("비공개 페이지에 (안전하지 않음) 링크가 존재합니다.")
            return True
        except TimeoutException:
            print("비공개 페이지에 (안전하지 않음) 링크가 존재하지 않습니다.")
            return False
        
    # 비공개 페이지에서 (안전하지 않음) 링크 클릭하기
    def click_unsafe_link(self):
        try:
            unsafe_link_button_click = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.unsafe_link)))
            actions = ActionChains(self.driver)
            actions.move_to_element(unsafe_link_button_click)
            actions.click(unsafe_link_button_click)
            actions.perform()
            print("비공개 페이지에서 (안전하지 않음) 링크를 클릭했습니다.")
            return True
        except TimeoutException:
            print("비공개 페이지에서 (안전하지 않음) 링크를 클릭하지 못했습니다.")
            return False