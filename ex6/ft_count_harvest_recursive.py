def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count_day(current):
        print(f"Day {current}")
        if current < days:
            count_day(current + 1)
        else:
            print("Harvest time!")

    count_day(1)
