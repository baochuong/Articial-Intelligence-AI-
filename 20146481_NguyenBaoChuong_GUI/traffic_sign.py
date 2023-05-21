from tkinter import *
from PIL import ImageTk, Image
import numpy as np
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from keras.utils.image_utils import load_img, img_to_array

model100 = load_model('traffic_sign_cnn.h5')

def CTCHINH():

	root1 = Tk()
	root1.title("Results")
	root1.geometry("240x120")
	img = load_img('camdithang.jpg',target_size= (64,64))
	plt.imshow(img)
	img = img_to_array(img)
	img = img.reshape(1,64,64,3)
	img = img.astype('float32')
	img = img/255
	a = np.argmax(model100.predict(img), axis = -1)
	if (a == 1):
		myLabel10 = Label(root1, text="an_coi", font="Arial 13 bold", fg="red")
		myLabel10.place(x = 100, y = 50,anchor = CENTER)
	if (a == 2):
		myLabel11 = Label(root1, text="cam_di_thang", font="Arial 13 bold", fg="red")
		myLabel11.place(x = 100, y = 50,anchor = CENTER)
	if (a == 3):
		myLabel12 = Label(root1, text="cam_xe_day", font="Arial 13 bold", fg="red")
		myLabel12.place(x = 100, y = 50,anchor = CENTER)
	if (a == 4):
		myLabel13 = Label(root1, text="di_cham", font="Arial 13 bold", fg="red")
		myLabel13.place(x = 100, y = 50,anchor = CENTER)
	if (a == 5):
		myLabel14 = Label(root1, text="duong_dien_phia_tren", font="Arial 13 bold", fg="red")
		myLabel14.place(x = 100, y = 50,anchor = CENTER)
	if (a == 6):
		myLabel15 = Label(root1, text="duong_doi", font="Arial 13 bold", fg="red")
		myLabel15.place(x = 100, y = 50,anchor = CENTER)
	if (a == 7):
		myLabel16 = Label(root1, text="giao_voi_duong_khong_uu_tien", font="Arial 13 bold", fg="red")
		myLabel16.place(x = 100, y = 50,anchor = CENTER)
	if (a == 8):
		myLabel17 = Label(root1, text="het_cam_vuot", font="Arial 13 bold", fg="red")
		myLabel17.place(x = 100, y = 50,anchor = CENTER)
	if (a == 9):
		myLabel18 = Label(root1, text="nguy_hiem", font="Arial 13 bold", fg="red")
		myLabel18.place(x = 100, y = 50,anchor = CENTER)
	if (a == 10):
		myLabel19 = Label(root1, text="vong_xuyen", font="Arial 13 bold", fg="red")
		myLabel19.place(x = 100, y = 50,anchor = CENTER)
	plt.show()
	root1.mainloop()
	
# Tạo cửa sổ giao diện chính
root = Tk()
root.title("Program Interface")
root.geometry("1366x720")

lgtruong = ImageTk.PhotoImage(Image.open("logotruong.png"))
lblgtruong = Label(image= lgtruong)
lblgtruong.place(x = 20, y = 5)

lgkhoa = Image.open("logokhoa.png")
resize_down1 = lgkhoa.resize((112,105))
lgkhoa_re = ImageTk.PhotoImage(resize_down1)
lblgkhoa = Label(image= lgkhoa_re)
lblgkhoa.place(x = 1150, y = 60,anchor = CENTER)

myLabel2 = Label(root, text="Faculty Of Mechanical Engineering", font="Arial 15 bold", fg="darkblue")
myLabel3 = Label(root, text="Mechatronics Engineering", font="Arial 15 bold", fg="darkblue")
myLabel2.place(x = 1150, y = 130,anchor = CENTER)
myLabel3.place(x = 1150, y = 160,anchor = CENTER)

anh1 = Image.open("di_cham.jpg")
resize_down3 = anh1.resize((200,200))
anh1_re = ImageTk.PhotoImage(resize_down3)
lbanh1 = Label(image= anh1_re)
lbanh1.place(x = 700, y = 230)

anh2 = Image.open("vongxuyen.jpg")
resize_down2 = anh2.resize((252,252))
anh2_re = ImageTk.PhotoImage(resize_down2)
lbanh2 = Label(image= anh2_re)
lbanh2.place(x =800 , y = 420)

anh3 = Image.open("ancoi.jpg")
resize_down3 = anh3.resize((150,150))
anh3_re = ImageTk.PhotoImage(resize_down3)
lbanh3 = Label(image= anh3_re)
lbanh3.place(x =950 , y = 300)

myLabel4 = Label(root, text="Traffic Sign Detection", font="Arial 23 bold", fg="red")
myLabel4.place(x = 683, y = 200,anchor = CENTER)

myLabel5 = Label(root, text="Subject: Artificial Intelligence", font="Arial 15 bold")
myLabel6 = Label(root, text="Instructors: PGS. Nguyen Truong Thinh", font="Arial 15 bold")
myLabel5.place(x = 50, y = 300,anchor = W)
myLabel6.place(x = 50, y = 330,anchor = W)

myLabel7 = Label(root, text="Author:", font="Arial 15 bold", fg="darkblue")
myLabel8 = Label(root, text="Nguyen Bao Chuong - 20146481", font="Arial 15 bold")

myLabel7.place(x = 50, y = 380)
myLabel8.place(x = 50, y =420)

btnLaunch = Button(root,text="START",font="Arial 30 bold", fg="red", command=CTCHINH)
btnLaunch.place(x = 250, y =600, anchor = CENTER)
btnStop = Button(root,text="QUIT",font="Arial 30 bold", fg="red", command=root.destroy)
btnStop.place(x = 550, y =600, anchor = CENTER)
# Gọi vòng lặp sự kiện chính để các hành động có thể diễn ra trên màn hình máy tính của người dùng
root.mainloop()