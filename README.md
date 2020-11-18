# DiscreteMath

## 1. Resolution method

Given a Boolean formula in 2-CNF, use the resolution method to determine whether it is satisfiable. Clauses of the 2-CNF can be of one of the three forms: α \/ β, or α -> β, or just α. Here α and β are literals (p or ~p, where p is a variable). The CNF is presented in the usual notation, for example: (p -> q) /\ (~r \/ s) /\ (~q -> p)

code: Resolution_method.py

tests: resolition_method_tests.txt

## 2. Graph with ego networks

The SNAP dataset called facebook_combined.txt includes a union of 10 ego networks from Facebook. An ego network is a subgraph of the full friendship graph which includes a central node (ego) together with the vertices to which the ego is connected directly, and edges among them. Thus, each vertex in our dataset is either one of the 10 ego network centers, or is directly connected to (at least) one of them.

The task is as follows. Consider the following set of 11 vertices: 0, 107, 348, 414, 612, 686, 698, 1684, 1912, 3437, 3980. It is guaranteed that this set includes all 10 ego network centers, plus one extra vertex. The program should distinguish the added 11th vertex from the 10 ego network centers. As the answer, please provide the number of this additional vertex.

Notice: for testing, the nodes in the dataset can be renamed, in order to aviod hard-coding of the correct answer.

code: Ego_networks.py

data: facebook_combined.txt
