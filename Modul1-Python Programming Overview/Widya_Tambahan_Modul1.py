## Soal No.1 :
## Buatlah suatu fungsi yang mengembalikan panjang terpendek dari suatu string kata yang terpisahkan oleh spasi (20 Point)
## Note: Kembalikan panjang dari kata yang terpendek, bukan katanya yang dikembalikan

## Answer :
def find_short(s) :
    word_split = s.split()
    word = 99999
    for i in word_split :
        if len(i) < word :
            word = len(i)
    return word

# print(find_short("I am studying"))
# print(find_short("Where did you go"))

## Based on Soal :
print(find_short("Many people get up early in the morning"))
print(find_short("Every office would getting newest monitor"))
print(find_short("Create new file after this morning"))



## Soal No.2 :
## Buatlah suatu fungsi yang menerima parameter angka positif, 
## dan mengembalikan total berapa kali harus dikalikan digit dari angka tersebut hingga mencapai 1 digit (20 Point).

## Answer :
def persistence(n) :
    angka = n
    jumlah_perulangan = 0
    while (len(str(angka)) > 1):
        hasil_kali = 1
        for i in str(angka) :
            hasil_kali *= int(i)
        angka = hasil_kali
        jumlah_perulangan += 1
    return jumlah_perulangan

##Try :
# print(persistence(28))
# print(persistence(1000))

##Based on Soal :
print(persistence(39))
print(persistence(999))
print(persistence(4))



## Soal No.3 :
## Buatlah suatu fungsi yang menerima dimensi dari Rows x Columns,
## sebagai parameter untuk membuat tabel multipikasi dengan ukuran sesuai dari dimensi yang
## diberikan dimana setiap value di tabel row berikutnya adalah hasil perkalian value di row pertama 
## dengan row keberapa value tersebut berada (30 point)

## Answer :
def multiplication_table(row,col) :
    z = ''
    for i in range (1, row + 1):
        for j in range (1, col + 1):
            z += str(i*j) + " "
        if i != row :
            z += '\n'
    return z

##Try:
# print(multiplication_table(5,5))

##Based on Soal:
print(multiplication_table(3,3))
print(multiplication_table(5,3))
print(multiplication_table(3,5))



## Soal No.4 :
## Buatlah suatu fungsi yang menerima string, dimana setiap huruf di string tersebut
## digantikan dengan posisinya di urutan alphabet. Bila ada string lain selain huruf alphabet, jangan dihiraukan (30 point).
## Note: “a” = 1, “b” = 2, dst.

## Answer :
def alphabet_position(text) :
    hasil = ""
    dictionary_huruf = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    for huruf in text.lower() :
        if huruf in dictionary_huruf.keys():
            hasil += str(dictionary_huruf[huruf])
            hasil += " "
    return hasil

##Try :
#print(alphabet_position("Tuesday"))
# print(alphabet_position("Widya"))

##Based on Soal :
print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("it’s never too late to try"))
print(alphabet_position("Have you done your homework?"))

