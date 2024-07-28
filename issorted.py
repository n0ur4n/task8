nums=input("please enter the numbers ")
def is_sorted():
    for i in range (len(nums)-1):
        if nums[i]>nums [i+1]:
            print("false")
            exit()
    
        else:
            continue

    print("true")
is_sorted()