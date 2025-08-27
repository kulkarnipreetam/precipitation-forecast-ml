import os
import sys
from sqlalchemy import create_engine, text

# Reconstruct root.crt from secret
with open("root.crt", "w") as f:
    f.write(os.getenv("DB_ROOT_CERT"))

# Build SQLAlchemy connection string with a 10-second timeout
db_url = (
    f"postgresql+psycopg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    "?sslmode=verify-full&sslrootcert=root.crt&connect_timeout=10"
)

# Create engine
engine = create_engine(db_url)

# Test DB connection
try:
    with engine.connect() as conn:
        # Wrap SQL string with text() for SQLAlchemy 2.x
        result = conn.execute(text("SELECT version();"))
        version = result.fetchone()[0]
        print(f"✅ DB Connection successful: {version}")
except Exception as e:
    print(f"❌ DB Connection failed: {e}")
    sys.exit(1)  # Exit with non-zero code for GitHub Actions
