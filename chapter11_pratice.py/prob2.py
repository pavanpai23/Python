class animals:
    pass
class cats(animals):
    pass
class dogs(cats):
    @staticmethod
    def bow():
        print("bow bow")


d=dogs()
d.bow()
 

    
