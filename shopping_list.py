from ingridient import Ingrigient
from recipe import Recipe

class ShoppingList:
    def __init__(self):
        self._items=[]
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled=recipe.scale(portions)
        for ing in scaled.ingredients:
            self._items.append((ing, recipe.title))
    def remove_recipe(self, title: str):
        new_items= []
        for i in self._items:
            recipe_title=i[1]
            if recipe_title!=title:
                new_items.append(i)
        self._items=new_items
    def get_list(self):
        total={}
        for i, j in self._items:
            key=(i.name, i.unit)
            if key in total:
                total[key]+=i.quantity
            else:
                total[key]=i.quantity
        res=[]
        for key in total:
            name, unit=key
            quantity=total[key]
            ing=Ingrigient(name, quantity, unit)
            res.append(ing)
        res.sort(key=lambda x: x.name)
        return res
    def __add__(self, other: ShoppingList):
        new_lst=ShoppingList()
        new_lst._items=self._items+other._items
        return new_lst






