import pyperclip
import pytesseract
import os
import uuid
import shutil                   
def copy_to_clipboard(strr):
    if len(strr)>1:
        pyperclip.copy(strr[:-1])
    if strr:
        print(strr)
        print('Copied')
def path_check_create(path):
    if os.path.exists(path):pass
    else:
        os.mkdir(path)
        print('Created Path', path)
def copy_to_textfile(file_name,strr,textfile=False):
    if textfile:
        with open(f'results\{file_name}.txt','w+') as f:
                f.write(strr[:-1])

def whole_process(path=os.getcwd(),):
    if os.path.exists(path):pass
    else: return f'Check the path'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract\tesseract.exe' #change to your tesseract location
    pics_path=os.getcwd()+'\pics'
    strr=''
    for i in os.listdir(pics_path):
        strr=pytesseract.image_to_string(f'{pics_path}\{i}')
        copy_to_clipboard(strr)
        file_name= f'{uuid.uuid4().node}'
        path_check_create(path+'\\results')
        copy_to_textfile(file_name,strr,True)
        shutil.move(f'{pics_path}\{i}',f'results\{file_name}_{i}')
if __name__=="__main__":
    whole_process()
