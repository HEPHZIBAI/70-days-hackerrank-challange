'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/queue-using-two-stacks/problem
'''



def implement_queue(queries):
    stack_enqueue = []  # The stack for enqueue operation
    stack_dequeue = []  # The stack for dequeue operation

    for query in queries:
        query_type = query[0]
        if query_type == 1:  # Enqueue operation
            element = query[1]
            stack_enqueue.append(element)
        elif query_type == 2:  # Dequeue operation
            if not stack_dequeue:  # Transfer elements from stack_enqueue to stack_dequeue in reverse order
                while stack_enqueue:
                    stack_dequeue.append(stack_enqueue.pop())
            stack_dequeue.pop()
        elif query_type == 3:  # Print front element operation
            if not stack_dequeue:  # Transfer elements from stack_enqueue to stack_dequeue in reverse order
                while stack_enqueue:
                    stack_dequeue.append(stack_enqueue.pop())
            print(stack_dequeue[-1])

if __name__ == "__main__":
    num_queries = int(input())
    queries = []
    for _ in range(num_queries):
        query = list(map(int, input().split()))
        queries.append(query)
    implement_queue(queries)
