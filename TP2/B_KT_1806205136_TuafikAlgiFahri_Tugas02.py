#!/usr/bin/env python3
"""Template Assignment #2."""
import turtle
import random
import math


def choose_file():
    """Prompts user to choose file to load via GUI-based modal window."""
    import tkinter
    from tkinter import filedialog

    root_window = tkinter.Tk()
    root_window.withdraw()

    return filedialog.askopenfilename()

# Fungsi untuk membuat judul turtle seperti perintah soal
def judul(string_judul):
    # string_judul merupakan var berisi sebuah baris dari input yang akan dijadikan judul, program ini akan memotong string menjadi list dan memisahkannya berdasarkan spasi
    string_judul = string_judul.split(" ")
    # string kosong yang akan digunakan untuk menyimpan judul
    string_judul_turtle = ""
    
    # untuk memasukkan list tadi ke dalam string
    for i in range (len(string_judul) - 1):
        string_judul_turtle += string_judul[i]  + " "

    # lanjutan program perulangan di atas, menambah "|" sebagai pemisah nama dan NPM
    string_judul_turtle += "| " + string_judul[-1]
    # mengembalikan nilai variabel judul ke fungsi judul
    return string_judul_turtle


# Fungsi untuk membuat square
def draw_square(pen, temp, line):
    # mengangkan pena agar tidak menggambar saat memindahkan posisi pena, memindahkan posisi pena, dan menurunkan pena kembali
    pen.penup()
    pen.goto(int(temp[1]), int(temp[2]))
    pen.pendown()

    # untuk mengecek apakah input ukurannya merupakan angka negatif
    if (int(temp[3]) < 0):
        print("Terdapat kesalahan input (memasukkan nilai negatif) pada baris ke {}" .format(line))
        temp[3] = str(abs(int(temp[3])))

    # perulagan untuk menggambar square
    for i in range (0, 4):
        pen.forward(int(temp[3]))
        pen.right(90)

# Fungsi untuk membuat rectangle
def draw_rectangle(pen, temp, line):
    # mengangkan pena agar tidak menggambar saat memindahkan posisi pena, memindahkan posisi pena, dan menurunkan pena kembali
    pen.penup()
    pen.goto(int(temp[1]), int(temp[2]))
    pen.pendown()

    # untuk mengecek apakah input ukurannya merupakan angka negatif
    for i in range (3, 5):
        if (int(temp[i]) < 0):
            print("Terdapat kesalahan input (memasukkan nilai negatif) pada baris ke {}" .format(line))
            temp[i] = str(abs(int(temp[i])))

    # perulagan untuk menggambar rectangle
    for i in range (0, 2):
        pen.forward(int(temp[3]))
        pen.right(90)
        pen.forward(int(temp[4]))
        pen.right(90)

def draw_circle(pen, temp, line):
    # mengangkan pena agar tidak menggambar saat memindahkan posisi pena, memindahkan posisi pena, dan menurunkan pena kembali
    pen.penup()
    pen.goto(int(temp[1]), int(temp[2]))
    pen.pendown()

    # untuk mengecek apakah input ukurannya merupakan angka negatif
    if (int(temp[3]) < 0):
        print("Terdapat kesalahan input (memasukkan nilai negatif) pada baris ke {}" .format(line))
        temp[3] = str(abs(int(temp[3])))

    # perintah untuk membuat lingkaran
    pen.circle(int(temp[3]))

def draw_petal(pen, temp, line):
    # mengangkan pena agar tidak menggambar saat memindahkan posisi pena, memindahkan posisi pena, dan menurunkan pena kembali
    pen.penup()
    pen.goto(int(temp[1]), int(temp[2]))
    pen.pendown()
    pen.left(60)

    # untuk mengecek apakah input ukurannya merupakan angka negatif
    for i in range (3, 5):
        if (int(temp[i]) < 0):
            print("Terdapat kesalahan input (memasukkan nilai negatif) pada baris ke {}" .format(line))
            temp[i] = str(abs(int(temp[i])))

    # perulagan untuk menggambar petal
    for i in range(int(temp[3])):
        for j in range (0,2):
            pen.circle(int(temp[4]), 60)
            pen.left(120)
        pen.left(360 / int(temp[3]))

