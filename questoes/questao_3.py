## QUESTÃO 3 ##
#
# Crie uma implementação da cifra rotacional, às vezes também chamada de cifra de César.
# 
# A cifra de César é uma simples cifra de deslocamento que se baseia na transposição 
# de todas as letras do alfabeto usando uma chave inteira entre 0 e 26. 
# O uso da chave 0 ou 26 sempre produzirá a mesma saída devido à aritmética modular. 
# A letra é deslocada para tantos valores quanto o valor da chave.
#
# A notação geral para cifras rotacionais é ROT + <chave>. A cifra rotacional mais comumente usada é a ROT13.
#
# Um ROT13 no alfabeto latino seria o seguinte:
# 	Normal:  abcdefghijklmnopqrstuvwxyz
#	Cifrado: nopqrstuvwxyzabcdefghijklm
#
# Exemplos:
#	Entrada: ROT5 omg 
#          Saída: trl
#	Entrada: ROT0 c 
#          Saída: c
#	Entrada: ROT26 Cool 
#          Saída: Cool
#	Entrada: ROT13 The quick brown fox jumps over the lazy dog. 
#          Saída: Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
#	Entrada: ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. 
#          Saída: The quick brown fox jumps over the lazy dog.
#
# Se um valor de entrada inválido for digitado, a seguinte mensagem 
# deve ser impressa: 'Erro'. 
# Entradas inválidas podem ser entradas que contém códigos de rotações 
# inválidos ou mensagens contendo caracteres que não estão no alfabeto. 
# Exemplos:
# 	Entrada: RARA abc Saída: Erro
# 	Entrada: ROT5 c99 Saída: Erro
#
# As entradas devem ser sempre compostas por ROT + <chave> + ' ' + 'mensagem', 
# ou seja, a cifra rotacional e a mensagem a ser cifrada separados por vírgula.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    inputString = input("Digite a entrada: ")

    if ("ROT" in inputString):
        numberRot = inputString[3:5].strip()
        text = inputString[5:].strip()
        numberRot = int(numberRot)
        if numberRot < 0 or numberRot > 26:
            print("Erro")
            return

        originalAlpha = 'abcdefghijklmnopqrstuvwxyz'
        rot = originalAlpha[0:numberRot]
        newAlpha = originalAlpha[numberRot:] + rot
        index = 0
        newText = ''

        while (index < len(text)):
            char = text[index]
            if char.isupper():
                char = char.lower()
                originalIndex = originalAlpha.find(char)
                newChar = newAlpha[originalIndex].upper()
            elif char is " " or char is ".":
                newChar = char
            elif originalAlpha.find(char) == -1:
                print("Erro")
                return
            else:
                originalIndex = originalAlpha.find(char)
                newChar = newAlpha[originalIndex]
            newText = newText + newChar
            index = index + 1
    
        print(newText)
    
    else:
        print("Erro")


if __name__ == '__main__':
    main()
