import webbrowser
import pyperclip
import sys


def look_map(address) -> None:
    edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge))
    webbrowser.get('edge').open_new_tab(f'google.com/maps/search/{address}')


def main() -> None:
    if len(sys.argv) > 1:
        address = ' '.join(sys.argv[1:])
    else:
        address = pyperclip.paste()
    look_map(address)


if __name__ == '__main__':
    main()
