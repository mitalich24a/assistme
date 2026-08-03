from app.bootstrap.bootstrap import Bootstrap
from app.bootstrap.startup import Startup

def main() -> None:

    Bootstrap.initialize()

    Startup.run()


if __name__ == "__main__":
    main()