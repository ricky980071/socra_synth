import os
import csv

dir = os.path.dirname(os.path.abspath(__file__))

topic_path = os.path.join(dir, 'topics')
A_path = os.path.join(topic_path, 'A.txt')
B_path = os.path.join(topic_path, 'B.txt')
Out_path = os.path.join(dir, 'output', 'capital_punishment.csv')

def readTxt(path):
    line_count = 0
    topics = []
    contents = []
    conclusion = ''
    with open(path, 'r') as f:
        for line in f:
            if len(line) <= 1:
                continue
            line = line.replace('*', '').replace('\n', '').replace(
                'Conclusion: ', '').replace('-', '').replace(':', '').replace(
                '1.', '').replace('2.', '').replace('3.', '').replace(
                '4.', '').replace('5.', '').strip()
            
            if line_count == 0:
                line_count += 1
            elif line_count in [1, 3, 5, 7, 9]:
                topics.append(line)
                line_count += 1
            elif line_count in [2, 4, 6, 8, 10]:
                contents.append(line)
                line_count += 1
            elif line_count == 11:
                conclusion = line
                line_count += 1

    return topics, contents, conclusion

def writeCSV(path, topics, A_contents, B_contents, A_conclusion, B_conclusion):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['topic', 'Agent-A', 'Agent-B'])
        for topic, A_content, B_content in zip(topics, A_contents, B_contents):
            writer.writerow([topic, A_content, B_content])
        writer.writerow(['conclusion', A_conclusion, B_conclusion])

A_topics, A_contents, A_conclusion = readTxt(A_path)
B_topics, B_contents, B_conclusion = readTxt(B_path)
print(A_topics)
writeCSV(Out_path, A_topics, A_contents, B_contents, A_conclusion, B_conclusion)

