import os
import sys
import argparse
import subprocess

from utils.wait import wait_close
from glob import iglob

IMAGE_EXTENSIONS = (
    'jpeg',
    'jpg',
    'png',
)


def parse_args() -> tuple[str, bool]:
    parser = argparse.ArgumentParser(description='convert images to webp')

    if len(sys.argv) == 1:
        parser.print_help()
        quit()

    parser.add_argument(
        'path',
        help='directory to search for images',
        metavar='path',
        type=str,
    )

    parser.add_argument(
        '-r',
        '--recursive',
        help='search recursively',
        dest='recursive',
        action='store_true',
    )

    args = parser.parse_args()

    return args.path, args.recursive


def main() -> None:
    path, recursive = parse_args()

    target_path = os.path.abspath(path)

    if not os.path.isdir(target_path):
        wait_close(f'{target_path} is not a directory!')

    glob_pattern = '/**/*' if recursive else '/*'

    images = [
        image
        for images_extension in IMAGE_EXTENSIONS
        for image in iglob(
            f'{target_path}{glob_pattern}.{images_extension}', recursive=recursive
        )
    ]

    print(f'This operation will convert these {len(images)} images to webp:')
    print('\n'.join(images))

    print('\nConverting to webp...\n')

    for image in images:
        subprocess.run(
            f'cwebp -q 80 {image} -o {image.replace(image.split(".")[-1], "webp")}'
        )
        print()

    print('Done!')


if __name__ == '__main__':
    main()
