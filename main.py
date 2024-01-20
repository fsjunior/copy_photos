# filename: main.py

from cleo.application import Application
from src.copy_photos_command import CopyPhotosCommand
from src.remove_photos_command import RemovePhotosCommand

app = Application()
app.add(CopyPhotosCommand())
app.add(RemovePhotosCommand())


if __name__ == "__main__":
    app.run()
