import wx
from xlwt import *
import os

class NewModelFrame(wx.Dialog):
    #新建型号界面
    def __init__(self, *args, **kw):
        super(NewModelFrame, self).__init__(*args, **kw)
        self.SetSize(400, 300)

        pnl = wx.Panel(self, -1, size=(200, 100))
        str = "请输入型号名称："
        st = wx.StaticText(pnl, -1, str, (100, 50))
        st.SetBackgroundColour("White")
        self.model_text = wx.TextCtrl(pnl, -1, pos=(100, 100), size=(200, -1))
        ok_btn = wx.Button(pnl, -1, "确定", pos=(100, 150))
        cancel_btn = wx.Button(pnl, -1, "取消", pos=(200, 150))

        self.Bind(wx.EVT_BUTTON, self.on_cancel_btn, cancel_btn)
        self.Bind(wx.EVT_BUTTON, self.on_ok_btn, ok_btn)

    def on_cancel_btn(self, event):
        self.Close(True)

    def on_ok_btn(self, event):
        model_name = self.model_text.GetValue()
        if model_name.strip() == '':
            wx.MessageBox("错误：型号名称不能为空！")
        else:
            if os.path.exists(model_name+'.xls') | os.path.exists(model_name+'.xlsx'):
                wx.MessageBox("文件已经存在，请更换文件名...")
            else:
                w = Workbook(encoding='utf-8')
                ws = w.add_sheet('状态1')
                model_name = model_name + '.xls'
                w.save(model_name)
                print(model_name)
                model_name = model_name[:-4]
                self.Close(True)
                wx.MessageBox(model_name+" 型号数据集 创建成功。", "结果报告")