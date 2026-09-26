class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = Counter(nums)

        res = sorted(hmap, key=hmap.get, reverse = True)[:k]
        return res

        