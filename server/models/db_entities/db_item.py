class DBItem:
    def __init__(self, itemID, itemName, itemDesc, img, price, business_id):
        self.ID = itemID  # int
        self.name = itemName  # string
        self.desc = itemDesc  # string
        self.img = img  # bytes
        self.price = price  # int
        self.business_id = business_id  # int



def test():
    i = Item(654564, "r3'eef shawarma", "r3'eef Shawarmet 7abash", "some bytes here", 34, 1)
    print(i.name + "'s price is: " + str(i.price) + ", it contains: " + i.desc)

