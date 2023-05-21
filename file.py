def read_file(file_path):
  with open(file_path, "rb") as f:
    data = f.read()
  return data