import configparser

config = configparser.RawConfigParser()
config.read("./Config/config.ini")


class ReadProperties:

    @staticmethod
    def getAppURL():
        url = config.get('common_vars', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common_vars', 'username')
        return username

    @staticmethod
    def getPassword():
        return config.get('common_vars', 'password')