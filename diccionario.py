dict = {
    "Tincho": "Un chico de clase alta que es arrogante y se preocupa por su estatus social.",
    "Quilombo": "Caos, desorden o problema.",
    "Joda": "Fiesta o un chiste.",
    "Facha": "Buen estilo o aspecto físico.",
    "Bardo": "Discusión o problema.",
    "Boludo": "Puede ser un insulto o de cariño, significa tonto.",
    "Che": "Para llamar la atención de alguien",
    "Pibe": "Para dirijirse a un niño jovén, o para una persona en general.",
}

for x in range (1, 6):
    word = input("Escribí una palabra que no entiendas: ")
    if word in dict.keys():
        print(word, "significa", dict[word])
    else: 
        print("Esa palabra no está en el diccionario.")
