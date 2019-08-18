# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 20:02:18 2019

@author: HARSH
"""

import heapq

H = [21, 1, 45, 78, 11, 19]
heapq.heapify(H)
print(H)

heapq.heappush(H, 2)
print(H)

heapq.heappop(H)
print(H)

heapq.heapreplace(H, 9)
print(H)