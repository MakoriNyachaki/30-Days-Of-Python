from __future__ import print_function

quote = '成功を収める人とは人が投げてきたレンガでしっかりした基盤を築くことができる人のことである。'

with open('utf8.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(quote))
