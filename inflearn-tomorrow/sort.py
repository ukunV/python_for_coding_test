#!/usr/bin/env python
# coding: utf-8

# ### Selection Sort

# In[15]:


nums = [5, 10, 66, 77, 54, 32, 11, 15]
l = []

while nums:
    l.append(min(nums))
    nums.pop(nums.index(min(nums)))
    print(l)
    print(nums)
    print('----------------------------------')
    
print('-final-')
print(l)
print(nums)


# In[7]:


nums = [5, 10, 66, 77, 1, 54, 32, 11, 15]

def fmin(l):
    min = l[0]
    count = 0
    for i in l:
        if min > i:
            min = i
            index = count
        count += 1
    return index

print(fmin(nums))


# In[9]:


nums = [5, 10, 66, 77, 1, 54, 32, 11, 15]

def min_index(l):
    idx = 0
    temp = l[0]
    for i in range(len(l)):
        if l[i] < temp:
            idx = i
    return idx

print(fmin(nums))


# ### Insert Sort

# In[16]:


nums = [5, 10, 66, 77, 54, 32, 11, 15]
l = []

def ins_idx(l, nums):
    for i in range(len(l)):
        if ins < l[i]:
            return i
        
    return len(l)

while nums:
    ins = nums.pop(0)
    idx = ins_idx(l, nums)
    l.insert(idx, ins)
    
print(l)


# ### Merge Sort

# In[19]:


# Meroge Sort : O(nlogn)
# Divide and Conquer
nums = [5, 10, 66, 77, 54, 32, 11, 15]
nc = 7
mid = 7 // 2 # 3

print(nums[:mid+1])
print(nums[mid+1:])


# In[21]:


def msort(nums):
    nlen = len(nums)
    res = []
    
    if nlen <= 1:
        return nums
    mid = nlen // 2
    g1 = msort(nums[:mid])
    g2 = msort(nums[mid:])
    while g1 and g2:
        if g1[0] < g2[0]:
            res.append(g1.pop(0))
        else:
            res.append(g2.pop(0))
    while g1:
        res.append(g1.pop(0))
    while g2:
        res.append(g2.pop(0))
    
    return res

print(msort([5, 10, 66, 77, 54, 32, 11, 15]))


# ### Quick Sort

# <pre>
# # Quick Sort : O(nlognn) but worst is O(n^2)
# # pivot
# 
# [66, 77, 54, 32, 10, 5, 11, 15]
# [54, 32, 10, 5, 11, 15] + [66] + [77]
# [32, 10, 5, 11, 15] + [54] + [66] + [77]
# [10, 5, 11, 15] + [32] + [54] + [66] + [77]
# [5] + [10] + [11, 15] + [32] + [54] + [66] + [77]
# [5] + [10] + [11] + [15] + [32] + [54] + [66] + [77]
# </pre>

# In[31]:


g_list = []

def qsort(nums):
    global g_list
    nlen = len(nums)
    if nlen <= 1:
        return nums
    pivot = nums.pop(0)
    g1 = []
    g2 = []
    for i in range(nlen-1):
        if nums[i] < pivot:
            g1.append(nums[i])
        else:
            g2.append(nums[i])
    
    result = 'group 1 : {} // pivot : {} // group 2 : {}' .format(g1, pivot, g2)
    g_list.append(result)
    
    return qsort(g1) + [pivot] + qsort(g2)

nums = [66, 77, 54, 32, 10, 5, 11, 15]
print(qsort(nums))

for i in g_list:
    print(i)

