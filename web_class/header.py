from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import time

# Remote Web header 영역
class HeaderArea:
    def __init__(self, driver):
        self.driver = driver
        
        # 워크스페이스 메뉴
        self.work_space_menu = (By.XPATH, "//section[@class='remote-layout']/header[@class='header workspace-selected']/div[@class='header-workspace']/nav[@class='header-workspace-lnb']/span[@class='popover--wrapper']")
        
        # 워크스페이스 메뉴 클릭
        self.work_space_options = [
            {
                "xpath": "//section[@class='remote-layout']/header[@class='header workspace-selected']/div[@class='header-workspace']/nav[@class='header-workspace-lnb']/span[@class='popover--wrapper']/button[@class='header-workspace-selector']",
                "message": "워크스페이스 메뉴를 클릭했습니다.",
                "timeout": 5
                },
            {
                "xpath": "//section[@class='remote-layout']/header[@class='header workspace-selected']/div[@class='header-workspace']/nav[@class='header-workspace-lnb']/span[@class='popover--wrapper']/button[@class='header-workspace-selector selected']",
                "message": "워크스페이스 메뉴를 닫았습니다.",
                "timeout": 5
                }
            ]
        
        # 영상 on/off 메뉴
        self.displaye_on_off = (By.XPATH, "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/div[1][@class='tooltip']")
        
        # 영상 off > on 메뉴 클릭
        self.video_display_options = [
            {
                "xpath": "//ul[@class='header-workspace-tools']/div[1][@class='tooltip']/button[@class='toggle-button active toggle-header stream']",
                "message": "영상 메뉴를 [off] 하였습니다.",
                "timeout": 5
                },
            {
                "xpath": "//ul[@class='header-workspace-tools']/div[1][@class='tooltip']/button[@class='toggle-button toggle-header stream']",
                "message": "영상 메뉴를 [on] 하였습니다.",
                "timeout": 5
                }
            ]
        
        # 마이크 on/off 메뉴
        self.mic_menu = (By.XPATH, "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/div[2][@class='tooltip']")
        
        # 마이크 on > off 클릭
        self.mic_options = [
            {
                "xpath": "//ul[@class='header-workspace-tools']/div[2][@class='tooltip']/button[@class='toggle-button toggle-header mic']",
                "message": "마이크를 on 하였습니다.",
                "timeout": 5
                },
            {
                "xpath": "//ul[@class='header-workspace-tools']/div[2][@class='tooltip']/button[@class='toggle-button active toggle-header mic']",
                "message": "마이크를 off 하였습니다.",
                "timeout": 5
                }
            ]
        
        # 스피커 메뉴
        self.speaker_menu = (By.XPATH, "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/div[3][@class='tooltip']")
        
        # 스피커 off > on 메뉴 클릭
        self.speaker_options = [
            {
                "xpath": "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/div[3][@class='tooltip']/button[@class='toggle-button active toggle-header speaker']",
                "message": "스피커를 off 하였습니다.",
                "timeout": 5
                },
            {
                "xpath": "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/div[3][@class='tooltip']/button[@class='toggle-button toggle-header speaker']",
                "message": "스피커를 on 하였습니다.",
                "timeout": 5
                }
        ]
        
        # 알림 메뉴
        self.noti_menu = (By.XPATH, "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/span[1][@class='popover--wrapper']")
        
        # 알림 리스트 옵션 박스 메뉴
        self.list_option_box = (By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-notice']/div[@class='popover--body']/div/div[@class='popover-notice__body']/div[@class='popover-notice__empty']")
        
        # 알림 Push off > on > 알림 메뉴 
        self.noti_menu_options = [
            {
                "xpath": "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-notice']/div[@class='popover--body']/div/div[@class='popover-notice__header']/span[text()='알림']/following-sibling::div[@class='switcher']/div[@class='switcher-toggle toggle']",
                "message": "Push를 [off] 했습니다.",
                "timeout": 5
                },
            {
                "xpath": "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-notice']/div[@class='popover--body']/div/div[@class='popover-notice__header']/span[text()='알림']/following-sibling::div[@class='switcher']/div[@class='switcher-toggle']",
                "message": "Push를 [on] 하였습니다.",
                "timeout": 5
                }
            ]
        
        # 나의 프로필 메뉴
        self.profile_menu = (By.XPATH, "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/span[2][@class='popover--wrapper']")
        
        # 나의 프로필 메뉴 (클릭)
        self.my_profile = (By.XPATH, 
            "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/span[2][@class='popover--wrapper']/figure[@class='profile']/div[@class='profile--thumb']")
        
        # 나의 프로필 리스트 옵션 박스
        self.my_profile_list = (By.XPATH,
            "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-profile']/div[@class='popover--body']")
        
        # 나의 프로필 > 워크스테이션
        self.work_station_menu = (By.XPATH, 
            "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-profile']/div[@class='popover--body']/div/div[@class='popover-profile__linklist']/div[@class='popover-profile__link']/button[contains(text(), '워크스테이션')]")
        
        # 나의 프로필 > 대시보드 메뉴
        self.dash_board_menu = (By.XPATH, 
            "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-profile']/div[@class='popover--body']/div/div[@class='popover-profile__linklist']/div[@class='popover-profile__link']/button[contains(text(), '대시보드')]")
        
        # 나의 프로필 > 로컬 파일 메뉴
        self.local_file_menu = (By.XPATH, 
            "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-profile']/div[@class='popover--body']/div/div[@class='popover-profile__linklist']/div[@class='popover-profile__link']/button[contains(text(), '로컬 녹화 파일')]")
        
        # 나의 프로필 > 로그아웃 메뉴
        self.logout_menu = (By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-profile']/div[@class='popover--body']/div/div[@class='popover-profile__linklist']/div[@class='popover-profile__link']/button[contains(text(), '로그아웃')]")
        
    # 워크스페이스 메뉴 확인하기
    def work_space_displayed(self):
        try:
            work_space_menu = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.work_space_menu)))
            work_space_menu.is_displayed()
            print("워크스페이스 메뉴가 존재합니다.")
            return True
        except NoSuchElementException:
            print("워크스페이스 메뉴가 존재하지 않습니다.")
            return False
        
    # 워크스페이스 메뉴를 두번 클릭하기
    def click_workspace_menu(self):
        try:
            for workspace in self.work_space_options:
                work_space_btn = WebDriverWait(self.driver, float(str(workspace["timeout"]))).until(
                    EC.element_to_be_clickable((By.XPATH, str(workspace["xpath"]))))
                actions = ActionChains(self.driver)
                actions.move_to_element(work_space_btn)
                actions.click(work_space_btn)
                actions.perform()
                print(workspace["message"])
                time.sleep(3)
            return True
        except NoSuchElementException:
            print("워크스페이스 메뉴를 클릭하지 못했습니다.")
            return False
        
    # 영상 on/off 메뉴 확인하기
    def dis_on_off_displayed(self):
        try:
            display_on_off = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.displaye_on_off)))
            display_on_off.is_displayed()
            print("영상 on/off 메뉴가 존재합니다.")
            return True
        except NoSuchElementException:
            print("영상 on/off 메뉴가 존재하지 않습니다.")
            return False
        
    # 영상 on/off 메뉴를 두번 클릭하기
    def click_display_on_off(self):
        try:
            for video_display in self.video_display_options:
                display_on_off = WebDriverWait(self.driver, float(str(video_display["timeout"]))).until(
                    EC.element_to_be_clickable((By.XPATH, str(video_display["xpath"]))))
                actions = ActionChains(self.driver)
                actions.move_to_element(display_on_off)
                actions.click(display_on_off)
                actions.perform()
                print(video_display["message"])
                time.sleep(3)
            return True
        except NoSuchElementException:
            print("영상 on/off 메뉴를 찾을 수 없습니다.")
            return False
            
    # 마이크 on/off 메뉴 확인하기
    def mic_on_off_displayed(self):
        try:
            mic_on_off = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.mic_menu)))
            mic_on_off.is_displayed()
            print("마이크 on/off 메뉴가 존재합니다.")
            return True
        except NoSuchElementException:
            print("마이크 on/off 메뉴가 존재하지 않습니다.")
            return False
        
    # 마이크 on/off 메뉴를 두번 클릭하기
    def click_mic_on_off(self):
        try:
            for mic_menu in self.mic_options:
                mic_on_off = WebDriverWait(self.driver, float(str(mic_menu["timeout"]))).until(
                    EC.element_to_be_clickable((By.XPATH, str(mic_menu["xpath"]))))
                actions = ActionChains(self.driver)
                actions.move_to_element(mic_on_off)
                actions.click(mic_on_off)
                actions.perform()
                print(mic_menu["message"])
                time.sleep(3)
            return True
        except NoSuchElementException:
            print("마이크 on/off 메뉴를 클릭하지 못했습니다.")
            return False
        
    # 스피커 on/off 메뉴 확인하기
    def speaker_menu_displayed(self):
        try:
            speaker_menu = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.speaker_menu)))
            speaker_menu.is_displayed()
            print("스피커 on/off 메뉴가 존재합니다.")
            return True
        except NoSuchElementException:
            print("스피커 on/off 메뉴가 존재하지 않습니다.")
            return False
        
    # 스피커 on/off 메뉴를 두번 클릭하기
    def click_speaker_on_off_menu(self):
        try:
            for speaker_menu in self.speaker_options:
                speaker_on_off = WebDriverWait(self.driver, float(str(speaker_menu["timeout"]))).until(
                    EC.element_to_be_clickable((By.XPATH, str(speaker_menu["xpath"]))))
                actions = ActionChains(self.driver)
                actions.move_to_element(speaker_on_off)
                actions.click(speaker_on_off)
                actions.perform()
                print(speaker_menu["message"])
                time.sleep(3)
            return True
        except NoSuchElementException:
            print("스피커 on/off 메뉴를 클릭하지 못했습니다.")
            return False
            
    # 알림 메뉴 확인하기
    def notification_menu_displayed(self):
        try:
            noti_menu = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.noti_menu)))
            noti_menu.is_displayed()
            print("알림 메뉴가 존재합니다.")
            return True
        except NoSuchElementException:
            print("알림 메뉴가 존재하지 않습니다.")
            return False
            
    # 알림 메뉴를 한번 클릭하기
    def one_click_noti_menu(self):
        try:
            oneclick_noti = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.noti_menu)))
            actions = ActionChains(self.driver)
            actions.move_to_element(oneclick_noti)
            actions.click(oneclick_noti)
            actions.perform()
            print("알림 메뉴를 클릭했습니다.")
            time.sleep(3)
            return True
        except NoSuchElementException:
            print("알림 메뉴를 클릭하지 못했습니다.")
            return False
        
    # 알림 메뉴 옵션 박스 메뉴 출력 확인하기
    def noti_menu_optionbox(self):
        try:
            noti_optionbox = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.list_option_box)))
            noti_optionbox.is_displayed()
            print("알림 메뉴 옵션 박스 메뉴가 출력되었습니다..")
            return True
        except NoSuchElementException:
            print("알림 메뉴 옵션 박스 메뉴가 출력되지 않습니다.")
            return False
        
    # 알림 Push off > on > 버튼 두번 클릭하기
    def click_noti_push_on_off(self):
        try:
            for push_on_off in self.noti_menu_options:
                noti_menu_click = WebDriverWait(self.driver, float(str(push_on_off["timeout"]))).until(
                    EC.element_to_be_clickable((By.XPATH, str(push_on_off["xpath"]))))
                actions = ActionChains(self.driver)
                actions.move_to_element(noti_menu_click)
                actions.click(noti_menu_click)
                actions.perform()
                print(push_on_off["message"])
                time.sleep(3)
            return True
        except NoSuchElementException:
            print("알림 메뉴를 두번 클릭하지 못했습니다.")
            return False
        
    # 알림 메뉴를 한번 더 클릭하여 알림 메뉴 닫기
    def re_click_noti_menu(self):
        try:
            reclick_noti = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.noti_menu)))
            actions = ActionChains(self.driver)
            actions.move_to_element(reclick_noti)
            actions.click(reclick_noti)
            actions.perform()
            print("알림 메뉴를 클릭했습니다.")
            return True
        except NoSuchElementException:
            print("알림 메뉴를 한번 더 클릭하지 못했습니다.")
            return False
        
    # 나의 프로필 메뉴 확인하기
    def my_profile_menu_displayed(self):
        try:
            my_profile = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.profile_menu)))
            my_profile.is_displayed()
            print("나의 프로필 메뉴가 존재합니다.")
            return True
        except NoSuchElementException:
            print("나의 프로필 메뉴가 존재하지 않습니다.")
            return False
            
    # 나의 프로필 메뉴를 클릭하기
    def click_myprofile_menu(self):
        try:
            my_profile_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.my_profile)))
            actions = ActionChains(self.driver)
            actions.move_to_element(my_profile_btn)
            actions.click(my_profile_btn)
            actions.perform()
            print("나의 프로필 메뉴를 클릭했습니다.")
            return True
        except NoSuchElementException:
            print("나의 프로필 메뉴를 클릭하지 못했습니다.")
            return False
        
    # 나의 프로필 리스트 옵션 박스 메뉴 출력 확인하기
    def my_profile_list_displayed(self):
        try:
            my_profile_dropdown = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.my_profile_list)))
            my_profile_dropdown.is_displayed()
            print("나의 프로필 옵션 박스 메뉴가 출력되었습니다.")
            return True
        except NoSuchElementException:
            print("나의 프로필 옵션 박스 메뉴가 출력되지 않습니다.")
            return False
        
    # 나의 프로필 메뉴에서 워크스테이션 메뉴 확인하기
    def work_station_menu_displayed(self):
        try:
            work_station = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.work_station_menu)))
            work_station.is_displayed()
            print("나의 프로필 메뉴에 워크스테이션 메뉴가 존재합니다.")
            return True
        except NoSuchElementException:
            print("나의 프로필 메뉴에서 워크스테이션 메뉴가 존재하지 않습니다.")
            return False
        
    # 나의 프로필 메뉴에서 대시보드 메뉴 확인하기
    def dash_board_menu_displyed(self):
        try:
            dash_board = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.dash_board_menu)))
            dash_board.is_displayed()
            print("나의 프로필 메뉴에 대시보드 메뉴가 존재합니다.")
            return True
        except NoSuchElementException:
            print("나의 프로필 메뉴에서 대시보드 메뉴가 존재하지 않습니다.")
            return False
        
    # 나의 프로필 메뉴에서 로컬 녹화 파일 메뉴 확인하기
    def local_file_menu_displayed(self):
        try:
            local_file = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.local_file_menu)))
            local_file.is_displayed()
            print("나의 프로필 메뉴에 로컬파일 메뉴가 존재합니다.")
            return True
        except NoSuchElementException:
            print("나의 프로필 메뉴에 로컬파일 메뉴가 존재하지 않습니다.")
            return False
        
    # 나의 프로필 메뉴에서 로그아웃 메뉴 확인하기
    def logout_menu_displayed(self):
        try:
            logout_menu = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.logout_menu)))
            logout_menu.is_displayed()
            print("나의 프로필 메뉴에 로그아웃 메뉴가 존재합니다.")
            return True
        except NoSuchElementException:
            print("나의 프로필 메뉴에 로그아웃 메뉴가 존재하지 않습니다.")
            return False
        
    # 나의 프로필 메뉴에서 로그아웃 메뉴 선택하기
    def click_logout_menu(self):
        try:
            logout_click = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.logout_menu)))
            actions = ActionChains(self.driver)
            actions.move_to_element(logout_click)
            actions.click(logout_click)
            actions.perform()
            print("나의 프로필 메뉴에서 로그아웃 버튼을 클릭했습니다.")
            return True
        except NoSuchElementException:
            print("나의 프로필 메뉴에서 로그아웃 버튼을 클릭하지 못했습니다.")
            return False