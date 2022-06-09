# # def filter_duplicates(*args):
# #     list1 = []
# #     for number in args:
#         if number in list1:
#             list1 = list1
#         else:
#             list1.append(number)
#
#     return list1
#
# print(filter_duplicates(1, 2, 4, 4, 5))

# def get_top_stocks(stocks, prices):
#     stockno = 0
#     avg = []
#     while stockno < len(prices[0]):
#         listno = 0
#         total = 0
#         while listno < len(prices):
#             stock = prices[listno][stockno]
#             total += stock
#             listno += 1
#         print(f"The average stock price for {stocks[stockno]} is {total/(listno)}")
#         avg.append(total/listno)
#         stockno += 1
#     top3 = 0
#     while top3 < 3:
#         print(stocks[avg.index(max(avg))])
#         avg.pop(avg.index(max(avg)))
#         top3 += 1
#
#     return avg
#
#
# print(get_top_stocks(['AMZN', 'CACC', 'EQIX', 'GOOG', 'ORLY', 'ULTA'],
#                      [[12.81, 11.09, 12.11, 10.93, 9.83, 8.14]
#                      , [10.34, 10.56, 10.14, 12.17, 13.1, 11.22]
#                      , [11.53, 10.67, 10.42, 11.88, 11.77, 10.21]]
#                      ))
#

