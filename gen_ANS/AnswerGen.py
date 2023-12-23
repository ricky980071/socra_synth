import os
import csv

dir = os.path.dirname(os.path.abspath(__file__))

topic_path = os.path.join(dir, 'topics')
A_path = os.path.join(topic_path, 'A.txt')
B_path = os.path.join(topic_path, 'B.txt')
Out_path = os.path.join(dir, 'output', 'capital_punishment.csv')

def readTxt(path):
    topic_gotten = False
    topic_count = 0
    topics = []
    contents = []
    conclusion = ''
    with open(path, 'r') as f:
        for line in f:
            if len(line) <= 1:
                continue
            if line[1] == '.':
                topics.append(line[3:-1].replace('*', '').replace(':', ''))
                topic_gotten = True
                topic_count += 1
            elif topic_gotten is True:
                contents.append(line[:-1].replace('Conclusion: ', ''))
                topic_gotten = False
            elif topic_count == 5:
                conclusion = line[:-1]
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
writeCSV(Out_path, A_topics, A_contents, B_contents, A_conclusion, B_conclusion)

