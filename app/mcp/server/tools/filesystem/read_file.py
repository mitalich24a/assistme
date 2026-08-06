from pathlib import Path
import traceback


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

        try:

            print(f"read_file called with: {path}")

            p = Path(path)

            print(f"Resolved path: {p.resolve()}")

            if not p.exists():
                return "File does not exist."

            return p.read_text(
                encoding="utf-8",
            )

        except Exception:

            traceback.print_exc()

            raise