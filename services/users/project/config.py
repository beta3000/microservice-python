class BaseConfig:
    """Base configuration"""
    TESTING = False


class DevelopmentConfig:
    """Development configuration"""
    pass


class TestingConfiguration:
    """"Testing configuration"""
    TESTING = True


class ProductionConfig:
    """Production configuration"""
    pass
