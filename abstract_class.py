from abc import ABC


class AbstractCipher(ABC):
    def encrypt(self):
        pass

    def decrypt(self):
        pass

    def start(self, action: str):
        if action == 'Encrypt':
            self.encrypt()
        if action == 'Decrypt':
            self.decrypt()
        if action == 'Hack':
            self.hack()
