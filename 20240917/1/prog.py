n = int(input())
print(f"A {"+" if n % 50 == 0 else "-"} B {"+" if n % 2 and n % 25 == 0 else "-"} C {"+" if n % 8 == 0 else "-"}")
