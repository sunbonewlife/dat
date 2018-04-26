import wx
import wx.xrc
import wx.grid
import zrsjFrame
from pylab import *

# 版本号标识
version = "Version：0.1"

class MainFrame(wx.Frame):
    # 程序的主界面
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)
        # 创建菜单栏
        self.make_menu_bar()
        # 创建状态栏
        self.CreateStatusBar()
        self.SetStatusText("欢迎使用数据分析工具!  如有疑问，请联系八部质量处孙波 手机：15000153349 固话：021-24185194")
        self.SetSize(800, 600)
        self.CentreOnScreen()
        self.SetBackgroundColour("White")

    def make_menu_bar(self):
        # 定义主界面的菜单
        # 创建“系统”菜单
        system_menu = wx.Menu()
        exit_item = system_menu.Append(-1, "&退出...","退出系统...")
        data_manage_menu = wx.Menu()
        load_data_item = data_manage_menu.Append(-1, "&载入数据...", "载入产品质量数据文件...")
        #test_menu = wx.Menu()
        #test_item = test_menu.Append(-1, "&测试效果...", "测试这段代码的效果...")

        menuBar = wx.MenuBar()
        menuBar.Append(system_menu, "&系统")
        menuBar.Append(data_manage_menu, "&数据管理")
        #menuBar.Append(test_menu, "&测试")

        #将菜单条添加到主界面中
        self.SetMenuBar(menuBar)
        #设置每个菜单选项的响应函数
        self.Bind(wx.EVT_MENU, self.on_exit,  exit_item)
        self.Bind(wx.EVT_MENU, self.on_load_data, load_data_item)
        #self.Bind(wx.EVT_MENU, self.on_test, test_item)

    def on_exit(self, event):
        sys.exit()

    def on_load_data(self, event):
        ZrsjFrame = zrsjFrame.LoadDataFrame(None, -1, "载入数据...")
        ZrsjFrame.CentreOnParent()
        ZrsjFrame.ShowModal()

    #def on_test(self, event):
    #    x = np.empty([3, 3])
    #    print(x)


if __name__ == '__main__':
    app = wx.App()
    main_win = MainFrame(None, title="Data Analysis Tool  " + '('+ version +')')
    main_win.Show()
    app.MainLoop()
