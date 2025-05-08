# The script of the game goes in this file.

# The game starts here.

label start:

    scene image "images/bg/club.png":
        zoom 1.5


    show monika casual happ at t32
    m om "You've created a new project Elysium Team."
    show screen invert(0.15, 0.1)
    m lean om "Once you add a story, pictures, and music, you can release it to the world!{p=1.0}{nw}" with dissolve
    show screen invert(0.15, 0.1)
    show m_rectstatic at cgfade
    m worr  "Oh...{p=1.0}{nw}" 
    show screen tear(number=10, offtimeMult=1, ontimeMult=1, offsetMin=0, offsetMax=50, srf=None)
    pause 3.0
    hide screen tear
    show screen invert(0.15, 0.1)
    extend "Fuck...{p=1.0}{nw}"
    show screen invert(0.15, 0.1)
    show screen tear(number=10, offtimeMult=1, ontimeMult=1, offsetMin=0, offsetMax=50, srf=None)
    pause 3.0
    hide screen tear
    show screen invert(0.15, 0.1)
    $ Pause(2.0)
    "{p=1.0}{nw}"
    show screen invert(0.15, 0.1)
    $ Pause(2.0)
    "{p=1.0}{nw}"
    show screen invert(0.15, 0.1)
    "{p=1.0}{nw}"
    show screen invert(0.15, 0.1)
    "{p=1.0}{nw}"
    show screen invert(0.15, 0.1)
    "{p=1.0}{nw}"
    show screen invert(0.15, 0.1)
    "{p=1.0}{nw}"
    $ renpy.quit()

    # This ends the game.

    return
