import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def dicionario(word):
    if word.lower() in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))>0:
        correct_word = get_close_matches(word, data.keys())[0]
        resp = input("Você quis dizer '"+correct_word+"'? (S/N)\n")
        if resp.lower() == 's':
            return data[correct_word]
        else:
            return ["Desculpe não encontramos a palavra."]
    else:
        return ["A palavra não existe."]

word = input("Qual palavra deseja buscar?\n")

significado = dicionario(word)

print("\n--------DICIONARIO--------\n")
for ans in significado:
    print(ans)
print("\n--------------------------\n")
