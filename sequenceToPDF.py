import img2pdf
import os


images = [i
    for i in os.listdir(".")
    if i.endswith(('.jpg')) ]

out_filename = "SAT_Review_Yay.pdf"
with open(out_filename, "wb") as f:
    f.write(img2pdf.convert(images))

print(f"Done! Converted: {len(images)} images.")
