from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASS: str = "admin"
    DB_NAME: str = "calling_app_db"

    DATABASE_URL: str = "postgresql+asyncpg://postgres:admin@localhost:5432/calling_app_db"

    SECRET_JWT_KEY: str = "supersecret"
    JWT_ALGHORITM: str = "HS256"

    @property
    def DATABASE_URI(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def SECRET_KEY(self):
        return self.SECRET_JWT_KEY
    
    @property
    def ALGORITHM(self):
        return self.JWT_ALGHORITM
    
    model_config = SettingsConfigDict(env_file='.env',env_file_encoding='utf-8', extra="ignore")

settings = Settings()

def get_auth_data():
    return {"secret_key" : settings.SECRET_KEY,"algorithm" : settings.ALGORITHM}
