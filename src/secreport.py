# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secreport1.ui'
#
# Created: 三  1月 13 14:08:25 2010
#      by: The PyQt User Interface Compiler (pyuic) 3.16
#
# WARNING! All changes made in this file will be lost!


from qt import *
from data_visual import Data_visual
import os
from htmlCreator import HtmlTable, Cell, TITLE, TABLE, TIME, NOTFOUND
import threading
from pychart import *
import sys

from util import _
def N_(s): return s

xtics = (
N_("configuration"),
N_("accounts_groups_or_roles"),
N_("logins"),
N_("failed_logins"),
N_("authentications"),
N_("failed_authentications"),
N_("users"),
N_("terminals"),
N_("host_names"),
N_("executables"),
N_("files"),
N_("AVC's"),
N_("MAC_events"),
N_("failed_syscalls"),
N_("anomaly_events"),
N_("responses_to_anomaly_events"),
N_("crypto_events"),
N_("keys"),
N_("process_IDs"),
N_("events")
)

filename_turple = (N_("Summary"),N_("Logins"),N_("Events"),N_("Users"),N_("Terminals"),N_("Syscalls"),N_("Hosts"),N_("Executables"),N_("ResponsesToAnomalyEvents"))

DEFAULT_FILL_STYLES=[fill_style.red,fill_style.blue,fill_style.aquamarine1,fill_style.brown,
                             fill_style.darkorchid,fill_style.green,fill_style.rdiag2,fill_style.yellow]

can=None
x, y = (50, 500)

startx = lambda x:x>5 and x-5 or x
endx =  lambda x:x+5>800 and x or x+5
starty = lambda y:y>5 and y-5 or y
endy = lambda y:y+5>600 and y or y+5

