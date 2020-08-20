# We will be working on packing and unpacking of elements in Python


def pack_unpack():
    """Let's pack and unpack some of the elements"""
    fruits = ['Apple', 'Mango', 'Guava', 'Kiwi']
    print(f"Elements of a list prior unpack are: {fruits}")
    print("Unpacking ...")
    apple, mango, guava, kiwi = fruits
    print(f"Elements post unpacking are: {apple}, {mango}, {guava}, {kiwi}")
    print("Packing ...")
    fruit1, fruit2, fruit3, fruit4 = 'Banana', 'Grape', 'Pomegranate', 'Citrus'
    print(f"Elements prior packing are: {fruit1}, {fruit2}, {fruit3}, {fruit4}")
    fruits_new_list = [fruit1, fruit2, fruit3, fruit4]
    print(f"Elements post packing are: {fruits_new_list}")
    print('Packing and Unpacking is done')


pack_unpack()
