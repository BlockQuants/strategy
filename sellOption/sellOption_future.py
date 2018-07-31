# -*- coding: utf-8 -*-

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
from generate_orderBook import orderBook_generator
import pandas as pd
import json

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
        Form.setFixedSize(650, 600)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        Form.setFont(font)
        Form.setMouseTracking(False)
        Form.setAcceptDrops(True)

        self.tableView = QtGui.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(280, 60, 350, 480))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.verticalHeader().setVisible(False)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 81, 81, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit_contract = QtGui.QTextEdit(Form)
        self.textEdit_contract.setGeometry(QtCore.QRect(140, 84, 91, 30))
        self.textEdit_contract.setObjectName(_fromUtf8("textEdit_contract"))
        self.label_exchange = QtGui.QLabel(Form)
        self.label_exchange.setGeometry(QtCore.QRect(40, 50, 81, 31))
        self.label.setObjectName(_fromUtf8("label_exchange"))
        self.textEdit_exchange = QtGui.QTextEdit(Form)
        self.textEdit_exchange.setGeometry(QtCore.QRect(140, 48, 91, 30))
        self.textEdit_exchange.setObjectName(_fromUtf8("textEdit_exchange"))


        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 275, 231, 310))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_type = QtGui.QLabel(self.groupBox)
        self.label_type.setGeometry(QtCore.QRect(10, 40, 72, 15))
        self.label_type.setObjectName(_fromUtf8("label_type"))
        self.label_amount = QtGui.QLabel(self.groupBox)
        self.label_amount.setGeometry(QtCore.QRect(10, 80, 72, 15))
        self.label_amount.setObjectName(_fromUtf8("label_amount"))
        self.label_K = QtGui.QLabel(self.groupBox)
        self.label_K.setGeometry(QtCore.QRect(10, 120, 72, 15))
        self.label_K.setObjectName(_fromUtf8("label_K"))
        self.label_vol = QtGui.QLabel(self.groupBox)
        self.label_vol.setGeometry(QtCore.QRect(10, 200, 72, 15))
        self.label_vol.setObjectName(_fromUtf8("label_vol"))
        self.label_exp = QtGui.QLabel(self.groupBox)
        self.label_exp.setGeometry(QtCore.QRect(10, 150, 72, 40))
        self.label_exp.setObjectName(_fromUtf8("label_exp"))
        self.label_tick = QtGui.QLabel(self.groupBox)
        self.label_tick.setGeometry(QtCore.QRect(10, 240, 72, 15))
        self.label_tick.setObjectName(_fromUtf8("label_tick"))

        self.comboBox_type = QtGui.QComboBox(self.groupBox)
        self.comboBox_type.setGeometry(QtCore.QRect(110, 30, 91, 31))
        self.comboBox_type.addItem(u'看跌期权')
        self.comboBox_type.addItem(u'看涨期权')
        self.textEdit_vol = QtGui.QTextEdit(self.groupBox)
        self.textEdit_vol.setGeometry(QtCore.QRect(110, 190, 91, 31))
        self.textEdit_vol.setObjectName(_fromUtf8("textEdit_vol"))
        self.textEdit_exp = QtGui.QTextEdit(self.groupBox)
        self.textEdit_exp.setGeometry(QtCore.QRect(110, 150, 91, 31))
        self.textEdit_exp.setObjectName(_fromUtf8("textEdit_exp"))
        self.textEdit_K = QtGui.QTextEdit(self.groupBox)
        self.textEdit_K.setGeometry(QtCore.QRect(110, 110, 91, 31))
        self.textEdit_K.setObjectName(_fromUtf8("textEdit_K"))
        self.textEdit_amount = QtGui.QTextEdit(self.groupBox)
        self.textEdit_amount.setGeometry(QtCore.QRect(110, 70, 91, 31))
        self.textEdit_amount.setObjectName(_fromUtf8("textEdit_amount"))
        self.textEdit_tick = QtGui.QTextEdit(self.groupBox)
        self.textEdit_tick.setGeometry(QtCore.QRect(110, 230, 91, 31))
        self.textEdit_tick.setObjectName(_fromUtf8("textEdit_tick"))

        self.groupBox_monitor = QtGui.QGroupBox(Form)
        self.groupBox_monitor.setGeometry(QtCore.QRect(30, 120, 231, 141))
        self.groupBox_monitor.setObjectName(_fromUtf8("groupBox_monitor"))
        self.textBrowser_price = QtGui.QTextBrowser(self.groupBox_monitor)
        self.textBrowser_price.setEnabled(False)
        self.textBrowser_price.setGeometry(QtCore.QRect(90, 20, 111, 31))
        self.textBrowser_price.setObjectName(_fromUtf8("textBrowser_price"))
        self.label_price = QtGui.QLabel(self.groupBox_monitor)
        self.label_price.setGeometry(QtCore.QRect(20, 30, 72, 15))
        self.label_price.setObjectName(_fromUtf8("label_price"))
        self.label_position = QtGui.QLabel(self.groupBox_monitor)
        self.label_position.setGeometry(QtCore.QRect(20, 70, 72, 15))
        self.label_position.setObjectName(_fromUtf8("label_position"))
        self.label_balance = QtGui.QLabel(self.groupBox_monitor)
        self.label_balance.setGeometry(QtCore.QRect(20, 110, 72, 15))
        self.label_balance.setObjectName(_fromUtf8("label_balance"))
        self.textBrowser_account = QtGui.QTextBrowser(self.groupBox_monitor)
        self.textBrowser_account.setEnabled(False)
        self.textBrowser_account.setGeometry(QtCore.QRect(90, 100, 111, 31))
        self.textBrowser_account.setObjectName(_fromUtf8("textBrowser_account"))
        self.textBrowser_position = QtGui.QTextBrowser(self.groupBox_monitor)
        self.textBrowser_position.setEnabled(False)
        self.textBrowser_position.setGeometry(QtCore.QRect(90, 60, 111, 31))
        self.textBrowser_position.setObjectName(_fromUtf8("textBrowser_position"))


        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_begin = QtGui.QPushButton(Form)
        self.pushButton_begin.setGeometry(QtCore.QRect(130, 0, 130, 40))
        self.pushButton_begin.setFont(font)
        self.pushButton_begin.setObjectName(_fromUtf8("pushButton_begin"))
        self.pushButton_cancelall = QtGui.QPushButton(Form)
        self.pushButton_cancelall.setGeometry(QtCore.QRect(390, 0, 130, 40))
        self.pushButton_cancelall.setFont(font)
        self.pushButton_cancelall.setObjectName(_fromUtf8("pushButton_cancelall"))
        self.pushButton_downLoadTrading = QtGui.QPushButton(Form)
        self.pushButton_downLoadTrading.setGeometry(QtCore.QRect(520, 0, 130, 40))
        self.pushButton_downLoadTrading.setFont(font)
        self.pushButton_downLoadTrading.setObjectName(_fromUtf8("pushButton_downLoadTrading"))
        self.pushButton_generatable = QtGui.QPushButton(self.groupBox)
        self.pushButton_generatable.setGeometry(QtCore.QRect(60, 270, 93, 28))
        self.pushButton_generatable.setObjectName(_fromUtf8("pushButton_generatable"))
        self.pushButton_generatable.setObjectName(_fromUtf8("pushButton_generatable"))
        self.pushButton_login = QtGui.QPushButton(Form)
        self.pushButton_login.setGeometry(QtCore.QRect(0, 0, 130, 40))
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName(_fromUtf8("pushButton_login"))
        self.pushButton_stop = QtGui.QPushButton(Form)
        self.pushButton_stop.setGeometry(QtCore.QRect(260, 0, 130, 40))
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName(_fromUtf8("pushButton_stop"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_begin, QtCore.SIGNAL(_fromUtf8("clicked()")), self.begin)
        QtCore.QObject.connect(self.pushButton_generatable, QtCore.SIGNAL(_fromUtf8("clicked()")), self.setPara)
        QtCore.QObject.connect(self.pushButton_login, QtCore.SIGNAL(_fromUtf8("clicked()")), self.login)
        QtCore.QObject.connect(self.pushButton_stop, QtCore.SIGNAL(_fromUtf8("clicked()")), self.stop)
        QtCore.QObject.connect(self.pushButton_cancelall, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cancelall)
        QtCore.QObject.connect(self.pushButton_downLoadTrading, QtCore.SIGNAL(_fromUtf8("clicked()")), self.download)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "动态对冲复制卖出期权策略(期货版)", None))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.pushButton_begin.setText(_translate("Form", "开始执行", None))
        self.pushButton_generatable.setText(_translate("Form", "设定参数", None))
        self.pushButton_stop.setText(_translate("Form", "中止执行", None))
        self.pushButton_cancelall.setText(_translate("Form", "全部撤单", None))
        self.pushButton_login.setText(_translate("Form", "账户登录", None))
        self.pushButton_downLoadTrading.setText(_translate("Form", "成交记录导出", None))
        self.groupBox.setTitle(_translate("Form", "策略参数", None))
        self.label.setText(_translate("Form", "合约代码", None))

        self.label_exchange.setText(_translate("Form", "交易所", None))
        self.label_amount.setText(_translate("Form", "合约数量", None))
        self.label_K.setText(_translate("Form", "执行价格", None))
        self.label_vol.setText(_translate("Form", "波动率", None))
        self.label_type.setText(_translate("Form", "期权类型", None))
        self.label_exp.setText(_translate("Form", "距到期时\n间（年）", None))
        self.label_tick.setText(_translate("Form", "挂单间隔", None))
        self.label_price.setText(_translate("Form", "当前价", None))
        self.label_position.setText(_translate("Form", "持仓", None))
        self.label_balance.setText(_translate("Form", "账户余额", None))

        self.textEdit_vol.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.4</p></body></html>", None))
        self.textEdit_exp.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.textEdit_K.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10000</p></body></html>", None))
        self.textEdit_amount.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1000</p></body></html>", None))

        self.groupBox_monitor.setTitle(_translate("Form", "策略监控", None))
        self.textBrowser_price.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">0</span></p></body></html>", None))
        self.textBrowser_account.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">0</span></p></body></html>", None))
        self.textBrowser_position.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">0</span></p></body></html>", None))

        self.textEdit_tick.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">30</p></body></html>", None))
        self.timer = QTimer(Form)
        self.timer.timeout.connect(self.unit_work)
        self.row_count = 0
        self.login_ok = 0
        self.onProcess = 0
        self.model = QtGui.QStandardItemModel(self.tableView)
        self.model.setRowCount(100)
        self.model.setColumnCount(1)
        self.model.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"日志"))
        self.tableView.setModel(self.model) 
        self.tableView.setColumnWidth(0,328)
        self.setting_ok = 0


    def begin(self):
        if self.login_ok == 1:
            if self.generate_ok == 1:
                today = datetime.date.today()
                self.start_time = self.api.parse8601('%sT00:00:00.0000' %today.isoformat())
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"开始执行"))
                self.row_count += 1
                self.tableView.setModel(self.model) 
                if self.onProcess == 1:
                    self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"正在执行"))
                    self.row_count += 1
                    self.tableView.setModel(self.model)                 
                self.onProcess = 1
                self.unit_work()
            else:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"尚未生成挂单表"))
                self.row_count += 1
                self.tableView.setModel(self.model)                

        else:
            self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"尚未登录"))
            self.row_count += 1
            self.tableView.setModel(self.model)
            
    def unit_work(self):
        try:
            temp_t = self.api.fetch_order_book(self.contract)
            self.textBrowser_price.setText('%s'%((float(temp_t['bids'][0][0])+float(temp_t['asks'][0][0]))/2))
        except:
            pass
        if self.onProcess == 1:
            try:
                #查询持仓
                
                Pos = self.api.privateGetPosition()
                holding_now = np.floor([x[u'currentQty'] for x in Pos if x[u'symbol']==self.symbol][0]/self.AMOUNT)
                temp_h = holding_now*self.AMOUNT
                self.textBrowser_position.setText('%s'%temp_h)
                #获取应挂单
                if holding_now in self.holding_u:
                    bid_p = self.bid_price_u[self.holding_u == holding_now][0]
                    bid_a = self.bid_amount_u[self.holding_u == holding_now][0]
                    ask_p = self.ask_price_u[self.holding_u == holding_now][0]
                    ask_a = self.ask_amount_u[self.holding_u == holding_now][0]
                #检验是否需要下单
                all_orders = self.api.fetchOrders(self.contract,self.start_time)
                working_price = [x['price'] for x in all_orders if x['status'] == 'open']
                if len(all_orders) < 100:
                    if holding_now in self.holding_u:
                        if bid_p not in working_price:
                            try:
                                self.api.create_limit_buy_order(self.contract, bid_a, bid_p)
                                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(time.strftime("%m-%d %H:%M", time.localtime()) +u" 挂买单  价：%s 量：%s"%(bid_p,bid_a)))
                                self.row_count += 1
                                self.tableView.setModel(self.model)
                            except:
                                pass

                        if ask_p not in working_price:
                            try:
                                self.api.create_limit_sell_order(self.contract, ask_a, ask_p)
                                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(time.strftime("%m-%d %H:%M", time.localtime()) +u" 挂卖单  价：%s 量：%s"%(ask_p,ask_a)))
                                self.row_count += 1
                                self.tableView.setModel(self.model)

                            except:

                                pass
                    elif holding_now > max(self.holding_u):
                        try:
                            if self.ask_price_u[self.holding_u == max(self.holding_u)][0] not in working_price:
                                self.api.create_limit_sell_order(self.contract, holding_now - max(self.holding_u), self.ask_price_u[self.holding_u == max(self.holding_u)][0])
                                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(time.strftime("%m-%d %H:%M", time.localtime())+u"  挂卖单  价：%s 量：%s"%(self.ask_price_u[self.holding_u == max(self.holding_u)],holding_now - max(self.holding_u))))
                                self.row_count += 1
                        except:
                            pass

                    elif holding_now < min(self.holding_u):
                        try:
                            if self.bid_price_u[self.holding_u == max(self.holding_u)][0] not in working_price:
                                self.api.create_limit_buy_order(self.contract, min(self.holding_u) - holding_now, self.bid_price_u[self.holding_u == max(self.holding_u)][0])
                                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(time.strftime("%m-%d %H:%M", time.localtime()) +u" 挂买单  价：%s 量：%s"%(self.bid_price_u[self.holding_u == min(self.holding_u)],min(self.holding_u) - holding_now)))
                                self.row_count += 1
                        except:
                            pass
                    else:
                        bid_p = self.bid_price_u[self.holding_u == max(self.holding_u[self.holding_u<holding_now])][0]
                        bid_a = min(self.holding_u[self.holding_u>holding_now]) - self.holding_now
                        ask_p = self.ask_price_u[self.holding_u == min(self.holding_u[self.holding_u>holding_now])][0]
                        ask_a = max(self.holding_u[self.holding_u<holding_now]) - self.holding_now
                        if bid_p not in working_price:
                            try:
                                self.api.create_limit_buy_order(self.contract, bid_a, bid_p)
                                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(time.strftime("%m-%d %H:%M", time.localtime()) +u" 挂买单  价：%s 量：%s"%(bid_p,bid_a)))
                                self.row_count += 1
                                self.tableView.setModel(self.model)
                            except:
                                pass

                        if ask_p not in working_price:
                            try:
                                self.api.create_limit_sell_order(self.contract, ask_a, ask_p)
                                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(time.strftime("%m-%d %H:%M", time.localtime()) +u" 挂卖单  价：%s 量：%s"%(ask_p,ask_a)))
                                self.row_count += 1
                                self.tableView.setModel(self.model)

                            except:

                                pass

                else:
                    all_orders = self.api.fetchOrders(self.contract,500)
                    all_working_orders_id = [x['id'] for x in all_orders if x['status']=='open']
                    for id in all_working_orders_id:
                        self.api.cancelOrder(id)
                    self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"执行正常"))
                    self.tableView.setModel(self.model) 
            except:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"查询失败"))
                self.tableView.setModel(self.model) 
                if self.error_count<10:
                        self.error_count += 1
                else:
                    with open(r'connect.json','r') as load_f:
                        load_dict = json.load(load_f)
                    exec("self.api = ccxt."+self.exchange+"({'apiKey': load_dict['apiKey'],'secret': load_dict['secret'],})")
            if self.onProcess == 1:
                try:
                    balace_temp = self.api.fetch_balance()[self.contract.split('/')[0]]
                    self.textBrowser_account.setText(" %s"%balace_temp['total'])
                except:
                    pass    
                self.timer.start(20000)



    def download(self):
        if self.login_ok == 1:
            today = datetime.date.today()
            start_time = self.api.parse8601('%sT00:00:00.0000' %today.isoformat()) - 100000000
            try:
                all_orders = self.api.fetchOrders(self.contract,start_time,500)
                trading_recode = pd.DataFrame()
                trading_recode['trade_time'] = [x['info']['timestamp'] for x in all_orders if x['info']['ordStatus'] in ['Filled','Partially Filled']]
                trading_recode['order_time'] =  [x['info']['transactTime'] for x in all_orders if x['info']['ordStatus'] in ['Filled','Partially Filled']]
                trading_recode['order_price'] = [x['price'] for x in all_orders  if x['info']['ordStatus'] in ['Filled','Partially Filled']]
                trading_recode['trade_price'] = [x['info']['avgPx'] for x in all_orders if x['info']['ordStatus'] in ['Filled','Partially Filled']]
                trading_recode['trade_amount'] = [x['filled'] for x in all_orders if x['info']['ordStatus'] in ['Filled','Partially Filled']]
                trading_recode['side'] = [x['side'] for x in all_orders if x['info']['ordStatus'] in ['Filled','Partially Filled']]

                trading_recode.to_csv('trade_recording.csv')
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

    def setPara(self):
        
        EXP = float(self.textEdit_exp.toPlainText())
        K = float(self.textEdit_K.toPlainText())
        AMOUNT = int(self.textEdit_amount.toPlainText())
        VOL = float(self.textEdit_vol.toPlainText())
        TICK = float(self.textEdit_tick.toPlainText())
        TYPE = ['put','call'][self.comboBox_type.currentText()==u'看涨期权']
        INF_PRICE = 15000

        temp_generator = orderBook_generator()
        #挂单价格区间
        temp_generator.temp_price = K
        temp_generator.max_GrowthRate = 0.9
        temp_generator.tick1 = TICK

        #合约参数
        temp_generator.prime_rate = 0.03
        temp_generator.year2mature = EXP
        temp_generator.est_vol = VOL
        temp_generator.K = K
        temp_generator.amount = AMOUNT
        temp_generator.option_type = TYPE
        df = temp_generator.cal_original_table()
        self.holding_u = np.array(df['delta_ref'])

        self.bid_price_u = np.array(df['p_d']).reshape((-1,))
        self.ask_price_u = np.array(df['p_u']).reshape((-1,))
        self.bid_amount_u = np.array(df['p_d_amount']).reshape((-1,))
        self.ask_amount_u = np.array(df['p_u_amount']).reshape((-1,))
        self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"参数设定成功"))
        self.row_count += 1

        if self.login_ok == 1:
            if self.onProcess == 0:
                try:
                    temp_t = self.api.fetch_order_book(self.contract)
                    self.textBrowser_price.setText(u'%s'%((float(temp_t['bids'][0][0])+float(temp_t['asks'][0][0]))/2))
                    self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"买一价: %s  卖一价: %s"%(temp_t['bids'][0],temp_t['asks'][0]) ))
                    self.row_count += 1
                    Pos = self.api.privateGetPosition()
                    holding_now = np.floor([x[u'currentQty'] for x in Pos if x[u'symbol']==self.symbol][0])
                    self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"当前持仓： %s"%(holding_now) ))
                    self.row_count += 1
                    if holding_now in self.holding_u:
                        self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"准备下单： 买入价: %s  卖出价: %s"%(self.bid_price_u[self.holding_u == holding_now],self.ask_price_u[self.holding_u == holding_now])))
                        self.row_count += 1
                    elif holding_now > max(self.holding_u):
                        self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"准备下单： 卖出价: %s 卖出量： %s"%(self.ask_price_u[self.holding_u == max(self.holding_u)],holding_now - max(self.holding_u))))
                        self.row_count += 1
                    elif holding_now < min(self.holding_u):
                        self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"准备下单： 买入价: %s 买入量： %s"%(self.bid_price_u[self.holding_u == min(self.holding_u)],min(self.holding_u) - holding_now)))
                        self.row_count += 1
                    else:
                        self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"准备下单： 买入价: %s  卖出价: %s"%(self.bid_price_u[self.holding_u == max(self.holding_u[self.holding_u<holding_now])],self.ask_price_u[self.holding_u == min(self.holding_u[self.holding_u>holding_now])])))
                        self.row_count += 1
                except:
                    self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"查询失败"))
                    self.row_count += 1  
            else:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"策略执行中，请先中止执行"))
                self.row_count += 1                
        else:
            self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"尚未登录"))
            self.row_count += 1
        self.tableView.setModel(self.model) 
        self.setting_ok = 1

    def login(self):
        if self.login_ok == 0:
            with open(r'connect.json','r') as load_f:
                load_dict = json.load(load_f)
            self.exchange = load_dict['exchange']
            self.contract = load_dict['contract']
            self.symbol = load_dict['symbol']
            exec("self.api = ccxt."+self.exchange+"({'apiKey': load_dict['apiKey'],'secret': load_dict['secret'],})")
            self.textEdit_exchange.setText(self.exchange)
            self.textEdit_contract.setText(self.contract)
            try:
                balance = self.api.fetch_balance()
                if self.contract.split('/')[0] in balance.keys():
                    balance_temp = balance[self.contract.split('/')[0]]
                else:
                    self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"contract字段有误，%s不在交易所的列表中"%self.contract.split('/')[0]))
                    self.row_count += 1 
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"登录成功"))
                self.row_count += 1
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"余额 : %s"%balance_temp['total']))
                self.row_count += 1
                self.textBrowser_account.setText(" %s"%balance_temp['total'])
                self.login_ok = 1
            except:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"登录失败"))
                self.row_count += 1

        else:
            self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"已经登录"))
            self.row_count += 1




    def stop(self):
        self.onProcess = 0
        self.model.setItem(self.row_count, 0, QtGui.QStandardItem("执行中止"))
        self.row_count += 1
        self.tableView.setModel(self.model)


    def cancelall(self):
        if self.login_ok == 1:
            today = datetime.date.today()
            start_time = self.api.parse8601('%sT00:00:00.0000' %today.isoformat()) - 100000000

            #全撤
            try:
                all_orders = self.api.fetchOrders(self.contract,start_time,500)
                all_working_orders_id = [x['id'] for x in all_orders if x['status']=='open']
                for id in all_working_orders_id:
                    self.api.cancelOrder(id)
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"撤单成功"))
                self.row_count += 1  
            except:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"撤单失败"))
                self.row_count += 1  
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