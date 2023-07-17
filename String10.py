def main(x,y):
    a=(x+y)*2
    b=f'({x}+{y})*2={a}'
    """
    Given three integers, x, y, return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    return b
print(main(3,7))