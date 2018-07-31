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
        Form. setFixedSize(800, 600)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        Form.setFont(font)
        Form.setMouseTracking(False)
        Form.setAcceptDrops(True)
        
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 270, 220, 261))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox_monitor = QtGui.QGroupBox(Form)
        self.groupBox_monitor.setGeometry(QtCore.QRect(30, 110, 220, 141))
        self.groupBox_monitor.setObjectName(_fromUtf8("groupBox_monitor"))

        self.label_exchange = QtGui.QLabel(Form)
        self.label_exchange.setGeometry(QtCore.QRect(40, 70, 81, 31))
        self.label_exchange.setObjectName(_fromUtf8("label_exchange"))
        self.label_contract = QtGui.QLabel(Form)
        self.label_contract.setGeometry(QtCore.QRect(260, 70, 81, 31))
        self.label_contract.setObjectName(_fromUtf8("label_contract"))
        self.label_amount = QtGui.QLabel(self.groupBox)
        self.label_amount.setGeometry(QtCore.QRect(30, 40, 72, 15))
        self.label_amount.setObjectName(_fromUtf8("label_amount"))
        self.label_zeropoint = QtGui.QLabel(self.groupBox)
        self.label_zeropoint.setGeometry(QtCore.QRect(30, 80, 72, 15))
        self.label_zeropoint.setObjectName(_fromUtf8("label_zeropoint"))
        self.label_maxposition = QtGui.QLabel(self.groupBox)
        self.label_maxposition.setGeometry(QtCore.QRect(30, 160, 72, 15))
        self.label_maxposition.setObjectName(_fromUtf8("label_maxposition"))
        self.label_minposition = QtGui.QLabel(self.groupBox)
        self.label_minposition.setGeometry(QtCore.QRect(30, 200, 72, 15))
        self.label_minposition.setObjectName(_fromUtf8("label_minpositon"))
        self.label_distance = QtGui.QLabel(self.groupBox)
        self.label_distance.setGeometry(QtCore.QRect(30, 120, 72, 15))
        self.label_distance.setObjectName(_fromUtf8("label_distance"))
        self.label_log = QtGui.QLabel(Form)
        self.label_log.setGeometry(QtCore.QRect(510, 130, 72, 15))
        self.label_log.setObjectName(_fromUtf8("label_log"))
        self.label_table = QtGui.QLabel(Form)
        self.label_table.setGeometry(QtCore.QRect(270, 130, 72, 15))
        self.label_table.setObjectName(_fromUtf8("label_table"))
        self.label_price = QtGui.QLabel(self.groupBox_monitor)
        self.label_price.setGeometry(QtCore.QRect(20, 30, 72, 15))
        self.label_price.setObjectName(_fromUtf8("label_price"))
        self.label_position = QtGui.QLabel(self.groupBox_monitor)
        self.label_position.setGeometry(QtCore.QRect(20, 70, 72, 15))
        self.label_position.setObjectName(_fromUtf8("label_position"))
        self.label_balance = QtGui.QLabel(self.groupBox_monitor)
        self.label_balance.setGeometry(QtCore.QRect(20, 110, 72, 15))
        self.label_balance.setObjectName(_fromUtf8("label_balance"))



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
        self.pushButton_generatable.setGeometry(QtCore.QRect(60, 230, 93, 28))
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

        self.tableView = QtGui.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(510, 160, 241, 370))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.verticalHeader().setVisible(False)
        self.tableView_table = QtGui.QTableView(Form)
        self.tableView_table.setGeometry(QtCore.QRect(270, 160, 221, 370))
        self.tableView_table.setObjectName(_fromUtf8("tableView_table"))
        self.tableView_table.verticalHeader().setVisible(False)

        self.textBrowser_price = QtGui.QTextBrowser(self.groupBox_monitor)
        self.textBrowser_price.setEnabled(False)
        self.textBrowser_price.setGeometry(QtCore.QRect(90, 20, 111, 31))
        self.textBrowser_price.setObjectName(_fromUtf8("textBrowser_price"))
        self.textBrowser_account = QtGui.QTextBrowser(self.groupBox_monitor)
        self.textBrowser_account.setEnabled(False)
        self.textBrowser_account.setGeometry(QtCore.QRect(90, 100, 111, 31))
        self.textBrowser_account.setObjectName(_fromUtf8("textBrowser_account"))
        self.textBrowser_position = QtGui.QTextBrowser(self.groupBox_monitor)
        self.textBrowser_position.setEnabled(False)
        self.textBrowser_position.setGeometry(QtCore.QRect(90, 60, 111, 31))
        self.textBrowser_position.setObjectName(_fromUtf8("textBrowser_position"))
        self.textEdit_contract = QtGui.QTextEdit(Form)
        self.textEdit_contract.setGeometry(QtCore.QRect(350, 70, 91, 31))
        self.textEdit_contract.setObjectName(_fromUtf8("textEdit_contract"))
        self.textEdit_exchange = QtGui.QTextEdit(Form)
        self.textEdit_exchange.setGeometry(QtCore.QRect(120, 70, 91, 31))
        self.textEdit_exchange.setObjectName(_fromUtf8("textEdit_exchange"))
 
        self.textEdit_maxposition = QtGui.QTextEdit(self.groupBox)
        self.textEdit_maxposition.setGeometry(QtCore.QRect(100, 150, 91, 31))
        self.textEdit_maxposition.setObjectName(_fromUtf8("textEdit_maxposition"))
        self.textEdit_minposition = QtGui.QTextEdit(self.groupBox)
        self.textEdit_minposition.setGeometry(QtCore.QRect(100, 190, 91, 31))
        self.textEdit_minposition.setObjectName(_fromUtf8("textEdit_minposition"))
        self.textEdit_distance = QtGui.QTextEdit(self.groupBox)
        self.textEdit_distance.setGeometry(QtCore.QRect(100, 110, 91, 31))
        self.textEdit_distance.setObjectName(_fromUtf8("textEdit_distance"))
        self.textEdit_zeropoint = QtGui.QTextEdit(self.groupBox)
        self.textEdit_zeropoint.setGeometry(QtCore.QRect(100, 70, 91, 31))
        self.textEdit_zeropoint.setObjectName(_fromUtf8("textEdit_zeropoint"))
        self.textEdit_amount = QtGui.QTextEdit(self.groupBox)
        self.textEdit_amount.setGeometry(QtCore.QRect(100, 30, 91, 31))
        self.textEdit_amount.setObjectName(_fromUtf8("textEdit_amount"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_begin, QtCore.SIGNAL(_fromUtf8("clicked()")), self.begin)
        QtCore.QObject.connect(self.pushButton_generatable, QtCore.SIGNAL(_fromUtf8("clicked()")), self.generatetable)
        QtCore.QObject.connect(self.pushButton_login, QtCore.SIGNAL(_fromUtf8("clicked()")), self.login)
        QtCore.QObject.connect(self.pushButton_stop, QtCore.SIGNAL(_fromUtf8("clicked()")), self.stop)
        QtCore.QObject.connect(self.pushButton_cancelall, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cancelall)
        QtCore.QObject.connect(self.pushButton_downLoadTrading, QtCore.SIGNAL(_fromUtf8("clicked()")), self.download)
        
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "网格策略（现货版）", None))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.pushButton_begin.setText(_translate("Form", "开始执行", None))
        self.label_exchange.setText(_translate("Form", "交易所", None))
        self.label_contract.setText(_translate("Form", "合约代码", None))
        self.pushButton_stop.setText(_translate("Form", "中止执行", None))
        self.pushButton_cancelall.setText(_translate("Form", "全部撤单", None))
        self.pushButton_login.setText(_translate("Form", "账户登录", None))
        self.pushButton_downLoadTrading.setText(_translate("Form", "成交记录导出", None))
        self.groupBox.setTitle(_translate("Form", "策略参数", None))
        self.label_amount.setText(_translate("Form", "挂单量", None))
        self.label_zeropoint.setText(_translate("Form", "中心价位", None))
        self.label_maxposition.setText(_translate("Form", "最大持仓", None))
        self.label_minposition.setText(_translate("Form", "最小持仓", None)) 
        self.label_distance.setText(_translate("Form", "挂单间隔", None))
        self.pushButton_generatable.setText(_translate("Form", "生成挂单表", None))
        self.textEdit_minposition.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-2700</p></body></html>", None))
        self.textEdit_maxposition.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2700</p></body></html>", None))
        self.textEdit_distance.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">30</p></body></html>", None))
        self.textEdit_zeropoint.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7930</p></body></html>", None))
        self.textEdit_amount.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">30</p></body></html>", None))
        self.label_log.setText(_translate("Form", "策略日志", None))
        self.groupBox_monitor.setTitle(_translate("Form", "策略监控", None))
        self.textBrowser_price.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">0</span></p></body></html>", None))
        self.label_price.setText(_translate("Form", "当前价", None))
        self.label_position.setText(_translate("Form", "持仓", None))
        self.label_balance.setText(_translate("Form", "账户余额", None))
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
        self.label_table.setText(_translate("Form", "挂单表", None))
        self.timer = QTimer(Form)
        self.timer.timeout.connect(self.unit_work)
        self.row_count = 0
        self.error_count = 0
        self.login_ok = 0
        self.onProcess = 0
        self.generate_ok = 0
        self.model = QtGui.QStandardItemModel(self.tableView)
        self.model.setRowCount(100)
        self.model.setColumnCount(1)
        self.model.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"日志"))
        self.tableView.setModel(self.model) 
        self.tableView.setColumnWidth(0,220)
        self.model_table = QtGui.QStandardItemModel(self.tableView_table)
        self.model_table.setRowCount(100)
        self.model_table.setColumnCount(3)
        self.model_table.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"持仓"))
        self.model_table.setHeaderData(1,QtCore.Qt.Horizontal,_fromUtf8(u"买单价"))
        self.model_table.setHeaderData(2,QtCore.Qt.Horizontal,_fromUtf8(u"卖单价"))
        self.tableView_table.setModel(self.model_table) 
        self.tableView_table.setColumnWidth(0,58)
        self.tableView_table.setColumnWidth(1,70)
        self.tableView_table.setColumnWidth(2,70)

    def begin(self):
        if self.login_ok == 1:
            if self.generate_ok == 1:
                today = datetime.date.today()
                self.since = self.api.parse8601('%sT00:00:00.0000' %today.isoformat())
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

    def download(self):
        if self.login_ok == 1:
            today = datetime.date.today()
            since = self.api.parse8601('%sT00:00:00.0000' %today.isoformat()) - 100000000
            try:
                all_orders = self.api.fetchOrders(self.contract,since,500)
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

    def cancelall(self):
        if self.login_ok == 1:
            today = datetime.date.today()
            since = self.api.parse8601('%sT00:00:00.0000' %today.isoformat()) - 100000000
            #全撤
            try:
                all_orders = self.api.fetchOrders(self.contract,since,500)
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

    def generatetable(self):
        DISTANCE = float(self.textEdit_distance.toPlainText())
        ZERO_POINT = float(self.textEdit_zeropoint.toPlainText())
        AMOUNT = int(self.textEdit_amount.toPlainText())
        MAX_HOLDING = np.floor(int(self.textEdit_maxposition.toPlainText())/AMOUNT)
        MIN_HOLDING = np.ceil(max(0,int(int(self.textEdit_minposition.toPlainText())/AMOUNT)))
        INF_PRICE = 15000
        self.holding_u = -scipy.linspace(MIN_HOLDING,MAX_HOLDING,-MIN_HOLDING+MAX_HOLDING+1)
        price_u = scipy.linspace(MIN_HOLDING*DISTANCE,MAX_HOLDING*DISTANCE,-MIN_HOLDING+MAX_HOLDING+1)
        self.bid_price_u = ZERO_POINT + np.hstack((-ZERO_POINT,price_u[:-1]))
        self.ask_price_u = ZERO_POINT + np.hstack((price_u[1:], INF_PRICE))
        self.AMOUNT = AMOUNT
        self.model_table.setRowCount(self.bid_price_u.shape[0])
        for i in range(self.bid_price_u.shape[0]):
            self.model_table.setItem(i, 0, QtGui.QStandardItem('%s'%(self.holding_u[i]*AMOUNT)))
            self.model_table.setItem(i, 1, QtGui.QStandardItem('%s'%self.bid_price_u[i]))
            self.model_table.setItem(i, 2, QtGui.QStandardItem('%s'%self.ask_price_u[i]))
        self.tableView_table.setModel(self.model_table) 
        if self.login_ok == 1:
            if self.onProcess == 0:
                try:
	                temp_t = self.api.fetch_order_book(self.contract)
	                self.textBrowser_price.setText('%s'%((float(temp_t['bids'][0][0])+float(temp_t['asks'][0][0]))/2))
	                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"买一价: %s  卖一价: %s"%(temp_t['bids'][0],temp_t['asks'][0]) ))
	                self.row_count += 1
	                Pos = self.api.fetch_balance()[self.contract.split('/')[0]]
	                holding_now = np.floor(Pos['total']/self.AMOUNT)
	                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"当前持仓： %s"%(holding_now * self.AMOUNT) ))
	                self.row_count += 1                    
	                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"准备下单： 买入价: %s  卖出价: %s"%(self.bid_price_u[self.holding_u == holding_now],self.ask_price_u[self.holding_u == holding_now])))
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
        self.generate_ok = 1 

    def login(self):
        if self.login_ok == 0:
            #读取connect.json的文件信息
            with open(r'C:\Users\public_s\Desktop\stra_ui\connect.json','r') as load_f:
                load_dict = json.load(load_f)
            self.exchange = load_dict['exchange']
            self.contract = load_dict['contract']
            exec("self.api = ccxt."+self.exchange+"({'apiKey': load_dict['apiKey'],'secret': load_dict['secret'],})")
            self.textEdit_exchange.setText(self.exchange)
            self.textEdit_contract.setText(self.contract)
            #读取账户信息
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
        self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"执行中止"))
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
                
                Pos = self.api.fetch_balance()[self.contract.split('/')[0]]
                holding_now = np.floor(Pos['total']/self.AMOUNT)
                temp_h = holding_now*self.AMOUNT
                self.textBrowser_position.setText('%s'%temp_h)
                #获取应挂单
                bid_p = self.bid_price_u[self.holding_u == holding_now][0]
                ask_p = self.ask_price_u[self.holding_u == holding_now][0]
                #检验是否需要下单
                all_orders = self.api.fetchOrders(self.contract,self.since)
                working_price = [x['price'] for x in all_orders if x['status'] == 'open']
                if len(all_orders) < 100:
                    if bid_p not in working_price:
                        try:
                            order_1 = self.api.create_limit_buy_order(self.contract, self.AMOUNT, bid_p)
                            self.model.setItem(self.row_count, 0, QtGui.QStandardItem(time.strftime("%m-%d %H:%M", time.localtime()) +u" 挂买单  %s"%bid_p))
                            self.row_count += 1
                            self.tableView.setModel(self.model)
                        except:
                            pass

                    if ask_p not in working_price:
                        try:
                            order_2 = self.api.create_limit_sell_order(self.contract, self.AMOUNT, ask_p)
                            self.model.setItem(self.row_count, 0, QtGui.QStandardItem(time.strftime("%m-%d %H:%M", time.localtime()) +u" 挂卖单  %s"%ask_p))
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

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())