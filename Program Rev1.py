from os import system

while True:
    print       ('---------------------------------\n')
    print       ('Program Cek Nilai Mahasiswa\n')
    print       ('---------------------------------\n')

    nikMahasiswa            =   int   (input ('Masukkan NIK                             : '))
    nilaiAlgoritma          =   float (input ('Masukkan Nilai Algoritma                 : '))
    nilaiDasarPemrograman   =   float (input ('Masukkan Nilai Dasar Pemrograman         : '))
    nilaiPtik               =   float (input ('Masukkan Nilai PTIK                      : '))
    nilaiRata2              =   (nilaiAlgoritma + nilaiDasarPemrograman + nilaiPtik)/3

    if nilaiRata2 < 10:
        grade = 'Z'
        kataMo = 'Practice makes us right, repetitions make us perfect'
    elif nilaiRata2 < 30:
        grade = 'F'
        kataMo = "Never lost hope, because it is the key to achieve all your dreams"
    elif nilaiRata2 < 50:
        grade = 'E'
        kataMo = "You are never too old to learn"
    elif nilaiRata2 < 70:
        grade = 'D'
        kataMo = "Stop wishing. Start doing"
    elif nilaiRata2 < 80:
        grade = 'C'
        kataMo = "A little progress each day in your self is ads thing up to big result"
    elif nilaiRata2 < 90:
        grade = ('B')
        kataMo = "Don’t be afraid to move, because the distance of 1000 miles starts by a single step"
    else:
        grade = 'A'
        kataMo = "Do not ever give up, the beginning is always the hardest"

    print ('')
    print ('Nilai rata - rata kamu                   :',nilaiRata2)
    print ('\nGrade NIK',nikMahasiswa,'adalah',grade)
    print (kataMo)
    input ('\nTekan sembarang untuk mulai ulang program !') 
    system ('cls') 