from cleo.commands.command import Command
from cleo.helpers import argument
import os
import shutil
from tqdm import tqdm
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from src.constants import ALLOWED_FILE_EXTENSIONS

def copy_file(source_target_pair):
    source, target = source_target_pair
    shutil.copy2(source, target)

def process_files(source_dir, target_dir, output):
    files_to_copy = []
    skipped_files_count = 0

    output.line("Starting to scan files...")

    # Get the total count of files for the progress bar
    total_files = sum([len(files) for r, d, files in os.walk(source_dir) if "_FUJI" in r])

    with tqdm(total=total_files, desc="Scanning files", unit="file") as pbar:
        for root, dirs, files in os.walk(source_dir):
            if "_FUJI" in root:
                for filename in files:
                    if filename.lower().endswith(ALLOWED_FILE_EXTENSIONS):
                        source_file = os.path.join(root, filename)
                        file_mod_time = datetime.fromtimestamp(os.path.getmtime(source_file))
                        year_month = file_mod_time.strftime("%Y/%m")
                        target_sub_dir = os.path.join(target_dir, year_month)

                        if not os.path.exists(target_sub_dir):
                            os.makedirs(target_sub_dir)

                        target_file = os.path.join(target_sub_dir, filename)

                        if not os.path.exists(target_file) or os.path.getsize(source_file) != os.path.getsize(target_file):
                            files_to_copy.append((source_file, target_file))
                        else:
                            skipped_files_count += 1

                    pbar.update(1)

    output.line("Starting to copy files...")

    with ThreadPoolExecutor(max_workers=8) as executor:
        list(tqdm(executor.map(copy_file, files_to_copy), total=len(files_to_copy), desc="Copying files", unit="file"))

    # for source_file, target_file in tqdm(files_to_copy, desc="Copying photos", unit="file"):
    #     shutil.copy2(source_file, target_file)

    return len(files_to_copy), skipped_files_count


class CopyPhotosCommand(Command):
    name = "copy_photos"
    description = "Copies photos from a source directory to a target directory"
    arguments = [
        argument('source', 'The source directory', optional=False),
        argument('target', 'The target directory', optional=False)
    ]

    def handle(self):
        source_dir = self.argument('source')
        target_dir = self.argument('target')
        self.line("Command started.")
        copied, skipped = process_files(source_dir, target_dir, self)
        self.line(f"Copied files: {copied}")
        self.line(f"Skipped files: {skipped}")
        self.line("Command finished.")
