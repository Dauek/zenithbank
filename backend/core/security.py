from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    # transforma a senha em texto puro em um hash
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # compara a senha digitada com o hash salvo, sem nunca reverter o hash
    return pwd_context.verify(plain_password, hashed_password)