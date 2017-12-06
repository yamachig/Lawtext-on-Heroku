from pathlib import Path
import os
import shutil

from tqdm import tqdm
from dotenv import load_dotenv
from lawtext import htmlapp

BASE_DIR = Path(__file__).parent.resolve()
HTMLAPP_ROOT_DIR = BASE_DIR / 'static_htmlapp'# / 'htmlapp'

def main():
    print('### Ready for building document...')

    DOTENV_LOADED = os.environ.get("DOTENV_LOADED")
    if not DOTENV_LOADED:
        load_dotenv(str(Path(__file__).parent / '.env'))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lawtext_site.settings")
    import django
    django.setup()

    from file_server.models import File

    print('### Build HTMLApp...')
    #htmlapp.main(str(HTMLAPP_ROOT_DIR), False)
    shutil.copyfile(
        str(HTMLAPP_ROOT_DIR / 'lawtext.html'),
        str(HTMLAPP_ROOT_DIR / 'index.html'),
    )

    print('### Save files...')

    for p in tqdm(list(HTMLAPP_ROOT_DIR.glob('**/*'))):
        if not p.is_file():
            continue
        relpath = p.relative_to(HTMLAPP_ROOT_DIR).as_posix()
        f = File()
        f.path = str(relpath)
        f.content = p.read_bytes()
        f.save()

if __name__ == '__main__':
    main()
