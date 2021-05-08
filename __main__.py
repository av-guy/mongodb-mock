import sys
from conf import Configuration
sys.path.append(Configuration.PROJECT_PATH)

if __name__ == "__main__":
    from mongo.src.main import initialize
    initialize()
