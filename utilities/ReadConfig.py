import configparser

config = configparser.RawConfigParser()
config.read("D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\PhpTravel"
            "\\Configuration\\config.ini")


class Readconfig:

    @staticmethod
    def URL():
        url = config.get('common info', 'url')
        return url

    @staticmethod
    def Email():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def Password():
        password = config.get('common info', 'password')
        return password
