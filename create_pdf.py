from fpdf import FPDF

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

def create_pdf(description,img,lyrics,data):
    lyrics = lyrics.encode('latin-1', 'replace').decode('latin-1')
    description = description.encode('latin-1', 'replace').decode('latin-1')
    pdf = PDF()  
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(75, 10, "Description", 0, 2, 'C')
    pdf.image('analysis/lin.jpg', x = None, y = None, w = 50, h = 50, type = '', link = '')
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-40)
    pdf.set_font('Times', '', 10)
    pdf.multi_cell(80, 10, '%s' % (description), 0, 0, 'C')

    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(75, 10, "Analysis", 0, 2, 'C')
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-40)
    pdf.image('analysis/descarga.png', x = None, y = None, w = 0, h = 0, type = '', link = '')

    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(60, 5, "Lyrics", 0, 2, 'C')
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-40)
    pdf.set_font('Times', '', 10)
    pdf.multi_cell(80, 10, '%s' % (lyrics), 0, 0, 'C')
    pdf.ln()
    pdf.set_col(0)
    pdf.cell(-90)
    pdf.output('analysis/test.pdf', 'F')