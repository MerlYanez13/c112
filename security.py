import cv2
import dropbox
import time
import random
startTime=time.time()
def takesnapshot():
    number=random.randint(0,100)
    vc0=cv2.VideoCapture(0)
    result=True
    while(result):
        rat,frame=vc0.read()
        imagename="img"+str(number)+".png"
        cv2.imwrite(imagename,frame)
        startTime=time.time()
        result=False
    return imagename 
    print("snapshot taken")
    vc0.release()
    cv2.destroyAllWindows()
def uploadFile(imagename):
    accesstoken="sl.A5Y9kuTiw2LZSRiYhDkJryB_9xJwYq4jg7KS-gBLgCsddnz7ZVBU0NrlYYM-VercUOcXFQQgDh0eE49gZCMGamdMwdC-SpTQdC5TKT0ZnTyyb_MKWO0TZpbI43cqeSuC7grDeHAFTX6n"
    dest="/Test/"+imagename
    dbx=dropbox.Dropbox(accesstoken)
    with open(imagename,'rb')as f:
        dbx.files_upload(f.read(),dest,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
def main():
    while True:
        if(time.time()-startTime)>=5:
            name=takesnapshot()
            uploadFile(name)
main()