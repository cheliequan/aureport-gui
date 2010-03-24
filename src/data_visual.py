# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_visual.ui'
#
# Created: 三  6月 10 10:44:30 2009
#      by: The PyQt User Interface Compiler (pyuic) 3.16
#
# WARNING! All changes made in this file will be lost!


from qt import *
import gettext
import os
from util import _
def N_(s): return s


class Data_visual(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0,filename = None,Caption = None):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("Data_visual")


        Data_visualLayout = QVBoxLayout(self,11,6,"Data_visualLayout")

        self.draw_label = QLabel(self,"draw_label")
        Data_visualLayout.addWidget(self.draw_label)
        self.draw_label.setLineWidth(1)
        self.draw_label.setScaledContents(1)      

        self.filename = filename     
 

        layout9 = QHBoxLayout(None,0,6,"layout9")
        spacer5 = QSpacerItem(40,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout9.addItem(spacer5)

        Data_visualLayout.addLayout(layout9)

        self.languageChange()

        self.resize(QSize(664,532).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)



    def languageChange(self):
        self.setCaption(_("Data Visualization"))
        self.draw_label.setText(QString.null)

    def run(self, filename = ''):
        '''Show the dialog to modify rule.'''
        self.pm = QPixmap(800,600)
        if  self.pm.load(filename.strip()): 
            self.draw_label.setPixmap(self.pm)
        self.draw_label.show ()
        os.remove(filename.strip()) 
        res = self.exec_loop()
        return res

