from fpdf import FPDF
import os

'''
class PDF(FPDF):
    col = 0
    y0 = 0
    def set_col(self,col):
        self.x = 10+col*100
        self.set_left_margin(self.x)
        self.set_x(self.x)

    def accept_page_break(self):
        if self.col <2:
            self.col+=1
            self.set_col(self.col)
            self.set_y(self.y0+15)
            return False
        else:
            self.col = 0
            self.set_col(self.col)
            return True
'''
def create_pdf(song,description,lyrics,dirName,data):
    lyrics = lyrics.encode('latin-1', 'replace').decode('latin-1')
    description = description.encode('latin-1', 'replace').decode('latin-1')
    pdf = FPDF()  
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(75, 10, "Description", 0, 2, 'C')
    if os.path.isfile(dirName+'/image.png'):
        pdf.image(dirName+'/image.png', x = None, y = None, w = 50, h = 50, type = '', link = '')
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-40)
    pdf.set_font('Times', '', 10)
    pdf.multi_cell(150, 10, '%s' % (description), 0, 0, 'C')

    pdf.cell(75, 10, "Data", 0, 2, 'C')
    pdf.set_font('arial','B', 8)
    for key,val in data.items():
        #print(key, "=>", val.values())
        pdf.cell(20,7,key,1,0,'C')
    pdf.ln()
    pdf.set_font('arial','', 8)
    for val in data.items():
        for i in val[1].items():
            pdf.cell(20,7,str(i[1]),1,0,'C')
    pdf.ln()

    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(75, 10, "Analysis", 0, 2, 'C')
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-40)
    if os.path.isfile(dirName+'/'+'ES_graph.png'):
        pdf.cell(75, 10, "ES Graph", 0, 2, 'C')
        pdf.image(dirName+'/'+'ES_graph.png', x = None, y = None, w = 150, h = 100, type = '', link = '')
    if os.path.isfile(dirName+'/'+'US_graph.png'):
        pdf.cell(75, 10, "US Graph", 0, 2, 'C')
        pdf.image(dirName+'/'+'US_graph.png', x = None, y = None, w = 150, h = 100, type = '', link = '')
    if os.path.isfile(dirName+'/'+'GLOBAL_graph.png'):
        pdf.cell(75, 10, "GLOBAL Graph", 0, 2, 'C')
        pdf.image(dirName+'/'+'GLOBAL_graph.png', x = None, y = None, w = 150, h = 100, type = '', link = '')
    if os.path.isfile(dirName+'/'+'GB_graph.png'):
        pdf.cell(75, 10, "GB Graph", 0, 2, 'C')
        pdf.image(dirName+'/'+'GB_graph.png', x = None, y = None, w = 150, h = 100, type = '', link = '')

    pdf.add_page()
    pdf.set_xy(50, 0)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(60, 5, "Lyrics", 0, 2, 'C')
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-40)
    pdf.set_font('Times', '', 10)
    pdf.multi_cell(80, 10, '%s' % (lyrics), 0, 0, 'C')
    pdf.ln()
    #pdf.set_col(0)
    pdf.cell(-90)
    pdf.output(dirName+'/'+song+'_analysis.pdf', 'F')