from app.bootstrap.bootstrap import Bootstrap
from app.bootstrap.startup import Startup

from app.core.logging import configure_logging

configure_logging()

def main() -> None:

    Bootstrap.initialize()

    Startup.run()


if __name__ == "__main__":
    main()