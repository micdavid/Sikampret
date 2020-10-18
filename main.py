class hewan :
    def __init__(self, bulu, suara, kaki):
        self.bulu=bulu
        self.suara=suara
        self.kaki=kaki

    def jenis(self):
        return self.bulu

ironman=hewan("Putih", "Semongko", 10)
print(ironman.jenis())