from py2neo import Graph, Node, Relationship, NodeMatcher
import csv

graph = Graph('bolt://localhost:7687', auth=("neo4j", "147258369"), name='neo4j')

# 删除所有已有节点
graph.delete_all()

with open('triples1.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        entity1 = Node("Entity", name=row['entity1'])
        entity2 = Node("Entity", name=row['entity2'])

        relationship = Relationship(entity1, row['relationship'], entity2)

        graph.create(entity1)
        graph.create(entity2)
        graph.create(relationship)

print("知识图谱创建完成")