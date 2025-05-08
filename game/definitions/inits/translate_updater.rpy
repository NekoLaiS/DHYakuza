init -990 python:
    import json
    import hashlib
    import requests
    from urllib.parse import urljoin

    class TranslationVersion:
        def __init__(self, version_string):
            self.version_string = version_string
            parts = version_string.split('.')
            self.major = int(parts[0])
            self.minor = int(parts[1])
            self.patch = int(parts[2])
        
        def __str__(self):
            return self.version_string
        
        def __lt__(self, other):
            if self.major != other.major:
                return self.major < other.major
            if self.minor != other.minor:
                return self.minor < other.minor
            return self.patch < other.patch

    class TranslationUpdater:
        def __init__(self, config):
            self.config = config
            self.mod_id = config.get("mod_id", "default")
            self.current_version = TranslationVersion(config.get("current_version", "0.0.0"))
            self.github_repo = config["github_repo"]
            self.update_progress = 0
            self.update_status = ""
            self.new_version = None
            
        def get_latest_release(self):
            """Получение информации о последнем релизе с GitHub"""
            try:
                api_url = f"https://api.github.com/repos/{self.github_repo}/releases/latest"
                response = requests.get(api_url)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                self.update_status = f"Ошибка при получении информации о релизе: {str(e)}"
                return None

        def check_update_available(self):
            """Проверка наличия обновления"""
            try:
                release = self.get_latest_release()
                if not release:
                    return False
                    
                # Ищем релиз для нашего мода
                if not release["tag_name"].startswith(f"{self.mod_id}/translation-"):
                    return False
                    
                version_str = release["tag_name"].split("-")[1]
                self.new_version = TranslationVersion(version_str)
                
                return self.new_version > self.current_version
            except Exception as e:
                self.update_status = f"Ошибка при проверке обновлений: {str(e)}"
                return False

        def download_file(self, url, local_path):
            """Загрузка файла с отслеживанием прогресса"""
            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()
                total_size = int(response.headers.get('content-length', 0))
                
                with open(local_path, 'wb') as f:
                    if total_size == 0:
                        f.write(response.content)
                    else:
                        downloaded = 0
                        for data in response.iter_content(chunk_size=4096):
                            downloaded += len(data)
                            f.write(data)
                            self.update_progress = (downloaded / total_size) * 100
                            renpy.restart_interaction()
                            
                return True
            except Exception as e:
                self.update_status = f"Ошибка при загрузке файла: {str(e)}"
                return False

        def verify_sha256(self, file_path, expected_hash):
            """Проверка SHA256 хэша файла"""
            try:
                sha256_hash = hashlib.sha256()
                with open(file_path, "rb") as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        sha256_hash.update(byte_block)
                return sha256_hash.hexdigest() == expected_hash
            except Exception as e:
                self.update_status = f"Ошибка при проверке хэша: {str(e)}"
                return False

        def update_translation(self):
            """Процесс обновления перевода"""
            try:
                self.update_status = "Получение информации о релизе..."
                self.update_progress = 0
                
                release = self.get_latest_release()
                if not release:
                    return False

                # Загрузка файлов
                for asset in release["assets"]:
                    if asset["name"] == f"{self.mod_id}_translation_ru.rpa":
                        self.update_status = "Загрузка файла перевода..."
                        if not self.download_file(asset["browser_download_url"], 
                                               f"game/tl/russian/{self.mod_id}_translation_ru.rpa"):
                            return False
                            
                    elif asset["name"] == f"{self.mod_id}_translation_ru.rpa.sha256":
                        self.update_status = "Загрузка хэш-суммы..."
                        if not self.download_file(asset["browser_download_url"],
                                               f"game/tl/russian/{self.mod_id}_translation_ru.rpa.sha256"):
                            return False

                # Проверка хэша
                self.update_status = "Проверка целостности файла..."
                with open(f"game/tl/russian/{self.mod_id}_translation_ru.rpa.sha256", "r") as f:
                    expected_hash = f.read().split()[0]
                
                if not self.verify_sha256(f"game/tl/russian/{self.mod_id}_translation_ru.rpa", expected_hash):
                    self.update_status = "Ошибка: Файл повреждён"
                    return False

                self.update_status = "Обновление успешно завершено!"
                self.update_progress = 100
                return True

            except Exception as e:
                self.update_status = f"Ошибка при обновлении: {str(e)}"
                return False 