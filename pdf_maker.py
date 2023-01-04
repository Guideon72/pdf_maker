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

    for y in range(20, 297, 10):
        pdf.line(10, y, 200, y)

    # building Footer (should do this for real by extending FPD and adding Footer() method)
    pdf.ln(267)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=8, txt=in_txt, align="R")


def main():
    for i, row in doc_df.iterrows():
        for i in range(row["Pages"]):
            mk_page(row["Topic"])

    pdf.output("output/new_pdf.pdf")


if __name__ == "__main__":
    main()
