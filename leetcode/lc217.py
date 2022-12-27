def containsDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for i in nums:
            if i in result:
                return True
            else:
                result.add(i)
        return False

if __name__ == '__main__':
    input = [1,23,4,1]
    print(containsDuplicate(input))