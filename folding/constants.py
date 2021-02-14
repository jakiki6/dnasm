spike_test = [9, 14, 20, 14, 11, 20, 16, 4, 20, 2, 11, 17, 5, 15, 17, 2, 16, 1, 7, 20, 19, 15, 12, 20, 20, 8, 17, 15, 14, 2, 20, 17, 18, 8, 0, 8, 16, 2, 7, 17, 14, 3, 15, 14, 2, 3, 7, 20, 19, 14, 0, 17, 16, 18, 10, 14, 7, 17, 17, 3, 11, 10, 20, 2, 0, 17, 2, 20, 20, 10, 12, 4, 6, 14, 5, 14, 4, 2, 3, 14, 7, 20, 19, 12, 12, 18, 9, 6, 20, 19, 16, 2, 2, 17, 14, 6, 19, 16, 15, 14, 11, 9, 11, 6, 12, 7, 2, 12, 2, 11, 6, 14, 14, 2, 10, 3, 7, 19, 14, 12, 19, 16, 15, 10, 2, 1, 3, 15, 7, 14, 0, 6, 3, 7, 10, 17, 14, 5, 17, 11, 0, 8, 19, 17, 15, 7, 3, 16, 16, 7, 18, 0, 7, 0, 0, 19, 19, 7, 19, 11, 5, 15, 17, 14, 12, 19, 2, 6, 2, 10, 3, 0, 4, 11, 15, 6, 4, 12, 17, 6, 12, 19, 5, 17, 16, 14, 5, 6, 16, 10, 20, 14, 15, 2, 10, 15, 14, 7, 6, 20, 14, 14, 16, 20, 19, 0, 18, 4, 20, 0, 3, 19, 16, 19, 2, 14, 17, 14, 4, 19, 16, 15, 17, 12, 2, 3, 14, 17, 2, 19, 3, 14, 10, 7, 3, 6, 5, 0, 5, 17, 10, 0, 3, 19, 2, 19, 12, 3, 3, 14, 20, 0, 18, 2, 16, 2, 11, 3, 16, 20, 7, 7, 2, 19, 2, 19, 14, 16, 2, 12, 15, 14, 3, 10, 17, 6, 19, 7, 15, 4, 2, 7, 20, 6, 7, 14, 2, 4, 14, 15, 5, 19, 7, 5, 17, 2, 7, 20, 7, 5, 11, 16, 14, 6, 11, 8, 17, 20, 4, 15, 12, 16, 17, 2, 20, 12, 12, 4, 2, 2, 7, 7, 20, 11, 17, 16, 12, 14, 15, 5, 5, 14, 10, 0, 17, 17, 3, 0, 1, 3, 11, 10, 11, 10, 4, 16, 14, 7, 7, 20, 2, 17, 16, 20, 0, 20, 11, 19, 3, 20, 6, 15, 20, 0, 10, 8, 3, 5, 11, 17, 15, 17, 18, 1, 20, 19, 16, 7, 16, 2, 20, 14, 5, 1, 4, 0, 6, 8, 19, 4, 10, 7, 7, 0, 19, 17, 17, 2, 16, 15, 1, 0, 5, 10, 17, 9, 11, 7, 6, 2, 20, 0, 16, 2, 16, 10, 2, 14, 17, 10, 20, 6, 10, 16, 9, 3, 4, 9, 10, 4, 7, 3, 17, 6, 2, 11, 5, 19, 14, 4, 5, 1, 0, 17, 0, 20, 6, 5, 12, 5, 6, 20, 14, 5, 12, 5, 10, 12, 10, 12, 3, 14, 7, 7, 14, 2, 14, 5, 3, 12, 14, 10, 6, 3, 11, 12, 11, 3, 0, 12, 5, 19, 7, 3, 11, 7, 3, 10, 0, 0, 10, 4, 5, 14, 11, 17, 20, 15, 3, 6, 9, 10, 0, 5, 17, 16, 7, 17, 16, 7, 18, 14, 7, 7, 0, 5, 14, 0, 9, 5, 9, 0, 19, 14, 2, 7, 10, 20, 2, 20, 19, 5, 12, 10, 5, 14, 2, 0, 10, 12, 10, 5, 11, 16, 11, 12, 11, 5, 3, 5, 2, 5, 0, 11, 20, 12, 5, 11, 2, 14, 7, 10, 20, 2, 3, 11, 1, 11, 12, 20, 0, 6, 5, 10, 3, 11, 5, 19, 17, 5, 5, 10, 0, 6, 0, 16, 0, 2, 11, 0, 0, 17, 12, 9, 4, 11, 5, 12, 20, 3, 14, 4, 19, 8, 11, 9, 15, 15, 8, 7, 8, 17, 19, 15, 5, 6, 17, 0, 15, 10, 4, 8, 3, 12, 14, 15, 1, 6, 7, 14, 20, 2, 18, 14, 5, 2, 14, 19, 6, 5, 10, 17, 14, 16, 7, 4, 3, 20, 10, 20, 19, 3, 15, 5, 15, 6, 3, 12, 19, 14, 2, 8, 3, 20, 3, 7, 16, 10, 2, 0, 20, 10, 5, 12, 6, 10, 2, 20, 2, 2, 6, 16, 3, 5, 6, 11, 19, 19, 12, 18, 18, 10, 18, 7, 14, 0, 10, 9, 10, 9, 11, 4, 9, 4, 4, 4, 4, 16, 4, 12, 14, 3, 6, 16, 12, 12, 8, 21]
