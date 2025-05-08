screen achievements():

    tag menu
    style_prefix "achievements"

    use game_menu(_("Awards")):

        fixed:
            # This vbox is responsible for the achievement display above the list
            # of possible achievements to display the selected achievements' info.
            vbox:
                xpos 0.26
                ypos -0.1

                hbox:

                    if selectedAchievement:

                        add ConditionSwitch(
                                selectedAchievement.unlocked, selectedAchievement.image, "True",
                                selectedAchievement.locked) at achievement_scaler(128)
                    else:
                        null height 128

                    spacing 20

                    vbox:
                        xsize 400
                        ypos 0.2

                        if selectedAchievement:

                            text selectedAchievement.name:
                                font gui.name_font
                                color "#fff"
                                outlines [(2, "#505050", 0, 0)]

                            if not selectedAchievement.unlocked and not selectedAchievement.show_desc_while_locked:
                                if isinstance(selectedAchievement, AchievementCount):
                                    text "[selectedAchievement.locked_desc] ([selectedAchievement.current_count] / [selectedAchievement.max_count])"
                                else:
                                    text selectedAchievement.locked_desc
                            else:
                                if isinstance(selectedAchievement, AchievementCount):
                                    text "[selectedAchievement.description] ([selectedAchievement.current_count] / [selectedAchievement.max_count])"
                                else:
                                    text selectedAchievement.description
                        else:
                            null height 128

            # This vpgrid is responsible for the list of achievements in the game.
            vpgrid:
                id "avp"
                rows math.ceil(len(achievementList) / 6.0)
                if len(achievementList) > 6: 
                    cols 6
                else: 
                    cols len(achievementList)

                spacing 25
                mousewheel True

                xalign 0.5
                yalign 0.85
                ysize 410

                for name, al in achievementList.items():

                    imagebutton:
                        idle Transform(ConditionSwitch(
                                al.unlocked, al.image, "True",
                                al.locked), size=(128,128))
                        action SetVariable("selectedAchievement", al)

            vbar value YScrollValue("avp") xalign 1.01 ypos 0.2 ysize 400

        textbutton "?":
            style "return_button"
            xpos 0.99 ypos 1.1
            action ShowMenu("dialog", "{b}Help{/b}\nGray icons indicate that this achievement is locked.\nContinue your progress in [config.name]\nto unlock all the achievements possible.", ok_action=Hide("dialog"))

        if config.developer:
            textbutton "Test Notif":
                style "return_button"
                xpos 0.8 ypos 1.1
                action ShowMenu("achievement_notify", startup)

## Achievements Notify Screen #############################################################
##
## This screen is used to notify a user of a unlocked achievement.
##
## Syntax:
##   reward.image - This variable contains the path or image tag of the achievement.
##   reward.name - This variable contains the locked image of the achievement.
## 
## To call on this menu, do 'show screen achievement_notify(X)' where X is the achievement in question itself.
## Make sure to set the variable assign to it or else it will show up as locked.
screen achievement_notify(reward):
    
    style_prefix "achievements"

    frame at achievement_notif_transition:
        xsize 300
        ysize 90
        xpos 0.4

        hbox:
            xalign 0.27
            yalign 0.5
            add reward.image at achievement_scaler(50)
            spacing 20
            vbox:
                spacing 5
                text "Achievement Unlocked!" size 16
                text reward.name size 14
    
    timer 4.0 action [Hide("achievement_notify"), With(Dissolve(1.0))]