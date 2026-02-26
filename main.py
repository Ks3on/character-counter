import sys

def count_clean_chars(text):
    """
    Counts characters in the text excluding spaces, punctuation, and numbers.
    Counts only alphabetic characters (letters).
    """
    # Count only characters that are letters (a-z, A-Z, and equivalents in other alphabets)
    count = sum(1 for char in text if char.isalpha())
    return count

def main():
    print("Программа для подсчета символов (только буквы, без цифр, пробелов и знаков препинания).")
    print("Вставьте ваш текст ниже.")
    print("Когда закончите, нажмите Enter, затем Ctrl+Z (на Windows) и снова Enter, чтобы получить результат.")
    print("-" * 50)
    
    try:
        # Read all input until EOF (Ctrl+D on Unix, Ctrl+Z on Windows)
        user_input = sys.stdin.read()
            
        result = count_clean_chars(user_input)
        
        print("\n" + "-" * 50)
        print(f"Количество букв: {result}")
        
    except KeyboardInterrupt:
        print("\nПрограмма остановлена.")
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")

if __name__ == "__main__":
    main()
