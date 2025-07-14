def pdfHandler():
    print("pdf handler called...")
    
def txtHandler():
    print("txt handler called...")    

def imageHandler():
    print("image handler called...")    
    

#cb == callBack
def handleFile(cb):    
    print("handle file called..")
    cb()


fileName = "abc.pdf"
if fileName.endswith(".txt"):
    handleFile(txtHandler)
elif fileName.endswith(".pdf"):
    handleFile(pdfHandler)
elif fileName.endswith(".jpg"):
    handleFile(imageHandler)
    