#import dilakukan agar dapat menggunakan library turtle dan random
import turtle, random

#baris ini berisi perintah untuk membuat judul program turtle, membuat variabel turtle yang bernama kura
turtle.title("Tugas Pemrograman 1")
kura = turtle.Turtle()

#bagian ini adalah untuk mendapatkan input dari pengguna
rows = int(kura.screen.numinput("Rows", "Masukkan Jumlah Baris", minval = 2, maxval = 25))
pixel = int(kura.screen.numinput("Pixel", "Masukkan Ukuran Kotak (Pixel)"))
petal = int(kura.screen.numinput("Petal", "Masukkan Jumlah Lembaran Daun"))

#baris ini mengatur posisi pena agar nantinya hasil chessboardnya berada ditengah, dan mengatur kecepatan gerak/gambar turtle
x = pixel * rows / 2
y = pixel
kura.penup()
kura.goto(-x,-y)
kura.speed(50)

#baris program untuk membuat kotak sebanyak rows*rows dan memberinya warna secara random
for i in range (rows):
	kura.pendown()
	for j in range (rows):
		kura.color(random.random(),random.random(),random.random())
		kura.begin_fill()
		for k in range (0,5):
			kura.forward(pixel)
			kura.left(90)
		kura.end_fill()
		kura.right(90)
	kura.penup()
	y += pixel
	kura.goto(-x,-y)

#baris program untuk membuat bunga di atas chessboard dan mengatur agar bunga pertama tegak lurus di atas chessboard
kura.goto(0, 110)
kura.pendown()
kura.pensize(2)
kura.left(60)

#baris program untuk membuat bunga dan memberi warna secara random
for i in range (petal):
	kura.color(random.random(),random.random(),random.random())
	for j in range (0,2):
		kura.circle(100, 60)
		kura.left(120)
	kura.left(360/petal)

#baris porgram untuk mengatur posisi tulisan di bawah chessboard sekaligus membuat tulisan dengan font dan ukuran yang sudah ditentukan
kura.penup()
kura.color("Blue")
if (pixel <= 15):
	y += pixel + 20
else :
	y += 10
kura.goto(0,-(y))
kura.write("Colorful Chessboard of " +  str(rows * rows) + " Squares and Flower of " + str(petal) + " Petals", move = False, align = "center", font = ("Muli",15, "normal"))

#baris porgram untuk menyembunyikan turtle (panah) dan mengatur agar program keluar setelah di klik
kura.hideturtle()
turtle.exitonclick()
