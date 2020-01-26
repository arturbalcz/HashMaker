import hashlib


class MdFive:

    @staticmethod
    def hash_md5(message):
        result = hashlib.md5(message)
        return result.hexdigest()
