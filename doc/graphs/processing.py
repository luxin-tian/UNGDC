fhand = open('processing', 'r').readlines()
i = 0

print('\\begin{table}\n\centering\n\\caption{Top 5 topics discussed over years}\n\label{tab:top 5 topics all}\n\\begin{tabular}{lrrrrr}')
print('\\toprule\nCountry &     Top 1 &     Top 2 &     Top 3 &     Top 4 &     Top 5 \\\\\n\midrule')

for line in fhand: 
    topic_list = [line[:-3].split('&')[0]]
    for topic in line[:-3].split('&')[1:]: 
        topic = topic.strip().split('_')[1]
        topic_list.append(topic)
    print(' & '.join(topic_list) + '\\\\')
    if i == 35: 
        i = 0
        print('\\bottomrule\n\\end{tabular}\\end{table}')
        print('\n\n')
        print('\\begin{table}\n\centering\n\\caption{Top 5 topics discussed over years (continued)}\n\label{tab:top 5 topics all}\n\\begin{tabular}{lrrrrr}')
        print('\\toprule\nCountry &     Top 1 &     Top 2 &     Top 3 &     Top 4 &     Top 5 \\\\\n\midrule')
    else: 
        i += 1
print('\\bottomrule\n\\end{tabular}\\end{table}')