import  wx

def singleton(class_):
    instance={}
    def getinstance(*args,**kwargs):
        if class_ not in instance:
            instance[class_]=class_(*args,**kwargs)

        return  instance[class_]
    return getinstance

@singleton
class PyMine(wx.Frame):

    def __init__(self,parent):

        wx.Frame.__init__(self,parent,size=(250,341))
        #?
        self.numMine=12
        # ?
        self.numFlaged=0
        # ?
        self.mineCount=self.numMine
        # ?
        self.timePassed=0
        # ?
        self.mine=MineAlgo(self.numMine,4,4)
        # ?
        #content
        self.controlPane=wx.Pane(self,-1,name='Control Panel',size=(210,30))
        # ?
        self.about=AboutFrame(None)

        self.mineNumIcon = [wx.Bitmap("0.gif"), wx.Bitmap("1.gif"),
                            wx.Bitmap("2.gif"), wx.Bitmap("3.gif"),
                            wx.Bitmap("4.gif"), wx.Bitmap("5.gif"),
                            wx.Bitmap("6.gif"), wx.Bitmap("7.gif"),
                            wx.Bitmap("8.gif")]

