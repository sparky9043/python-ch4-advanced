"""Module that contains number analyzer function"""

def number_analyzer():
    """Function that generates numbers 1-100 and make lists of:
    even numbers, multiples of 5, squares and makes more lists
    from slices
    """
    numbers = list(range(1, 101))
    evens = [number for number in numbers if number % 2 == 0]
    multiples_of_5 = [number for number in numbers if number % 5 == 0]
    squares = [number ** 2 for number in numbers]
    
    print(f"First 10 evens: {evens[:10]}")
    print(f"Last 5 multiples of 5: {multiples_of_5[-5:]}\n")
    print(f"Total squares sum: {sum(squares)}")
    print(f"Total evens: {len(evens)}")
    print(f"Total multiples of 5: {len(multiples_of_5)}")
        
number_analyzer()