import random # vertex 내부 value 값을 넣기 위한 random 모듈

## ADT
# 1. object 
#       : A. DFS, BFS를 수행하는 Graph 생성
#       : B. 인접 행렬 (2차원 행렬 기반) Graph 생성
#       : C. 인접 리스트(Linked List 기반) Graph 생성
    # 1) vertex property 정의 
        # 1-1) L_adjacency : 인접한 vertex List 
        # 1-2) i_edgeNum : Edge 갯수 (integer)
        # 1-3) i_value : 임의의 숫자 (integer)
    # 2) graph 정의
        # 2-1) L_vertex : vertex List
        # 2-2) edge_Num : edge의 갯수

# 2. Operation :
    # 1) add_vertex() : vertex 생성 함수
    # 2) vertex 삭제 함수
    # 3) DFS 수행 함수 (input : 찾는 vertex Info, return : vertex)
    # 4) BFS 수행 함수 (input : 찾는 vertex Info, return : vertex)
    # 5) 인접 vertex 확인 함수
    # 6) vertex 연결 함수 (input : 인접할 vertex, return : 0)
    # 7) get_vertexNum(graph.L_vertex) : vertex Length 확인 용도의 함수
    # 8) add_Edge(graph, currentVertexNum, targetVertexNum) : 지정된 graph의 start Vertex와 연결할 target Vertex의 Edge 추가

# 진행 하며 추가된 Operation
    # 1) is_empty : vertex가 비여있는지 확인하는 함수

MAX_VERTEX = 10 # graph vertex 수 최대값 지정(최대 vertex 수 지정)
class matrix_Vertex: # 인접 행렬 vertex
    def __init__(self):
        self.i_value = random.randrange(1,101) #1~100 사이에 난수 지정

class matrix_Graph: # 인접 행렬 Graph
    def __init__ (self, L_vertex = None, L_adjacency = None):
        self.L_vertex = []     # graph가 갖고 있는 vertex List
        self.vertexNum = []    # vertex 갯수 
                                            # -> vertex List의 수를 확인하는 함수로 적용하면 됌 L_vertex.length() 
                                            # -> 파이썬에서는 length()함수가 아닌, len()를 이용함. 따라서, retrun len(L_vertex)를 갖고 있는 함수를 생성할 예정
        # self.edge = edge              # Edge는 연결된 위치를 알기 위한 vertex Num 갯수 
                                        # -> 생각해보니, 인접 vertex List를 갖고 있으면, edge는 알 필요가 없음.
            
        self.L_adjacency = []  # 해당 vertex의 인접한 vertex를 알기 위한 List
   
    def is_empty(self):
        if len(self.L_vertex) == 0 :
            return False
        else :
            return True
        
    def get_vertexNum(self): # vertex 갯수 getter 
        m_length = len(self.L_vertex)
        return m_length

    def add_vertex(self):
        vertexNum = self.get_vertexNum()
        if vertexNum + 1 > MAX_VERTEX :
            print("Vertex 최대 값 %d를 추가 하였습니다.\n", MAX_VERTEX)
            return 
        self.L_vertex.append(matrix_Vertex()) # Vertex 추가    
        
        ## L_adjacency에 행 증가
        L_temp = []
        for j in range(vertexNum+1):
            L_temp.append(0)
        self.L_adjacency.append(L_temp) 

        ## L_adjacency에 열 증가
        for i in range(vertexNum):
            self.L_adjacency[i].append(0)


    def add_edge(self, currentVertexNum, targetVertexNum) : #1번째 와 3번째 엣지 연결
        vertexNum = self.get_vertexNum()
        if(currentVertexNum >= vertexNum or targetVertexNum >= vertexNum ):
            print("Graph에 없는 vertex를 연결하였습니다. \n")
            return 
        
        self.L_adjacency[currentVertexNum-1][targetVertexNum-1] = 1 # 2차원 배열에서 관계성(Edge) 없음을 의미, true == 1
        self.L_adjacency[targetVertexNum-1][currentVertexNum-1] = 1
        
    def print_graph(self):
        vertexNum = self.get_vertexNum()
        print("vertexNum : %d" %vertexNum)
        for i in range(vertexNum):
            print(self.L_adjacency[i])
 
    def create_Graph(self, number): # 임의의 graph 생성 : (number x number 행렬) 
        # *************** create_Graph 초기 생성에서 문제 발생함 *************** # 
        #    for i in range(number):
                # for j in range(number):
                #     self.L_adjacency[i,j] = 0 # 2차원 배열에서 관계성(Edge) 없음을 의미, False == 0 
        # 에러명 : TypeError: list indices must be integers or slices, not tuple
        # 원인 : List를 2차원 행렬로 지정하려고 했을 때, List 문법 문제... 기존 C, Java처럼 지정하여 문제 발생함.
        
        # 해결방법 
            # # case1 
            # self.L_adjacency = [ [0 for j in range(number)] 
            #                     for i in range(number) ]  # 2차원 배열에서 관계성(Edge) 없음을 의미, False == 0 
            # for i in range(number):
            #     self.L_vertex.append(matrix_Vertex())
            #case 2
            for i in range(number):
                self.L_vertex.append(matrix_Vertex())
                L_temp = []
                for j in range(number):
                    L_temp.append(0)
                self.L_adjacency.append(L_temp)   # 2차원 배열에서 관계성(Edge) 없음을 의미, False == 0 
                     
        # 결론.
            #  python에서 2차원 행렬은 1차원 리스트 요소에 n차원
            # 참고 URL(List 2차원 행렬 초기화) : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=dsz08082&logNo=221328844937
            # 참고 URL2(얇은 복사 개념) : https://yechoi.tistory.com/52

## Main
# 인접 행렬 (2차원 행렬 기반) Graph 테스트 
testGraph = matrix_Graph()
testGraph.create_Graph(5)
testGraph.print_graph()
testGraph.add_vertex()
testGraph.print_graph()
testGraph.add_edge(1,2)
testGraph.print_graph()
testGraph.add_edge(4,3)
testGraph.print_graph()

class DFS: #시간 부족.. 주말에 진행.....
    def __init__(self):
        self.root = None
