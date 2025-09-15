nums=[1,2,3]
#nums=[2,3,4,5,6]
def folk(nums):
    for i in nums:
        for j in nums:
            print (i+j)

def min_max(nums):
    return(min(nums), max(nums))


def sleep(cs):
    for i in range(20):
        print (tuple('spam')*len(cs))
