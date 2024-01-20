import os
from unittest.mock import Mock
from cleo.application import Application
from src.copy_photos_command import CopyPhotosCommand, process_files
from tempfile import TemporaryDirectory
from test.utils import create_test_file

def test_process_files_with_all_extensions():
    with TemporaryDirectory() as source, TemporaryDirectory() as target:
        fuji_subdir = os.path.join(source, "100_FUJI")
        os.makedirs(fuji_subdir)

        extensions = ['png', 'jpg', 'jpeg', 'raf']
        for ext in extensions:
            create_test_file(fuji_subdir, f"test.{ext}")

        copied, _ = process_files(source, target, Mock())

        year_month_dir = os.path.join(target, "2021", "01")

        assert copied == len(extensions)
        for ext in extensions:
            assert os.path.exists(os.path.join(year_month_dir, f"test.{ext}"))

def test_skip_existing_files():
    with TemporaryDirectory() as source, TemporaryDirectory() as target:
        fuji_subdir = os.path.join(source, "100_FUJI")
        os.makedirs(fuji_subdir)
        create_test_file(fuji_subdir, "test.jpg")

        year_month_dir = os.path.join(target, "2021", "01")
        os.makedirs(year_month_dir)
        create_test_file(year_month_dir, "test.jpg")

        _, skipped = process_files(source, target, Mock())

        assert skipped == 1

def test_cleo_command_registration():
    app = Application()
    app.add(CopyPhotosCommand())

    assert app.has('copy_photos')

    command = app.find('copy_photos')
    assert command.name == 'copy_photos'
    assert command.description == 'Copies photos from a source directory to a target directory'

# Additional tests can be added as needed
