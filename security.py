from passlib.context import CryptContext

# Configure password hashing context
pwd_context = CryptContext(
    schemes=["argon2"],
    argon2__time_cost=3,          # Number of iterations
    argon2__memory_cost=65536,    # 64MB memory usage
    argon2__parallelism=4,        # Number of parallel threads
    argon2__hash_len=32,          # Hash length
    deprecated="auto"             # Mark deprecated algorithms automatically
)

def get_password_hash(password: str) -> str:
    """Generate a secure hash of the password"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash"""
    return pwd_context.verify(plain_password, hashed_password)