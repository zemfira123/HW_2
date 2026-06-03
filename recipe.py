from ingridient import Ingrigient
class Recipe:
    def __init__(self, title:str, ingredients=None):
        self.title=title
        if ingredients is not None:
            self.ingredients=ingredients
        else:
            self.ingredients=[]
    def add_ingridients(self, ingredient: Ingrigient):
        for already_have in self.ingredients:
            if already_have==ingredient:
                already_have.quantity+=ingredient.quantity
                return
        self.ingredients.append(ingredient)
    @staticmethod
    def is_valid_ratio(ratio):
        if type(ratio)==int or type(ratio)==float:
            if ratio>0:
                return True
        return False
    def scale(self, ratio: float):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным")
        update=[]
        for ing in self.ingredients:
            new=Ingrigient(ing.name,
                            ing.quantity*ratio,
                            ing.unit
                            )
            update.append(new)
        return Recipe(self.title, update)

    def __len__(self):
        return len(self.ingredients)
    def __str__(self):
        res=f"{self.title}:\n"
        for i in self.ingredients:
            res+=str(i)+"\n"
        return res









