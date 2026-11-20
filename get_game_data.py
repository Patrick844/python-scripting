"""Find game folders in a source directory and copy them into a target directory."""

import logging
import shutil
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

GAME_FOLDER_KEYWORD = "game"
GAME_FOLDER_SUFFIX = "_game"


def find_game_folders(source_folder: Path) -> list[Path]:
    """Return the folders directly inside source_folder whose name contains "game"."""
    game_folders: list[Path] = []
    for entry in source_folder.iterdir():
        if entry.is_dir() and GAME_FOLDER_KEYWORD in entry.name.lower():
            logger.info("Found game folder: %s", entry.name)
            game_folders.append(entry)
    return game_folders


def create_folder(folder: Path) -> None:
    """Create folder if it doesn't already exist."""
    if folder.exists():
        logger.info("Folder already exists: %s", folder)
    else:
        folder.mkdir()
        logger.info("Created folder: %s", folder)


def remove_suffix_from_name(folder: Path, suffix: str) -> str:
    """Return the folder's name with suffix removed, e.g. "chess_game" -> "chess"."""
    return folder.name.replace(suffix, "")


def copy_folder_with_overwrite(source_folder: Path, destination_folder: Path) -> None:
    """Copy source_folder to destination_folder, replacing it if it already exists."""
    if destination_folder.exists():
        shutil.rmtree(destination_folder)
    shutil.copytree(source_folder, destination_folder)
    logger.info("Copied %s -> %s", source_folder, destination_folder)


def copy_game_folders(source_folder: Path, target_folder: Path) -> None:
    """Copy each game folder into target_folder, dropping the "_game" suffix."""
    if not source_folder.is_dir():
        raise NotADirectoryError(f"Source folder not found: {source_folder}")

    game_folders = find_game_folders(source_folder)
    create_folder(target_folder)

    for game_folder in game_folders:
        new_name = remove_suffix_from_name(game_folder, GAME_FOLDER_SUFFIX)
        copy_folder_with_overwrite(game_folder, target_folder / new_name)


def main() -> None:
    """Read the source and target folders from the command line and copy the games."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    arguments = sys.argv[1:]
    if len(arguments) != 2:
        logger.error("Usage: python get_game_data.py <source_folder> <target_folder>")
        sys.exit(1)

    source_folder = Path.cwd() / arguments[0]
    target_folder = Path.cwd() / arguments[1]

    try:
        copy_game_folders(source_folder, target_folder)
    except OSError:
        logger.exception("Failed to copy game folders")
        sys.exit(1)


if __name__ == "__main__":
    main()
