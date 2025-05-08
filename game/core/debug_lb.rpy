if not config.developer:
    init python:
        from renpy.store import config
        from renpy.store import ui
        import os

        def scriptline():
            fullfn, line = renpy.get_filename_line()
            ui.button(clicked=None, xpos=config.screen_width, xanchor=1.0, ypos=0, xpadding=6, xminimum=200)
            ui.text("Script line: %s:%d" % (os.path.basename(fullfn), line))
        def sayimagetag():
            ui.button(clicked=None, xpos=config.screen_width, xanchor=1.0, ypos=30, xpadding=6, xminimum=200)
            if renpy.get_say_image_tag() == None:
                ui.text("Say Image tag: NONE")
            else:
                ui.text("Say Image tag: " + renpy.get_say_image_tag())
        def listtf():
            ui.button(clicked=None, xpos=config.screen_width, xanchor=1.0, ypos=60, xpadding=6, xminimum=200)
            if renpy.get_say_image_tag() == None:
                ui.text("List of TFs (IDs): List is empty!")
            else:
                ui.text("List of TFs (IDs): %s" % id(renpy.get_at_list(renpy.get_say_image_tag())))
        def skippinginfo():
            ui.button(clicked=None, xpos=config.screen_width, xanchor=1.0, ypos=90, xpadding=6, xminimum=200)
            ui.text("Skipping?: %s" % config.skipping)

        config.overlay_functions.append(scriptline)
        config.overlay_functions.append(sayimagetag)
        config.overlay_functions.append(listtf)
        config.overlay_functions.append(skippinginfo)


