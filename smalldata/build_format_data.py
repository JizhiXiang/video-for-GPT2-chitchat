

# 这个脚本将raw_data.txt转换为data.txt
# raw_data.txt从https://github.com/MarkWuNLP/MultiTurnResponseSelection下载的
# data.txt格式为GPT2-chitchat所需格式
'''
想看你的美照
亲我一口就给你看
我亲两口
讨厌人家拿小拳拳捶你胸口

下一组语料
'''
path = 'raw_data.txt'
out = 'data.txt'
fw = open(out,'w',encoding='utf-8')
for line in open(path,'r',encoding='utf-8').readlines():
    parts = line.split('\t')  # 一个样本
    for one_sent in parts[1:]:  # 里面包含很多句话
        one_sent = ''.join(one_sent.strip().split(' '))
        fw.write(one_sent+'\n')
    fw.write('\n')
fw.close()
print('finish')