import wx
import xlrd


class LoadDataFrame(wx.Dialog):
    # 新建型号界面
    def __init__(self, *args, **kw):
        super(LoadDataFrame, self).__init__(*args, **kw)
        self.SetSize(500, 300)

        pnl = wx.Panel(self, -1, size=(200, 100))
        str = "请点击“浏览”选择数据文件。\n注：文件应为 .xls 格式（目前不支持 .xlsx 格式）"
        st = wx.StaticText(pnl, -1, str, (50, 50))
        st.SetBackgroundColour("White")
        self.data_path_text = wx.TextCtrl(pnl, -1, pos=(50, 100), size=(350, -1))
        browser_btn = wx.Button(pnl, -1, "浏览...", pos=(50, 150))
        ok_btn = wx.Button(pnl, -1, "确定", pos=(50, 200))
        cancel_btn = wx.Button(pnl, -1, "取消", pos=(150, 200))

        self.Bind(wx.EVT_BUTTON, self.on_cancel_btn, cancel_btn)
        self.Bind(wx.EVT_BUTTON, self.on_ok_btn, ok_btn)
        self.Bind(wx.EVT_BUTTON, self.on_browser_btn, browser_btn)

        filename = ""

    def on_cancel_btn(self, event):
        self.Close(True)

    def on_browser_btn(self, event):
        file_wildcard = "Excel files(*.xls)|*.xls"
        dlg = wx.FileDialog(self, "Open excel file...", wildcard=file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            self.data_path_text.SetValue(dlg.GetPath())
        dlg.Destroy()

    def on_ok_btn(self, event):
        filename = self.data_path_text.GetValue()
        data = xlrd.open_workbook(filename)
        table = data.sheet_by_name(u'Sheet1')
        # 行数，即数据总条目数
        n_rows = table.nrows
        # 获取表头，须规定Excel文件首行为参数项目名称
        col_names = table.row_values(0)
        row1 = table.row_values(1)
        print()
        list = []
        for rownum in range(1, n_rows):
            row1 = table.row_values(rownum)
            print(row1)
            if row:
                app = {}
                for i in range(len(col_names)):
                    app[col_names[i]] = row[i]
                list.append(app)
            return list