
import joblib
from pathlib import Path

class MovesStorage:
    def __init__(self, path="./storage", compress=9):
        self.__path = Path(path)
        self.__compress = compress
        self.__path.mkdir(parents=True, exist_ok=True)

        # Delete all existing files in storage
        for file in self.__path.iterdir():
            if file.is_file():
                file.unlink()

    def __get_file_path(self, key):
        key_hash = key
        return self.__path / f"{key_hash}.joblib"

    def load(self, key):
        file_path = self.__get_file_path(key)
        if not file_path.exists():
            return None
        return joblib.load(file_path)

    def insert(self, key, data):
        file_path = self.__get_file_path(key)
        joblib.dump(data, file_path, compress=self.__compress)

    def insert_many(self, records):
        for key, data in records.items():
            self.insert(key, data)

    def delete(self, key):
        file_path = self.__get_file_path(key)
        if file_path.exists():
            file_path.unlink()
            return True
        return False

    def exists(self, key):
        return self.__get_file_path(key).exists()

    def clear(self):
        for file in self.__path.iterdir():
            if file.is_file():
                file.unlink()

if __name__ == "__main__":
    storage = MovesStorage()
    storage.clear()
