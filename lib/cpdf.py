from lib.Semail import send_email
from lib.dele import delte
import requests
from fpdf import FPDF
from datetime import datetime

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_top_margin(30)
pdf.set_left_margin(15)


def save_pdf(data):
    data = data
    pdf.set_font('helvetica', 'B', 20,)
    pdf.multi_cell(0, 8, txt="Gov Websites Reports", align='C', ln=1)
    ntime = datetime.now()
    now = ntime.strftime("%I:%M %p")
    pdf.set_font("Times", size=18)
    pdf.multi_cell(0, 8, txt=f"{now}", align='C', ln=1)
    pdf.set_font("Times", size=12)
    pdf.multi_cell(0, 8, txt='', ln=1)
    pdf.set_fill_color(255,7,7)
    line_height = pdf.font_size * 2.5
    col_width = pdf.epw / 4 # distribute content evenly
    for row in data:
        for wdetail in row:
            if row[-1] == "Down":
                pdf.multi_cell(col_width, line_height, wdetail, align='C', border=1, ln=3, fill=True, max_line_height=pdf.font_size)
            else:
                pdf.multi_cell(col_width, line_height, wdetail, align='C', border=1, ln=3, max_line_height=pdf.font_size)
        pdf.ln(line_height)


    #pdf name and save
    tdate = datetime.today()
    today = tdate.strftime("%d-%m-%Y")
    name = ('Gov'+ str(today) +'.pdf')
    pdf.output(f"{name}")
    print(name)
    print('success')


    # send mail
    send_email(name)

    # delete pdf file
    delte(name)
