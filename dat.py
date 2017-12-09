import wx
#from xlwt import *

class MainFrame(wx.Frame):#程序的主界面
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(MainFrame, self).__init__(*args, **kw)
        mainBackground = wx.Bitmap("zght.jpg")
        sb = wx.StaticBitmap(self,bitmap=mainBackground)
        sb.CentreOnParent()
        # 创建菜单栏
        self.makeMenuBar()
        # 创建状态栏
        self.CreateStatusBar()
        self.SetStatusText("欢迎使用数据分析工具!  如有疑问，请联系八部质量处孙波 手机：15000153349 固话：021-24185194")
        self.SetSize(800,600)
        self.Centre()

    def makeMenuBar(self):#定义主界面的菜单
        # 创建“文件”菜单
        wenjianMenu = wx.Menu()
        xinjianxinghaoItem = wenjianMenu.Append(-1, "&新建型号...","创建一个新的型号...")#创建“新建型号...”子菜单，"\t..." 用来定义快捷键
        tuichuItem = wenjianMenu.Append(-1, "&退出...","退出系统...")

        shujuguanliMenu = wx.Menu()
        zairushujuItem = shujuguanliMenu.Append(-1,"&载入数据...","载入产品数据表...")
        chenggongshujuguanliItem = shujuguanliMenu.Append(-1,"&成功数据管理...","管理飞行成功数据样本...")

        fenxiMenu=wx.Menu()
        danpiliangfenxiItem=fenxiMenu.Append(-1,"&单批量分析...","绘制某批产品数据的散点图...")
        duopiliangfenxiItem=fenxiMenu.Append(-1,"&多批量分析...","绘制多批产品数据的散点图...")

        bangzhuMenu = wx.Menu()
        caozuobuzhouItem = bangzhuMenu.Append(-1, "&操作步骤...", "获取帮助文件...")
        guanyuItem = bangzhuMenu.Append(-1, "&关于...", "获取软件信息...")

        menuBar = wx.MenuBar()
        menuBar.Append(wenjianMenu, "&文件")
        menuBar.Append(shujuguanliMenu, "&数据管理")
        menuBar.Append(fenxiMenu, "&分析")
        menuBar.Append(bangzhuMenu, "&帮助")

        font = menuBar.GetFont()
        font.PointSize += 10
        menuBar.SetFont(font)

        #将菜单条添加到主界面中
        self.SetMenuBar(menuBar)
        #设置每个菜单选项的响应函数
        self.Bind(wx.EVT_MENU, self.OnXinjianxinghao, xinjianxinghaoItem)
        self.Bind(wx.EVT_MENU, self.OnTuichu,  tuichuItem)
        self.Bind(wx.EVT_MENU, self.OnGuanyu, guanyuItem)

    def OnTuichu(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def OnXinjianxinghao(self, event):
        self.Close(True)

    def OnGuanyu(self, event):
        wx.MessageBox("Version：0.1.0\n\n编者：八部质量处 孙波"
                      "\n电话：021-24185194"
                      "\n         15000153349","关于...")

if __name__ == '__main__':
    app = wx.App()
    frm = MainFrame(None, title='Data Analysis Tool')
    frm.Show()
    app.MainLoop()