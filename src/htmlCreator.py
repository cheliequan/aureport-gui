TITLE="title"
TABLE="table"
TIME="time"
NOTFOUND="notfound"

class HtmlTable:
    def __init__(self, col):
        self.col = col
        self.rows = {}
        self.cursor = 0
        self.up = False
        self.left = False

    def setHeader(self, up, left):
        self.up = up
        self.left = left
       
    #insert element into table;the number of cells less than len(cells)
    def insertTr(self, cells):
        self.rows[self.cursor] = cells
        self.cursor = self.cursor + 1

    def insertRow(self, cells):
        if len(cells) != self.col:
            raise InvalidParam
        self.rows[self.cursor] = cells
        self.cursor = self.cursor + 1

    def genTitleHtml(self):
        html = ""
        lines = self.rows.keys()
        lines.sort()
        for line in lines:
            text = ""
            for cell in self.rows[line]:
                if cell.type == TITLE:
                    text = text + cell.tohtml()
                else:
                    continue
            if text is not "":
                html = html + "<tr>" + text + "</tr>\n"
        return "<div align=\"center\">\n" + \
		"<table border=0 cellpadding=1 bgcolor=\"#000000\">\n" + \
		html + \
		"</table></div>" 

    def genTimeHtml(self):
        html = ""
        lines = self.rows.keys()
        lines.sort()
        for line in lines:
            text = ""
            for cell in self.rows[line]:
                if cell.type == TIME:
                    text = text + cell.tohtml()
                else:
                    continue
            if text is not "":
                html = html + "<tr>" + text + "</tr>\n"
        if html:
            return "<div align=\"center\">\n" + \
		"<table border=0 cellpadding=1 bgcolor=\"#000000\">\n" + \
		html + \
		"</table></div>" 
        else:
            return "" 

    def genTableHtml(self):
        html = ""
        lines = self.rows.keys()
        lines.sort()
        for line in lines:
            text = ""
            for cell in self.rows[line]:
                if cell.type == TABLE:
                    text = text + cell.tohtml() 
            if text is not "":
                html = html + "<tr>" + text + "</tr>\n"

        return "<div align=\"center\">\n" + \
               "<table border=0 cellpadding=1 bgcolor=\"#000000\">\n" + \
               html + \
               "</table></div>"

    def genhtml(self):
        html = ""
        html = self.genTitleHtml() + self.genTableHtml() + self.genTimeHtml() 
        return html

class Cell:
    def __init__(self, text, bgColor = "", fontColor = "", type = TABLE, maxlen = 42 ):
        self.text = text
        self.html = None
        self.fcolor = fontColor
        self.bcolor = bgColor
        self.maxlen = maxlen
        self.type = type

    def __trunc(self):
        result = [] 
        text = self.text[:]
        while len(text) != 0:
            result.append(text[:self.maxlen])
            text = text[self.maxlen:]
        return result

    def tohtml(self):
        pgs = self.__trunc()
        text = ""
        if self.type == TITLE or self.type == TIME:
            for pg in pgs:
                text = text + pg 
            bglabs =  ["<td align=\"center\">\n", "</td>"]
            ftlabs = ["<b><font>","</font></b>"]

            if self.fcolor != "":
                ftlabs[0] = "<b><font color=\"%s\">"%(self.fcolor,)

        elif self.type == TABLE:
            for pg in pgs:
                text = text + pg + "<br>"
            bglabs =  ["<td align=\"left\" valign=\"middle\">\n", "</td>"]
            ftlabs = ["font", "</font>"]

            if self.bcolor != "":
                bglabs[0] = "<td align=\"left\" valign=\"middle\" bgcolor=\"%s\">"%(self.bcolor,)
            if self.fcolor != "":
                ftlabs[0] = "<font color=\"%s\">"%(self.fcolor,)
                ftlabs[1] = "</font>"

        else:
            return ""
        return bglabs[0] + ftlabs[0] + text + ftlabs[1] + bglabs[1]
