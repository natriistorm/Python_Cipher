from abc import ABC


class AbstractCipher(ABC):
    def encrypt(self):
        pass

    def decrypt(self):
        pass

    def start(self, action: str):
        pass
