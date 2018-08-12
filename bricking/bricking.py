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
        self.tableView.setGeometry(QtCore.QRect(110, 260, 470, 240))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView_table = QtGui.QTableView(Form)
        self.tableView_table.setGeometry(QtCore.QRect(110, 75, 470, 150))
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
        self.label_10.setGeometry(QtCore.QRect(30, 240, 72, 15))
        self.label_10.setObjectName(_fromUtf8("label_10"))

        self.label_12 = QtGui.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(30, 60, 72, 15))
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
        self.error_count = 0
        self.onProcess = 0
        self.load_ok = 0
        self.model = QtGui.QStandardItemModel(self.tableView)
        self.model.setRowCount(100)
        self.model.setColumnCount(1)
        self.model.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"日志"))
        self.tableView.setModel(self.model) 
        self.tableView.setColumnWidth(0,415)
        self.model_table = QtGui.QStandardItemModel(self.tableView_table)
        self.model_table.setRowCount(100)
        self.model_table.setColumnCount(6)
        self.model_table.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"合约"))
        self.model_table.setHeaderData(1,QtCore.Qt.Horizontal,_fromUtf8(u"账户余额"))
        self.model_table.setHeaderData(2,QtCore.Qt.Horizontal,_fromUtf8(u"实际持仓"))
        self.model_table.setHeaderData(4,QtCore.Qt.Horizontal,_fromUtf8(u"下单量比例"))
        self.model_table.setHeaderData(3,QtCore.Qt.Horizontal,_fromUtf8(u"中间价"))
        self.model_table.setHeaderData(5,QtCore.Qt.Horizontal,_fromUtf8(u"最小价差"))
        self.tableView_table.setModel(self.model_table) 
        self.tableView_table.setColumnWidth(0,70)
        self.tableView_table.setColumnWidth(1,70)
        self.tableView_table.setColumnWidth(2,70)
        self.tableView_table.setColumnWidth(3,70)
        self.tableView_table.setColumnWidth(4,70)
        self.tableView_table.setColumnWidth(5,70)

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
                self.balance_list = []
                self.mid_p_list = []
                self.bid_p_list = []
                self.ask_p_list = []
                buyable_list = []
                sellable_list = []
                for j in range(len(self.contract_list)):
                    api = self.api_list[j]
                    contract = self.contract_list[j]
                    temp_t = api.fetch_order_book(contract)
                    self.model_table.setItem(j, 3, QtGui.QStandardItem('%s'%((float(temp_t['bids'][0][0])+float(temp_t['asks'][0][0]))/2)))
                    Pos = api.fetch_balance()
                    holding_now = Pos[contract.split('/')[0]]['total']
                    balance_now = Pos[contract.split('/')[1]]['total']
                    self.model_table.setItem(j, 1, QtGui.QStandardItem('%s'%(holding_now)))
                    self.holding_list.append(holding_now)
                    self.balance_list.append(balance_now)
                    self.mid_p_list.append((float(temp_t['bids'][0][0])+float(temp_t['asks'][0][0]))/2)
                    self.bid_p_list.append(float(temp_t['bids'][0][0]))
                    self.ask_p_list.append(float(temp_t['asks'][0][0]))
                    #可买可卖列表
                    if holding_now > self.AMOUNT_list[j]:
                        sellable_list.append(1)
                    else:
                        sellable_list.append(0)
                    if balance_now/(float(temp_t['asks'][0][0])+self.slide_list[j]) > self.AMOUNT_list[j]:
                        buyable_list.append(1)
                    else:
                        buyable_list.append(0)

                self.tableView_table.setModel(self.model_table) 
    


                #检验是否需要下单
                buy_num = -1
                sell_num = -1
                revenue = 0
                for num_1 in range(len(self.contract_list)):
                    if sellable_list[num_1] > 0:
                        sell_price = self.bid_p_list[num_1] - self.slide_list[num_1]
                        for num_2 in range(len(self.contract_list)):
                            if buyable_list[num_2] > 0:
                                buy_price = self.ask_p_list[num_2] + self.slide_list[num_2]
                                spread = sell_price - buy_price
                                if spread > revenue:
                                    revenue = spread
                                    sell_num = num_1
                                    buy_num = num_2
                if revenue > max(self.min_spread[sell_num],self.min_spread[buy_num]):
                       try:
                            order_1 = self.api_list[buy_num].create_limit_buy_order(self.contract_list[buy_num], self.AMOUNT_list[buy_num], self.bid_p_list[buy_num] + self.slide_list[buy_num])
                            self.model.setItem(self.row_count, 0, QtGui.QStandardItem("下单：%s  买单  %s"%(self.contract_list[buy_num],self.bid_p_list[buy_num] + self.slide_list[buy_num])))
                            self.row_count += 1
                            self.tableView.setModel(self.model)
                        except:
                            self.model.setItem(self.row_count, 0, QtGui.QStandardItem("下单失败：%s  买单  %s"%(self.contract_list[buy_num],self.bid_p_list[buy_num] + self.slide_list[buy_num])))
                            self.row_count += 1

                            self.tableView.setModel(self.model)
                       try:
                            order_2 = self.api_list[sell_num].create_limit_sell_order(self.contract_list[sell_num], self.AMOUNT_list[sell_num], self.bid_p_list[sell_num] + self.slide_list[sell_num])                            

                            self.model.setItem(self.row_count, 0, QtGui.QStandardItem("下单：%s  卖单  %s"%(self.contract_list[sell_num],self.bid_p_list[sell_num] + self.slide_list[sell_num])))
                            self.row_count += 1
                            self.tableView.setModel(self.model)
                        except:

                            self.model.setItem(self.row_count, 0, QtGui.QStandardItem("下单失败：%s  卖单  %s"%(self.contract_list[sell_num],self.bid_p_list[sell_num] + self.slide_list[sell_num])))
                            self.row_count += 1
                            self.tableView.setModel(self.model)    
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem("执行正常"))
                self.tableView.setModel(self.model) 
            except:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem("查询失败"))
                self.tableView.setModel(self.model) 
                if self.error_count<10:
                        self.error_count += 1
                else:
                    with open(r'connect.json','r') as load_f:
                        load_dict = json.load(load_f)
                    exec("self.api = ccxt."+self.exchange+"({'apiKey': load_dict['apiKey'],'secret': load_dict['secret'],})")


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
        path = r'config_table.xlsx'
        df_table = pd.read_excel(path)
        df_table.index = df_table['exchange']
        self.aiming_ratio_list = []
        self.AMOUNT_list = []
        self.slide_list = []
        self.contract_list = []
        self.min_spread = []
        try:
            for exchange in self.exchange_list:
                self.AMOUNT_list.append(df_table['amount'][exchange])
                self.slide_list.append(df_table['slide_point'][exchange])
                self.min_spread.append(df_table['min_spread'][exchange])
        except:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"载入配置表失败"))
                self.row_count += 1  

        #表与登录信息对应

        for i in range(len(self.aiming_ratio_list)):

            self.model_table.setItem(i, 0, QtGui.QStandardItem('%s'%self.exchange_list[i]))
            self.model_table.setItem(i, 4, QtGui.QStandardItem('%s'%self.AMOUNT_list[i]))
            self.model_table.setItem(i, 5, QtGui.QStandardItem('%s'%self.slide_list[i]))
            self.model_table.setItem(i, 6, QtGui.QStandardItem('%s'%self.slide_list[i]))


        self.tableView_table.setModel(self.model_table) 

        if self.login_ok == 1:
            if self.onProcess == 0:
                try:
                    self.holding_list = []
                    self.mid_p_list = []
                    self.precision_list = []
                    self.amount_limit_list = []
                    self.balance_list = []
                    for j in range(len(self.contract_list)):
                        temp_t = self.api_list[j].fetch_order_book(self.contract_list[j])
                        self.model_table.setItem(j, 3, QtGui.QStandardItem('%s'%((float(temp_t['bids'][0][0])+float(temp_t['asks'][0][0]))/2)))
                        Pos = self.api_list[j].fetch_balance()
                        holding_now = Pos[self.contract_list[j].split('/')[0]]['total']
                        balance_now = Pos[self.contract_list[j].split('/')[1]]['total']
                        self.model_table.setItem(j, 1, QtGui.QStandardItem('%s'%(holding_now)))
                        self.model_table.setItem(j, 2, QtGui.QStandardItem('%s'%(balance_now)))
                        self.holding_list.append(holding_now)
                        self.balance_list.append(holding_now)
                        self.mid_p_list.append((float(temp_t['bids'][0][0])+float(temp_t['asks'][0][0]))/2)
                        content = self.api_list[j].market(self.contract_list[j])
                        precision = content['precision']
                        self.amount_limit_list.append(content['limits']['amount'])
                        self.slide_list[j] = np.ceil(self.slide_list[j])/10**precision['price']
                        self.precision_list.append(precision['amount'])
                        if self.AMOUNT_list[j] > self.amount_limit_list[j]['max'] or self.AMOUNT_list[j] < self.amount_limit_list[j]['min']:
                            self.model.setItem(self.row_count, 0, QtGui.QStandardItem("下单量不符合规范，请重新设置"))
                            self.row_count += 1
                            return  
                    self.tableView_table.setModel(self.model_table) 
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
            with open(r'connect_bricking.json','r') as load_f:
                load_dict = json.load(load_f)                
            self.api_list = []
            self.contract_list = []
            self.exchange_list = []
            for connect in load_dict['info']:
                exec("self.api_list.append(ccxt."+connect['exchange']+"({'apiKey': connect['apiKey'],'secret': connect['secret'],}))")
                self.contract_list.append(connect['contract'])
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