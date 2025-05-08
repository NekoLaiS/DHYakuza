init -950 python:
    def process_check(stream_list):
        process_list = []

        if renpy.windows:
            try: process_list = subprocess.run("wmic process get Description", check=True, shell=True, stdout=subprocess.PIPE).stdout.lower().decode("utf-8").replace("\r", "").replace(" ", "").strip().split("\n")
            except subprocess.CalledProcessError:
                try:
                    process_list = subprocess.run("powershell (Get-Process).ProcessName", check=True, shell=True, stdout=subprocess.PIPE).stdout.lower().decode("utf-8").replace("\r", "").strip().split("\n") # For W10/11 builds > 22000

                    for i, x in enumerate(process_list):
                        process_list[i] = x + ".exe"
                except:
                    pass

            # Проверка для Windows
            for process in process_list:
                if process.lower() in [x.lower() for x in stream_list]:
                    return True
        else:
            try:
                # Получаем список процессов в Linux
                process_list = subprocess.run(["ps", "-A", "--format", "cmd"], check=True, stdout=subprocess.PIPE).stdout.decode("utf-8").strip().split("\n")
                process_list.pop(0)  # Удаляем заголовок
            except:
                return False

            # Проверка для Linux
            for process in process_list:
                process = process.lower()
                for check_process in stream_list:
                    if check_process in process:
                        return True
        
        return False

    def scan_translations():

        languages = renpy.known_languages()

        if not languages:
            return None

        rv = [(i, renpy.translate_string("{#language name and font}", i)) for i in languages ]
        rv.sort(key=lambda a : renpy.filter_text_tags(a[1], allow=[]).lower())

        rv.insert(0, (None, "English"))

        bound = math.ceil(len(rv)/2.)

        return (rv[:bound], rv[bound:2*bound])
