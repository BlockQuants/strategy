# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'order.ui'
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
        Form.setFixedSize(653, 562)
        self.groupBox_contract = QtGui.QGroupBox(Form)
        self.groupBox_contract.setGeometry(QtCore.QRect(20, 40, 291, 231))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_contract.setFont(font)
        self.groupBox_contract.setObjectName(_fromUtf8("groupBox_contract"))
        self.label_2 = QtGui.QLabel(self.groupBox_contract)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 41, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox_contract = QtGui.QComboBox(self.groupBox_contract)
        self.comboBox_contract.setGeometry(QtCore.QRect(10, 110, 101, 31))
        self.comboBox_contract.setObjectName(_fromUtf8("comboBox_contract"))
        self.label = QtGui.QLabel(self.groupBox_contract)
        self.label.setGeometry(QtCore.QRect(10, 30, 51, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox_exchange = QtGui.QComboBox(self.groupBox_contract)
        self.comboBox_exchange.setGeometry(QtCore.QRect(10, 50, 101, 31))
        self.comboBox_exchange.setObjectName(_fromUtf8("comboBox_exchange"))
        self.label_7 = QtGui.QLabel(self.groupBox_contract)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox_contract)
        self.label_8.setGeometry(QtCore.QRect(130, 20, 71, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.textBrowser_market = QtGui.QTextBrowser(self.groupBox_contract)
        self.textBrowser_market.setGeometry(QtCore.QRect(130, 40, 151, 131))
        self.textBrowser_market.setObjectName(_fromUtf8("textBrowser_market"))
        self.textBrowser_market.setFont(font)
        self.textBrowser_account = QtGui.QTextBrowser(self.groupBox_contract)
        self.textBrowser_account.setGeometry(QtCore.QRect(10, 180, 271, 50))
        self.textBrowser_account.setObjectName(_fromUtf8("textBrowser_account"))
        self.groupBox_order = QtGui.QGroupBox(Form)
        self.groupBox_order.setGeometry(QtCore.QRect(20, 310, 271, 221))
        self.groupBox_order.setFont(font)
        self.groupBox_order.setObjectName(_fromUtf8("groupBox_order"))
        self.comboBox_direction = QtGui.QComboBox(self.groupBox_order)
        self.comboBox_direction.setGeometry(QtCore.QRect(130, 120, 101, 31))
        self.comboBox_direction.setObjectName(_fromUtf8("comboBox_direction"))
        self.textEdit_amount = QtGui.QTextEdit(self.groupBox_order)
        self.textEdit_amount.setGeometry(QtCore.QRect(130, 80, 104, 31))
        self.textEdit_amount.setObjectName(_fromUtf8("textEdit_amount"))
        self.label_5 = QtGui.QLabel(self.groupBox_order)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_3 = QtGui.QLabel(self.groupBox_order)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textEdit_price = QtGui.QTextEdit(self.groupBox_order)
        self.textEdit_price.setGeometry(QtCore.QRect(130, 40, 104, 31))
        self.textEdit_price.setObjectName(_fromUtf8("textEdit_price"))
        self.label_4 = QtGui.QLabel(self.groupBox_order)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 71, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_order = QtGui.QPushButton(self.groupBox_order)
        self.pushButton_order.setGeometry(QtCore.QRect(80, 180, 93, 28))
        self.pushButton_order.setFont(font)
        self.pushButton_order.setObjectName(_fromUtf8("pushButton_order"))
        
        self.tableView_log = QtGui.QTableView(Form)
        self.tableView_log.setGeometry(QtCore.QRect(350, 50, 271, 211))
        self.tableView_log.setObjectName(_fromUtf8("tableView_log"))
        self.tableView_log.verticalHeader().setVisible(False)


        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(350, 310, 271, 221))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tableView_order = QtGui.QTableView(self.tab)
        self.tableView_order.setGeometry(QtCore.QRect(0, 0, 271, 191))
        self.tableView_order.setObjectName(_fromUtf8("tableView_order"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tableView_workingOrder = QtGui.QTableView(self.tab_2)
        self.tableView_workingOrder.setGeometry(QtCore.QRect(0, 0, 271, 191))
        self.tableView_workingOrder.setObjectName(_fromUtf8("tableView_workingOrder"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tableView_trading = QtGui.QTableView(self.tab_3)
        self.tableView_trading.setGeometry(QtCore.QRect(0, 0, 271, 191))
        self.tableView_trading.setObjectName(_fromUtf8("tableView_trading"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.pushButton_refresh = QtGui.QPushButton(Form)
        self.pushButton_refresh.setGeometry(QtCore.QRect(380, 270, 101, 28))
        self.pushButton_refresh.setFont(font)
        self.pushButton_refresh.setObjectName(_fromUtf8("pushButton_refresh"))
        self.pushButton_cancellAll = QtGui.QPushButton(Form)
        self.pushButton_cancellAll.setGeometry(QtCore.QRect(510, 270, 101, 28))
        self.pushButton_cancellAll.setFont(font)
        self.pushButton_cancellAll.setObjectName(_fromUtf8("pushButton_cancellAll"))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton_cancellAll, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cancellAll)
        QtCore.QObject.connect(self.pushButton_refresh, QtCore.SIGNAL(_fromUtf8("clicked()")), self.refresh)
        QtCore.QObject.connect(self.pushButton_order, QtCore.SIGNAL(_fromUtf8("clicked()")), self.order)

        QtCore.QObject.connect(self.comboBox_exchange, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.setExchange)
        QtCore.QObject.connect(self.comboBox_contract, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.setContract)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "下单器(现货版)", None))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox_contract.setTitle(_translate("Form", "合约选择", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">合约</span></p></body></html>", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">交易所</span></p></body></html>", None))
        self.label_7.setText(_translate("Form", "<html><head/><body><p>账户持仓</p></body></html>", None))
        self.label_8.setText(_translate("Form", "<html><head/><body><p>行情</p></body></html>", None))
        self.groupBox_order.setTitle(_translate("Form", "委托", None))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">委托方向</span></p></body></html>", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">委托价格</span></p></body></html>", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">委托数量</span></p></body></html>", None))
        self.pushButton_order.setText(_translate("Form", "下单", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "委托记录", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "活动委托", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "成交记录", None))
        self.pushButton_refresh.setText(_translate("Form", "委托刷新", None))
        self.pushButton_cancellAll.setText(_translate("Form", "全部撤单", None))
        self.exchange = 0
        self.exchange_list = []
        self.contract = 0
        self.contract_list = []
        self.row_count = 0
        with open(r'connect_order.json','r') as load_f:
            load_dict = json.load(load_f)                
        self.api_list = []
        self.comboBox_exchange.addItem(' ')
        for connect in load_dict['info']:
            exec("self.api_list.append(ccxt."+connect['exchange']+"({'apiKey': connect['apiKey'],'secret': connect['secret'],}))")
            self.exchange_list.append(connect['exchange'])
            self.comboBox_exchange.addItem(connect['label'])
        self.comboBox_direction.addItem(u'买')
        self.comboBox_direction.addItem(u'卖')
        self.model = QtGui.QStandardItemModel(self.tableView_log)
        self.model.setRowCount(10)
        self.model.setColumnCount(1)
        self.model.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"日志"))
        self.tableView_log.setModel(self.model)
        self.tableView_log.setColumnWidth(0,270) 
        self.order_list = []

        self.model_order = QtGui.QStandardItemModel(self.tableView_order)
        self.model_order.setRowCount(10)
        self.model_order.setColumnCount(6)
        self.model_order.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"合约"))
        self.model_order.setHeaderData(1,QtCore.Qt.Horizontal,_fromUtf8(u"价格"))
        self.model_order.setHeaderData(2,QtCore.Qt.Horizontal,_fromUtf8(u"量"))
        self.model_order.setHeaderData(3,QtCore.Qt.Horizontal,_fromUtf8(u"状态"))        
        self.model_order.setHeaderData(4,QtCore.Qt.Horizontal,_fromUtf8(u"交易所"))
        self.model_order.setHeaderData(5,QtCore.Qt.Horizontal,_fromUtf8(u"时间"))        
        self.tableView_order.setModel(self.model_order) 
        self.tableView_order.setColumnWidth(0,58)
        self.tableView_order.setColumnWidth(1,70)
        self.tableView_order.setColumnWidth(2,70)
        self.tableView_order.setColumnWidth(3,58)
        self.tableView_order.setColumnWidth(4,70)
        self.tableView_order.setColumnWidth(5,70)

        self.model_workingOrder = QtGui.QStandardItemModel(self.tableView_workingOrder)
        self.model_workingOrder.setRowCount(10)
        self.model_workingOrder.setColumnCount(5)
        self.model_workingOrder.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"合约"))
        self.model_workingOrder.setHeaderData(1,QtCore.Qt.Horizontal,_fromUtf8(u"价格"))
        self.model_workingOrder.setHeaderData(2,QtCore.Qt.Horizontal,_fromUtf8(u"量"))       
        self.model_workingOrder.setHeaderData(3,QtCore.Qt.Horizontal,_fromUtf8(u"交易所"))
        self.model_workingOrder.setHeaderData(4,QtCore.Qt.Horizontal,_fromUtf8(u"时间"))        
        self.tableView_workingOrder.setModel(self.model_workingOrder) 
        self.tableView_workingOrder.setColumnWidth(0,58)
        self.tableView_workingOrder.setColumnWidth(1,70)
        self.tableView_workingOrder.setColumnWidth(2,70)
        self.tableView_workingOrder.setColumnWidth(3,58)
        self.tableView_workingOrder.setColumnWidth(4,70)


        self.model_trading = QtGui.QStandardItemModel(self.tableView_trading)
        self.model_trading.setRowCount(10)
        self.model_trading.setColumnCount(6)
        self.model_trading.setHeaderData(0,QtCore.Qt.Horizontal,_fromUtf8(u"合约"))
        self.model_trading.setHeaderData(1,QtCore.Qt.Horizontal,_fromUtf8(u"价格"))
        self.model_trading.setHeaderData(2,QtCore.Qt.Horizontal,_fromUtf8(u"量"))
        self.model_trading.setHeaderData(3,QtCore.Qt.Horizontal,_fromUtf8(u"成交时间"))        
        self.model_trading.setHeaderData(4,QtCore.Qt.Horizontal,_fromUtf8(u"交易所"))
        self.model_trading.setHeaderData(5,QtCore.Qt.Horizontal,_fromUtf8(u"时间"))        
        self.tableView_trading.setModel(self.model_trading) 
        self.tableView_trading.setColumnWidth(0,58)
        self.tableView_trading.setColumnWidth(1,70)
        self.tableView_trading.setColumnWidth(2,70)
        self.tableView_trading.setColumnWidth(3,58)
        self.tableView_trading.setColumnWidth(4,70)
        self.tableView_trading.setColumnWidth(5,70)

    def cancellAll(self):
        try:
            for pair in self.order_list:
                if pair[0].fetch_order(pair[1]['id'])['status'] == 'open':
                    pair[0].cancelOrder(pair[1]['id'])
            self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"撤单成功"))
            self.row_count += 1
            self.tableView_log.setModel(self.model) 
        except:
            self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"撤单失败"))
            self.row_count += 1
            self.tableView_log.setModel(self.model) 
        self.refresh()

    def refresh(self):
        #获取委托数据
        i = 0
        i_working = 0
        i_trading = 0
        try:
            for pair in self.order_list:

                info = pair[0].fetch_order(pair[1]['id'])
                status = info['status']
                
                self.model_order.setItem(i, 0, QtGui.QStandardItem(info['symbol']))
                self.model_order.setItem(i, 1, QtGui.QStandardItem(str(info['price'])))
                self.model_order.setItem(i, 2, QtGui.QStandardItem(str(info['amount'])))
                self.model_order.setItem(i, 3, QtGui.QStandardItem(info['status']))
                self.model_order.setItem(i, 4, QtGui.QStandardItem(pair[2]))
                self.model_order.setItem(i, 5, QtGui.QStandardItem(info['datetime']))
                i += 1

                if status == 'open':
                    self.model_workingOrder.setItem(i_working, 0, QtGui.QStandardItem(info['symbol']))
                    self.model_workingOrder.setItem(i_working, 1, QtGui.QStandardItem(str(info['price'])))
                    self.model_workingOrder.setItem(i_working, 2, QtGui.QStandardItem(str(info['amount'])))
                    self.model_workingOrder.setItem(i_working, 3, QtGui.QStandardItem(pair[2]))
                    self.model_workingOrder.setItem(i_working, 4, QtGui.QStandardItem(info['datetime']))
                    i_working += 1

                if status == 'filled':
                    self.model_order.setItem(i_trading, 0, QtGui.QStandardItem(info['symbol']))
                    self.model_order.setItem(i_trading, 1, QtGui.QStandardItem(str(info['average'])))
                    self.model_order.setItem(i_trading, 2, QtGui.QStandardItem(str(info['amount'])))
                    self.model_order.setItem(i_trading, 3, QtGui.QStandardItem(info['status']))
                    self.model_order.setItem(i_trading, 4, QtGui.QStandardItem(pair[2]))
                    self.model_order.setItem(i_trading, 5, QtGui.QStandardItem(info['datetime']))
                    i_trading += 1
            self.model_workingOrder.setRowCount(i_working)
            self.tableView_workingOrder.setModel(self.model_workingOrder) 
            self.tableView_trading.setModel(self.model_trading) 
            self.tableView_order.setModel(self.model_order) 
        except:
            self.model.setItem(self.row_count, 0, QtGui.QStandardItem(u"查询失败"))
            self.row_count += 1
            self.tableView_log.setModel(self.model)   

    def order(self):
        #检查下单是否合法
        price = float(self.textEdit_price.toPlainText())
        amount = float(self.textEdit_amount.toPlainText())
        dir = [1,-1][self.comboBox_direction.currentText()==u'卖']
        if self.api != 0:
            try:
                if dir == 1:
                    order = self.api.create_limit_buy_order(self.contract, amount, price)
                else:
                    order = self.api.create_limit_sell_order(self.contract, amount, price)
                self.order_list.append([self.api,order,self.exchange])
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(time.strftime("%m-%d %H:%M", time.localtime()) + "  %s委托成功"%(self.contract)))
                self.row_count += 1
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem("方向：%s  价：%s  量：%s"%([u'买',u'卖'][dir == -1],price,amount)))
                self.row_count += 1               
                self.tableView_log.setModel(self.model) 
            except:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem(time.strftime("%m-%d %H:%M", time.localtime()) + "  %s委托失败"%(self.contract)))
                self.row_count += 1
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem("方向：%s  价：%s  量：%s"%([u'买',u'卖'][dir == -1],price,amount)))
                self.row_count += 1 
                self.tableView_log.setModel(self.model) 
        else:
            self.model.setItem(self.row_count, 0, QtGui.QStandardItem("账户尚未登录"))
            self.row_count += 1
            self.tableView_log.setModel(self.model)            

    def setExchange(self):
        # self._setExchange()
        t = threading.Thread(target=self._setExchange())
        t.start()

    def _setExchange(self):
        index_exchange = self.comboBox_exchange.currentIndex() - 1
        if index_exchange > -1:
            self.exchange = self.exchange_list[index_exchange]
            self.api = self.api_list[index_exchange]
            try:
                self.contract_list = list(self.api.load_markets().keys())
                self.comboBox_contract.clear()
                self.comboBox_contract.addItem(' ')
                for contract in self.contract_list:
                    self.comboBox_contract.addItem(contract)
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem("登录%s账户成功"%self.exchange))
                self.row_count += 1
                self.tableView_log.setModel(self.model) 
            except:
                self.model.setItem(self.row_count, 0, QtGui.QStandardItem("登录%s账户失败，请检查网络"%self.exchange))
                self.row_count += 1
                self.tableView_log.setModel(self.model) 
                self.comboBox_exchange.currentIndex = 0

    def setContract(self):
        index_contract = self.comboBox_contract.currentIndex() - 1
        if index_contract > -1:
            self.contract = self.contract_list[index_contract]

            #查询账户余额
            
            balance = self.api.fetch_balance()            
            self.textBrowser_account.setText("%s:%s\n%s:%s "%(self.contract.split('/')[0],balance[self.contract.split('/')[0]]['total'],self.contract.split('/')[1],balance[self.contract.split('/')[1]]['total']))
            #获取行情数据
            temp_t = self.api.fetch_order_book(self.contract)
            self.textBrowser_market.setText(u'卖二价:%s\n卖一量:%s\n卖一价:%s\n\n买一价:%s\n买一量:%s\n买二价:%s'%(temp_t['asks'][1][0],temp_t['asks'][0][1],temp_t['asks'][0][0],temp_t['bids'][0][0],temp_t['bids'][0][1],temp_t['bids'][1][0]))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())