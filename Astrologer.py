"""
學習目標:
1. 學習撰寫模組，在python，一個檔案或是一個資料夾都可被視為一個模組。
2. 用test_case來測試自己寫的東西對不對
核心概念:先畫靶再射箭，先設定好自己要的結果，再開始coding。
"""


def get_constellation(month, day) -> str:

    num = month*100+day

    if num < 321:
        num = num+1200

    if num >= 220+1200:
        return '雙魚座'
    elif num >= 122+1200:
        return '水瓶座'
    elif num >= 1223:
        return '魔羯座'
    elif num >= 1123:
        return '射手座'
    elif num >= 1023:
        return '天蠍座'
    elif num >= 923:
        return '天秤座'
    elif num >= 823:
        return '處女座'
    elif num >= 723:
        return '獅子座'
    elif num >= 621:
        return '巨蟹座'
    elif num >= 521:
        return '雙子座'
    elif num >= 421:
        return '金牛座'
    elif num >= 321:
        return '牡羊座'
    """
    根據生日回傳正確的星座
    牡羊座	3月21日～4月20日
    金牛座	4月21日～5月20日
    雙子座	5月21日～6月20日
    巨蟹座	6月21日～7月22日
    獅子座	7月23日～8月22日
    處女座	8月23日～9月22日
    天秤座	9月23日～10月22日
    天蠍座	10月23日～11月22日
    射手座	11月23日～12月22日
    魔羯座	12月23日～1月21日
    水瓶座	1月22日～2月19日
    雙魚座	2月20日～3月20日
    """

    return ''


def get_each_number( number ) -> []:
    """
    輸入一個正整數，然後將每一位數分開。
    ex get_each_number(1920)
    return [1,9,2,0]
    """

    result = []
    while number>=10:
        result.append(number%10)
        number=int(number/10)
    result.append(number)

    result.reverse()

    return result


def get_life_number(year=1900, month=1, day=1) -> int:
    """
    會回傳一個生命靈數，生命靈數的計算方式是出生年月日的每一個數字的總和，不斷加總至個位數。
    ex 1995 12 13 -> 1+9+9+5+1+2+1+3 = 31 -> 3+1 =4
    這樣生命靈數就是4
    """

    total_num = []
    y = get_each_number(year)
    m = get_each_number(month)
    d = get_each_number(day)
    total_num = y+m+d

    while len(total_num)>1:
        sum = 0
        for n in total_num:
            sum += n
        total_num = get_each_number(sum)
    life_num = total_num[0]
    return life_num


