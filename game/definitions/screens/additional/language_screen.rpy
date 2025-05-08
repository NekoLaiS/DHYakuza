screen choose_language():
    default local_lang = _preferences.language
    default chosen_lang = _preferences.language

    modal True
    style_prefix "radio"

    add "gui/overlay/confirm.png"

    frame:
        style "confirm_frame"

        vbox:
            xalign .5
            yalign .5
            xsize 760
            spacing 30

            label renpy.translate_string(_("{#in language font}Please select a language"), local_lang):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign .5
                for tran in translations:
                    vbox:
                        for tlid, tlname in tran:
                            textbutton tlname:
                                xalign .5
                                action SetScreenVariable("chosen_lang", tlid)
                                hovered SetScreenVariable("local_lang", tlid)
                                unhovered SetScreenVariable("local_lang", chosen_lang)

            $ lang_name = renpy.translate_string("{#language name and font}", local_lang)
            
            hbox:
                xalign 0.5
                spacing 100

                textbutton renpy.translate_string(_("{#in language font}Select"), local_lang):
                    style "confirm_button"
                    action [Language(chosen_lang), Return()]
                    
translate None strings:
    old "{#language name and font}"
    new "English"

label choose_language:
    call screen choose_language
    return
