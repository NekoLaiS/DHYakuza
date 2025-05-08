
# This transform fades the screen for CGs to be shown/hidden.
transform cgfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

# This variable defines the effect used by 'dissolve' by characters.
define dissolve = Dissolve(0.25)

# These variables define Dissolve(X) for CGs and scenes.
define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)

# This variable makes the screen dissolve itself to black to show another scene later.
define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

# This variable dissolves the screen for a bit then shows the next scene afterwards.
define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

# This variable makes the screen shut to black; like your eyes closing themselves.
define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])

# This variable makes the screen show the scene in return; like your eyes opening themselves.
define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])

# This variable makes the screen instantly hide to black.
define trueblack = MultipleTransition([
    Solid("#000"), Pause(0.25),
    Solid("#000")
    ])

# This variable makes the current character hide by wiping their sprite off-screen to the left.
define wipeleft = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64)

# This variable makes the current scene wipe to black from the left, then shows another scene.
define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    True])

# This variable makes the current character hide by wiping their sprite off-screen to the right.
define wiperight = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64, reverse=True)

# This variable makes the current scene wipe to black from the right, then shows another scene.
define wiperight_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64, reverse=True),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64, reverse=True),
    True])