def draw_hexagon(pen, temp, line):
    # mengangkan pena agar tidak menggambar saat memindahkan posisi pena, memindahkan posisi pena, dan menurunkan pena kembali
    pen.penup()
    pen.goto(int(temp[1]), int(temp[2]))
    pen.pendown()

    # untuk mengecek apakah input ukurannya merupakan angka negatif
    if (int(temp[3]) < 0):
        print("Terdapat kesalahan input (memasukkan nilai negatif) pada baris ke {}" .format(line))
        temp[3] = str(abs(int(temp[3])))

    # perulagan untuk menggambar hexagon
    for i in range (0, 6):
        pen.right(60)
        pen.forward(int(temp[3]))

def draw_octagon(pen, temp, line):
    # mengangkan pena agar tidak menggambar saat memindahkan posisi pena, memindahkan posisi pena, dan menurunkan pena kembali
    pen.penup()
    pen.goto(int(temp[1]), int(temp[2]))
    pen.pendown()
    pen.right(8)

    # untuk mengecek apakah input ukurannya merupakan angka negatif
    if (int(temp[3]) < 0):
        print("Terdapat kesalahan input (memasukkan nilai negatif) pada baris ke {}" .format(line))
        temp[3] = str(abs(int(temp[3])))

    # perulagan untuk menggambar octagon
    for i in range (0,8):
        pen.right(45)
        pen.forward(int(temp[3]))

# Fungsi untuk mengcek apakah ada kesalahan penulisan dalam input, jika hanya salah satu huruf, identifikasi kebenaran dan lanjutkan menggambar
def cek_typo(cek, line):
    res = 0
    # jika huruf pertama s , akan dicek kemiripan dengan square
    if (cek[0] == 's'):
        correct = 'square'
        # untuk membandingkan string input dan string yang seharusnya
        for i in range (len(cek)) :
            if (cek[i] == correct[i]) :
                res += 1
        # jika kesalahan hanya satu atau lebih, maka perintah akan dijalankan
        if (res >= len(cek) - 1):
            if (res == len(cek) - 1):
                print('Terdapat kesalahan penulisan pada baris ke {}'.format(line+1)) 
            return 'square'

    # jika huruf pertama r , akan dicek kemiripan dengan rectangle
    elif (cek[0] == 'r') :
        correct = 'rectangle'
        # untuk membandingkan string input dan string yang seharusnya
        for i in range (len(cek)) :
            if (cek[i] == correct[i]) :
                res += 1
        # jika kesalahan hanya satu atau lebih, maka perintah akan dijalankan
        if (res >= len(cek) - 1):
            if (res == len(cek) - 1):
                print('Terdapat kesalahan penulisan pada baris ke {}'.format(line+1)) 
            return 'rectangle'

    # jika huruf pertama c , akan dicek kemiripan dengan circle
    elif (cek[0] == 'c'):
        correct = 'circle'
        # untuk membandingkan string input dan string yang seharusnya
        for i in range (len(cek)) :
            if (cek[i] == correct[i]) :
                res += 1
    # jika kesalahan hanya satu atau lebih, maka perintah akan dijalankan
        if (res >= len(cek) - 1):
            if (res == len(cek) - 1):
                print('Terdapat kesalahan penulisan pada baris ke {}'.format(line+1)) 
            return 'circle'

    # jika huruf pertama p , akan dicek kemiripan dengan petal
    elif (cek[0] == 'p'):
        correct = 'petal'
        # untuk membandingkan string input dan string yang seharusnya
        for i in range (len(cek)) :
            if (cek[i] == correct[i]) :
                res += 1
        # jika kesalahan hanya satu atau lebih, maka perintah akan dijalankan
        if (res >= len(cek) - 1):
            if (res == len(cek) - 1):
                print('Terdapat kesalahan penulisan pada baris ke {}'.format(line+1)) 
            return 'petal'

    # jika huruf pertama h , akan dicek kemiripan dengan hexagon
    elif (cek[0] == 'h'):
        correct = 'hexagon'
        # untuk membandingkan string input dan string yang seharusnya
        for i in range (len(cek)) :
            if (cek[i] == correct[i]) :
                res += 1
        # jika kesalahan hanya satu atau lebih, maka perintah akan dijalankan
        if (res >= len(cek) - 1):
            if (res == len(cek) - 1):
                print('Terdapat kesalahan penulisan pada baris ke {}'.format(line+1)) 
            return 'hexagon'

    # jika huruf pertama o , akan dicek kemiripan dengan octagon
    elif (cek[0] == 'o'):
        correct = 'octagon'
        # untuk membandingkan string input dan string yang seharusnya
        for i in range (len(cek)) :
            if (cek[i] == correct[i]) :
                res += 1
        # jika kesalahan hanya satu atau lebih, maka perintah akan dijalankan
        if (res >= len(cek) - 1):
            if (res == len(cek) - 1):
                print('Terdapat kesalahan penulisan pada baris ke {}'.format(line+1)) 
            return 'octagon'


