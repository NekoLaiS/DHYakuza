## Gallery Screen #############################################################
##
## This screen is used to make a gallery view of in-game art to the player in 
## the main menu.
##
## Syntax:
##   gl.image - This variable contains the path or image tag (sayori 1a) of the 
##              image.
##   gl.small_size - This variable contain the path or image tag of a shorten version
##                   of the image in the gallery.
##   gl.name - This variable contains the human-readable name of the image in the
##               gallery.
##   gl.sprite - This variable checks if the image declared is a character sprite.
##   gl.locked - This variable checks if this image should not be included in
##               the gallery until it is shown in-game.
screen gallery():

    tag menu

    use game_menu(_("Gallery")):
        
        fixed:

            vpgrid:
                id "gvp"

                rows math.ceil(len(galleryList) / 3.0)

                if len(galleryList) > 3:
                    cols 3
                else:
                    cols len(galleryList)

                spacing 25
                mousewheel True

                xalign 0.5
                yalign 0.5

                for name, gl in galleryList.items():
                    vbox:
                        if gl.unlocked:
                            imagebutton: 
                                idle gl.small_size
                                action [SetVariable("current_img_name", name), ShowMenu("preview"), With(Dissolve(0.5))]
                            text "[name]": 
                                xalign 0.5
                                color "#555"
                                outlines []
                                size 14
                        else:
                            imagebutton: 
                                idle "mod_assets/mod_extra_images/galleryLock.png"
                                action Show("dialog", message="This image is locked. Continue playing [config.name] to unlock this image.", ok_action=Hide("dialog"))
                            text "Locked": 
                                xalign 0.5
                                color "#555"
                                outlines []
                                size 14

            vbar value YScrollValue("gvp") xalign 0.99 ysize 560

## Gallery Screen #################################################################
##
## This screen shows the currently selected screen to the player in-game.
screen preview():

    tag menu

    hbox: 
        add galleryList[current_img_name].image yoffset 40
    hbox:
        add Solid("#fcf") size(config.screen_width, 40)

    hbox:
        ypos 0.005
        xalign 0.5 
        text current_img_name: 
            color "#000"
            outlines[]
            size 24 

    hbox:
        ypos 0.005
        xalign 0.98
        if galleryList[current_img_name].artist:
            textbutton "?":
                text_style "navigation_button_text"
                action Show("dialog", message="Artist: " + galleryList[current_img_name].artist, ok_action=Hide("dialog"))

        textbutton "E":
            text_style "navigation_button_text"
            action Function(galleryList[current_img_name].export) 

        textbutton "X":
            text_style "navigation_button_text"
            action ShowMenu("gallery")

    textbutton "<":
        text_style "navigation_button_text"
        xalign 0.0
        yalign 0.5
        action Function(next_image, True)

    textbutton ">":
        text_style "navigation_button_text"
        xalign 1.0
        yalign 0.5
        action Function(next_image)

    on "replaced" action With(Dissolve(0.5))