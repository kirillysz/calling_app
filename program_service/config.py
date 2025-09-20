from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASS: str = "admin"
    DB_NAME: str = "agent_db"

    DATABASE_URL: str = "postgresql+asyncpg://postgres:admin@localhost:5432/agent_db"


    @property
    def DATABASE_URI(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file='.env',env_file_encoding='utf-8', extra="ignore")

settings = Settings()

