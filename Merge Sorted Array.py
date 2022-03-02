class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def mm(n1,n2,i,j,k):
            if k<0:
                if j>=0:
                    n1[i]=n1[j]
                    i-=1
                    j-=1
                else:
                    return
            elif j<0:
                if k>=0:
                    n1[i]=n2[k]
                    i-=1
                    k-=1
                else:
                    return                
            elif n1[j]>=n2[k]:
                n1[i]=n1[j]
                i-=1
                j-=1
            else:
                n1[i]=n2[k]
                i-=1
                k-=1
            
            mm(n1,n2,i,j,k)
            
        mm(nums1,nums2,m+n-1,m-1,n-1)