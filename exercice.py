#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Ajouter en cours de route
from collections import Counter

def histogram (string: str) -> dict : 
    return dict(Counter(string))


def order(values: list = None) -> bool:
    if values is None:
        # TODO: Demander les valeurs ici
        print("Veuillez entrer deux valeurs : ")
        values = [input() for _ in range(2)]

    return values == sorted(values)  # Sort la liste sans la modifie 
    # return  values.sort()  # Modifie la liste en l'ordonnant


def anagrams(words: list = None) -> bool:
    
    if words is None:
        # TODO: Demander les mots ici
        print("Veuillez entrer deux anagrammes : ")
        words = [sorted(input()) for _ in range(2)] 

    return  words[0] == words[1]


def contains_doubles(items: list) -> bool:
    
    uniques = set(items)
 
    return len(items) == len(uniques)


def best_grades(student_grades: dict) -> tuple:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    
    average = {}
    best_note = 0 

    for student in student_grades:
        notes =  student_grades[student]
        average[student] = (sum(notes) / len(notes))
 
    for student in average:
        if best_note < average[student]:
            name = student

    return name, average[name]

    #sorted_grades = sorted(list(student_grades.items()), key = lambda s: -sum(s[1]) / len(s[1]))
    #best_average = sum(sorted_grades[0][1]) / len(sorted_grades[0][1])
    #return sorted_grades[0][0], best_average


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    histogramme = {}
    
    for char in sentence:
        if char in histogramme:
            histogramme[char] += 1     
        
        else :
            histogramme[char] = 1

    frequency_threshold = 5
    most_frequent_chars = [k for k, v in histogramme.items() if v > frequency_threshold and k != " "]
    print(most_frequent_chars)

    return histogramme, most_frequent_chars.sort(reverse = True)


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 

    recipes = { }
    answer = 'Oui'

    while answer == 'Oui' :
        recipe = input("Quel est le nom de la recette ? ")
        print("Quels sont les 5 ingrédients nécessaire ? ")
        recipes[recipe] = [input() for _ in range(5)]
        answer = input("Voulez-vous ajouter une autre recette ? (Oui ou Non) ")

    return recipes



def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    
    recipe = input("Quel est le nom de la recette ? ")
    print(ingredients.get(recipe))


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(f"La liste est ordonnée : {order()}")

    print(f"On vérifie les anagrammes...")
    print(f"Les deux mots donnés sont des anagrammes : {anagrams()}")

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste ne contient pas de doublons : {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")
    
    sentence = input("Donnez une phrase: ")
    print(histogram(sentence))
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
