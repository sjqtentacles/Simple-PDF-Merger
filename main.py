from PyPDF2 import PdfFileMerger
import PySimpleGUI as sg
import os

def merge_files_in(dir):
  merger = PdfFileMerger()

  files_in_dir = list(map(lambda x: '{}/{}'.format(dir, x), os.listdir(dir)))
  pdf_files = list(filter(lambda x: x.endswith('.pdf'), files_in_dir))
  sorted_pdfs = sorted(pdf_files)
  
  for f in sorted_pdfs:
    input_doc = open(f,'rb')
    merger.append(input_doc)
  
  output = open('merged-files.pdf', 'wb')
  merger.write(output)

sg.theme('LightPurple')
layout = [  [sg.Text('Merge Files in Directory in Alphanumerical Order')],
            [sg.Input(), sg.FolderBrowse()],
            [sg.Button('Merge'), sg.Exit()] ]

window = sg.Window('PDF Merger', layout)
while True:
  event, values = window.read()
  if event in (None, 'Exit'):
    break
  if event == 'Merge':
    merge_files_in(values[0])
    sg.popup("Done! Check this program's current folder for the output.")

window.close()