import zipfile

newZip = zipfile.ZipFile('<zip_name>', 'w') #example for name - new.zip
newZip.write('<File_path>', compress_type=zipfile.ZIP_DEFLATED)

newZip.close()
