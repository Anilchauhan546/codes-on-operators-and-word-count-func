# codes-on-expression-and-word-count-func

def calculate(expression):
    def operate(a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b

    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def apply_ops(values, ops):
        b = values.pop()
        a = values.pop()
        op = ops.pop()
        values.append(operate(a, b, op))

    values = []
    ops = []
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        elif expression[i].isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = val * 10 + int(expression[i])
                i += 1
            values.append(val)
            continue
        elif expression[i] == '(':
            ops.append(expression[i])
        elif expression[i] == ')':
            while ops and ops[-1] != '(':
                apply_ops(values, ops)
            ops.pop()  # remove '('
        else:  # operator
            while ops and precedence(ops[-1]) >= precedence(expression[i]):
                apply_ops(values, ops)
            ops.append(expression[i])
        i += 1

    while ops:
        apply_ops(values, ops)

    return values[0]

****************************************************************************************************************************************************************

# Word Count function

def word_count(sentence, N=3):

    sentence = sentence.lower()
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for p in punctuation:
        sentence = sentence.replace(p, "")
    words = sentence.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:N]






