with open('once.txt', 'r') as dosya:
  # dosya içeriğini oku
  a = dosya.readline()

with open('sonra.txt', 'w') as dosya:
  # dosya içeriğini ikili gruplar halinde yaz
  for i in range(0, len(a), 2):
    dosya.write(a[i:i+2] + ' ')