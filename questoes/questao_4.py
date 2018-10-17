## QUESTÃO 4 ##
#
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data 
# será inserida em formato numérico com três instruções de entrada separadas; 
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    date = input("Type the date: ")

    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:])

    validDate = (month > 0 and month <= 12) and (day > 0 and day <= 31)
    bissextileYear = year%4 == 0 and year%100 != 0 or year%400==0

    if (validDate):
        if month == 2:
            if bissextileYear:
                if day < 29: day = day + 1
                elif day > 29: return
                else:
                    day = 1
                    if month < 12:
                        month = month + 1
                    else:
                        month = 1
                        year = year + 1
            else:
                if day < 28: day = day + 1
                elif day > 28: return
                else:
                    day = 1
                    if month < 12:
                        month = month + 1
                    else:
                        month = 1
                        year = year + 1

        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day < 30: day = day + 1
            elif day == 31: return
            else:
                day = 1
                if month < 12:
                    month = month + 1
                else:
                    month = 1
                    year = year + 1
        
        else:
            if day < 31: day = day + 1
            else:
                day = 1
                if month < 12:
                    month = month + 1
                else:
                    month = 1
                    year = year + 1

        print("{:04d}-{:02d}-{:02d}".format(year, month, day))

    
if __name__ == '__main__':
    main()
