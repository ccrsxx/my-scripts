import os
import sys
import argparse

from PIL import Image


def parse_args() -> tuple[str, bool]:
    parser = argparse.ArgumentParser(description='convert .png to webicon')

    if len(sys.argv) == 1:
        parser.print_help()
        quit()

    parser.add_argument(
        '-d', '--delete', help='delete the .png file', action='store_true'
    )
    parser.add_argument('filename', help='.png file', type=str)

    args = parser.parse_args()

    return args.filename, args.delete


def main() -> None:
    filename, delete = parse_args()

    if not filename.endswith('.png'):
        print('❌ file must be a .png')
        return

    if not os.path.exists(filename):
        print(f'❌ {filename} does not exist')
        return

    with Image.open(filename) as im:
        im.save('favicon.ico', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])

        for size in [(192, 192), (512, 512)]:
            im.resize(size).save(f'logo{size[0]}.png')

    if delete:
        os.remove(filename)
        print(f'✅ {filename} deleted')

    print('✅ converted successfully!')


if __name__ == '__main__':
    main()
