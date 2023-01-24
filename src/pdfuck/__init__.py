# PDFuck: pdfuck/__init__.py
# Author JiJi <i@mmdjiji.com>
# GitHub https://github.com/mmdjiji/pdfuck

import argparse
import pikepdf

def pdfuck(filepath, output, password):

  # add '.fuck' sign for the output file
  if not output:
    splited = filepath.rsplit('.', 1)
    prefix = splited[0]
    output = prefix + '.fucked'
    if(len(splited) >= 2):
      suffix = splited[1]
      output += '.' + suffix

  try:
    with pikepdf.open(filename_or_stream=filepath, password=password) as pdf:
      pdf.save(filename_or_stream=output)
    print('Decryption succeeded, saved to \'' + output + '\'')

  except Exception as e:
    print(e)

def main():
  parser = argparse.ArgumentParser(description='PDFuck: Remove the password of your PDF file')
  parser.add_argument('filepath', metavar='<filepath>', type=str, help='path of the source PDF file')
  parser.add_argument('-o', '--output', metavar='<filepath>', type=str, help='path of the target PDF file')
  parser.add_argument('-p', '--password', metavar='<password>', type=str, help='reading password of the source PDF file')
  args = parser.parse_args()

  filepath, output, password = args.filepath, args.output, args.password or ''
  pdfuck(filepath=filepath, output=output, password=password)

if __name__ == '__main__':
  main()