# This is where the splashscreen, disclaimer and menu code reside in.

# This python statement checks that 'audio.rpa', 'fonts.rpa' and 'images.rpa'
# are in the game folder and if the project is in a cloud folder (OneDrive).
# Note: For building a mod for PC/Android, you must keep the DDLC RPAs 
# and decompile them for the builds to work.
init python:
    # Списки процессов для разных платформ
    windows_processes = [
        "obs32.exe", 
        "obs64.exe", 
        "obs.exe", 
        "xsplit.core.exe", 
        "livehime.exe", 
        "pandatool.exe", 
        "yymixer.exe", 
        "douyutool.exe", 
        "huomaotool.exe",
        "Streamlabs OBS.exe"
    ]

    linux_processes = [
        "obs",
        "simplescreenrecorder",
        "wf-recorder",
        "/usr/bin/gjs -m /usr/share/gnome-shell/org.gnome.Shell.Screencast"
    ]

    if not config.developer:
        if not renpy.android:
            print("CHECKING")
            for archive in ['audio','images','fonts']:
                if archive not in config.archives:
                    raise DDLCRPAsMissing(archive)

        if renpy.windows:
            onedrive_path = os.environ.get("OneDrive")
            if onedrive_path is not None:
                if onedrive_path in config.basedir:
                    raise IllegalModLocation

init 999 python:
    # Флаг для отслеживания, была ли уже проверка обновлений
    _translation_update_checked = False

label check_translation_update:
    if not _translation_update_checked:
        $ _translation_update_checked = True
        if updater.check_update_available():
            call screen translation_update
    return


label splashscreen:

    python:
        # Проверяем обновления только если включен русский язык
        if _preferences.language == "russian":
            renpy.call_in_new_context("check_translation_update")

    if not persistent.has_chosen_language and translations:

        if _preferences.language is None:
            call choose_language
    
    $ persistent.has_chosen_language = True

    ## This if statement checks if we are running any common streaming/recording 
    ## software so the game can enable Let's Play Mode automatically and notify
    ## the user about it if extra settings are enabled.
    if not persistent.lets_play:
        if renpy.windows and process_check(windows_processes):
            $ persistent.lets_play = True
        elif process_check(linux_processes):
            $ persistent.lets_play = True

    $ basedir = config.basedir.replace('\\', '/')

    if persistent.autoload:
        jump autoload

    ## Block skip for unviewed dialogs
    $ config.allow_skipping = False

    return

label autoload:
    python:
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    # if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
    #     $ persistent.yuri_kill += 200

    if renpy.get_return_stack():
        $ renpy.pop_call()
    jump expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = None
    return
