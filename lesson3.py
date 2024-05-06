class Kertenkele():
    
    sinif ="Surunenler"
    
    def __init__(self,ad,yas,reng):
        self.ad =ad
        self.yas=yas
        self.reng=reng
        
    def pullu_dərilidir(self):
        return f"{self.ad} pulu_dərilidir"
    
    def suda_yasaya_bilme(self,suda_yasaya_bilme=False):
        if suda_yasaya_bilme:
            return f"{self.ad} suda_yasayir"
        else:
            return f"{self.ad} suda yasaya bilmir"
    
    def zəhərlilik(self,zəhərlilik=False):
        if zəhərlilik:
            return f"{self.ad} zəhərlidir"
        else:
            return f"{self.ad} zəhərli deyil"
        
    def gecə_fəaliyyeti(self,gecə_fəaliyyeti=False):
        if gecə_fəaliyyeti:
            return f"{self.ad} gecə gəzər"
        else:
            return f"{self.ad} gunduz gəzər"
        
səhraİquanasi = Kertenkele("Səhra İquanasi",3,"Sari")
çolİquanasi = Kertenkele("Çol İquanasi",4,"Qəhvəyi")
buqələmun = Kertenkele("Buqələmun",1,"Yasil")

print(f"{səhraİquanasi.ad}-nin {səhraİquanasi.yas} yasi var ve rengi {səhraİquanasi.reng}-dir.{səhraİquanasi.sinif} sinifine aiddir:")
print(f"{çolİquanasi.ad}-nin {çolİquanasi.yas} yasi var ve rengi {çolİquanasi.reng}-dir.{çolİquanasi.sinif} sinfine daxildir:")
print(f"{buqələmun.ad}-nin {buqələmun.yas} yasi var ve rengi {buqələmun.reng}-dir.{buqələmun.sinif} sinfine daxildir:")
      
print(səhraİquanasi.pullu_dərilidir())
print(f"{səhraİquanasi.suda_yasaya_bilme(False)} ve {səhraİquanasi.zəhərlilik(True)} ve {səhraİquanasi.gecə_fəaliyyeti(False)}")

print(çolİquanasi.pullu_dərilidir())
print(f"{çolİquanasi.suda_yasaya_bilme(False)} ve {çolİquanasi.zəhərlilik(False)} ve {çolİquanasi.gecə_fəaliyyeti(False)}")

print(buqələmun.pullu_dərilidir())
print(f"{buqələmun.suda_yasaya_bilme(True)} ve {buqələmun.zəhərlilik(True)} ve {buqələmun.gecə_fəaliyyeti(True)}")

