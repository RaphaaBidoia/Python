nome = input('Qual seu nome?')
print('muito prazer', nome,)
prazer = input('por favor digite algo:')
print('o que foi digitado é composto apenas por espaço?', prazer.isspace())
print('o que foi digitado é composto por digitos apenas?', prazer.isdigit())
print('o que foi digitado é composto por letras apenas?', prazer.isalpha())
print('o que foi digitado é composto por letras e numeros?', prazer.isalnum())
print('o tipo primitivo do que foi digitado é', type(prazer))