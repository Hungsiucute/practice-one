from dslk import *

def main():
  ds = DSLienKet()
  ds.in_ds()
  so=0
  # 1 - them
  print('1: them ----------------\n')
  while so != -999:
    print("nhap -999 de ngat\n")
    so = int(input("nhap so vao : "))
    if so == -999:
      break
    else:
      print()
      print(f'Them {so}\n')
      ds.them(so)
      ds.in_ds()
      print()
  so=0
  vitri=0
  # 2 - chen
  print('\n2: chen ----------------\n')
  while so != -999:
    print("---nhap -999 de ngat---\n")
    so = int(input("nhap so vao : "))
    print()
    if so == -999:
      break
    else:
      vitri = int(input("nhap vi tri vao : "))
      print(f'\nchen {so} vao vi tri {vitri}\n')
      ds.chen(vitri,so)
      ds.in_ds()
      print()
  # 3 - tim
  so=0
  print('3: tim ----------------\n')
  while so != -999:
    print("nhap -999 de ngat\n")
    ds.in_ds()
    so = int(input("\nnhap so can tim : "))
    if so == -999:
      break
    else:
      print()
      print(f'Tim {so}\n')
      vt=ds.tim(so)
      print(f'So {so} tai vi tri {vt}\n')
  # 4 - xoa
  so=0
  print('4: xoa ----------------\n')
  while so != -999:
    print("nhap -999 de ngat")
    so = int(input("\nnhap so can xoa : "))
    if so == -999:
      break
    else:
      print()
      print(f'xoa {so}\n')
      vt=ds.xoa(so)
      ds.in_ds()
      print()
  # 5 - cap nhap
  so=0
  print('\n5: cap nhap ----------------\n')
  while so != -999:
    print("---nhap -999 de ngat---\n")
    so = int(input("nhap so can thay vao : "))
    print()
    if so == -999:
      break
    else:
      vitri = int(input("nhap vi tri can thay vao : "))
      print(f'\ncap nhap {so} vao vi tri {vitri}\n')
      ds.cap_nhap(vitri,so)
      ds.in_ds()
      print()
  # 6 - xoa het
  print('6 : xoa het----')
  so=0
  print("---nhap -999 de xoa het---\n")
  if so == -999:
    ds.xoa_het()
  ds.in_ds

# def
if __name__ == '__main__':
  main()
# if