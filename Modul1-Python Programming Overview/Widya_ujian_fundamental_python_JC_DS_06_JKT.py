
# # Soal 1 Year of Investment
def calculate_years(principal, interest, tax, desired):
    year = 0
    if principal >= desired:
        return print(year)
    else:
        while True:
            principal += ((1 - tax) * principal * interest)
            year += 1
            if principal >= desired:
                return print(year)

calculate_years(1000.00, 0.05, 0.18, 1100.00)
calculate_years(1200.00, 0.17, 0.05, 2000.00)
calculate_years(1500.00, 0.07, 0.6, 5000.00)

# # Soal 2 Number in Expanded Form
def expandedForm(num):
    list_form = list(str(num))
    str_form = ''

    for i,val in zip(range(len(list_form)-1,-1,-1),list_form):
        temp = int(val)*10**i
        if(temp > 0):
            str_form += str(temp)+'+'
        if(i == 0 and str_form[-1] == '+'):
            str_form = str_form[:-1]
    print(str_form)

expandedForm(12)
expandedForm(42)
expandedForm(70304)


# # Soal 3 Build Towers
def tower_builder(n_floors, block_size):
    w,h = block_size
    tower = ''
    for i,j in zip(range(1,n_floors*2,2),range(n_floors-1,-1,-1)):
        for kolom_spasi in range(h):
            for jumlah_spasi in range(j):
                for baris_spasi in range(w):
                    tower += ' '
            for jumlah_spasi in range(i):
                for baris in range(w):
                    tower += '*'
            tower += '\n'
    return print(tower)

tower_builder(3,(2,3))
tower_builder(6,(2,1))

def tower_triangle(n_floors,triangle_floor):
    spasi = triangle_floor*2-1
    tower = ''
    for i,j in zip(range(1,n_floors*2,2),range(n_floors-1,-1,-1)):
        for jumlah_bintang, jumlah_spasi in zip(range(1,triangle_floor*2,2),range(triangle_floor-1,-1,-1)):
            for z in range(j):
                for out_spasi in range(spasi):
                    tower += ' '
            for k in range(i):
                for in_spasi in range(jumlah_spasi):
                    tower += ' '
                for in_bintang in range(jumlah_bintang):
                    tower += '*'
                for in_spasi in range(jumlah_spasi):
                    tower += ' '
            tower += '\n'
    return print(tower)

tower_triangle(3,2)
tower_triangle(3,3)