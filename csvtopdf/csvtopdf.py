from fpdf import FPDF
import csv
from datetime import datetime


TITLE = "Your title here"
# Default date is today, but you can put any specified date here.
# DATE = "2019-11-11"
DATE = datetime.today().strftime('%Y-%m-%d')
# Image file should be in the same directory. JPEG, PNG and GIF are supported
IMAGE_FILE = 'image.jpg'
INPUT_FILE = 'input.csv'
OUTPUT_FILE = 'output.pdf'


class CustomPDF(FPDF):
    def header(self):
        # Add title with specified font, style, size
        self.set_font('Arial', 'B', 15)
        self.cell(5)
        self.cell(0, 5, TITLE, ln=1)
        # Add logo at specified position at right corner
        # Image has fixed height = 30mm, but different width
        # If you use image with very high width you should
        # change it's position from 230 to smaller number
        self.image(IMAGE_FILE, 230, 5, h=30)
        # Line Breaks after header
        self.ln(30)

    def footer(self):
        # Add date and page number
        self.set_y(-15)
        self.set_font('Arial', 'B', 10)
        self.cell(0, 10, DATE, 0, 0, 'L')
        page = 'Page ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'R')


def create_pdf(pdf_path):
    pdf = CustomPDF(orientation='L', unit='mm', format='A4')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)

    with open(INPUT_FILE, 'r') as f:
        reader = csv.reader(f)
        table_titles = next(reader)
        spacing = 2  # You can specify space between rows
        # Width is equal for all columns
        col_width = pdf.w / (len(table_titles) + 1)
        row_height = pdf.font_size

        # Drowing table title
        pdf.set_font('times', 'B', 8)
        pdf.set_fill_color(180, 180, 180)
        for title in table_titles:
            pdf.cell(col_width, row_height*spacing, txt=title, border=1, fill=True)
        pdf.ln(row_height*spacing)

        # Drowing table items
        pdf.set_font('times', '', 8)
        for row in reader:
            i = 0
            for item in row:
                pdf.set_fill_color(255, 255, 255)  # Default color for all cells
                # Make first column Bold
                if i == 0:
                    pdf.set_font('times', 'B', 8)
                else:
                    # All values exept first row are float
                    item = float(item)
                    pdf.set_font('times', '', 8)

                # In this block you can specify conditions of coloring different columns
                # In third column color background in green or red with condition  > 1
                if i == 2:
                    if item < 1:
                        pdf.set_fill_color(250, 80, 80)
                    else:
                        pdf.set_fill_color(80, 250, 80)

                # Define output format for different columns
                if i == 3:
                    item = "{:.0f}".format(item)
                elif 5 <= i <= 9:
                    item = "{:.6f}".format(item)

                pdf.cell(col_width, row_height*spacing, txt=str(item), border=1, fill=True)
                i += 1
            pdf.ln(row_height*spacing)
    pdf.output(pdf_path)


if __name__ == '__main__':
    create_pdf(OUTPUT_FILE)
