# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gridtrading2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui
import ccxt
import time
import datetime
import scipy
import numpy as np
from threading import Timer
import threading
from PyQt4.QtCore import QTimer
import json
import pandas as pd

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setFixedSize(638, 530)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        Form.setFont(font)
        Form.setMouseTracking(False)
        Form.setAcceptDrops(True)
        self.pushButton_begin = QtGui.QPushButton(Form)
        self.pushButton_begin.setGeometry(QtCore.QRect(240, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_begin.setFont(font)
        self.pushButton_begin.setObjectName(_fromUtf8("pushButton_begin"))

        self.tableView = QtGui.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(110, 260, 421, 240))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView_table = QtGui.QTableView(Form)
        self.tableView_table.setGeometry(QtCore.QRect(110, 75, 421, 150))
        self.tableView_table.setObjectName(_fromUtf8("tableView_table"))

        self.pushButton_stop = QtGui.QPushButton(Form)
        self.pushButton_stop.setGeometry(QtCore.QRect(360, 0, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName(_fromUtf8("pushButton_stop"))
        self.pushButton_downLoadTrading = QtGui.QPushButton(Form)
        self.pushButton_downLoadTrading.setGeometry(QtCore.QRect(500, 0, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_downLoadTrading.setFont(font)
        self.pushButton_downLoadTrading.setObjectName(_fromUtf8("pushButton_downLoadTrading"))
        self.pushButton_login = QtGui.QPushButton(Form)
        self.pushButton_login.setGeometry(QtCore.QRect(0, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setCheckable(False)
        self.pushButton_login.setObjectName(_fromUtf8("pushButton_login"))
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(20, 255, 72, 15))
        self.label_10.setObjectName(_fromUtf8("label_10"))

        self.label_12 = QtGui.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(20, 60, 72, 15))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.pushButton_loadtable = QtGui.QPushButton(Form)
        self.pushButton_loadtable.setGeometry(QtCore.QRect(120, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_loadtable.setFont(font)
        self.pushButton_loadtable.setCheckable(False)
        self.pushButton_loadtable.setObjectName(_fromUtf8("pushButton_loadtable"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_begin, QtCore.SIGNAL(_fromUtf8("clicked()")), self.begin)
        QtCore.QObject.connect(self.pushButton_login, QtCore.SIGNAL(_fromUtf8("clicked()")), self.login)
        QtCore.QObject.connect(self.pushButton_stop, QtCore.SIGNAL(_fromUtf8("clicked()")), self.stop)
        QtCore.QObject.connect(self.pushButton_downLoadTrading, QtCore.SIGNAL(_fromUtf8("clicked()")), self.download)
        QtCore.QObject.connect(self.pushButton_loadtable, QtCore.SIGNAL(_fromUtf8("clicked()")), self.loadtable)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "币值平衡策略", None))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.pushButton_begin.setText(_translate("Form", "开始执行", None))
        self.pushButton_stop.setText(_translate("Form", "中止执行", None))
        self.pushButton_downLoadTrading.setText(_translate("Form", "成交记录导出", None))
        self.pushButton_login.setText(_translate("Form", "账户登录", None))
        self.label_10.setText(_translate("Form", "策略日志", None))
        self.label_12.setText(_translate("Form", "平衡表", None))
        self.pushButton_loadtable.setText(_translate("Form", "载入平衡表", None))

        self.timer = QTimer(Form)
        self.timer.timeout.connect(self.unit_work)
        self.row_count = 0
        self.login_ok = 0
        self.onProcess = 0
        self.load_ok = 0
        self.model = QtGui.QStandardItemModel(self.tableView)
        self.model.setRowCount(100)
        self.model.setColumnCount(1)
        self.model.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"日志"))
        self.tableView.setModel(self.model) 
        self.tableView.setColumnWidth(0,365)
        self.model_table = QtGui.QStandardItemModel(self.tableView_table)
        self.model_table.setRowCount(100)
        self.model_table.setColumnCount(5)
        self.model_table.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"合约"))
        self.model_table.setHeaderData(1,QtCore.Qt.Horizontal,_fromUtf8(u"目标权重"))
        self.model_table.setHeaderData(2,QtCore.Qt.Horizontal,_fromUtf8(u"实际持仓"))
        self.model_table.setHeaderData(4,QtCore.Qt.Horizontal,_fromUtf8(u"下单量比例"))
        self.model_table.setHeaderData(3,QtCore.Qt.Horizontal,_fromUtf8(u"中间价"))
        self.tableView_table.setModel(self.model_table) 
        self.tableView_table.setColumnWidth(0,60)
        self.tableView_table.setColumnWidth(1,70)
        self.tableView_table.setColumnWidth(2,90)
        self.tableView_table.setColumnWidth(3,80)
        self.tableView_table.setColumnWidth(4,60)

    def begin(self):

        if self.login_ok == 1:
            if self.load_ok == 1:
                today = datetime.date.today()
                self.since = self.api_list[0].parse8601('%sT00:00:00.0000' %today.isoformat())
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem("开始执行"))
                self.row_count += 1
                self.tableView.setModel(self.model) 
                if self.onProcess == 1:
                    self.model.setItem(self.row_count, 0, QtGui.QStandardItem("正在执行"))
                    self.row_count += 1
                    self.tableView.setModel(self.model)                 
                self.onProcess = 1
                self.unit_work()
            else:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem("尚未载入平衡表"))
                self.row_count += 1
                self.tableView.setModel(self.model)                

        else:
            self.model.setItem(self.row_count, 0, QtGui.QStandardItem("尚未登录"))
            self.row_count += 1
            self.tableView.setModel(self.model)
            
    def unit_work(self):
        if self.onProcess == 1:
            try:
                #查询持仓
                self.holding_list = []
                self.mid_p_list = []
                self.bid_p_list = []
                self.ask_p_list = []
                for j in range(len(self.contract_list)):
                    api = self.api_list[j]
                    contract = self.contract_list[j]
                    if j > 0:                    
                        temp_t = api.fetch_order_book(contract)
                        self.model_table.setItem(j, 3, QtGui.QStandardItem('%s'%((float(temp_t['bids'][0][0])+float(temp_t['asks'][0][0]))/2)))
                        Pos = api.fetch_balance()[contract.split('/')[0]]
                        holding_now = Pos['total']
                        self.model_table.setItem(j, 2, QtGui.QStandardItem('%s'%(holding_now)))
                        self.holding_list.append(holding_now)
                        self.mid_p_list.append((float(temp_t['bids'][0][0])+float(temp_t['asks'][0][0]))/2)
                        self.bid_p_list.append(float(temp_t['bids'][0][0]))
                        self.ask_p_list.append(float(temp_t['bids'][0][0]))
                    else:
                        Pos = api.fetch_balance()[contract.split('/')[0]]
                        holding_now = Pos['total']
                        self.model_table.setItem(j, 2, QtGui.QStandardItem('%s'%(holding_now)))
                        Pos_base_currency = api.fetch_balance()[contract.split('/')[0]]['total']
                self.tableView_table.setModel(self.model_table) 
    
    
                #检验是否需要下单
                total_value = Pos_base_currency + sum([self.holding_list[j] * self.mid_p_list[j] for j in range(len(self.holding_list))])
                for j in range(len(self.contract_list)):
                    if j > 0:
                        if ((self.holding_list[j - 1] * self.mid_p_list[j - 1])/total_value) > self.aiming_ratio_list[j]:
                            if ((self.holding_list[j-1] - self.AMOUNT_list[j]) * (self.bid_p_list[j-1] - self.slide_list[j])/total_value)> self.aiming_ratio_list[j]:
                                try:
                                    order_1 = self.api_list[j].create_limit_sell_order(self.contract_list[j], self.AMOUNT_list[j], self.bid_p_list[j-1] - self.slide_list[j])
                                    self.model.setItem(self.row_count, 0, QtGui.QStandardItem("下单：%s  卖单  %s"%(self.contract_list[j],self.bid_p_list[j-1] - self.slide_list[j])))
                                    self.row_count += 1
                                    self.tableView.setModel(self.model)
                                except:
                                    pass
    
                        else:
                            if ((self.holding_list[j-1] + self.AMOUNT_list[j]) * (self.bid_p_list[j-1] + self.slide_list[j])/total_value) < self.aiming_ratio_list[j]:
                                try:
                                    order_1 = self.api_list[j].create_limit_buy_order(self.contract_list[j], self.AMOUNT_list[j], self.bid_p_list[j-1] + self.slide_list[j])
                                    self.model.setItem(self.row_count, 0, QtGui.QStandardItem("下单：%s  买单  %s"%(self.contract_list[j],self.bid_p_list[j-1] + self.slide_list[j])))
                                    self.row_count += 1
                                    self.tableView.setModel(self.model)
                                except:
                                    pass
    
    
    
    
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem("执行正常"))
                self.tableView.setModel(self.model) 
            except:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem("查询失败"))
                self.row_count += 1
                self.tableView.setModel(self.model) 

            today = datetime.date.today()
            since = self.api_list[0].parse8601('%sT00:00:00.0000' %today.isoformat()) - 100000000
            for j in range(len(self.contract_list)):
                contract = self.contract_list[j]
                #全撤
                try:
                    all_orders = self.bitmex.fetchOrders(contract,since,500)
                    all_working_orders_id = [x['id'] for x in all_orders if x['status']=='open']
                    for id in all_working_orders_id:
                        self.bitmex.cancelOrder(id)
                except:
                    pass

            if self.onProcess == 1:

                self.timer.start(20000)



    def loadtable(self):
        path = r'balance_table.xlsx'
        df_table = pd.read_excel(path)
        df_table.index = df_table['coin']
        self.aiming_ratio_list = []
        self.AMOUNT_list = []
        self.slide_list = []
        self.contract_list = []
        try:
            for coin in self.coin_list:
                self.aiming_ratio_list.append(df_table['aiming'][coin])
                self.AMOUNT_list.append(df_table['amount'][coin])
                self.slide_list.append(df_table['slide_point'][coin])
                self.contract_list.append(coin+'/'+self.coin_list[0])
        except:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"载入平衡表失败"))
                self.row_count += 1  

        #表与登录信息对应

        for i in range(len(self.aiming_ratio_list)):

            self.model_table.setItem(i, 0, QtGui.QStandardItem('%s'%self.coin_list[i]))
            self.model_table.setItem(i, 1, QtGui.QStandardItem('%s'%self.aiming_ratio_list[i]))
            self.model_table.setItem(i, 4, QtGui.QStandardItem('%s'%self.AMOUNT_list[i]))

        self.tableView_table.setModel(self.model_table) 

        if self.login_ok == 1:
            if self.onProcess == 0:
                try:
                    self.holding_list = []
                    self.mid_p_list = []
                    self.precision_list = []
                    self.amount_limit_list = []
                    for j in range(len(self.coin_list)):
                        coin = self.coin_list[j]
                        if j == 0:
                            self.model_table.setItem(j, 3, QtGui.QStandardItem('-'))
                            self.model_table.setItem(j, 4, QtGui.QStandardItem('-'))
                            Pos = self.api_list[j].fetch_balance()[coin]
                            holding_now = Pos['total']
                            self.model_table.setItem(j, 2, QtGui.QStandardItem('%s'%(holding_now)))
                            Pos_base_currency = holding_now
                        else:
                            temp_t = self.api_list[j].fetch_order_book(coin+'/'+self.coin_list[0])
                            self.model_table.setItem(j, 3, QtGui.QStandardItem('%s'%((float(temp_t['bids'][0][0])+float(temp_t['asks'][0][0]))/2)))
                            Pos = self.api_list[j].fetch_balance()[coin]
                            holding_now = Pos['total']
                            self.model_table.setItem(j, 2, QtGui.QStandardItem('%s'%(holding_now)))
                            self.holding_list.append(holding_now)
                            self.mid_p_list.append((float(temp_t['bids'][0][0])+float(temp_t['asks'][0][0]))/2)
                            content = self.api_list[j].market(coin+'/'+self.coin_list[0])
                            precision = content['precision']
                            self.amount_limit_list.append(content['limits']['amount'])
                            self.slide_list[j] = np.ceil(self.slide_list[j])/10**precision['price']
                            self.precision_list.append(precision['amount'])
                    self.tableView_table.setModel(self.model_table) 
                    total_value = Pos_base_currency + sum([self.holding_list[j] * self.mid_p_list[j] for j in range(len(self.holding_list))])
                    for j in range(len(self.coin_list)):
                        if j > 0:
                            self.AMOUNT_list[j] = min(max(round(total_value/self.mid_p_list[j-1]*self.aiming_ratio_list[j]* self.AMOUNT_list[j],self.precision_list[j - 1]),self.amount_limit_list[j - 1]['min']),self.amount_limit_list[j - 1]['max'])
                    self.load_ok = 1 
                except:
                    self.model.setItem(self.row_count, 0, QtGui.QStandardItem("查询失败"))
                    self.row_count += 1  
            else:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem("策略执行中，请先中止执行"))
                self.row_count += 1                
        else:
            self.model.setItem(self.row_count, 0, QtGui.QStandardItem("尚未登录"))
            self.row_count += 1
        self.tableView.setModel(self.model)


    def login(self):
        if self.login_ok == 0:
            with open(r'connect_balance.json','r') as load_f:
                load_dict = json.load(load_f)                
            self.api_list = []
            self.coin_list = []
            self.exchange_list = []
            for connect in load_dict['info']:
                exec("self.api_list.append(ccxt."+connect['exchange']+"({'apiKey': connect['apiKey'],'secret': connect['secret'],}))")
                self.coin_list.append(connect['coin'])
                self.exchange_list.append(connect['exchange'])
                
            try:
                balance_list = []
                for i in range(len(self.api_list)):
                    balace_temp = self.api_list[i].fetch_balance()[self.coin_list[i]]
                    balance_list.append(balace_temp['free'])
                    #显示各个账户余额
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"登录成功"))
                self.row_count += 1
                self.login_ok = 1
            except:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"登录失败"))
                self.row_count += 1
        else:
            self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"已经登录"))
            self.row_count += 1

    def stop(self):
        self.onProcess = 0
        self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"执行中止"))
        self.row_count += 1
        self.tableView.setModel(self.model)


    def cancelall(self):
        if self.login_ok == 1:
            if self.load_ok == 1:
                today = datetime.date.today()
                since = self.bitmex.parse8601('%sT00:00:00.0000' %today.isoformat()) - 100000000
                for j in range(len(self.contract_list)):
                    if j > 0 :
                        contract = self.contract_list[j]
                        if j > 0 :
                            #全撤
                            try:
                                all_orders = self.api_list[j].fetchOrders(contract,since,500)
                                all_working_orders_id = [x['id'] for x in all_orders if x['status']=='open']
                                for id in all_working_orders_id:
                                    self.bitmex.cancelOrder(id)
                            except:
                                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"撤单失败"))
            else:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"尚未导入平衡表"))
                self.row_count += 1              
        else:        
            self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"尚未登录"))
            self.row_count += 1

        self.tableView.setModel(self.model) 
    def download(self):
        if self.login_ok == 1:
            today = datetime.date.today()
            since = self.api_list[0].parse8601('%sT00:00:00.0000' %today.isoformat()) - 100000000
            try:
                trading_recode_all = pd.DataFrame()
                for j in range(len(self.contract_list)-1):
                    all_orders = self.api_list[0].fetchOrders(self.contract_list[j+1],since,500)
                    trading_recode = pd.DataFrame()
                    trading_recode['trade_time'] = [x['datetime'] for x in all_orders if x['info']['state'] in ['filled','partially filled']]
                    trading_recode['order_price'] = [x['price'] for x in all_orders  if x['info']['state'] in ['filled','partially filled']]
                    trading_recode['trade_price'] = [x['info']['price'] for x in all_orders if x['info']['state'] in ['filled','partially filled']]
                    trading_recode['trade_amount'] = [x['filled'] for x in all_orders if x['info']['state'] in ['filled','partially filled']]
                    trading_recode['side'] = [x['side'] for x in all_orders if x['info']['state'] in ['filled','partially filled']]
                    trading_recode['symbol'] = [x['symbol'] for x in all_orders if x['info']['state'] in ['filled','partially filled']]
                    trading_recode_all.append(trading_recode)
                trading_recode_all.to_csv('trade_recording_balance.csv')
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"导出成功"))
                self.row_count += 1
                self.tableView.setModel(self.model) 
            except:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"导出失败"))
                self.row_count += 1
                self.tableView.setModel(self.model) 
        else:
            self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"尚未登录"))
            self.row_count += 1
            self.tableView.setModel(self.model)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())