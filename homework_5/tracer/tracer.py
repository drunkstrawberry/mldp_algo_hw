def tracer(func):
    depth = 0
    steps = []

    def traced(arg):
        nonlocal depth
        if depth == 0:
            steps.clear()
        steps.append('  ' * depth + 'вызов ' + str(arg))
        depth += 1
        result = func(arg)
        depth -= 1
        steps.append('  ' * depth + 'возврат ' + str(result))
        return result

    traced.steps = steps
    return traced
