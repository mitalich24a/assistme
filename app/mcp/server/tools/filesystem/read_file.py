from pathlib import Path


def register_read_file(
    mcp,
):

    @mcp.tool()
    def read_file(
        path: str,
    ) -> str:
        """
        Read a text file.
        """

        p = Path(path)

        if not p.exists():
            return "File does not exist."

        return p.read_text(
            encoding="utf-8",
        )