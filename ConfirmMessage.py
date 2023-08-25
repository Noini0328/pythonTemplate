import tkinter as tk
from tkinter import messagebox

class ConfirmMessage:
    title = None
    message = None
    def confirm(self):
        result = messagebox.askquestion(self.title, self.message)
        if result == "yes":
            print("Confirm Yes.")
        else:
            print("Confirm No.")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # hide main window
    #confirm_execution()

    Confirm1st = ConfirmMessage()
    Confirm1st.title = "Confirmation"
    Confirm1st.message = "Developed by sakai(kanagawa). \nPlease run this program at your own responsibility.\nBe sure to check the evidence against the analysis results and report any bugs.\nDo you agree to the above and proceed with the execution?"
    Confirm1st.confirm()