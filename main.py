class hewan :
    def __init__(self, bulu, suara, kaki):
        self.bulu=bulu
        self.suara=suara
        self.kaki=kaki

    def jenis(self):
        return self.bulu

    def bunyi(self):
        return self.suara

ironman=hewan("Putih", "Semongko", 10)
print(ironman.jenis())