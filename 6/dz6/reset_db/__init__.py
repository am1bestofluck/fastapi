from .default_content import main as asynced_content
from .sqla import DB_URL, main as scheme_setup
import asyncio
from pathlib import Path


def main(*, forced: bool = False, dummy_content: bool = True):
    if forced:
        Path(DB_URL).unlink()
    scheme_setup()
    if dummy_content:
        asyncio.run(asynced_content())


if __name__ == '__main__':
    main()
