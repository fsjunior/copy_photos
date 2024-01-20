from cleo.commands.command import Command
from cleo.helpers import argument
import os
from datetime import datetime
from tqdm import tqdm

def remove_files(source_dir, target_dir, output):
    removed_files_count = 0

    output.line("Starting to scan files...")

    for root, dirs, files in os.walk(source_dir):
        if "_FUJI" in root:
            for filename in tqdm(files, desc="Scanning files", unit="file"):
                source_file = os.path.join(root, filename)
                file_mod_time = datetime.fromtimestamp(os.path.getmtime(source_file))
                year_month = file_mod_time.strftime("%Y/%m")
                target_sub_dir = os.path.join(target_dir, year_month)

                if not os.path.exists(target_sub_dir):
                    os.makedirs(target_sub_dir)

                target_file = os.path.join(target_sub_dir, filename)

                if os.path.exists(target_file) and os.path.getsize(source_file) == os.path.getsize(target_file):
                    # os.remove(source_file)
                    output.line(f"Removing {source_file}")
                    removed_files_count += 1

    return removed_files_count

class RemovePhotosCommand(Command):
    name = "remove_photos"
    description = "Removes photos from the source directory that are already in the target directory"
    arguments = [
        argument('source', 'The source directory', optional=False),
        argument('target', 'The target directory', optional=False)
    ]

    def handle(self):
        source_dir = self.argument('source')
        target_dir = self.argument('target')
        self.line("Command started.")
        removed = remove_files(source_dir, target_dir, self)
        self.line(f"Removed files: {removed}")
        self.line("Command finished.")