from unittest.mock import Mock
from src.remove_photos_command import remove_files
from tempfile import TemporaryDirectory
import os
from test.utils import create_test_file


def test_remove_files():
    with TemporaryDirectory() as source, TemporaryDirectory() as target:
        fuji_subdir = os.path.join(source, "100_FUJI")
        os.makedirs(fuji_subdir)

        # Create test files in the source directory and an identical file in the target directory
        create_test_file(fuji_subdir, "test1.jpg")
        assert os.path.exists(os.path.join(fuji_subdir, "test1.jpg"))

        create_test_file(target, "2021/01/test1.jpg")
        # Call remove_files
        removed = remove_files(source, target, Mock())

        # Check if the file is removed
        assert removed == 1
        assert not os.path.exists(os.path.join(fuji_subdir, "test1.jpg"))

# Additional tests can be added as needed