def main():
    """Executes main program."""
    # The program starts by asking user to select a file to read
    # agar input selalu diminta sampai user memasukkan file yang berformat .txt
    while True:
        try:
            selected_file = choose_file()
            if (selected_file[-1:-4:-1] == 'txt'):
                break
            else:
                print("Format file salah atau anda belum memasukkan file")
        except Exception:
            print("Type file salah!")

    # debug:
    print ("Selected file: {}".format (selected_file))
    # in your assignment, you should open this selected file and
    # read the drawing commands
    infile = open(selected_file, 'r')
    # membuat judul turtle dengan baris pertama dari input
    turtle.title(judul(infile.readline()))
    # Create the canvas where shapes will be draw onto
    canvas = turtle.Screen()

    # Create the pen object that will be used for drawing shapes
    pen = turtle.Turtle()

    # menngatur kecepatan menggambar, mengangkat pena, mengubah mode warna
    pen.speed(100)
    pen.penup()
    turtle.colormode(255)
    # membaca keseluruhan file dari baris kedua (setelah judul), menghitung jumlah baris, dan membuat list berdasarkan baris
    all_input = infile.read() 
    loop = all_input.count("\n")
    all_input = all_input.split("\n")
    # membuat var baru yang berisi bari ke i atau list all_input[i] dan membuat list dengan memisahkan berdasarkan spasi 
    temp = all_input[0]
    temp = temp.split(" ")
    # inisiasi untuk melakukan looping
    i = 1

    # perulangan yang merupakan inti program untuk menggambar, dan terus jalan selama belum mencapai baris terakhir input
    while (i <= loop):
        # kode untuk mengubah warna sesuai input
        if (temp[0].lower() == "color"):
            if (temp[1].lower() == "random"):
                pen.color(random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))

            else:
                for j in range (1,3):
                    # kode untuk melihat apakah input warna valid, jika tidak maka akan dipilih angka random
                    if (int(temp[j]) > 255):
                        print("Pada baris ke {} terdapat kesalahan input warna" .format(i+1))
                        temp[j] = str(random.randrange(0,256))
                pen.color(int(temp[1]), int(temp[2]), int(temp[3]))

            # untuk lanjut ke baris selanjutnya
            temp = all_input[i]
            temp = temp.split(" ")
            i += 1

        # kode untuk melihat apakah baris ke dua diberikan input warna atau tidak, jika tidak maka akan dipilih warna random
        elif (i == 1 and temp[0].lower() != "color"):
            print("Baris ke {} tidak dilakukan pemberian warna" .format(i))
            pen.color(random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))

        pen.penup()
        # kode untuk melihat input yang merupakan baris kosong
        if (temp[0] == ""):
            print("Baris ke {} merupakan baris kosong" .format(i+1))
            temp = all_input[i]
            temp = temp.split(" ")

        # kode untuk memanggil fungsi untuk melihat kesalahan penulisan
        elif (temp[0] != "color"):
            temp[0] = cek_typo(temp[0].lower(), i)

        # kode untuk melakukan perintah menggambar sesuai input
        if (temp[0].lower() == "square"):
            draw_square(pen, temp, i)

        if (temp[0].lower() == "rectangle"):
            draw_rectangle(pen, temp, i)

        if (temp[0].lower() == "circle"):
            draw_circle(pen, temp, i)

        if (temp[0].lower() == "petal"):
            draw_petal(pen, temp, i)

        if (temp[0].lower() == "hexagon"):
            draw_hexagon(pen, temp, i) 

        if (temp[0].lower() == "octagon"):
            draw_octagon(pen, temp, i)

        if (i < loop):
            temp = all_input[i]
            temp = temp.split(" ")

        # untuk perulangan while
        i += 1

    # menutup file yang sedang dibuka, menyembunyikan kepala turtle, dan menutup canvas ketika canvas diklik
    infile.close()
    pen.hideturtle()
    canvas.exitonclick()
    return 0

if __name__ == '__main__':
    main()
