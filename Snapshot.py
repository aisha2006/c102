import cv2
import time
import random
import dropbox

start_time = time.time()

def take_snapshot():
    number=random.randint(0,100)
    #initializing cv2
    videoCaptureObj = cv2.VideoCapture(0)
    result = True
    while(result):
        #reads frames while camera is on
        ret,frame = videoCaptureObj.read()
        #To save the image in any storage device
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print('snapshot has been taken')
    #To close the webcam
    videoCaptureObj.release()
    #Closes all windows that might be opened during thing process
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.Av5Prtlu_maoy87pC3qtzS6oNKWVMHUofLqP01EZmLsGdE46TS6jh6L9Hoiyg1NTLI0GFQD-IO3_kfV4CMYity8yJoZpOk2d4xtysofBMphxEE205BgczDu4ZFGpb0cJFIDm5ck"
    #file = img_name
    file_from = img_name
    file_to = "/captured/"+ img_name
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
            print('file uploaded')

def main():
    while(True):
        if((time.time()-start_time)>=3):
            name = take_snapshot()
            upload_file(name)

main()