class Secreport(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("Secreport")


        SecreportLayout = QGridLayout(self,1,1,11,6,"SecreportLayout")

        layout17 = QHBoxLayout(None,0,6,"layout17")

        self.secreport_label = QLabel(self,"secreport_label")
        layout17.addWidget(self.secreport_label)

        self.security_items = QComboBox(0,self,"security_items")
        self.security_items.setEnabled(0)
        layout17.addWidget(self.security_items)

        SecreportLayout.addLayout(layout17,0,0)

        layout18 = QHBoxLayout(None,0,6,"layout18")

        self.textLabel1 = QLabel(self,"textLabel1")
        layout18.addWidget(self.textLabel1)

        self.buttonGroup1 = QButtonGroup(self,"buttonGroup1")
        self.buttonGroup1.setEnabled(0)
        self.buttonGroup1.setLineWidth(0)

        self.All_radiobtn = QRadioButton(self.buttonGroup1,"All_radiobtn")
        self.All_radiobtn.setGeometry(QRect(0,10,70,19))
        self.All_radiobtn.setChecked(1)

        self.Success_radiobtn = QRadioButton(self.buttonGroup1,"Success_radiobtn")
        self.Success_radiobtn.setGeometry(QRect(96,11,72,19))

        self.Failed_radiobtn = QRadioButton(self.buttonGroup1,"Failed_radiobtn")
        self.Failed_radiobtn.setGeometry(QRect(204,11,59,19))
        layout18.addWidget(self.buttonGroup1)

        SecreportLayout.addLayout(layout18,1,0)

        layout19 = QHBoxLayout(None,0,6,"layout19")
        spacer3 = QSpacerItem(61,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout19.addItem(spacer3)

        self.query_button = QPushButton(self,"query_button")
        self.query_button.setEnabled(0)
        self.query_button.setFlat(1)
        layout19.addWidget(self.query_button)

        self.data_visual_button = QPushButton(self,"data_visual_button")
        self.data_visual_button.setEnabled(0)
        self.data_visual_button.setAutoDefault(1)
        self.data_visual_button.setFlat(1)
        layout19.addWidget(self.data_visual_button)

        SecreportLayout.addLayout(layout19,2,0)

        self.security_tb = QTextBrowser(self,"security_tb")

        SecreportLayout.addWidget(self.security_tb,3,0)

        self.languageChange()

        self.resize(QSize(352,464).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.security_items,SIGNAL("activated(const QString&)"),self.security_item_select)
        self.connect(self.data_visual_button,SIGNAL("released()"),self.data_visual)
        self.connect(self.query_button,SIGNAL("released()"),self.display_summary)
        self.isNew = False
        self.result = None
        self.display_data = None
        self.shortparam = ['']
        self.longparam = ['']
        self.__long_param_map = (('All_radiobtn', ''),
                        ('Success_radiobtn', 'success'),
                        ('Failed_radiobtn', 'failed')
                   )

        self.isNew = True
        self.upComponents()

    def languageChange(self):
        self.setCaption(_("Security Report"))
        self.secreport_label.setText(_("<b>Security Report Type :</b>"))
        self.security_items.clear()
        self.security_items.insertItem(_("summary"))
        self.security_items.insertItem(_("logins"))
        self.security_items.insertItem(_("events"))
        self.security_items.insertItem(_("users"))
        self.security_items.insertItem(_("terminals"))
        self.security_items.insertItem(_("syscalls"))
        self.security_items.insertItem(_("hosts"))
        self.security_items.insertItem(_("executables"))
        self.security_items.insertItem(_("responses to anomaly events"))
        self.textLabel1.setText(_("<b>Query Status :</b>"))
        self.buttonGroup1.setTitle(QString.null)
        self.All_radiobtn.setText(_("All"))
        self.Success_radiobtn.setText(_("Success"))
        self.Failed_radiobtn.setText(_("Failed"))
        self.query_button.setText(_("query"))
        self.data_visual_button.setText(_("Data Visualization"))

    def get_long_param(self):
        self.longparam = ['']
        long_param = self._radio_get(self.__long_param_map)
        if long_param:
            self.longparam.append(long_param)

    def data_visualation(self):
       index = self.security_items.currentItem() 
       raw_file_name = filename_turple[index]
       if self.shortparam == [''] and self.result:  
            data =  self.result.split('\n')
            for element in data:
                if not element:
                    data.remove(element)  
            del data[:4]
            use_data = []
            i = 0
            for element in data:
                if element:
                    tmp_list = []
                    element_list = []
                    tmp_list = element.split(':')
                    if i<len(xtics):  
                        element_list = tmp_list[1] +' ' + xtics[i]
                        i = i + 1         
                        use_data.append(element_list)   
            data_str = '\n'.join(use_data)
       else:
           data_str = self.result 
       self.draw_summary(raw_file_name,data_str)

    def data_visual(self):
        plot_done = False

        index = self.security_items.currentItem() 
        raw_file_name = filename_turple[index]
        filename = caption = raw_file_name.strip()
        fname = "/tmp/%s"%filename
        fname += ".png"

        th = threading.Thread(target = self.draw_plot,args=(fname,caption))
        th.start()

        while not self.plot_done:
            qApp.processEvents()

        threading.Thread.join(th)


        if self.close_canvas():
            dlg = Data_visual(self,filename = fname ,Caption = _(caption))
            dlg.run(filename = fname)

    def draw_plot(self,fname,caption):
        self.plot_done = False

        global can, x, y
        x, y = (50,500)
        can = None

        self.init_canvas(fname)
        data_str = self.result
        data= self.cut_top8data(data_str)
        sort_data = self.sort_data(data)
        bar_data = self.format_bar_data(sort_data)
        self.draw_title(caption)
        y -= 150 
        self.draw_pie(sort_data) 
        x += 350
        self.draw_bar(bar_data)
        x -= 350
        y -= 50
        self.draw_table(sort_data) 
        self.plot_done = True
    
    def init_canvas(self,fname):
        global can
        theme.use_color = True
        theme.reinitialize()

        can = canvas.init(fname, format="png")

    def cut_top8data(self,data_str):
        data = []
        data_list =  data_str.split('\n')
        del data_list[:4]
        if self.shortparam == ['']:
            for item in data_list:
                tmp=str(item).split(':')
                if len(tmp)==2:
                    tmp_turple = (tmp[0],int(tmp[1].strip())) 
                    data.append(tmp_turple)
        else:
            for item in data_list:
                tmp=str(item).split()
                if len(tmp)==2:
                    tmp_turple = (tmp[1],int(tmp[0].strip()))
                    data.append(tmp_turple)
         
        data = self.encode_escapechar(data)
        return data
      
    def sort_data(self,data):
        data.sort(key=lambda x:x[1],reverse=True)
        sort_data = data[:7]
        num=0
        for item in data[7:]:
            num += item[1]
        if num: 
            sort_data.append(("Others",num))
        return sort_data
    
    def format_bar_data(self,sort_data):
        bar_data = [] 
        bar_xtics = range(1,10,1)
         
        for item in sort_data:
           if len(item) == 2:
               tmpbar_turple = (bar_xtics[len(bar_data)], item[0],item[1])
               bar_data.append(tmpbar_turple)
        return bar_data 

    def except_none_data(self,data):
        data = [(x,y) for x, y in data if y!=0]
        return data
 
    def draw_pie(self,data):
        global can, x, y
        
        ar = area.T(loc=(0,y-80),
                    size=(360,270),
                    legend=None, 
                    x_grid_style = None, y_grid_style = None)
        plot = pie_plot.T(data=data, 
                        arc_offsets=[0,0,0,0,0,0,0,0],
                          shadow = (2, -2, fill_style.gray50),
                          label_format=None,
                          fill_styles=DEFAULT_FILL_STYLES,
                         )
        ar.add_plot(plot)
        ar.draw(can)
    
    def draw_bar(self,data):
        global can, x, y
        ar = area.T(legend = legend.T(), loc=(x,y),
                x_range = (0, None),
            x_axis=axis.X(label="X label",format="/a-30{}%d" ),
            y_axis=axis.Y(label="Y label" ))
        i = 0
        for item in data: 
            ar.add_plot(bar_plot.T(data=[item],label=item[1], hcol=2,fill_style = DEFAULT_FILL_STYLES[i]) ) 
            i = i + 1
        ar.draw(can)
        

    def draw_title(self,fname):
        global can, x, y
        can.line(line_style.red, startx(x), starty(y), endx(x+600), starty(y))
        x += 300
        self.draw_textv(fname)    
        x -= 300

    def draw_table(self,data):
        global can, x, y
        can.line(line_style.red, startx(x), endy(y), endx(x+600), endy(y))
        y -= 10
        for text,num in data:   
            self.draw_text(text,num)
        can.line(line_style.red, startx(x), starty(y), endx(x+600), starty(y))


    def draw_text(self,text,num):
        global can, x, y
        can.show( x, y, "/12/C" + text )
        textwidth =  len(text)*(theme.default_font_size)

        originx = x + 250       
        can.show( originx, y, "/12/C" + str(num) )
        y -= 20 

    def draw_textv(self,str):
        global can, x, y
        can.show(x, y, "/12/C" + str)
 
    def close_canvas(self):
       global can
       try:
           can.close() 
       except:
           return False
       return True  

    def encode_escapechar(self,data_list):
        encode_list=[]
        for item in data_list:
            if len(item) == 2:
                if "/" in item[0] :
                    encode_list.append((item[0].replace("/","//"),item[1]))
                else:
                    encode_list.append(item)
            elif len(item) == 3:
                if "/" in item[1] :
                    encode_list.append(item(0),(item[1].replace("/","//"),item[2]))
                else:
                    encode_list.append(item)
                
        return encode_list


    def draw_gnuplotbar(self,raw_file_name,data_str):
            caption = raw_file_name.strip()
            file_name = "/tmp/%s"%raw_file_name.strip()
            command = "mkbar %s"%file_name
            pipe_in , pipe_out = os.popen2(command, "wr");
            pipe_in.write(data_str);
            pipe_in.write("\n"); 
            pipe_in.flush() 
            ourstring = pipe_out.readline(); 
            if ourstring:
                dlg = Data_visual(self,filename = ourstring,Caption = _(caption))
                dlg.run()

            

    def display_summary(self):
        self.result = None
        self.security_tb.setEnabled(False)
        self.security_tb.clear()
        self.get_long_param()        


        dlg = WaitDlg(self)
        dlg.show()
        self.done = False
        th = threading.Thread(target = self.getData, args = (self,))
        th.start()
        
        self.setCursor(QCursor(3))
        self.setCursor(QCursor(3))
        while not self.done:
            qApp.processEvents()
        threading.Thread.join(th)
        self.setCursor(QCursor(0))
        self.setCursor(QCursor(0))

        self.display_data = self.result 
        self.isNew = True
        self.upComponents()
        dlg.accept()

    def security_item_select(self,string):
        self.shortparam = ['']
        if string == _('summary'):
           pass
        if string == _('logins'):
           self.shortparam.append('l')
        if string == _('events'):
           self.shortparam.append('e')
        if string == _('users'):
           self.shortparam.append('u')
        if string == _('terminals'):
           self.shortparam.append('tm')
        if string == _('syscalls'):
           self.shortparam.append('s')
        if string == _('hosts'):
           self.shortparam.append('h')
        if string == _('executables'):
           self.shortparam.append('x')
        if string == _('responses to anomaly events'):
           self.shortparam.append('r')
        self.data_visual_button.setEnabled(False)
        self.security_tb.clear()

    def invoke_get_secreport(self,shortparam = None,longparam = None):
        command = 'aureport'
        if shortparam:
            for param in  shortparam:
                if param.strip()!= 'i' and param.strip():     
                    command += ' -%s '%param
        command += ' -i '
        param = None
        if longparam:    
            for param in longparam:
                if param.strip() != 'summary' and param.strip():
                    command += ' --%s '%param
        command += ' --summary '    
        result = os.popen("LANG='C';LANGUAGE='C';"+command).read()
        result = result.strip()
        return  result


    def format2html(self, data):
        H_BG_COLOR = "#003366"
        H_FONT_COLOR = "#FFFFFF"
        BG_COLOR1 = "#666666"
        BG_COLOR2 = "#999999"
        range_time = ""
        selected_time = ""

        table = HtmlTable(3)
        data_list = data.splitlines()
       
        title = [
                 Cell(data_list[0], "", H_FONT_COLOR,TITLE),
                ]
        table.insertTr(title)

        del data_list[:1]
        for line in data_list:
            if not line:
                continue
            if "<no events of interest were found>" in line:
                row = [
                      Cell("", H_BG_COLOR, H_FONT_COLOR),
                      Cell("no events of interest were found", H_BG_COLOR, H_FONT_COLOR),
                      Cell("", H_BG_COLOR, H_FONT_COLOR),
                      ]
                table.insertTr(row)
                continue  
            if "Range of time in logs" in  line:
                range_time = line[line.find(":")+1:]    
                continue
            if "Selected time for report" in  line: 
                selected_time = line[line.find(":")+1:]
                continue
            if "=" in line:
                continue
            if ':' in line:
                element = line.split(':')
            else:
                element = line.split()
            bgcolor = ""
            if table.cursor%2 == 1:
                bgcolor = BG_COLOR1
            else:
                bgcolor = BG_COLOR2

            row = [
                  Cell("", bgcolor, H_FONT_COLOR),
                  Cell(element[0], bgcolor, H_FONT_COLOR),
                  Cell(element[1], bgcolor, H_FONT_COLOR),
                  ]
            table.insertRow(row)
        #add the timestamp
	if self.shortparam == ['']:
            timestamp_row=[
                          Cell("Range of time in logs", H_BG_COLOR, H_FONT_COLOR,TIME),
                          Cell(range_time, H_BG_COLOR, H_FONT_COLOR,TIME),
                          ]
            table.insertTr(timestamp_row)   

        return table.genhtml() 

    def upComponents(self):
        if self.isNew:
                self.isNew = False
        else:
            return
        
                
        self.security_tb.setEnabled(True)
        self.security_items.setEnabled(True)
        self.buttonGroup1.setEnabled(True)
        self.query_button.setEnabled(True)


        if self.result:
            display_text = self.format2html(self.display_data)
            self.security_tb.setText(display_text)
        else:
            self.security_tb.setText('')
        if self.result:
            if '<no events of interest were found>' in self.result:
                self.data_visual_button.setEnabled(False)
            elif not self.except_none_data( self.cut_top8data(self.result) ):
                self.data_visual_button.setEnabled(False) 
            else:
                self.data_visual_button.setEnabled(True)
        else:
            self.data_visual_button.setEnabled(False)
            

    def get_secreport_result(self,shortparam = None,longparam = None):
        res = self.invoke_get_secreport(shortparam,longparam)
        self.result = res

    def _radio_get(self, pairs):
        '''Get the "active" button from a group of radio buttons.

        The pairs parameter is a tuple of (widget name, return value) pairs.
        If no widget is active, an assertion will fail.

        '''
        for (name, value) in pairs:
            if getattr(self, name).isChecked():
                return value
        assert False, 'No widget is active'

    def getData(self,widget):
        widget.done = False
        self.get_secreport_result(self.shortparam,self.longparam)
        widget.done = True
        return

class WaitDlg(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("WaitDlg")

        self.setCaption(_("Retrieving..."))

        self.label = QLabel(self,"label")
        self.label.setGeometry(QRect(30,20,291,80))
        self.label.setText(_("Retrieving data from server...\n"
                           "Please wait"))
       
        self.setFixedSize(354, 115)
        self.resize(QSize(354,115).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)
        self.setModal(True)

    def reject(self):
        pass 
