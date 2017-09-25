import os
import psutil
import time
from selenium import webdriver
from pyvirtualdisplay import Display


class Action():

    def clear_appdata(self):

        self.clear_appdata_command_list = ['taskkill /F /IM CUE.exe',
                                           'RD /S /Q "%USERPROFILE%\AppData\Roaming\Corsair\CUE"',
                                           'RD /S /Q "%USERPROFILE%\AppData\Local\Corsair\CUE\logs"',
                                           'explorer "C:\Program Files (x86)\Corsair\Corsair Utility Engine\CUE.exe"']

        for el in self.clear_appdata_command_list:
            os.system(el)
            time.sleep(1)

    def del_logs(self):

        self.del_logs_command_list = ['taskkill /F /IM CUE.exe',
                                      'RD /S /Q "%USERPROFILE%\AppData\Local\Corsair\CUE\logs"',
                                      'explorer "C:\Program Files (x86)\Corsair\Corsair Utility Engine\CUE.exe"']

        for el in self.del_logs_command_list:
            os.system(el)
            time.sleep(1)

    def restart_CUE(self, state):

        self.restart_CUE_command_list = ['taskkill /F /IM CUE.exe',
                                         'explorer "C:\Program Files (x86)\Corsair\Corsair Utility Engine\CUE.exe"']
        if state == 1:
            self.clear_appdata()
        else:
            for el in self.restart_CUE_command_list:
                os.system(el)
                time.sleep(1)

    def close_CUE(self):

        self.close_CUE_command_list = ['taskkill /F /IM CUE.exe']

        for el in self.close_CUE_command_list:
           os.system(el)
           time.sleep(1)

    def start_CUE(self):

        self.start_CUE_command_list = ['explorer "C:\Program Files (x86)\Corsair\Corsair Utility Engine\CUE.exe"']

        for el in self.start_CUE_command_list:
            os.system(el)
            time.sleep(1)

    def open_appdata_folder(self):

        self.open_appdata_folder_command_list = ['explorer "%APPDATA%\Corsair\CUE"']

        for el in self.open_appdata_folder_command_list:
            os.system(el)
            time.sleep(1)

    def open_logs_folder(self):

        self.open_logs_folder_command_list = ['explorer "%USERPROFILE%\AppData\Local\Corsair\CUE\logs"']

        for el in self.open_logs_folder_command_list:
            os.system(el)
            time.sleep(1)

    def get_builds_list(self):

         display = Display(visible=0, size=(800, 600))
         display.start()

         browser = webdriver.Firefox()
         browser.get('https://builder.devx.dp.ua/corsair-builds/cue/?C=M&O=D')
         print('its ok')
         browser.quit()

         display.stop()


