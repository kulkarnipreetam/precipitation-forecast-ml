import os
from sqlalchemy import create_engine
import psycopg

# Reconstruct root.crt if stored as a secret
with open("root.crt", "w") as f:
    f.write(os.getenv("DB_ROOT_CERT"))

# Build SQLAlchemy connection string
db_url = f"postgresql+psycopg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}?sslmode=verify-full&sslrootcert=root.crt"

engine = create_engine(db_url)

# Test connection
try:
    with engine.connect() as conn:
        result = conn.execute("SELECT version();")
        print(f"✅ DB Connection successful: {result.fetchone()}")
except Exception as e:
    print(f"❌ DB Connection failed: {e}")
