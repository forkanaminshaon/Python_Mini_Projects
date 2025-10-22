#Merge PDF Files 

from PyPDF2 import PdfMerger

AllPDF = ["Career with AI.pdf","LinkedIn 101.pdf"]

Ourmerger = PdfMerger()

for NewPDF in AllPDF:
    Ourmerger.append(NewPDF)

Ourmerger.write("Shaon.pdf")
Ourmerger.close()