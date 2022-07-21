from PyQt5.QtCore import pyqtSignal, QThread
from selenium import webdriver
import json
import os
import platform
import time
import random
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

CHROME = 1
FIREFOX = 2


class Web(QThread):
    __URL = 'https://web.whatsapp.com/'
    driverNum = 0
    lcdNumber_reviewed = pyqtSignal(int)
    lcdNumber_nwa = pyqtSignal(int)
    lcdNumber_wa = pyqtSignal(int)
    Log = pyqtSignal(str)
    wa = pyqtSignal(str)
    nwa = pyqtSignal(str)
    EndWork = pyqtSignal(str)

    def __init__(self, parent=None, counter_start=0, step='A', numList=None, sleepMin=3, sleepMax=6, text='', path='',
                 Remember=False, browser=1):
        super(Web, self).__init__(parent)
        self.counter_start = counter_start
        self.Numbers = numList
        self.step = step
        self.sleepMin = sleepMin
        self.sleepMax = sleepMax
        self.text = text
        self.path = path
        self.remember = Remember
        self.isRunning = True
        try:
            if not os.path.exists('./temp/cache'):
                os.makedirs('temp/cache/')
        except:
            os.makedirs('./temp/cache/')
        # Save Session Section
        self.__platform = platform.system().lower()
        if self.__platform != 'windows' and self.__platform != 'linux':
            raise OSError('Only Windows and Linux are supported for now.')

        self.__browser_choice = 0
        self.__browser_options = None
        self.__browser_user_dir = None
        self.__driver = None

        if browser == 1:
            self.set_browser(CHROME)
        elif browser == 2:
            self.set_browser(FIREFOX)

        self.__init_browser()

    def driverBk(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        # options.add_argument(fr"--user-data-dir={userDataPath}")
        try:
            try:
                self.__driver = webdriver.Chrome(
                    chrome_options=options, service_args=["hide_console", ])
            except Exception as e:
                print("error remeber", e)
                self.__driver = webdriver.Chrome(
                    service_args=["hide_console", ])
        except Exception as e:
            print("Chrome ->:", e)
            try:
                try:
                    self.__driver = webdriver.Firefox()
                except:
                    self.__driver = webdriver.Firefox(
                        executable_path="geckodriver.exe")
            except Exception as e:
                print("ّFirefox ->:", e)
        self.__driver.set_window_position(0, 0)
        self.__driver.set_window_size(670, 800)

    def is_logged_in(self):
        status = self.__driver.execute_script(
            "if (document.querySelector('*[data-icon=chat]') !== null) { return true } else { return false }"
        )
        return status

    def ANALYZ(self):
        try:
            print("analyz")
            if self.remember:
                cacheList = os.listdir('temp/cache/')
                if len(cacheList) != 0:
                    self.access_by_file(f"./temp/cache/{cacheList[0]}")
                    print('recover')
                else:
                    self.driverBk()
                    self.__driver.get(self.__URL)
            else:
                self.driverBk()
                self.__driver.get(self.__URL)

            while True:
                time.sleep(1)
                if self.is_logged_in():
                    print("login")
                    log = "Login Success"
                    self.Log.emit(log)
                    break
            print("thread:", self.counter_start)
            i = 0
            f = 0
            nf = 0
            for num in self.Numbers:
                log = ""
                try:
                    time.sleep(3)
                    if i == 0:
                        execu = f"""
                                var a = document.createElement('a');
                                var link = document.createTextNode("my_user_num");
                                a.appendChild(link); 
                                a.href = "https://wa.me/{num}"; 
                                document.head.appendChild(a);
                                """
                        try:
                            self.__driver.execute_script(execu)
                        except Exception as e:
                            print("error")
                    else:
                        element = self.__driver.find_element_by_xpath(
                            '/html/head/a')
                        self.__driver.execute_script(f"arguments[0].setAttribute('href','https://wa.me/{num}');",
                                                     element)
                    user = self.__driver.find_element_by_xpath('/html/head/a')
                    self.__driver.execute_script("arguments[0].click();", user)
                    time.sleep(2)
                    sourceWeb = self.__driver.page_source
                    if "Phone number shared via url is invalid" in sourceWeb:
                        print(f"Not Found {num}")
                        nf += 1
                        self.lcdNumber_nwa.emit(nf)
                        log = f"Number::{num} => Not Find!"
                        self.nwa.emit(f"{num}")
                    else:
                        print("find", num)
                        f += 1
                        self.lcdNumber_wa.emit(f)
                        log = f"Number::{num} => Find."
                        self.wa.emit(f"{num}")
                except:
                    log = f"Number::{num} Error !"
                    continue
                finally:
                    i += 1
                    print(i)
                    self.lcdNumber_reviewed.emit(i)
                    self.Log.emit(log)
            time.sleep(2)
            print("end")
            self.EndWork.emit("-- analysis completed --")
            self.isRunning = False
            self.__driver.quit()
        except Exception as e:
            print("Analyz ->:", e)

    def SendTEXT(self):
        print("sent text")
        if self.remember:
            cacheList = os.listdir('temp/cache/')
            if len(cacheList) != 0:
                self.access_by_file(f"./temp/cache/{cacheList[0]}")
                print('recover')
            else:
                self.driverBk()
                self.__driver.get(self.__URL)
        else:
            self.driverBk()
            self.__driver.get(self.__URL)
        time.sleep(2)
        while True:
            time.sleep(1)
            if self.is_logged_in():
                print("login")
                log = "Login Success"
                self.Log.emit(log)
                break
        i = 0
        f = 0
        nf = 0
        from random import randint
        print(self.Numbers)
        for num in self.Numbers:
            log = ""
            try:
                time.sleep(3)
                if i == 0:
                    execu = f"""
                            var a = document.createElement('a');
                            var link = document.createTextNode("my_user_num");
                            a.appendChild(link); 
                            a.href = "https://wa.me/{num}"; 
                            document.head.appendChild(a);
                            """
                    try:
                        self.__driver.execute_script(execu)
                    except Exception as e:
                        print("error")
                        log = "ERROR !"
                        break
                else:
                    element = self.__driver.find_element_by_xpath(
                        '/html/head/a')
                    self.__driver.execute_script(
                        f"arguments[0].setAttribute('href','https://wa.me/{num}');", element)
                user = self.__driver.find_element_by_xpath('/html/head/a')
                self.__driver.execute_script("arguments[0].click();", user)
                time.sleep(2)
                sourceWeb = self.__driver.page_source
                if "Phone number shared via url is invalid" in sourceWeb:
                    print(f"Not Found {num}")
                    nf += 1
                    self.lcdNumber_nwa.emit(nf)
                    log = f"Number::{num} => No Send!"
                    self.nwa.emit(f"{num}")
                else:
                    print("find", num)
                    textBox = self.__driver.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
                    time.sleep(1)
                    textBox.send_keys(self.text)
                    self.__driver.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
                    time.sleep(1)
                    f += 1
                    self.lcdNumber_wa.emit(f)
                    log = f"Number::{num} => Sent."
                    self.wa.emit(f"{num}")
                time.sleep(randint(self.sleepMin, self.sleepMax))
            except:
                log = f"Error To Number = {num} "
                continue
            finally:
                i += 1
                self.lcdNumber_reviewed.emit(i)
                self.Log.emit(log)
        print("end msg")
        self.EndWork.emit("-- Send Message completed --")
        self.stop()
        self.isRunning = False

    def SendIMG(self):
        print("sent text")
        if self.remember:
            cacheList = os.listdir('temp/cache/')
            if len(cacheList) != 0:
                self.access_by_file(f"./temp/cache/{cacheList[0]}")
                print('recover')
            else:
                self.driverBk()
                self.__driver.get(self.__URL)
        else:
            self.driverBk()
            self.__driver.get(self.__URL)
        time.sleep(2)
        while True:
            time.sleep(1)
            if self.is_logged_in():
                print("login")
                log = "Login Success"
                self.Log.emit(log)
                break
        i = 0
        f = 0
        nf = 0
        from random import randint
        print(self.Numbers)
        for num in self.Numbers:
            log = ""
            try:
                time.sleep(3)
                if i == 0:
                    execu = f"""
                            var a = document.createElement('a');
                            var link = document.createTextNode("my_user_num");
                            a.appendChild(link); 
                            a.href = "https://wa.me/{num}"; 
                            document.head.appendChild(a);
                            """
                    try:
                        self.__driver.execute_script(execu)
                    except Exception as e:
                        print("error")
                        log = "ERROR !"
                        break
                else:
                    element = self.__driver.find_element_by_xpath(
                        '/html/head/a')
                    self.__driver.execute_script(
                        f"arguments[0].setAttribute('href','https://wa.me/{num}');", element)
                user = self.__driver.find_element_by_xpath('/html/head/a')
                self.__driver.execute_script("arguments[0].click();", user)
                time.sleep(2)
                sourceWeb = self.__driver.page_source
                if "Phone number shared via url is invalid" in sourceWeb:
                    print(f"Not Found {num}")
                    nf += 1
                    self.lcdNumber_nwa.emit(nf)
                    log = f"Number::{num} => No Send"
                    self.nwa.emit(f"{num}")
                else:
                    print("find", num)
                    self.__driver.find_element_by_xpath(
                        '//span[@data-icon="clip"]').click()
                    time.sleep(2)
                    attch = self.__driver.find_element_by_xpath(
                        '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                    attch.send_keys(self.path)
                    time.sleep(2)
                    if self.text != '' or self.text != ' ':
                        caption = self.__driver.find_element_by_xpath(
                            '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]')
                        caption.send_keys(self.text)
                        time.sleep(2)
                    self.__driver.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span').click()
                    f += 1
                    self.lcdNumber_wa.emit(f)
                    log = f"Number::{num} => Sent"
                    self.wa.emit(f"{num}")
                time.sleep(randint(self.sleepMin, self.sleepMax))
            except:
                log = f"Error To Number = {num} "
                continue
            finally:
                i += 1
                self.lcdNumber_reviewed.emit(i)
                self.Log.emit(log)
        self.EndWork.emit("-- Send Image completed --")
        self.stop()
        self.isRunning = False

    def addAcc(self):
        try:
            print("Add Account")
            if self.remember:
                if self.path == '':
                    cacheName = str(random.randint(1, 9999999))
                    self.path = cacheName
                self.save_profile(self.get_active_session(),
                                  f"./temp/cache/{self.path}")
                print('File saved.')
            print("thread:", self.counter_start)
            self.EndWork.emit("-- Add Account completed --")
            self.isRunning = False
        except Exception as e:
            print("Add Account ->:", e)

    def run(self):
        while self.isRunning == True:
            if self.step == 'A':
                self.ANALYZ()
            elif self.step == 'M':
                self.SendTEXT()
            elif self.step == 'I':
                self.SendIMG()
            elif self.step == 'Add':
                self.addAcc()

    def stop(self):
        self.isRunning = False
        print('stopping thread...')
        try:
            self.__driver.quit()
        except:
            pass

    def __init_browser(self):
        if self.__browser_choice == CHROME:
            self.__browser_options = webdriver.ChromeOptions()

            if self.__platform == 'windows':
                self.__browser_user_dir = os.path.join(os.environ['USERPROFILE'],
                                                       'Appdata', 'Local', 'Google', 'Chrome', 'User Data')
            elif self.__platform == 'linux':
                self.__browser_user_dir = os.path.join(
                    os.environ['HOME'], '.config', 'google-chrome')

        elif self.__browser_choice == FIREFOX:
            self.__browser_options = webdriver.FirefoxOptions()

            if self.__platform == 'windows':
                self.__browser_user_dir = os.path.join(
                    os.environ['APPDATA'], 'Mozilla', 'Firefox', 'Profiles')
                self.__browser_profile_list = os.listdir(
                    self.__browser_user_dir)
            elif self.__platform == 'linux':
                self.__browser_user_dir = os.path.join(
                    os.environ['HOME'], '.mozilla', 'firefox')

        self.__browser_options.headless = True
        self.__refresh_profile_list()

    def __refresh_profile_list(self):
        if self.__browser_choice == CHROME:
            self.__browser_profile_list = ['']
            for profile_dir in os.listdir(self.__browser_user_dir):
                if 'profile' in profile_dir.lower():
                    if profile_dir != 'System Profile':
                        self.__browser_profile_list.append(profile_dir)
        elif self.__browser_choice == FIREFOX:

            self.__browser_profile_list = []
            for profile_dir in os.listdir(self.__browser_user_dir):
                if not profile_dir.endswith('.default'):
                    if os.path.isdir(os.path.join(self.__browser_user_dir, profile_dir)):
                        self.__browser_profile_list.append(profile_dir)

    def __get_indexed_db(self):
        self.__driver.execute_script('window.waScript = {};'
                                     'window.waScript.waSession = undefined;'
                                     'function getAllObjects() {'
                                     'window.waScript.dbName = "wawc";'
                                     'window.waScript.osName = "user";'
                                     'window.waScript.db = undefined;'
                                     'window.waScript.transaction = undefined;'
                                     'window.waScript.objectStore = undefined;'
                                     'window.waScript.getAllRequest = undefined;'
                                     'window.waScript.request = indexedDB.open(window.waScript.dbName);'
                                     'window.waScript.request.onsuccess = function(event) {'
                                     'window.waScript.db = event.target.result;'
                                     'window.waScript.transaction = window.waScript.db.transaction('
                                     'window.waScript.osName);'
                                     'window.waScript.objectStore = window.waScript.transaction.objectStore('
                                     'window.waScript.osName);'
                                     'window.waScript.getAllRequest = window.waScript.objectStore.getAll();'
                                     'window.waScript.getAllRequest.onsuccess = function(getAllEvent) {'
                                     'window.waScript.waSession = getAllEvent.target.result;'
                                     '};'
                                     '};'
                                     '}'
                                     'getAllObjects();')
        while not self.__driver.execute_script('return window.waScript.waSession != undefined;'):
            time.sleep(1)
        wa_session_list = self.__driver.execute_script(
            'return window.waScript.waSession;')
        return wa_session_list

    def __get_profile_storage(self, profile_name=None):
        self.__refresh_profile_list()

        if profile_name is not None and profile_name not in self.__browser_profile_list:
            raise ValueError(
                'The specified profile_name was not found. Make sure the name is correct.')

        if profile_name is None:
            self.__start_visible_session()
        else:
            self.__start_invisible_session(profile_name)

        indexed_db = self.__get_indexed_db()

        self.__driver.quit()

        return indexed_db

    def __start_session(self, options, profile_name=None, wait_for_login=True):
        if profile_name is None:
            if self.__browser_choice == CHROME:
                self.__driver = webdriver.Chrome(options=options)
                self.__driver.set_window_position(0, 0)
                self.__driver.set_window_size(670, 800)
            elif self.__browser_choice == FIREFOX:
                self.__driver = webdriver.Firefox(options=options)

            self.__driver.get(self.__URL)

            if wait_for_login:
                verified_wa_profile_list = False
                while not verified_wa_profile_list:
                    time.sleep(1)
                    verified_wa_profile_list = False
                    for object_store_obj in self.__get_indexed_db():
                        if 'WASecretBundle' in object_store_obj['key']:
                            verified_wa_profile_list = True
                            break
        else:
            if self.__browser_choice == CHROME:
                options.add_argument(
                    'user-data-dir=%s' % os.path.join(self.__browser_user_dir, profile_name))
                self.__driver = webdriver.Chrome(options=options)
            elif self.__browser_choice == FIREFOX:
                fire_profile = webdriver.FirefoxProfile(
                    os.path.join(self.__browser_user_dir, profile_name))
                self.__driver = webdriver.Firefox(
                    fire_profile, options=options)

            self.__driver.get(self.__URL)

    def __start_visible_session(self, profile_name=None, wait_for_login=True):
        options = self.__browser_options
        options.headless = False
        self.__refresh_profile_list()

        if profile_name is not None and profile_name not in self.__browser_profile_list:
            raise ValueError(
                'The specified profile_name was not found. Make sure the name is correct.')

        self.__start_session(options, profile_name, wait_for_login)

    def __start_invisible_session(self, profile_name=None):
        self.__refresh_profile_list()
        if profile_name is not None and profile_name not in self.__browser_profile_list:
            raise ValueError(
                'The specified profile_name was not found. Make sure the name is correct.')

        self.__start_session(self.__browser_options, profile_name)

    def set_browser(self, browser):
        if type(browser) == str:
            if browser.lower() == 'chrome':
                self.__browser_choice = CHROME
            elif browser.lower() == 'firefox':
                self.__browser_choice = FIREFOX
            else:
                raise ValueError(
                    'The specified browser is invalid. Try to use "chrome" or "firefox" instead.')
        else:
            if browser == CHROME:
                pass
            elif browser == FIREFOX:
                pass
            else:
                raise ValueError(
                    'Browser type invalid. Try to use WaWebSession.CHROME or WaWebSession.FIREFOX instead.')

            self.__browser_choice = browser

    def get_active_session(self, use_profile=None):
        profile_storage_dict = {}
        use_profile_list = []
        self.__refresh_profile_list()

        if use_profile and use_profile not in self.__browser_profile_list:
            raise ValueError('Profile does not exist: %s', use_profile)
        elif use_profile is None:
            return self.__get_profile_storage()
        elif use_profile and use_profile in self.__browser_profile_list:
            use_profile_list.append(use_profile)
        elif type(use_profile) == list:
            use_profile_list.extend(self.__browser_profile_list)
        else:
            raise ValueError(
                "Invalid profile provided. Make sure you provided a list of profiles or a profile name.")

        for profile in use_profile_list:
            profile_storage_dict[profile] = self.__get_profile_storage(profile)

        return profile_storage_dict

    def create_new_session(self):
        return self.__get_profile_storage()

    def access_by_obj(self, wa_profile_list):
        verified_wa_profile_list = False
        for object_store_obj in wa_profile_list:
            if 'WASecretBundle' in object_store_obj['key']:
                verified_wa_profile_list = True
                break

        if not verified_wa_profile_list:
            raise ValueError(
                'This is not a valid profile list. Make sure you only pass one session to this method.')

        self.__start_visible_session(wait_for_login=False)
        self.__driver.execute_script('window.waScript = {};'
                                     'window.waScript.insertDone = 0;'
                                     'window.waScript.jsonObj = undefined;'
                                     'window.waScript.setAllObjects = function (_jsonObj) {'
                                     'window.waScript.jsonObj = _jsonObj;'
                                     'window.waScript.dbName = "wawc";'
                                     'window.waScript.osName = "user";'
                                     'window.waScript.db;'
                                     'window.waScript.transaction;'
                                     'window.waScript.objectStore;'
                                     'window.waScript.clearRequest;'
                                     'window.waScript.addRequest;'
                                     'window.waScript.request = indexedDB.open(window.waScript.dbName);'
                                     'window.waScript.request.onsuccess = function(event) {'
                                     'window.waScript.db = event.target.result;'
                                     'window.waScript.transaction = window.waScript.db.transaction('
                                     'window.waScript.osName, "readwrite");'
                                     'window.waScript.objectStore = window.waScript.transaction.objectStore('
                                     'window.waScript.osName);'
                                     'window.waScript.clearRequest = window.waScript.objectStore.clear();'
                                     'window.waScript.clearRequest.onsuccess = function(clearEvent) {'
                                     'for (var i=0; i<window.waScript.jsonObj.length; i++) {'
                                     'window.waScript.addRequest = window.waScript.objectStore.add('
                                     'window.waScript.jsonObj[i]);'
                                     'window.waScript.addRequest.onsuccess = function(addEvent) {'
                                     'window.waScript.insertDone++;'
                                     '};'
                                     '}'
                                     '};'
                                     '};'
                                     '}')
        self.__driver.execute_script(
            'window.waScript.setAllObjects(arguments[0]);', wa_profile_list)

        while not self.__driver.execute_script(
                'return (window.waScript.insertDone == window.waScript.jsonObj.length);'):
            time.sleep(1)

        self.__driver.refresh()


    def access_by_file(self, profile_file):
        profile_file = os.path.normpath(profile_file)

        if os.path.isfile(profile_file):
            with open(profile_file, 'r') as file:
                wa_profile_list = json.load(file)

            verified_wa_profile_list = False
            for object_store_obj in wa_profile_list:
                if 'WASecretBundle' in object_store_obj['key']:
                    verified_wa_profile_list = True
                    break
            if verified_wa_profile_list:
                self.access_by_obj(wa_profile_list)
            else:
                raise ValueError('There might be multiple profiles stored in this file.'
                                 ' Make sure you only pass one WaSession file to this method.')
        else:
            raise FileNotFoundError(
                'Make sure you pass a valid WaSession file to this method.')

    def save_profile(self, wa_profile_list, file_path):
        file_path = os.path.normpath(file_path)

        verified_wa_profile_list = False
        for object_store_obj in wa_profile_list:
            if 'key' in object_store_obj:
                if 'WASecretBundle' in object_store_obj['key']:
                    verified_wa_profile_list = True
                    break
        if verified_wa_profile_list:
            with open(file_path, 'w') as file:
                json.dump(wa_profile_list, file, indent=4)
        else:
            saved_profiles = 0
            for profile_name in wa_profile_list.keys():
                profile_storage = wa_profile_list[profile_name]
                verified_wa_profile_list = False
                for object_store_obj in profile_storage:
                    if 'key' in object_store_obj:
                        if 'WASecretBundle' in object_store_obj['key']:
                            verified_wa_profile_list = True
                            break
                if verified_wa_profile_list:
                    single_profile_name = os.path.basename(
                        file_path) + '-' + profile_name
                    self.save_profile(profile_storage, os.path.join(
                        os.path.dirname(file_path), single_profile_name))
                    saved_profiles += 1
            if saved_profiles > 0:
                pass
            else:
                raise ValueError(
                    'Could not find any profiles in the list. Make sure to specified file path is correct.')
