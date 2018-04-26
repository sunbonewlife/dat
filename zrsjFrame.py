import wx.xrc
import wx.grid
import xlrd
from dat import *


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
        file = xlrd.open_workbook(filename)
        all_sheets_list = file.sheet_names()  # 读取excel文件的所有工作表名称
        sheet_data = file.sheet_by_index(0)
        print("产品名称：", all_sheets_list[0])
        print("检索到", sheet_data.nrows - 3, "条产品数据，", sheet_data.ncols - 3, "项指标参数")
        data = []
        for i in range(0, sheet_data.nrows):
            data.append(sheet_data.row_values(i))
        # print(data)
        datat = np.array(data).T# 转换方向以后的数据
        # 形式为   编号          blank  blank  no1  no2  no3...
        #          批次                        1    2    3
        #          是否成功子样                0    1    0
        #          参数1         上限   下限   数值 数值 数值
        #          参数n         上限   下限   数值 数值 数值
        for i in range(3, sheet_data.ncols):
            temp = list(map(float, datat[i][3:sheet_data.nrows]))
            zhibiao = list(map(float, datat[i][1:3]))
            from pylab import mpl
            mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
            mpl.rcParams['axes.unicode_minus'] = False
            h = plt.figure(i-2, figsize=(20, 10), frameon=True)
            ax1 = h.add_axes([0.05,0.1,0.8,0.8])
            ax1.scatter(range(1, sheet_data.nrows - 2, 1), temp, color='k')
            ax1.set_xlim(0, sheet_data.nrows+20)
            # 绘制平均值线
            ax1.axhline(sum(temp)/len(temp), color='r')
            ax1.text(sheet_data.nrows+22, sum(temp)/len(temp), '平均值'+str(round(sum(temp)/len(temp), 3)), fontsize=20)
            # 绘制指标要求上下限
            ax1.axhline(zhibiao[0], color='g')
            ax1.text(sheet_data.nrows+22, zhibiao[0], '指标上限'+str(zhibiao[0]), fontsize=20)
            ax1.axhline(zhibiao[1], color='g')
            ax1.text(sheet_data.nrows+22, zhibiao[1], '指标下限'+str(zhibiao[1]), fontsize=20)
            # 绘制包络线
            ax1.axhline(sum(temp)/len(temp)+3*std(temp), color='b')
            ax1.text(sheet_data.nrows+22, sum(temp)/len(temp)+3*std(temp), '包络上限'+ \
                     str(round(sum(temp)/len(temp)+3*std(temp), 3)), fontsize=20)
            ax1.axhline(sum(temp)/len(temp)-3*std(temp), color='b')
            ax1.text(sheet_data.nrows+22, sum(temp)/len(temp)-3*std(temp), '包络下限'+ \
                     str(round(sum(temp)/len(temp)-3*std(temp), 3)), fontsize=20)
            plt.title(datat[i][0]+'的成功数据包络图', fontsize=30)
            plt.xlabel('产品序号', fontsize=20)
            plt.ylabel(datat[i][0], fontsize=20)
            ax1.grid(linestyle='--')
            plt.savefig(datat[i][0]+'.png')
        LoadDataFrame.Destroy(self)