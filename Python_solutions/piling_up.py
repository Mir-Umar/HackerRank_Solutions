# Enter your code here. Read input from STDIN. Print output to STDOUT
def piling_up(cubes):
    left = 0
    right = len(cubes) - 1
    last_cube = float('inf')  # Initialize to a very large value
    while left <= right:
        if cubes[left] >= cubes[right]:
            chosen_cube = cubes[left]
            left += 1
        else:
            chosen_cube = cubes[right]
            right -= 1
        
        if chosen_cube > last_cube:
            return "No"
        
        last_cube = chosen_cube
    
    return "Yes"

if __name__ == '__main__':
    cases = int(input())
    for i in range(cases):
        num_blocks = int(input())
        blocks = list(map(int, input().split()))
        print(piling_up(blocks))
