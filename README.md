# Photo Management Tool

## Overview
This Photo Management Tool is a command-line application designed to efficiently manage photo files. It includes features to copy photos from a source to a target directory and remove photos from the source that are already present in the target directory.

## Features
- Copy photos with the option to organize them into year/month subdirectories.
- Remove photos from the source directory that are already present in the target directory, based on name and size.
- Uses `ThreadPoolExecutor` for concurrent file operations to enhance performance.
- Progress bars for user-friendly operation status.

## Technical Details
- The project was almost entirely created with the assistance of OpenAI's ChatGPT (including this readme!). Check the ChatGPT log: https://chat.openai.com/share/8ef9fc5a-5b40-4cb8-9d1e-4e90861aaedd
- Dependency management and virtual environment handled using Poetry.

## Setup and Usage
1. Ensure Python and Poetry are installed on your system.
2. Clone this repository.
3. Navigate to the project directory and run `poetry install` to set up the environment and install dependencies.
4. Use the command-line interface to execute commands. Example usage:

```shell
python main.py copy_photos <source_directory> <target_directory>
python main.py remove_photos <source_directory> <target_directory>
```

## Contributing
Contributions to the project are welcome. Please follow standard practices for pull requests and coding standards. Only ChatGPT code will be accepted.

## License
Licensed under The Unlicense License.

## Acknowledgements
Special thanks to OpenAI's ChatGPT for assisting in the creation of this project.
