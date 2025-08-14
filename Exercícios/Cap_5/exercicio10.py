import re

frase = 'Uma vez flamengo, sempre flamengo! Flamengo sempre eu hei de ser!'

# Encontrar todas as palavras que aparecem depois de "Flamengo" (case-insensitive)
palavras_apos_flamengo = re.findall(r'(?i)Flamengo\s+(\w+)', frase)

# Pegar a segunda ocorrência
segunda_apos_flamengo = palavras_apos_flamengo[1] if len(palavras_apos_flamengo) > 1 else None

# Encontrar a palavra depois de "hei"
palavra_apos_hei = re.search(r'(?i)hei\s+(\w+)', frase)
palavra_apos_hei = palavra_apos_hei.group(1) if palavra_apos_hei else None

print("Palavra após 2ª 'Flamengo':", segunda_apos_flamengo)
print("Palavra após 'hei':", palavra_apos_hei)
