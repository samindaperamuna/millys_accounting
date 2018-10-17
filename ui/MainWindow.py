from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from ui.new2 import NewWindow
from ui.newbutton import Ui_Form


class MainWindow:

    def __init__(self, window: QMainWindow):
        self.window = window
        self.window.resize(554, 517)

        self.centralWidget = QtWidgets.QWidget(window, flags=None)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget, flags=None)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 430, 431, 41))

        self.boxLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.boxLayout.setContentsMargins(0, 0, 0, 0)

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.boxLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.boxLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.boxLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.boxLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.boxLayout.addWidget(self.pushButton_5)

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 501, 391))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("resources/logo_small.jpg"))

        window.setCentralWidget(self.centralWidget)

        self.mainMenuBar = QtWidgets.QMenuBar(window)
        self.mainMenuBar.setGeometry(QtCore.QRect(0, 0, 554, 21))

        self.menuFile = QtWidgets.QMenu(self.mainMenuBar)
        self.menuCompany = QtWidgets.QMenu(self.mainMenuBar)
        self.menuAccountant = QtWidgets.QMenu(self.mainMenuBar)
        self.menuCustomer = QtWidgets.QMenu(self.mainMenuBar)
        self.menuVendor = QtWidgets.QMenu(self.mainMenuBar)
        self.menuBank = QtWidgets.QMenu(self.mainMenuBar)
        self.menuReport = QtWidgets.QMenu(self.mainMenuBar)
        self.menuAccountsTaxes = QtWidgets.QMenu(self.menuReport)
        self.menuFinancial = QtWidgets.QMenu(self.menuReport)

        window.setMenuBar(self.mainMenuBar)

        self.statusBar = QtWidgets.QStatusBar(window)
        window.setStatusBar(self.statusBar)

        self.actionNew = QtWidgets.QAction(window)
        self.actionNew.triggered.connect(self.on_action_new)

        self.actionOpen = QtWidgets.QAction(window)

        self.actionBack_Up = QtWidgets.QAction(window)

        self.actionSingle_User = QtWidgets.QAction(window)

        self.actionUtilities = QtWidgets.QAction(window)

        self.actionLog_off = QtWidgets.QAction(window)

        self.actionExit = QtWidgets.QAction(window)

        self.actionExit.triggered.connect(self.on_action_exit)

        self.actionMy_Company = QtWidgets.QAction(window)

        self.actionSnap_Shot = QtWidgets.QAction(window)

        self.actionChart_of_Accounts = QtWidgets.QAction(window)

        self.actionClosing_Date = QtWidgets.QAction(window)

        self.actionPlan_Budget = QtWidgets.QAction(window)

        self.actionUsers = QtWidgets.QAction(window)

        self.actionEntity = QtWidgets.QAction(window)

        self.actionJournal = QtWidgets.QAction(window)

        self.actionReconcile = QtWidgets.QAction(window)

        self.actionItem_List = QtWidgets.QAction(window)

        self.actionCustomer_Center = QtWidgets.QAction(window)

        self.actionCreate_Estimate = QtWidgets.QAction(window)

        self.actionCreate_Invoice = QtWidgets.QAction(window)

        self.actionCreate_Sales_Receipt = QtWidgets.QAction(window)

        self.actionReceive_Payment = QtWidgets.QAction(window)

        self.actionCredit_Memo_Refund = QtWidgets.QAction(window)

        self.actionVendor_Center = QtWidgets.QAction(window)

        self.actionEnter_bills = QtWidgets.QAction(window)

        self.actionPay_Bills = QtWidgets.QAction(window)

        self.actionWrite_Cheque = QtWidgets.QAction(window)

        self.actionMake_Deposit = QtWidgets.QAction(window)

        self.actionTransfunds = QtWidgets.QAction(window)

        self.actionCredit_Card_Charges = QtWidgets.QAction(window)

        self.actionReconcile_2 = QtWidgets.QAction(window)

        self.actionFixed_Asset = QtWidgets.QAction(window)

        self.actionInvestment = QtWidgets.QAction(window)

        self.actionLoans = QtWidgets.QAction(window)

        self.actionAR_Report = QtWidgets.QAction(window)

        self.actionAP_Report = QtWidgets.QAction(window)

        self.actionBank = QtWidgets.QAction(window)

        self.actionAudit_Trail = QtWidgets.QAction(window)

        self.actionBalance_Sheet = QtWidgets.QAction(window)

        self.actionProfit_and_Loss = QtWidgets.QAction(window)

        self.actionTrial_Balance = QtWidgets.QAction(window)

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionBack_Up)
        self.menuFile.addAction(self.actionSingle_User)
        self.menuFile.addAction(self.actionUtilities)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLog_off)
        self.menuFile.addAction(self.actionExit)
        self.menuCompany.addAction(self.actionMy_Company)
        self.menuCompany.addAction(self.actionSnap_Shot)
        self.menuCompany.addSeparator()
        self.menuCompany.addAction(self.actionChart_of_Accounts)
        self.menuCompany.addAction(self.actionClosing_Date)
        self.menuCompany.addAction(self.actionPlan_Budget)
        self.menuCompany.addAction(self.actionEntity)
        self.menuCompany.addAction(self.actionItem_List)
        self.menuAccountant.addAction(self.actionJournal)
        self.menuAccountant.addAction(self.actionReconcile)
        self.menuAccountant.addAction(self.actionUsers)
        self.menuAccountant.addSeparator()
        self.menuAccountant.addAction(self.actionFixed_Asset)
        self.menuAccountant.addAction(self.actionInvestment)
        self.menuAccountant.addAction(self.actionLoans)
        self.menuCustomer.addAction(self.actionCustomer_Center)
        self.menuCustomer.addSeparator()
        self.menuCustomer.addAction(self.actionCreate_Estimate)
        self.menuCustomer.addAction(self.actionCreate_Invoice)
        self.menuCustomer.addAction(self.actionCreate_Sales_Receipt)
        self.menuCustomer.addAction(self.actionReceive_Payment)
        self.menuCustomer.addAction(self.actionCredit_Memo_Refund)
        self.menuVendor.addAction(self.actionVendor_Center)
        self.menuVendor.addSeparator()
        self.menuVendor.addAction(self.actionEnter_bills)
        self.menuVendor.addAction(self.actionPay_Bills)
        self.menuBank.addAction(self.actionWrite_Cheque)
        self.menuBank.addAction(self.actionMake_Deposit)
        self.menuBank.addAction(self.actionTransfunds)
        self.menuBank.addAction(self.actionCredit_Card_Charges)
        self.menuBank.addSeparator()
        self.menuBank.addAction(self.actionReconcile_2)
        self.menuAccountsTaxes.addAction(self.actionTrial_Balance)
        self.menuFinancial.addAction(self.actionBalance_Sheet)
        self.menuFinancial.addAction(self.actionProfit_and_Loss)
        self.menuReport.addAction(self.menuFinancial.menuAction())
        self.menuReport.addSeparator()
        self.menuReport.addAction(self.actionAR_Report)
        self.menuReport.addAction(self.actionBank)
        self.menuReport.addAction(self.actionAP_Report)
        self.menuReport.addSeparator()
        self.menuReport.addAction(self.menuAccountsTaxes.menuAction())
        self.menuReport.addAction(self.actionAudit_Trail)
        self.mainMenuBar.addAction(self.menuFile.menuAction())
        self.mainMenuBar.addAction(self.menuCompany.menuAction())
        self.mainMenuBar.addAction(self.menuAccountant.menuAction())
        self.mainMenuBar.addAction(self.menuCustomer.menuAction())
        self.mainMenuBar.addAction(self.menuVendor.menuAction())
        self.mainMenuBar.addAction(self.menuBank.menuAction())
        self.mainMenuBar.addAction(self.menuReport.menuAction())

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, MainWindow):
        translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(translate("MainWindow", "MainWindow"))

        self.pushButton.setText(translate("MainWindow", "Invoice"))
        self.pushButton_2.setText(translate("MainWindow", "Bills"))
        self.pushButton_3.setText(translate("MainWindow", "Journal"))
        self.pushButton_4.setText(translate("MainWindow", "Bank"))
        self.pushButton_5.setText(translate("MainWindow", "Report"))
        self.menuFile.setTitle(translate("MainWindow", "FILE"))
        self.menuCompany.setTitle(translate("MainWindow", "Company"))
        self.menuAccountant.setTitle(translate("MainWindow", "Accountant"))
        self.menuCustomer.setTitle(translate("MainWindow", "Customer"))
        self.menuVendor.setTitle(translate("MainWindow", "Vendor"))
        self.menuBank.setTitle(translate("MainWindow", "Bank"))
        self.menuReport.setTitle(translate("MainWindow", "Report"))
        self.menuAccountsTaxes.setTitle(translate("MainWindow", "Accoounts & Taxes"))
        self.menuFinancial.setTitle(translate("MainWindow", "Financials"))
        self.actionNew.setText(translate("MainWindow", "New"))
        self.actionOpen.setText(translate("MainWindow", "Open"))
        self.actionBack_Up.setText(translate("MainWindow", "Back-Up"))
        self.actionSingle_User.setText(translate("MainWindow", "Single User"))
        self.actionUtilities.setText(translate("MainWindow", "Utilities"))
        self.actionLog_off.setText(translate("MainWindow", "Log off"))
        self.actionExit.setText(translate("MainWindow", "Exit"))
        self.actionMy_Company.setText(translate("MainWindow", "My Company"))
        self.actionSnap_Shot.setText(translate("MainWindow", "Snap-Shot"))
        self.actionChart_of_Accounts.setText(translate("MainWindow", "Charts of Accounts"))
        self.actionClosing_Date.setText(translate("MainWindow", "Closing Date"))
        self.actionPlan_Budget.setText(translate("MainWindow", "Plan/Budget"))
        self.actionUsers.setText(translate("MainWindow", "Users"))
        self.actionEntity.setText(translate("MainWindow", "Entity"))
        self.actionJournal.setText(translate("MainWindow", "Journal"))
        self.actionReconcile.setText(translate("MainWindow", "Reconcile"))
        self.actionItem_List.setText(translate("MainWindow", "Item List"))
        self.actionCustomer_Center.setText(translate("MainWindow", "Customer Center"))
        self.actionCreate_Estimate.setText(translate("MainWindow", "Estimate/Pro-Forma"))
        self.actionCreate_Invoice.setText(translate("MainWindow", "Invoice"))
        self.actionCreate_Sales_Receipt.setText(translate("MainWindow", "Sales Receipt"))
        self.actionReceive_Payment.setText(translate("MainWindow", "Receive Payment"))
        self.actionCredit_Memo_Refund.setText(translate("MainWindow", "Credit Memo/Refund"))
        self.actionVendor_Center.setText(translate("MainWindow", "Vendor Center"))
        self.actionEnter_bills.setText(translate("MainWindow", "Bills"))
        self.actionPay_Bills.setText(translate("MainWindow", "Pay Bills"))
        self.actionWrite_Cheque.setText(translate("MainWindow", "Write Cheque"))
        self.actionMake_Deposit.setText(translate("MainWindow", "Make Deposit"))
        self.actionTransfunds.setText(translate("MainWindow", "Transfer"))
        self.actionCredit_Card_Charges.setText(translate("MainWindow", "Credit Card Charges"))
        self.actionReconcile_2.setText(translate("MainWindow", "Reconcile"))
        self.actionFixed_Asset.setText(translate("MainWindow", "Fixed Asset"))
        self.actionInvestment.setText(translate("MainWindow", "Investment"))
        self.actionLoans.setText(translate("MainWindow", "Loans"))
        self.actionAR_Report.setText(translate("MainWindow", "Receivables"))
        self.actionAP_Report.setText(translate("MainWindow", "Bank"))
        self.actionBank.setText(translate("MainWindow", "Payables"))
        self.actionAudit_Trail.setText(translate("MainWindow", "Audit Trail"))
        self.actionBalance_Sheet.setText(translate("MainWindow", "Balance Sheet"))
        self.actionProfit_and_Loss.setText(translate("MainWindow", "Profit and Loss"))
        self.actionTrial_Balance.setText(translate("MainWindow", "Trial Balance"))

    def on_action_new(self):
        main_window = QtWidgets.QMainWindow(parent=self.window, flags=Qt.Window)
        new_window = Ui_Form()
        new_window.setupUi(self.window, main_window)
        main_window.show()

    def on_action_exit(self):
        exit(0)
