## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("ElysiumModTemplate")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "ElysiumModTemplate"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = dissolve


## Used when entering the main menu after the game has ended.

define config.end_game_transition = fade

## Used when ended splash screen

define config.end_splash_transition = dissolve


## Used when use yesno frame

define config.exit_yesno_transition = dissolve
define config.enter_yesno_transition = dissolve

## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "ElysiumModTemplate-1726373592"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"

init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)

## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:
    ## The following variables take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##  * matches all characters, except the directory separator.
    ##  ** matches all characters, including the directory separator.
    ##
    ## Examples:
    ##  "*.txt" matches txt files in the base directory.
    ##  "game/**.ogg" matches ogg files in the game directory or any of its
    ## subdirectories.
    ##  "**.psd" matches psd files anywhere in the project.

    # These variables declare the packages to build your mod that is Team Salvato
    # IPG compliant. Do not mess with these variables whatsoever.
    build.package("Renpy8-DDLCMod", 'zip', 'windows linux mac renpy mod',
        description="Ren'Py 8 DDLC Compliant Mod")

    # These variables declare the archives that will be made to your packaged mod.
    # To add another archive, make a build.archive variable like in this example:
    build.archive("scripts", 'mod')
    build.archive("mod_assets", 'mod')
    # Архив для файлов перевода
    build.archive("translation_ru", 'mod')

    # Do not touch these lines. This is so Ren'Py can add your mods' py file
    # and a special launcher for Linux and macOS to run your mod. 
    build.renpy_patterns.remove(('renpy.py', ['all']))
    build.classify_renpy("renpy.py", "renpy all")
    
    build.early_base_patterns.remove(('*.sh', None))
    build.classify("LinuxLauncher.sh", "linux") ## Linux Launcher Script
    build.classify("*.sh", None)
    
    #############################################################
    # These variables classify packages for PC and Android platforms.
    # Make sure to add 'all' to your build.classify variable if you are planning
    # to build your mod on Android like in this example.
    #   Example: build.classify("game/**.pdf", "scripts all")
    build.classify("game/mod_assets/**", "mod_assets all")
    build.classify("game/presplash.png", "scripts all")
    build.classify("game/**.rpyc", "scripts all")
    build.classify("game/README.md", None)
    build.classify("game/**/README.md", None)
    build.classify("game/**.txt", "scripts all")
    build.classify("game/**.chr", "scripts all")
    build.classify("game/advanced_scripts/**","scripts all") ## Backwards Compatibility
    
    # Настройка классификации файлов перевода
    build.classify("game/tl/**", None) # Отключаем старую классификацию
    build.classify("game/tl/None/**", "scripts all") # Базовые файлы перевода
    build.classify("game/tl/russian/**", "translation_ru all") # Русский перевод
    
    build.classify("game/mod_extras/**.rpyc", "scripts") ## Extra Features (Backwards Compatibility)

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa', None)
    build.classify('README.html','mod all')
    build.classify('README.linux', 'linux')
   
    # This sets' README.html as documentation
    build.documentation('README.html')

    build.include_old_themes = False
