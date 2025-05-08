init offset = -900

default enable_gallery = True
default enable_achievements = True
default persistent.has_chosen_language = False
default translations = scan_translations()

define player = _("MC")
define s_name = _("Sayori")
define m_name = _("Monika")
define n_name = _("Natsuki")
define y_name = _("Yuri")

define narrator = Character(what_prefix='', what_suffix='')
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"')
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"')
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"')
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"')
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"')

## Developer Mode
define config.developer = True


init python:
    def reset_persistent():
        persistent._clear(progress=True)
        renpy.utter_restart()
        # You can also use renpy.quit(relaunch=True) if you want to (Note: It takes longer.)

    def save_playtime(d):
        d["playtime"] = renpy.get_game_runtime()

    config.save_json_callbacks.append(save_playtime)

    def screenshot_callback(path):
        message = "Ты сохранил говно в %s." % path
        with open(path, "rb") as g:
            #fit="contain" because image manipulators suck
            image = Transform(im.Data(g.read(), path), fit="contain")
    
        renpy.show_screen("notify", message=message)

    config.screenshot_callback = screenshot_callback