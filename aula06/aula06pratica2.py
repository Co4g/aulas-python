#Se adicionarmos '.is' após a variável, podemos receber respostas em boleano na hora do print:

n = input ('Digite algo: ')
print(n, 'é um número ou letra?', n.isalnum()) #importante lembrar dos () vazios após o .is.
#No caso a seguir, o valor retornado é 'True', pois o valor digitado foi 5 e ele é alfanumérico.
#Outros tipos de .is envolvem .isnumeric para números e .isalpha para alfabeto.

