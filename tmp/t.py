#
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str):
#         dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
#         text1 = "#" +text1
#         text2 = "#" +text2
#         for i in range(1, len(text1)):
#             for j in range(1, len(text2)):
#                 if text1[i] == text2[j]:
#                     dp[i][j] = 1 + dp[i-1][j-1]
#                 else:
#                     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#         # for d in dp:
#         #     print(d)
#         backtext = []
#         back_index = []
#         i = len(text1) - 1
#         j = len(text2) - 1
#         while i != 0 and j != 0:
#             if text1[i] == text2[j]:
#                 backtext.append(text1[i])
#                 back_index.append(i-1)
#                 i -= 1
#                 j -= 1
#             else:
#                 if dp[i-1][j] == dp[i][j]:
#                     i -= 1
#                 elif dp[i][j-1] == dp[i][j]:
#                     j -= 1
#                 else:
#                     assert False
#         # print("".join(backtext)[::-1])
#         # print(back_index[::-1])
#         return dp[-1][-1], "".join(backtext)[::-1], back_index[::-1]
# print(Solution().longestCommonSubsequence("abcde", 'ace'))
#
# print(Solution().longestCommonSubsequence("圆通速递(600233)9月24日晚间公告，20.38亿股限售股将于9月30日上市流通，占公司总股本的71.85%。",
#                                           "圆通速递：20.38亿股限售股9月30日上市流通占总股本71%"))
print(''.join([]))