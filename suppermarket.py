class supermarket:
    print("Tasavvur qiling bu yerda juda yaxshi kod bor")
    def __init__(self,name,location,reyting):
        self.name=name
        self.location=location
        self.reyting=reyting
    tovar={}
    def add_basket(self, product, price):
        supermarket.tovar[product]=price
market = supermarket("Al_ofiyat","SHahriston","O'ta baland sifatli")

    
