from aocd import data, submit


def find_space(arr, start_pos):
    for i, elem in enumerate(arr[start_pos:]):
        if elem == '.':
            return i+start_pos
    return -1


def generate_representation(data):
    arr = []
    isData = True
    index = 0
    for num in data:
        for i in range(int(num)):
            if isData:
                arr.append(index)
            else:
                arr.append('.')
        if isData:
            index+=1    
        isData = not isData
    return arr


def find_space_with_length(arr, index, block_len):
    while index < len(arr) - block_len:
        if arr[index] != '.':
            index+=1
            continue
        end_location = -1
        for i in range(block_len):
            if arr[index+i] != '.':
                end_location = index+i
                break
        if end_location != -1:
            index = end_location
        else:
            return index
    return -1


def part_a(data):
    data = data.strip()
    arr = generate_representation(data)

    space_pos = 0
    for i, elem in reversed(list(enumerate(arr))):
        space_pos = find_space(arr, space_pos)
        if space_pos != -1:
            arr[space_pos] = arr.pop() # could also just replace with .
        else:
            break

    checksum = 0
    for i, elem in enumerate(arr):
        checksum+=i*elem
    return checksum


def part_b(data):
    data = data.strip()
    arr = generate_representation(data)
 
    index = len(arr) - 1
    
    while index >= 0:
        if arr[index] == '.':
            index=index-1
            continue
        block_length = 1
        for i in range(index):
            if arr[index-i] != arr[index]:
                block_length = i
                break
        
        space_start_pos = find_space_with_length(arr, 0, block_length)
        # checking this here is not efficient
        if space_start_pos > index - block_length:
            index = index - block_length
            continue

        if space_start_pos != -1:
            for i in range(block_length):
                arr[space_start_pos+i] = arr[index-i]
                arr[index-i] = '.'
        index = index - block_length

    checksum = 0
    for i, elem in enumerate(arr):
        if elem == '.':
            continue
        checksum+=i*elem
    return checksum


test_data = """\
2333133121414131402
"""


if __name__ == "__main__":
    # assert part_a(test_data) == 1928
    # part_a_ans = part_a(data)
    # print(part_a_ans)
    # input("Submit?")
    # submit(part_a_ans)  
  
    assert part_b(test_data) == 2858
    part_b_ans = part_b(data)
    print(part_b_ans)
    input("Submit?")
    submit(part_b_ans, part='b')      