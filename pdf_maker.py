import pandas as pd
from fpdf import FPDF

doc_df = pd.read_csv("data/topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")


def mk_page(txt):
    pdf.add_page()
    # set font in order to prevent errors on systems with no existing default
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=txt, align="L", ln=1, border=0)
    pdf.line((10, 21), (200, 21))


# mk_page("My first Python PDF")
# pdf.set_font(family="Times", style="", size=10)

# mk_page("My second line of text")
# # pdf.add_page()

# # pdf.cell(w=0, h=12, txt="My first Python PDF", align="L", ln=1, border=1)
# # pdf.cell(w=0, h=12, txt="My second line of text", align="L", ln=1, border=0)

for i, row in doc_df.iterrows():
    mk_page(row["Topic"])

pdf.output("output/new_pdf.pdf")
