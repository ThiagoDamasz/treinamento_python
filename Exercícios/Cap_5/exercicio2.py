palavras = 'O Flamengo é o melhor time do Brasil.'.split()

resultado = map(lambda w:[w.upper(), w.lower(), len(w)], palavras)    