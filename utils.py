import math
def evaluate_expression(expr):
    allowed_names={
        "sqrt":math.sqrt,
        "pow":math.pow,
        "sin":math.sin,
        "cos":math.cos,
        "tan":math.tan,
        "log":math.log,
        "log10":math.log10,
        "pi":math.pi,
        "e":math.e,
        "abs":abs,
        "round":round,
        "factorial":math.factorial,
        "degrees":math.degrees,
        "radians":math.radians,
        "floor":math.floor,
        "ceil":math.ceil,
        "__builtins__":None
    }

    try:
        result=eval(expr,{"__builtins__":None},allowed_names)
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except ValueError as ve:
        return f"Math Error: {ve}"
    except Exception as e:
        return f"Error: {e}"