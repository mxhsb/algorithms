"""
Created on Mon Apr  2 00:27:26 2018 ----------- @author: mxhfield
"""

def max_area(A):
    n = len(A)
    mx = 0
    
    left = 0
    right = n-1
        
    while left < right:
        current = min(A[left], A[right])
        mx = max(mx, (right-left)*current)
        
        print('min:',A[left], A[right], '=======','max:',mx, (right-left),'*',current)
        
        if A[left] < A[right]:
            left += 1
        else:
            right -= 1
    return mx


def maxArea(A):
    
    index_r = 0
    index_l = len(A)-1
    max_area = 0
    
    while(index_r<index_l):
        height = min(A[index_r], A[index_l])
        max_area= max(max_area, height*(index_l-index_r))
        while(index_r<index_l and A[index_r]<=height):
            index_r += 1
        while(index_r<index_l and A[index_l]<=height):
            index_l -= 1
    
    return max_area

a = [7495, 3935, 164, 6024, 6141, 5103, 6452, 4927, 5366, 1096, 9836, 6170, 7801, 7637, 556, 8383, 6750, 2757, 2195, 5080, 3715, 1867, 610, 5864, 7725, 5658, 5090, 8830, 6185, 913, 8362, 571, 5940, 645, 3468, 4160, 5806, 9220, 7390, 108, 8786, 9920, 9077, 3341, 7192, 3812, 664, 6913, 1310, 9222, 6796, 5041, 5320, 8330, 529, 4949, 4888, 9537, 8914, 9545, 6611, 8457, 688, 980, 9653, 6837, 1956, 3818, 17, 6311, 2344, 3918, 9023, 6423, 653, 886, 4364, 9461, 477, 8892, 2336, 1639, 1812, 224, 1489, 7860, 4705, 2482, 9454, 560, 7955, 8782, 9289, 3316, 3760, 7112, 5813, 9161, 6982, 871, 8355, 5508, 8025, 3883, 4932, 4637, 2019, 4766, 5143, 7555, 5160, 2418, 2103, 8293, 9184, 6961, 2361, 6480, 5518, 2454, 1332, 8232, 4961, 252, 8885, 7859, 5026, 7783, 4216, 4832, 3041, 6441, 6520, 4208, 1559, 3622, 8607, 1017, 6728, 2753, 5266, 8160, 4941, 4154, 4557, 8922, 9715, 8846, 5117, 1247, 9305, 4483, 7020, 5124, 9762, 9988, 8399, 2512, 7656, 9162, 5839, 4642, 9103, 4217, 8946, 9396, 3109, 5154, 9224, 8986, 1012, 9323, 2097, 2764, 3508, 8801, 3091, 1295, 6799, 5394, 7911, 3628, 1971, 1599, 8541, 7996, 8303, 4088, 6241, 444, 1459, 1317, 2402, 5264, 1664, 591, 1039, 7103, 4466, 9164, 2491, 1108, 7162, 9127, 7527, 945, 8555, 9679, 2258, 723, 1399, 2717, 1949, 3739, 410, 4120, 1892, 9258, 9735, 9665, 9618, 2990, 696, 4758, 5729, 3869, 6880, 9282, 3526, 3861, 7681, 2973, 7476, 7899, 9787, 5288, 427, 8792, 2584, 3117, 626, 5992, 3094, 3004, 9115, 9044, 2812, 9570, 621, 5559, 6808, 7566, 4842, 2868, 4308, 965, 990, 6948, 4563, 4231, 7643, 8276, 525, 7950, 9717, 5089, 9112, 7066, 4180, 6062, 1538, 7866, 1829, 6369, 6653, 5699, 4939, 3048, 9522, 6355, 9802, 8517, 1338, 84, 169, 8274, 6728, 2581, 3254, 6143, 4566, 1185, 9617, 9939, 4272, 2380, 2918, 4199, 7493, 2775, 1464, 229, 752, 3540, 2705, 6039, 8456, 5492, 5014, 6334, 5496, 8772, 4767, 401, 1881, 9016, 3440, 4842, 6833, 9065, 4816, 8138, 968, 6996, 4351, 7560, 1916, 726, 5231, 3930, 6153, 2394, 3846, 9949, 9869, 5977, 2152, 5601, 6732, 1383, 2503, 9713, 8139, 3643, 9928, 7878, 4432, 5338, 3666, 2636, 9312, 1452, 7766, 9679, 6461, 315, 8206, 1369, 9425, 4947, 8090, 6184, 563, 5379, 5768, 4553, 6894, 2861, 6439, 8930, 8766, 4216, 4554, 5443, 1352, 2419, 8630, 7534, 7217, 669, 2173, 1597, 3935, 2786, 6416, 1367, 7429, 1032, 5707, 4923, 960, 2967, 8968, 4797, 6270, 7144, 2531, 977, 1724, 6693, 4355, 6661, 2969, 8636, 9772, 6090, 5738, 9463, 3181, 6187, 8124, 7073, 4440, 8301, 4557, 3886, 5752, 575, 353, 6222, 1190, 9782, 6164, 8563, 9683, 2752, 7511, 2205, 1440, 7627, 2865, 9952, 8657, 4468, 1596, 1545, 6895, 4202, 9506, 4810, 3525, 6991, 4153, 1895, 8471, 193, 8293, 5110, 9237, 8710, 6002, 1027, 3274, 2964, 4026, 4024, 4750, 4027, 2798, 8722, 4270, 3393, 9846, 5132, 8827, 7758, 2309, 5987, 2339, 2408, 275, 840, 2868, 577, 2108, 5911, 9355, 1657, 3196, 5841, 7915, 7005, 3539, 2169, 8001, 1919, 1457, 1778, 3323, 1200, 6565, 9106, 3783, 7511, 9265, 1053, 3556, 4839, 6220, 795, 5760, 1661, 9910, 2746, 3492, 4242, 4043, 7652, 2422, 3608, 6685, 4214, 1823, 8084, 9027, 7547, 5880, 6391, 7952, 6078, 1347, 3408, 71, 7458, 7281, 5363, 5737, 9625, 5217, 1787, 2616, 3818, 9943, 6051, 1984, 9251, 9160, 5396, 7156, 5065, 4381, 5520, 5641, 9052, 4043, 9444, 8566, 3504, 5483, 9221, 4676, 7473, 1712, 2424, 1476, 3825, 1585, 8067, 6867, 6703, 1668, 6522, 5100, 8736, 4298, 9959, 122, 2362, 3476, 2871, 9893, 534, 7175, 5809, 1354, 2168, 5047, 5718, 6804, 5078, 8753, 4780, 7701, 4460, 8782, 9665, 6495, 6338, 8075, 8380, 7976, 5037, 5290, 9105, 3750, 1287, 8163, 424, 876, 5103, 5353, 7295, 6242, 9932, 3406, 5047, 1429, 7874, 3365, 3594, 2076, 8191, 5474, 2836, 8329, 6083, 3318, 8820, 3975, 5832, 8638, 8992, 1077, 4510, 8645, 7617, 1018, 3517, 9453, 9847, 756, 75, 2037, 3076, 643, 2905, 5940, 704, 618, 8490, 4729, 7030, 5634, 3383, 852, 8380, 5865, 6246, 9491, 209, 408, 6823, 5616, 4956, 3279, 4128, 5483, 1640, 9058, 8541, 4962, 1759, 7410, 9357, 9514, 5135, 3282, 624, 7131, 9984, 1773, 6143, 167, 431, 7832, 7563, 9171, 2533, 5585, 5526, 7716, 432, 6543, 8094, 9627, 8339, 4244, 8684, 7545, 1002, 9921, 2497, 2693, 252, 5570, 2784, 4860, 5330, 8589, 5905, 6631, 6867, 4773, 1809, 4035, 9397, 3437, 9250, 6596, 9098, 3844, 4950, 108, 8023, 1033, 4945, 8178, 8540, 5954, 7781, 2049, 9704, 3473, 9331, 1993, 1149, 1545, 3253, 8017, 5932, 2628, 7594, 9789, 9775, 6379, 2384, 4702, 9594, 1152, 6836, 7122, 7108, 1548, 4800, 6387, 2658, 117, 2228, 6191, 6731, 5174, 5476, 2893, 3707, 5375, 5263, 2949, 2064, 3333, 9717, 7271, 3602, 9649, 4360, 3801, 1309, 8383, 8425, 8810, 9143, 9280, 6203, 4766, 7878, 1051, 5117, 5401, 9447, 8264, 2361, 7903, 2284, 3920, 7063, 5852, 7849, 3148, 2389, 2038, 2248, 3772, 3083, 6256, 1584, 160, 5311, 3066, 466, 6766, 2698, 885, 8431, 65, 9494, 7509, 4894, 4158, 7438, 205, 5467, 3198, 7346, 8398, 8445, 1512, 7834, 404, 3281, 6717, 3587, 9259, 4887, 6152, 2635, 3361, 4514, 4552, 1595, 7810, 6059, 1901, 8364, 6535, 8589, 8722, 7422, 7057, 8336, 3377, 7773, 8865, 4899, 5351, 7172, 3960, 9585, 6283, 396, 8377, 1185, 2166, 3307, 4282, 8628, 5716, 3810, 2203, 3513, 5827, 8992, 7576, 9673, 2321, 9427, 5746, 7364, 4322, 7374, 6661, 9284, 1315, 5593, 5316, 2091, 9815, 7851, 7982, 2748, 6317, 9389, 6681, 6676, 7355, 4958, 3671, 2013, 1992, 3622, 2958, 4512, 9486, 3435, 1209, 6220, 3931, 2898, 8917, 2299, 6575, 696, 1920, 3332, 2102, 5347, 8444, 4476, 7917, 1247, 6590, 584, 3179, 2354, 7326, 2954, 2457, 9930, 3524, 5929, 5104, 1064, 7637, 8533, 1685, 1340, 7570, 8915, 7378, 2432, 3032, 99, 7150, 2267, 3526, 6358, 5447, 4093, 2125, 8108, 3990, 8045, 212, 527, 5490, 3042, 8125, 2501, 2436, 3550, 6803, 8482, 6037, 1229, 4448, 113, 6991, 2704, 8847, 3108, 2487, 1222, 6116, 933, 266, 469, 5468, 2033, 4902, 5375, 2530, 300, 5723, 6615, 5949, 1348, 9675, 2239, 6794]
#print(max_area([1, 5, 4, 3]))
print(max_area(a))