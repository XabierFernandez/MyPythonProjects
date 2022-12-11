def compute_lcw(string_1, string_2):
   val = [[-1]*(len(string_2) + 1) for _ in range(len(string_1) + 1)]
   for i in range(len(string_1) + 1):
      val[i][len(string_2)] = 0
   for j in range(len(string_2)):
      val[len(string_1)][j] = 0
   lcw_i = lcw_j = -1
   lcw_len = 0
   for i in range(len(string_1) - 1, -1, -1):
      for j in range(len(string_2)):
         if string_1[i] != string_2[j]:
            val[i][j] = 0
         else:
            val[i][j] = 1 + val[i + 1][j + 1]
            if lcw_len < val[i][j]:
               lcw_len = val[i][j]
               lcw_i = i
               lcw_j = j
   return lcw_len, lcw_i, lcw_j

if __name__ == '__main__':
   string_1 = 'bull'
   string_2 = 'bullied'
   lcw_len, lcw_i, lcw_j = compute_lcw(string_1, string_2)
   print("The longest common substring is : ")
   if lcw_len > 0:
      print(string_1[lcw_i:lcw_i + lcw_len])