# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/work/pyqode.core/forms/search_panel.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from pyqode.qt import QtCore, QtGui, QtWidgets

class Ui_SearchPanel(object):
    def setupUi(self, SearchPanel):
        SearchPanel.setObjectName("SearchPanel")
        SearchPanel.resize(884, 90)
        SearchPanel.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(SearchPanel)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(SearchPanel)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widgetSearch = QtWidgets.QWidget(self.frame)
        self.widgetSearch.setObjectName("widgetSearch")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetSearch)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelSearch = QtWidgets.QLabel(self.widgetSearch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSearch.sizePolicy().hasHeightForWidth())
        self.labelSearch.setSizePolicy(sizePolicy)
        self.labelSearch.setMinimumSize(QtCore.QSize(0, 0))
        self.labelSearch.setMaximumSize(QtCore.QSize(18, 18))
        self.labelSearch.setText("")
        self.labelSearch.setPixmap(QtGui.QPixmap(":/pycode-icons/rc/edit-find.png"))
        self.labelSearch.setScaledContents(True)
        self.labelSearch.setObjectName("labelSearch")
        self.horizontalLayout.addWidget(self.labelSearch)
        self.lineEditSearch = PromptLineEdit(self.widgetSearch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSearch.sizePolicy().hasHeightForWidth())
        self.lineEditSearch.setSizePolicy(sizePolicy)
        self.lineEditSearch.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.horizontalLayout.addWidget(self.lineEditSearch)
        self.toolButtonPrevious = QtWidgets.QToolButton(self.widgetSearch)
        self.toolButtonPrevious.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pyqode_icons/rc/go-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonPrevious.setIcon(icon)
        self.toolButtonPrevious.setObjectName("toolButtonPrevious")
        self.horizontalLayout.addWidget(self.toolButtonPrevious)
        self.toolButtonNext = QtWidgets.QToolButton(self.widgetSearch)
        self.toolButtonNext.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pycode-icons/rc/go-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonNext.setIcon(icon1)
        self.toolButtonNext.setObjectName("toolButtonNext")
        self.horizontalLayout.addWidget(self.toolButtonNext)
        self.checkBoxRegex = QtWidgets.QCheckBox(self.widgetSearch)
        self.checkBoxRegex.setObjectName("checkBoxRegex")
        self.horizontalLayout.addWidget(self.checkBoxRegex)
        self.checkBoxCase = QtWidgets.QCheckBox(self.widgetSearch)
        self.checkBoxCase.setStyleSheet("")
        self.checkBoxCase.setObjectName("checkBoxCase")
        self.horizontalLayout.addWidget(self.checkBoxCase)
        self.checkBoxWholeWords = QtWidgets.QCheckBox(self.widgetSearch)
        self.checkBoxWholeWords.setObjectName("checkBoxWholeWords")
        self.horizontalLayout.addWidget(self.checkBoxWholeWords)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelMatches = QtWidgets.QLabel(self.widgetSearch)
        self.labelMatches.setObjectName("labelMatches")
        self.horizontalLayout.addWidget(self.labelMatches)
        self.toolButtonClose = QtWidgets.QToolButton(self.widgetSearch)
        self.toolButtonClose.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pycode-icons/rc/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonClose.setIcon(icon2)
        self.toolButtonClose.setObjectName("toolButtonClose")
        self.horizontalLayout.addWidget(self.toolButtonClose)
        self.verticalLayout_2.addWidget(self.widgetSearch)
        self.widgetReplace = QtWidgets.QWidget(self.frame)
        self.widgetReplace.setObjectName("widgetReplace")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetReplace)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelReplace = QtWidgets.QLabel(self.widgetReplace)
        self.labelReplace.setMaximumSize(QtCore.QSize(18, 18))
        self.labelReplace.setText("")
        self.labelReplace.setPixmap(QtGui.QPixmap(":/pycode-icons/rc/edit-find-replace.png"))
        self.labelReplace.setScaledContents(True)
        self.labelReplace.setObjectName("labelReplace")
        self.horizontalLayout_2.addWidget(self.labelReplace)
        self.lineEditReplace = PromptLineEdit(self.widgetReplace)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditReplace.sizePolicy().hasHeightForWidth())
        self.lineEditReplace.setSizePolicy(sizePolicy)
        self.lineEditReplace.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEditReplace.setObjectName("lineEditReplace")
        self.horizontalLayout_2.addWidget(self.lineEditReplace)
        self.toolButtonReplace = QtWidgets.QToolButton(self.widgetReplace)
        self.toolButtonReplace.setObjectName("toolButtonReplace")
        self.horizontalLayout_2.addWidget(self.toolButtonReplace)
        self.toolButtonReplaceAll = QtWidgets.QToolButton(self.widgetReplace)
        self.toolButtonReplaceAll.setObjectName("toolButtonReplaceAll")
        self.horizontalLayout_2.addWidget(self.toolButtonReplaceAll)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lineEditReplace.raise_()
        self.toolButtonReplace.raise_()
        self.toolButtonReplaceAll.raise_()
        self.labelReplace.raise_()
        self.verticalLayout_2.addWidget(self.widgetReplace)
        self.verticalLayout.addWidget(self.frame)
        self.actionSearch = QtWidgets.QAction(SearchPanel)
        icon = QtGui.QIcon.fromTheme("edit-find")
        self.actionSearch.setIcon(icon)
        self.actionSearch.setIconVisibleInMenu(True)
        self.actionSearch.setObjectName("actionSearch")
        self.actionActionSearchAndReplace = QtWidgets.QAction(SearchPanel)
        icon = QtGui.QIcon.fromTheme("edit-find-replace")
        self.actionActionSearchAndReplace.setIcon(icon)
        self.actionActionSearchAndReplace.setIconVisibleInMenu(True)
        self.actionActionSearchAndReplace.setObjectName("actionActionSearchAndReplace")
        self.actionFindNext = QtWidgets.QAction(SearchPanel)
        icon = QtGui.QIcon.fromTheme("go-down")
        self.actionFindNext.setIcon(icon)
        self.actionFindNext.setIconVisibleInMenu(True)
        self.actionFindNext.setObjectName("actionFindNext")
        self.actionFindPrevious = QtWidgets.QAction(SearchPanel)
        icon = QtGui.QIcon.fromTheme("go-up")
        self.actionFindPrevious.setIcon(icon)
        self.actionFindPrevious.setIconVisibleInMenu(True)
        self.actionFindPrevious.setObjectName("actionFindPrevious")

        self.retranslateUi(SearchPanel)
        QtCore.QMetaObject.connectSlotsByName(SearchPanel)
        SearchPanel.setTabOrder(self.lineEditSearch, self.lineEditReplace)
        SearchPanel.setTabOrder(self.lineEditReplace, self.toolButtonPrevious)
        SearchPanel.setTabOrder(self.toolButtonPrevious, self.toolButtonNext)
        SearchPanel.setTabOrder(self.toolButtonNext, self.checkBoxCase)
        SearchPanel.setTabOrder(self.checkBoxCase, self.checkBoxWholeWords)
        SearchPanel.setTabOrder(self.checkBoxWholeWords, self.toolButtonReplace)
        SearchPanel.setTabOrder(self.toolButtonReplace, self.toolButtonReplaceAll)
        SearchPanel.setTabOrder(self.toolButtonReplaceAll, self.toolButtonClose)

    def retranslateUi(self, SearchPanel):
        _translate = QtCore.QCoreApplication.translate
        SearchPanel.setWindowTitle(_translate("SearchPanel", "Form"))
        self.lineEditSearch.setToolTip(_translate("SearchPanel", "Search term"))
        self.toolButtonPrevious.setToolTip(_translate("SearchPanel", "Select previous occurence"))
        self.toolButtonNext.setToolTip(_translate("SearchPanel", "Select next occurence"))
        self.checkBoxRegex.setToolTip(_translate("SearchPanel", "Use a regular expression for search occurences"))
        self.checkBoxRegex.setText(_translate("SearchPanel", "Regex"))
        self.checkBoxCase.setToolTip(_translate("SearchPanel", "Enable case sensitive search"))
        self.checkBoxCase.setText(_translate("SearchPanel", "Match case"))
        self.checkBoxWholeWords.setToolTip(_translate("SearchPanel", "Search for whole words only"))
        self.checkBoxWholeWords.setText(_translate("SearchPanel", "Whole words"))
        self.labelMatches.setText(_translate("SearchPanel", "0 matches"))
        self.lineEditReplace.setToolTip(_translate("SearchPanel", "Replacement text"))
        self.toolButtonReplace.setToolTip(_translate("SearchPanel", "Replace current occurence"))
        self.toolButtonReplace.setText(_translate("SearchPanel", "Replace"))
        self.toolButtonReplaceAll.setToolTip(_translate("SearchPanel", "Replace all occurences"))
        self.toolButtonReplaceAll.setText(_translate("SearchPanel", "Replace All"))
        self.actionSearch.setText(_translate("SearchPanel", "Search"))
        self.actionSearch.setToolTip(_translate("SearchPanel", "Show the search panel"))
        self.actionSearch.setShortcut(_translate("SearchPanel", "Ctrl+F"))
        self.actionActionSearchAndReplace.setText(_translate("SearchPanel", "Search and replace"))
        self.actionActionSearchAndReplace.setToolTip(_translate("SearchPanel", "Show the search and replace panel"))
        self.actionActionSearchAndReplace.setShortcut(_translate("SearchPanel", "Ctrl+R"))
        self.actionFindNext.setText(_translate("SearchPanel", "Find next"))
        self.actionFindNext.setToolTip(_translate("SearchPanel", "Find the next occurrence (downward)"))
        self.actionFindNext.setShortcut(_translate("SearchPanel", "F3"))
        self.actionFindPrevious.setText(_translate("SearchPanel", "Find previous"))
        self.actionFindPrevious.setToolTip(_translate("SearchPanel", "Find previous occurrence (upward)"))
        self.actionFindPrevious.setShortcut(_translate("SearchPanel", "Shift+F3"))

from pyqode.core.widgets import PromptLineEdit
from . import pyqode_core_rc