## Copyright 2019-2024 Azariel Del Carmen (bronya_rand). All rights reserved.

## achievements.rpy
# This file contains the code for the achievements menu and notification that 
# shows your progress throughout the mod.

default persistent.achievements = {}

init -1 python in achievements:
    from store import persistent, im
    achievementList = {}
    
    # This class declares the code to make a achievement (Non-Counting).
    # Syntax:
    #   name - This variable contains the human-readable name of the achievement.
    #   description - This variable contains the human-readable description of your
    #       achievement.
    #   image - This variable contains the path or image tag of the achievement.
    #   locked_desc - This variable contains the human-readable description of your
    #       achievement when it is locked.
    #   show_desc_while_locked - This variable determines whether to show the actual description
    #       of the achievement or a locked one.
    #
    # To unlock an achievment, simply do `$ X.unlock()` (without the `'s where X is your achievements' variable name).
    class Achievement(object):

        def __init__(self, name, description, image, locked_desc="???", show_desc_while_locked=False):
            # The human readable name of the achievement.
            self.name = name

            # The description of the achievement.
            self.description = description

            # The image variable or path of the achievement image.
            self.image = image

            # The image variable or path of the achievement image if the 
            # achievement hasn't been unlocked.
            self.locked = im.MatrixColor(image, im.matrix.desaturate())
            self.locked_desc = locked_desc

            self.show_desc_while_locked = show_desc_while_locked

            if self.name not in persistent.achievements:
                persistent.achievements[self.name] = {
                    "unlocked": False,
                    "current_count": 0,
                }

            self.unlocked = persistent.achievements[self.name]['unlocked']

            achievementList[self.name] = self
        
        def unlock(self):
            self.unlocked = True
            persistent.achievements[self.name]['unlocked'] = True
            renpy.show_screen("achievement_notify", self)
    
    # This class declares the code to make a achievement (Non-Counting).
    # This class has the same syntax as Achievement but 1 more argurment.
    # Refer to Achievement for the rest of the argurments here.
    # Syntax:
    #   max_count = The total counts needed to unlock the achievement
    class AchievementCount(Achievement):
        def __init__(self, name, description, image, show_desc_while_locked=False, max_count=100):
            Achievement.__init__(self, name, description, image, show_desc_while_locked)

            self.current_count = persistent.achievements[self.name]['current_count']
            self.max_count = max_count
        
        def increase_count(self):
            self.current_count += 1
            persistent.achievements[self.name]['current_count'] += 1
            if self.current_count == self.max_count:
                self.unlock()

init python:
    selectedAchievement = None
    # This section declares the achievements. See the 'Achievements' class
    # syntax to declare one.
    startup = achievements.Achievement("Welcome to DDLC!", "Thanks for accepting the TOS.",
            "gui/logo.png")
    steam = achievements.Achievement("Steam", "Steam User.",
            "gui/logo.png")
    lets_count = achievements.AchievementCount("Count", "1-3",
            "gui/logo.png", max_count=3)

    # Fast Sort (DO NOT REMOVE)
    achievements.achievementList = {k: achievements.achievementList[k] for k in sorted(achievements.achievementList)}

## Achievements Screen #############################################################
##
## This screen is used to make a achievements view of all possible achievements
## the mod has in the main menu.
##
## Syntax:
##   al.image - This variable contains the path or image tag of the achievement.
##   al.locked - This variable contains the locked image of the achievement.
##   al.persistent - This variable contains the name of the in-game variable to check
##                      if the achievement is completed or not.
##   al.maxCount - This variable contains the number needed for the achievement to be
##                  unlocked.
##   gl.description - This variable contains the description of the achievement.





