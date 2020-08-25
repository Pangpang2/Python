from pywinauto.application import Application

app = Application().start('notepad.exe')
app.UntitledNotepad.menu_select("Help->About Notepad")
#app.AboutNotepad.OK.click()