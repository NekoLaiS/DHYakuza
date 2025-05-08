init -950 python in morphiter:
    def morphiter(player):
        try:
            import pymorphy3
            import pymorphy3_dicts_ru
            morph = pymorphy3.MorphAnalyzer(path=pymorphy3_dicts_ru.get_path())
            name = morph.parse(player)[0]

            name_what = name.inflect({"datv"}).word.capitalize()
            name_who = name.inflect({"ablt"}).word.capitalize()
            name_whom = name.inflect({"gent"}).word.capitalize()
            name_about_someone = name.inflect({"loct"}).word.capitalize()
            name_someone = name.inflect({"accs"}).word.capitalize()

        except Exception:
            name_what = player
            name_who = player
            name_whom = player
            name_about_someone = player
            name_someone = player

        return name_what, name_who, name_whom, name_about_someone, name_someone


# Руководство

    # "Имя в дательном падеже: [name_what]"
    # "Имя в творительном падеже: [name_who]"
    # "Имя в родительном падеже: [name_whom]"
    # "Имя в предложном падеже: [name_about_someone]"
    # "Имя в винительном падеже: [name_someone]"