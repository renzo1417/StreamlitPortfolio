"""Build a source-only ZIP, excluding environments, caches, and other apps."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parent
FILES = ['app.py', 'content.py', 'state.py', 'ui.py', 'styles.css',
         'requirements.txt', '.streamlit/config.toml', '.gitignore']
DIRECTORIES = ['screens', 'assets']


def package(destination=None):
    target = Path(destination) if destination else ROOT.parent / 'Renzo_Pogoy_Streamlit_Portfolio.zip'
    files = [ROOT / name for name in FILES]
    for directory in DIRECTORIES:
        files.extend(path for path in (ROOT / directory).rglob('*') if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc')
    missing = [path.relative_to(ROOT).as_posix() for path in files if not path.is_file()]
    if missing:
        raise FileNotFoundError(f'Missing submission files: {missing}')
    with ZipFile(target, 'w', compression=ZIP_DEFLATED) as archive:
        for path in sorted(files):
            archive.write(path, path.relative_to(ROOT))
    with ZipFile(target) as archive:
        if archive.testzip() is not None:
            raise ValueError('ZIP integrity check failed')
    return target


if __name__ == '__main__':
    print(package())
