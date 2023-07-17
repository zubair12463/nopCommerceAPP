import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")
class ReadConfig:
    @staticmethod
    def get_baseUrl():
        base_URL = config.get('common', 'base_URL')
        return base_URL
    
    @staticmethod
    def get_username():
        username = config.get('common','username')
        return username
    
    @staticmethod
    def get_passward():
        passward = config.get('common', 'password')
        return passward
    


    