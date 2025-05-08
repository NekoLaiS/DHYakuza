import pymorphy3

def name_declension(name: str, case: str) -> str:
    morph = pymorphy3.MorphAnalyzer()
    name = morph.parse(name)[0]

    match case:
        case "what": name = name.inflect({"datv"})
        case "who": name = name.inflect({"ablt"})
        case "whom": name = name.inflect({"gent"})
        case "about_someone": name = name.inflect({"loct"})
        case "someone": name = name.inflect({"accs"})
    
    return name.word.capitalize()

print(name_declension("Андрей", "what"))
print(name_declension("Андрей", "who"))
print(name_declension("Андрей", "whom"))
print(name_declension("Андрей", "about_someone"))
print(name_declension("Андрей", "someone"))