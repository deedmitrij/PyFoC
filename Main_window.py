from tkinter import *
import tkinter.ttk as ttk
from data.builds_list import builds
from Actions import Action

class UI():

    action = Action()

    def run_main_window(self):

        self.root=Tk()
        self.root.title('PyfoC')
        self.root.geometry('260x290')
        self.root.resizable(False, False)

        self.first_menu_item_label = Label(self.root, text="1.")
        self.first_menu_item_label.grid(column=1, row=0, sticky=E)

        self.second_menu_item_label = Label(self.root, text="2.")
        self.second_menu_item_label.grid(column=1, row=2, sticky=E)

        self.third_menu_item_label = Label(self.root, text="3.")
        self.third_menu_item_label.grid(column=1, row=4, sticky=E)

        self.fourth_menu_item_label = Label(self.root, text="4.")
        self.fourth_menu_item_label.grid(column=1, row=7, sticky=E)

        self.appdata_lable = Label(self.root, text="-- Operations with AppData -----------")
        self.appdata_lable.grid(column=2, row=0, columnspan=2, pady=3, sticky=W)

        self.open_appdata_folder_button = Button(self.root, text="Open AppData",
                                                 command=self.action.open_appdata_folder)
        self.open_appdata_folder_button.grid(row=1, column=2)

        self.clear_appdata_button = Button(self.root, text="Clear AppData", command=self.action.clear_appdata)
        self.clear_appdata_button.grid(row=1, column=3)

        self.logs_lable = Label(self.root, text="-- Operations with Logs ---------------")
        self.logs_lable.grid(column=2, row=2, columnspan=2, pady=3, sticky=W)

        self.open_logs_folder_button = Button(self.root, text="Open Logs", command=self.action.open_logs_folder)
        self.open_logs_folder_button.grid(row=3, column=2)

        self.delete_logs_button = Button(self.root, text="Delete Logs", command=self.action.del_logs)
        self.delete_logs_button.grid(row=3, column=3)

        self.CUE_lable = Label(self.root, text="-- Operations with CUE ----------------")
        self.CUE_lable.grid(column=2, row=4, columnspan=2, pady=3, sticky=W)

        self.start_CUE_button = Button(self.root, text="Start CUE", command=self.action.start_CUE)
        self.start_CUE_button.grid(row=5, column=2)

        self.close_CUE_button = Button(self.root, text="Close CUE", command=self.action.close_CUE)
        self.close_CUE_button.grid(row=5, column=3)

        self.clear_appdata_check = IntVar()
        self.with_cleared_appdata_checkbutton = Checkbutton(self.root, text='with cleared AppData',
                                                            variable=self.clear_appdata_check,
                                                            onvalue=1, offvalue=0)
        self.with_cleared_appdata_checkbutton.grid(row=6, column=3, pady=5, sticky=W)

        self.restart_CUE_button = Button(self.root, text="Restart CUE",
                                         command=self.get_clear_appdata_check_state)
        self.restart_CUE_button.grid(row=6, column=2, pady=5, ipadx=5)

        self.builds_downloading_lable = Label(self.root, text="-- Build's downloading ----------------")
        self.builds_downloading_lable.grid(column=2, row=7, columnspan=2, pady=3, sticky=W)

        self.get_builds_button = Button(self.root, text="get", command=self.action.get_builds_list)
        self.get_builds_button.grid(row=8, column=2, sticky=E)

        self.downloading_builds_button = Button(self.root, text="Download", command=self.action.close_CUE)
        self.downloading_builds_button.grid(row=9, column=3, sticky=E)

        self.build = StringVar()
        self.choose_build_combobox = ttk.Combobox(self.root, textvariable=self.build, values=builds[::-1],
                                                  state='readonly', height=6,
                                                  width=5)
        self.choose_build_combobox.grid(row=8, column=2, sticky=W)

        self.builds_versions = StringVar()
        self.builds_versions_list = []
        self.choose_builds_versions_combobox = ttk.Combobox(self.root, textvariable=self.builds_versions,
                                                            values=self.builds_versions_list,
                                                            state='readonly', height=10, width=18)
        self.choose_builds_versions_combobox.grid(row=8, column=3, sticky=E)

        self.root.mainloop()

    def get_clear_appdata_check_state(self):
        self.state = self.clear_appdata_check.get()
        self.action.restart_CUE(self.state)