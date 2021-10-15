from donut import Donut

def main():
    chocolate_donut = Donut(weight=90, kcal=352, name='Chocolate donut')
    vanilla_donut = Donut(weight=80, kcal=250, name='Vanilla donut')
    print('Available donuts: ')
    chocolate_donut.print_donut()
    vanilla_donut.print_donut()

    
if __name__ == '__main__':
    main()