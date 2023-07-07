# Author: Kibwe Gooding
# Email: marscornelius@proton.me
# Date: 2023-07-07
# Copyright (c) 2023, Kibwe Gooding. All rights reserved.

import os
import send2trash

path = '/Users/marscornelius/Downloads'


def clear_downloads():
    file_names = os.listdir(path)
    if os.path.exists(path):
        for file in file_names:
            try:
                file_path = os.path.join(path, file)
                os.chmod(file_path, 0o777)
                send2trash.send2trash(file_path)
            except OSError as e:
                print(str(e) + ": " + file)

    else:
        return "path invalid."


if __name__ == '__main__':
    clear_downloads()
