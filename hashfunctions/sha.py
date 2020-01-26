import hashlib


class Sha:
    @staticmethod
    def generate_sha1(message):
        result = hashlib.sha1(message)
        return result.hexdigest()

    @staticmethod
    def generate_sha2(message):
        result = hashlib.sha256(message)
        return result.hexdigest()

    @staticmethod
    def generate_sha3(message):
        result = hashlib.sha3_256(message)
        return result.hexdigest()
