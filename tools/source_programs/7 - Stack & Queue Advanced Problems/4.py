# Stock Span Problem :

def stock_span(prices):
    n = len(prices)
    span = [0] * n
    stack = []

    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        span[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    return span

prices = [100, 80, 60, 70, 60, 75, 85]
span = stock_span(prices)
print("Stock Span:", span)


# Output :

# Stock Span: [1, 1, 1, 2, 1, 4, 6]