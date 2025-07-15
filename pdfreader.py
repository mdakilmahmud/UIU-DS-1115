import pyttsx3
import PyPDF3

book=open("DS_1115__Final_assignment.pdf", "rb")
pdf_reader=PyPDF3.PdfFileReader(book)
pages=len(pdf_reader.pages)
print(pages)

speak=pyttsx3.init()
for num in range(pages):
    page=pdf_reader.pages[num]
    text=page.extractText()
    speak.say(text)
    speak.runAndWait()