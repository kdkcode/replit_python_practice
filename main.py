





'''
#퀵정렬 -> 파이썬 장점을 살린 방식

array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):

  if len(array) <=1:
    return array
  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side=[x for x in tail if x> pivot]

  return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))
'''











'''
#DFS

def dfs(graph,v,visited):
  visited[v]=True
  print(v,end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)


graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]


visited=[False]*9

dfs(graph,1,visited)


'''
'







'''
#재귀함수
def recursive_function():
  print('재귀함수를 호출합니다.')
  recursive_function()


recursive_function()

'''




'''
from decimal import Decimal


f = Decimal('0.1')
sum=0
for i in range(100):
  sum +=f
print(sum)

'''










'''
score = [ 45, 89, 72, 53, 94 ]
for s in map(lambda x:x / 2, score):
    print(s, end=", ")
'''

'''
score=[['kim',90],['lee',80],['han',85]]

sorted_score=list(sorted(score,key=lambda x:x[1],reverse=True))
print(sorted_score)
for s in enumerate(sorted_score,1):
  no,st=s
  name,avg=st
  print(no,name,round(avg,2))

'''







'''

max=100
t=[50,70,500,60]

print(any(num)> max for num in t)


'''


'''
product={'꼬북칩': 1200,'장난감':1500}
product_s={}
def register_product():
  
  product_name=input("상품명 : ")
  price=int(input("가격 : "))
  
  product[product_name]=price
  

def display_product():
  for product_list in product.items():
      name,price =product_list
      print(f'상품명 : {name} // 가격 : {price}')

def search_product():
  product_name=input('가격 조회활 상품 이름:')
  if product_name in product:
    print(f'그 상품의 가격은 ->{product[product_name]}원\n')
  else:
    print("조회상품x")

def sale_product():
  print('\n결제금액')
  product_name=input('상품명 :')
  product_num=int(input('판매수량 :'))

  if product_name in product:
    product_s[product_name]+=product_num
    print(f'결제금액은 {product[product_name]*product_num}입니다')
    
  else:
    print('상품명이 존재하지 않습니다.')

def total_product():
  print('\n매출집계\n')
  total=0
  for name,total_price in product_s.items():
    total+=product[name]*total_price
    print(f'상품명 :{name}// 금액 : {product[name]*total_price}원')

    print(f'총매출은 {total}원 입니다.')

    print('\n----전체 매출-----\n')
    






while True:
  print('1. 상품등록')
  print('2. 상품목록')
  print('3. 상품 가격 조회')
  print('4. 결재금액')
  print('5. 매출 집계')
  print('9.종료')

  choice=(input("\n번호 선택 ->"))

  if choice == '1':
    register_product()
  elif choice == '2':
    display_product()
  elif choice == '3':
    search_product()
  elif choice == '4':
    sale_product()
  elif choice == '5':
    total_product()
  elif choice == '9':
    break


print("프로그램을 종료합니다.")


'''















'''
product={'꼬북칩': 1200,'장난감':1500}

def register_product():
  
  product_name=input("상품명 : ")
  price=int(input("가격 : "))
  
  product[product_name]=price
  

def display_product():
  for product_list in product.items():
      name,price =product_list
      print(f'상품명 : {name} // 가격 : {price}')

def search_product():
  product_name=input('가격 조회활 상품 이름:')
  if product_name in product:
    print(f'그 상품의 가격은 ->{product[product_name]}원\n')
  else:
    print("조회상품x")


while True:
  print('1. 상품등록')
  print('2. 상품목록')
  print('3. 상품 가격 조회')
  print('9.종료')

  choice=(input("\n번호 선택 ->"))

  if choice == '1':
    register_product()
  elif choice == '2':
    display_product()
  elif choice == '3':
    search_product()
  elif choice == '9':
    break


print("프로그램을 종료합니다.")



'''










'''
name_list=[
('신수','추'),('광현','김'),('다익손','브록'),('스캇','루크')
]


def welcome_msg():
  for player in name_list:
    f_name, l_name=player
    print(f'{l_name}{f_name} 선수 환영합니다.')

def register_player():
  f_name=input("\n이름 입력:")
  l_name=input("성 입력:")
  print('')
  name_list.append((f_name,l_name))


welcome_msg()
register_player()
welcome_msg()
'''

'''
nums=[n*2 for n in range(1,11)]

print(nums)

nums=[]
for n in range(1,11):
  nums.append(n*2)
print(nums)
'''

'''
st_list=[
  ['kim',95.4,67.8,89.5],
   ['lee',85.4,78.8,84.5],
    ['park',76.3,73.8,68.5]
]



for person in st_list:
  avg_sum=0
  for avg_s in person[1:]:
    avg_sum=avg_sum+avg_s
  print(f'{person[0]}학생의 평균점수는{round(avg_sum/len(person[1:]),1)}')
''' 

 






 
'''
 #재귀함수

def factorial_s(num):
   if num<=1:
     return 1

   return num*factorial_s(num-1)

print(factorial_s(5))

'''














'''
#큐예제
from collections import deque

queue=deque()


queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()

queue.append(4)
queue.popleft()


print(queue)
queue.reverse()
print(queue)
'''





'''
#실습7-8장
def check_phone():
  phone_num=input("입력 \n \t 전화번호 :")
  if len(phone_num) != 13:
      return print("출력 \n \t 사용 불가능한 전화번호입니다")
  else:
      return print(f"출력 \n \t 사용가능한 전화번호입니다.({phone_num.replace('-','')})")

check_phone()

'''


'''
#스택
stack=[]

stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(1)


print(stack)
print(stack[::-1])

'''






'''

article='* 앞으로 10년 안에 꼭 이루고 싶은 버킷리스트는 무엇이며, 그것을 이루기 위해 어떤 노력을 하고 있고 향후 어떻게 준비해 나갈 계획인지 기술하시오. (1500자)'

articles=article.split()

for word in articles:
  
  w= word.strip('.\"')
  #print(w)
  print(w,article.count(w))
  

'''







'''
def check_id(myid):
  if len(myid) !=14:
    return False
  
  if myid[6] != '-':
    return False
  return True


jid=input("id : ")
if check_id(jid)==True:
    print("확인되었습니다.")
else:
    print("잘못된 주번")

'''







'''
#4-3 왕실의 나이트
input_data=input()
row=int(input_data[1])
column=int(ord(input_data[0]))-int(ord('a'))+1

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result=0
for step in steps:
  next_row=row+step[0]
  next_column=column+step[1]

  if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
    result += 1

print(result)
'''
'''

h=int(input())

count=0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        count +=1

print(count)
'''



'''
meter1=int(input('이동거리?'))

def distance(meter):
  velocity=60
  return velocity/meter


print('시간 :',round(distance(meter1),2),'h')
'''



'''
n=int(input())

x,y=1,1
plans=input().split()

dx=[0,0,-1,1]
dy=[-1,1,0,0]

move_type=['L','R','U','D']


for plan in plans:

  for i in range(len(move_type)):
    if plan == move_type[i]:
      nx = x + dx[i]
      ny = y + dy[i]

    if nx<1 or ny<1 or nx>n or ny>n:
      continue
    x,y=nx,ny

print(x,y)
'''