from py2neo import Graph, Node, Relationship, NodeMatcher

graph = Graph('bolt://localhost:7687', auth=("neo4j", "147258369"), name='neo4j')

# 删除所有已有节点
graph.delete_all()

teacher = Node('Person', name='老师')
studenta = Node('Person', name='学生A')
studentb = Node('Person', name='学生B')

graph.create(Relationship(teacher, "师生", studenta))
graph.create(Relationship(teacher, "师生", studentb))
graph.create(Relationship(studenta, "同学", studentb))

print("知识图谱创建完成")