import wx
def calculate():
    print 10
app = wx.App()
#show ui
win = wx.Frame(None,title="simple Editor",size=(410,355))
#button
loadButton = wx.Button(win,label="Open",pos=(225,5),size=(80,25))
#button
saveButton = wx.Button(win,label="Save",pos=(315,5),size=(80,25))
filename = wx.TextCtrl(win,pos=(5,5),size=(210,25))
contents = wx.TextCtrl(win,pos=(5,35),size=(390,260),style=wx.TE_MULTILINE | wx.HSCROLL)
loadButton.Bind(wx.EVT_BUTTON,calculate)
#show
win.Show()
app.MainLoop()

