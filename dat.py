import wx
import xjxhFrame
import sys

class MainFrame(wx.Frame):
    # 程序的主界面
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)
        main_background = wx.Bitmap("zght.jpg")
        sb = wx.StaticBitmap(self, bitmap=main_background)
        sb.Centre()
        # 创建菜单栏
        self.make_menu_bar()
        # 创建状态栏
        self.CreateStatusBar()
        self.SetStatusText("欢迎使用数据分析工具!  如有疑问，请联系八部质量处孙波 手机：15000153349 固话：021-24185194")
        self.SetSize(800,600)
        self.CentreOnScreen()
        self.SetBackgroundColour("White")

    def make_menu_bar(self):
        # 定义主界面的菜单
        # 创建“文件”菜单
        file_menu = wx.Menu()
        new_model_item = file_menu.Append(-1, "&新建型号...","创建一个新的型号...")
        exit_item = file_menu.Append(-1, "&退出...","退出系统...")

        data_manage_menu = wx.Menu()
        load_data_item = data_manage_menu.Append(-1, "&载入数据...", "载入产品数据表...")
        success_data_manage_item = data_manage_menu.Append(-1, "&成功数据管理...", "管理飞行成功数据样本...")

        analysis_menu = wx.Menu()
        single_batch_item = analysis_menu.Append(-1, "&单批量分析...", "绘制某批产品数据的散点图...")
        multiple_batch_item = analysis_menu.Append(-1, "&多批量分析...", "绘制多批产品数据的散点图...")

        help_menu = wx.Menu()
        help_step_item = help_menu.Append(-1, "&操作步骤...", "获取帮助文件...")
        about_item = help_menu.Append(-1, "&关于...", "获取软件信息...")

        menuBar = wx.MenuBar()
        menuBar.Append(file_menu, "&文件")
        menuBar.Append(data_manage_menu, "&数据管理")
        menuBar.Append(analysis_menu, "&分析")
        menuBar.Append(help_menu, "&帮助")

        font = menuBar.GetFont()
        font.PointSize += 10
        menuBar.SetFont(font)

        #将菜单条添加到主界面中
        self.SetMenuBar(menuBar)
        #设置每个菜单选项的响应函数
        self.Bind(wx.EVT_MENU, self.on_new_model, new_model_item)
        self.Bind(wx.EVT_MENU, self.on_exit,  exit_item)
        self.Bind(wx.EVT_MENU, self.on_about, about_item)

    def on_exit(self, event):
        sys.exit()

    def on_new_model(self, event):
        XinjianxinghaoFrame = xjxhFrame.NewModelFrame(None, -1, "新建型号...")
        XinjianxinghaoFrame.CentreOnParent()
        XinjianxinghaoFrame.ShowModal()

    def on_about(self, event):
        wx.MessageBox("Version：0.1.0.20171210\n\n编者：八部质量处 孙波"
                      "\n电话：021-24185194"
                      "\n         15000153349","关于...")

if __name__ == '__main__':
    app = wx.App()
    wx.MessageBox("欢迎使用数据分析工具！")
    MainFrame(None, title="Data Analysis Tool  Ver: 0.1.0").Show()
    app.MainLoop()