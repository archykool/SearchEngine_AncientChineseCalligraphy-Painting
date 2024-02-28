import pandas as pd
# 打开文件
data = pd.read_excel('C:/Users/lenovo/Desktop/h/文件名.xlsx')

# 去除全部为空/特定字段为空的行
data = data.dropna(subset=[''])
# 字符串化
data['size'] = data['size'].astype(str)
# 将尺寸字段统一为"纵xx厘米,横xx厘米."
data['sz'] = data['size'].str.extract(r'纵.*?。',expand=False)
# 去除掉爬取到的内容中标签内的东西
data = data['content'].str.contains(r'<.*?>')
data['content'] = data['content'].replace(regex = [r'<.*?>'],value = '')


# 保存文件
data.to_excel('C:/Users/lenovo/Desktop/p/content.xlsx')


匹配起止：a.*?b
