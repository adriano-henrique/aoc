import os

def build_lists(filename):
    l1 = []
    l2 = []
    if os.path.exists(f'files/{filename}'):
        with open(f'files/{filename}', 'r') as file:
            for line in file:
                first_num = int(line.split(" ")[0])
                sec_num = int(line.split(" ")[-1])
                l1.append(first_num)
                l2.append(sec_num)
    else:
        print("File does not exist")

    return l1,l2

def handle_p1(filename = "p1.txt"):
    l1, l2 = build_lists(filename)
    result = 0
    l1.sort()
    l2.sort()
            
    length = len(l1)
    for i in range(length):
        diff = abs(l1[i] - l2[i])
        result += diff
    
    print(result)

def handle_p2(filename = "p2.txt"):
    l1,l2 = build_lists(filename)
    count_map = {}
    result = 0

    for element in l1:
        if element not in count_map:
            count_map[element] = 0
            for sec_element in l2:
                if sec_element == element:
                    count_map[element] += 1

    for element in l1:
        result += element*count_map[element]
        
    print(result)

def test():
    handle_p1('tp1.txt')
    handle_p2('tp2.txt')

def main():
    test()
    handle_p1()
    handle_p2()

main()