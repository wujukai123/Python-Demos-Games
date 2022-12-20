import wx
app = wx.App(False) # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
frame.Show(True) # Show the frame
app.mainLoop()
py2applet --make-setup hello.py
python setup.py py2app -A
