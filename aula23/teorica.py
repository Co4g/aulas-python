#Aula 23 - Tratamento de Erros e Exceções
'''
Para verificar se o usuário está agndo corretamente na hora de prrencher os dados, ou mesmo o código está escrito corretamente, podemos usar o tratamento de erros, que utiliza try e except.
'''
try: #Tente. Tentará executar o código abaixo.
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): #Toda tentativa, precisa de sua exceção, que é o que ocorrerá caso a tentativa não funcione.
    print('Infelizmente, tivemos um problema com os tipos de dados que você digitou!')
except Exception as erro: #Identifica um erro e atribui ele a uma variável.
    #Com a variável erro determinada, podemos criar um print mostrando o erro.
    print(f'O erro encontrado foi{erro.__cause__}') #Aqui usamos a variável erro, com a causa ou causa ou classe do erro.
else: #Opcional, dirá o que ocorrerá caso a tentativa funcione.
    print(f'O resultado é {r:.1f}')
finally: #Define o que ocorrerá, independe da tentativa funcionar ou não.
    print('Volte sempre. Muito obrigado!')
 