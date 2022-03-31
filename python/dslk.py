class Nut:
  def __init__(self,gia_tri):
    self.gia_tri = gia_tri
    self.nut_ke = None
  # def
# class

class DSLienKet:
  def __init__(self):
    self.dau = None
    self.duoi = None
  # def

  def in_ds(self):
    stt=0
    hien_tai = self.dau
    kq = 'DS['
    while hien_tai != None:
      stt +=1
      if stt ==1:
        kq+=' ' + str(hien_tai.gia_tri)
      else:
        kq+=' -> ' + str(hien_tai.gia_tri)
      # if
      hien_tai = hien_tai.nut_ke
    # while
    kq += ' ]'
    print(kq)
  # def

  def them(self,gia_tri):
    nut = Nut(gia_tri)
    if self.dau==None:
      self.dau=nut
      self.duoi=nut
    else:
      self.duoi.nut_ke=nut
      self.duoi=nut
    # if
  # def

  def chen(self,chi_muc,gia_tri):
    nut = Nut(gia_tri)
    truoc = None
    hien_tai = self.dau
    i = 0
    while i < chi_muc and hien_tai != None:
      i+=1
      truoc = hien_tai
      hien_tai = hien_tai.nut_ke
    # while
    if truoc == None:
      # them vao dau danh sach
      nut.nut_ke=self.dau
      self.dau=nut
      if self.duoi==None:
        self.duoi=nut
      # if
    else:
      if hien_tai == None:
        # Them vao cuoi danh sach
        self.duoi.nut_ke = nut
        self.duoi = nut
      else:
        # Them vao giua danh sach
        truoc.nut_ke = nut
        nut.nut_ke = hien_tai
  # def

  def tim(self,gia_tri):
    hien_tai = self.dau
    vi_tri = 0
    while hien_tai!=None and hien_tai.gia_tri!=gia_tri:
      hien_tai = hien_tai.nut_ke
      vi_tri+=1
    # while
    if hien_tai == None:
      return None
    else:
      return vi_tri
    # if
  # def

  def xoa(self,gia_tri):
    hien_tai = self.dau
    truoc = None
    while hien_tai != None and hien_tai.gia_tri!=gia_tri:
      truoc = hien_tai
      hien_tai = hien_tai.nut_ke
    # while
    if hien_tai!=None:
      # tim thay
      if hien_tai == self.dau and hien_tai==self.duoi:
        # xoa phan tu duy nhat
        self.dau = self.duoi = None
      elif hien_tai == self.dau:
        # xoa phan tu dau tien
        self.dau = self.dau.nut_ke
      elif hien_tai == self.duoi:
        #xoa phan tu duoi 
        truoc.nut_ke = None
        self.duoi = truoc
      else:
        # xoa o giua
        truoc.nut_ke = hien_tai.nut_ke
      # if
      del hien_tai

  # def

  def cap_nhap(self,vi_tri,gia_tri):
    hien_tai = self.dau
    i = 0
    while i < vi_tri and hien_tai != None:
      i+=1
      hien_tai = hien_tai.nut_ke
    # while
    if hien_tai != None:
      hien_tai.gia_tri = gia_tri
    # if
  # def

  def xoa_het(self):
    hien_tai = self.dau
    self.dau = self.duoi = None
    while hien_tai != None:
      tam = hien_tai
      hien_tai = hien_tai.nut_ke
      del tam
    # while
  # def



    