texto = "el mono momoxy toca el xilofon."

def contar_palabras_cuat(texto):
    '''Determina cuantas palabras tienen mas de 4 letras.'''
    count = 0
    cant_pal_4 = 0
    for i in texto:
        if i != ' ' and i != '.':
            count += 1
        elif (i == ' ' or i == '.') and count > 4:
            cant_pal_4 += 1
            count = 0
        else:
            count = 0
    return cant_pal_4


def contar_pal_xy(texto):
    ''' Determinar cuantas palabras tenian al menos una vez la letra "x" o la letra "y".'''
    cant_pal_xy = 0
    flag = False
    for i in texto:
        if i != ' ' and i != '.':
            if (i == 'y' or i == 'x') and flag == False:
                cant_pal_xy += 1
                flag = True
        elif i == ' ':
            flag = False
    return cant_pal_xy



def palabras_promedio(texto):
    ''' Determinar el promedio de letras por palabra en todo el texto.'''
    cont_let = 0
    cont_pal = 0
    for i in texto:
        if i != ' ' and i != '.':
            cont_let += 1
        else:
            cont_pal += 1
    return round(cont_let/cont_pal, 2)


#print(palabras_promedio(texto))

#print(contar_pal_xy(texto))

def contar_mo(texto):
    count_mo = 0
    car_a = ''
    flag = False
    for i in texto:
        if i != ' ' and i != '.':
            if i == 'm':
                car_a = i
            elif car_a == 'm' and i == 'o' and flag is False:
                flag = True
            else:
                car_a = ''
                #flag = False
        else:
            if flag is True:
                count_mo += 1
                flag = False

    return count_mo

print(contar_mo(texto))