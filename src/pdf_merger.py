import os
import argparse

from glob import glob
from utils.wait import wait_close
from PyPDF2 import PdfFileMerger


def parse_args():
    parser = argparse.ArgumentParser(description='merge pdf files')

    parser.add_argument(
        'path',
        help='directory to search for PDF files',
        metavar='path',
        default='',
        nargs='?',
        type=str,
    )

    args = parser.parse_args()

    return args.path


def pdf_merger(path: str):
    target_path = os.path.abspath(path)

    if not os.path.isdir(target_path):
        wait_close(f'{target_path} is not a directory!')

    pdfs = glob(os.path.join(path, '*.pdf') if path else '*.pdf')

    if not pdfs:
        wait_close(f'No PDF files found in {target_path}!')

    if len(pdfs) == 1:
        wait_close(f'Only one PDF file found in {target_path}!')

    merger = PdfFileMerger()

    pdfs.sort()

    print(f'This operation will merge these {len(pdfs)} PDF files:')
    print('\n'.join(pdfs))

    try:
        print('\nMerging...\n')

        for pdf in pdfs:
            print(f'Adding {pdf}')
            merger.append(pdf)

        print('\nSaving...\n')

        with open('merged.pdf', 'wb') as f:
            merger.write(f)
    except KeyboardInterrupt:
        wait_close('\nUser interrupted the program!')
    except Exception as e:
        wait_close(f'Error {e} while merging PDF')

    wait_close(f'Merged PDF file created in {os.path.join(os.getcwd(), "merged.pdf")}')


def main():
    path = parse_args()
    pdf_merger(path)


if __name__ == '__main__':
    main()
