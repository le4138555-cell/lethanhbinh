def solve_linear_equation(a: float, b: float) -> str:
    if a == 0:
        if b == 0:
            return "Phương trình có vô số nghiệm"
        return "Phương trình vô nghiệm"

    return f"Phương trình có nghiệm x = {-b / a}"


if __name__ == "__main__":
    try:
        a = float(input("Nhập hệ số a: "))
        b = float(input("Nhập hệ số b: "))
        print(solve_linear_equation(a, b))
    except ValueError:
        print("Vui lòng nhập số hợp lệ")
