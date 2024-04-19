def box_printer(*words):
    max_length = max(len(word) for word in words)
    print("*" * (max_length+2))
    for word in words:
        print(f"*{word}{" "*(max_length-len(word))}*")
    print("*" * (max_length + 2))
def main():
    box_printer("Hello", "this", "is", "my", "test","file")
if __name__ == "__main__":
    main()