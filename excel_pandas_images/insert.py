import pandas as pd
import os.path


EXCEL_INPUT = 'Accessories.xlsx'
EXCEL_OUTPUT = EXCEL_INPUT.split('.')[0] + '_with_images.xlsx'
IMAGE_DIR = "AccessoriesPhoto\\"


df = pd.read_excel(EXCEL_INPUT)
writer = pd.ExcelWriter(EXCEL_OUTPUT, engine='xlsxwriter')
workbook  = writer.book
worksheet = workbook.add_worksheet('Accessories')
worksheet.write(0, 0, 'Title')
worksheet.write(0, 1, 'Photo')
worksheet.set_column(0, 1, 27)
worksheet.set_column(1, 2, 35)

i = 0
for index, row in df.iterrows():
    image = IMAGE_DIR + str(row[0]).strip() + '.jpg'
    worksheet.set_row(i+1, 150)
    worksheet.write(i+1, 0, str(row[0]).strip())

    if os.path.exists(image):
        worksheet.insert_image(i+1, 1, image, {'x_scale': 0.4, 'y_scale': 0.4, 'x_offset': 10, 'y_offset': 10})
    else:
        print("Can't find image with row=%s image_name=%s" % (i+2, image))
    i += 1
writer.save()
