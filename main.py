from utils import evaluate_expression
from datetime import datetime
HISTORY_FILE="history.txt"

def log_to_file(expression,result):
    with open(HISTORY_FILE,"a") as f:
        timestamp=datetime.now().strftime("%Y-%m-%d   %H:%M:%S")
        f.write(f"[{timestamp}]\t{expression} = {result}\n")
def main():
    print("="*10+"🔢 Scientific Calculator CLI"+"="*10)
    print("Type your expression (e.g., sqrt(25) + abs(-5))")
    print("Type 'EXIT' to quit.\n")

    while(True):
        expr=input("Enter expression: ").strip()
        if expr.lower()=="exit":
            print("Exiting......")
            break
        result=evaluate_expression(expr)
        print("Calculating.......")
        print(f"✅ Result: {result}")
        print("_"*50)
        log_to_file(expr,result)
if __name__=="__main__":
         main()