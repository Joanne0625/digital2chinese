class NumToCh():
    def __init__(self):

        self.num_dic = ["零" , "壹" , "貳" , "參" , "肆" , "伍" , "陸" , "柒" , "捌" , "玖"]
        self.unit_dic = ["十" , "百" , "千"]
    
    def four_ch(self,num_str):
        result = ""
        num_len = len(num_str)
        for i in range(num_len):
            num = int(num_str[i])
            if i != num_len - 1 and num != 0 :
                result += self.num_dic[num] + self.unit_dic[num_len - 2 - i]
            else :
                if num == 0 and result and result[-1]=='零':
                    continue
                else:
                    result += self.num_dic[num]
        return result

    def NumTB(self,num_str):
        str_len = len(num_str)
        if str_len > 12 :
            print('數字太大！')
            return
        elif str_len > 8:
            hanstr = self.four_ch(num_str[:-8]) + "億" + \
                self.four_ch(num_str[-8: -4]) + "萬" + \
                self.four_ch(num_str[-4:])
        elif str_len > 4:
            hanstr = self.four_ch(num_str[:-4]) + "萬" + \
                self.four_ch(num_str[-4:])
        else:
            hanstr = self.four_ch(num_str)

        if hanstr[-1]=='零':
            hanstr = hanstr[:-1]
        return hanstr

num = '88880000'
nth = NumToCh()
ans = nth.NumTB(num)
print(ans)