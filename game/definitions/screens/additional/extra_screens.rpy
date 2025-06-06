screen extras():
    tag menu
    style_prefix "extras"

    use game_menu(_("Extras")):

        fixed:
                
            vpgrid id "ext":

                rows 1
                cols 3
                        
                xalign 0.5
                yalign 0.4

                spacing 18

                if enable_gallery:
                    frame:
                        xsize 160
                        ysize 140

                        vbox:
                            xalign 0.5
                            yalign 0.5

                            imagebutton:
                                idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/gallery.png", (40, 75), Text("Gallery", style="extras_text"))
                                hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/gallery.png", (38, 73), Text("Gallery", style="extras_hover_text"))
                                action ShowMenu("gallery")

                if enable_achievements: 
                    frame:
                        xsize 160
                        ysize 140

                        vbox:
                            xalign 0.5
                            yalign 0.5
            
                            imagebutton:
                                idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/achievements.png", (40, 75), Text("Awards", style="extras_text"))
                                hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/achievements.png", (38, 73), Text("Awards", style="extras_hover_text"))
                                action ShowMenu("achievements")

                frame:
                    xsize 160
                    ysize 140

                    vbox:
                        xalign 0.5
                        yalign 0.5
            
                        imagebutton:
                            idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/about.png", (40, 75), Text("Credits", style="extras_text"))
                            hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/about.png", (38, 73), Text("Credits", style="extras_hover_text"))
                            action ShowMenu("about")

            vbar value YScrollValue("ext") xalign 0.99 ysize 560