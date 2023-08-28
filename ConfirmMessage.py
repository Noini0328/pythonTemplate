import sys
from art import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


class ConfirmMessage:
    title = None
    message = None
    def confirm(self):
        result = messagebox.askquestion(self.title, self.message)
        if result == "yes":
            print("Confirm Yes.")
        else:
            print("Confirm No.")
            print("Type any key to exit the program...")
            input()
            sys.exit()


if __name__ == "__main__":
    tprint("Tools Name",font="rnd-medium")

    root = tk.Tk()
    root.withdraw()  # hide main window
    #confirm_execution()

    Confirm1st = ConfirmMessage()
    Confirm1st.title = "Confirmation"
    Confirm1st.message = "Developed by xxxx(xxxx). \nPlease run this program at your own responsibility.\nBe sure to check the evidence against the  results and report any bugs.\nDo you agree to the above and proceed with the execution?"
    Confirm1st.confirm()


    input_file = filedialog.askopenfilename(title="入力ファイルを選択してください", filetypes=[("すべてのファイル", "*.*")])
    print(input_file)

    input_fold = filedialog.askdirectory(title="入力フォルダを選択してください")
    print(input_fold)


