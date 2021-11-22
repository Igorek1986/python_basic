from parent import Parent
from child import Child

igor = Parent('Igor', 35)
dima = Child('Dima', 7, True, True)
igor.add_child(dima)
igor.print_info()
dima.print_info()
dima.calm(igor)
dima.hunger(igor)
dima.print_info()

# зачёт!
