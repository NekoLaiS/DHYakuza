style achievements_text is gui_text
style achievements_text:
    color "#000"
    outlines []
    size 20

transform achievement_scaler(x):
    size(x, x)

transform achievement_notif_transition:
    alpha 0.0
    linear 0.5 alpha 1.0

style achievements_image_button:
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound