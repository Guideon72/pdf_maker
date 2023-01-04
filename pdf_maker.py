import pandas as pd
from fpdf import FPDF


doc_df = pd.read_csv("data/topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


def mk_page(in_txt):
    pdf.add_page()
    # set font in order to prevent errors on systems with no existing default
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=in_txt, align="L", ln=1, border=0)
    pdf.line(10, 21, 200, 21)

    # building Footer (should do this for real by extending FPD and adding Footer() method)
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=8, txt=in_txt, align="R")


# mk_page("My first Python PDF")
# pdf.set_font(family="Times", style="", size=10)

# mk_page("My second line of text")
# # pdf.add_page()

# # pdf.cell(w=0, h=12, txt="My first Python PDF", align="L", ln=1, border=1)
# # pdf.cell(w=0, h=12, txt="My second line of text", align="L", ln=1, border=0)

for i, row in doc_df.iterrows():
    for i in range(row["Pages"]):
        mk_page(row["Topic"])


pdf.output("output/new_pdf.pdf")
