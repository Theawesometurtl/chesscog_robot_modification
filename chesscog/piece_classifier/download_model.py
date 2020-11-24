"""Script to download the best piece classifier."""

import functools
from chesscog.utils.io import download_zip_folder


ensure_model = functools.partial(download_zip_folder,
                                 "https://github.com/georgw777/chesscog/releases/download/0.1.0/piece_classifier.zip",
                                 "models://piece_classifier")


if __name__ == "__main__":
    ensure_model(show_size=True)
