import re
import json


def parse():
    try:
        with open('raw.txt', 'r', encoding='utf-8') as f:
            data = f.read()

        # RegEx Patterns 
        date = re.search(r'\d{2}\.\d{2}\.\d{4}', data)
        prices = re.findall(r'\d+[\s\.,]\d{2}', data)

        result = {
            "date": date.group() if date else "None",
            "all_prices": prices
        }
        
        print(json.dumps(result, indent=4))
        
    except FileNotFoundError:
        print("error")

if __name__ == "__main__":
    parse()



import re
import json

def main():
    # 1.
    try:
        with open('raw.txt', 'r', encoding='utf-8') as file:
            content = file.read()

        # RegEx patterns
        bin_num = re.search(r"БИН (\d+)", content).group(1) if re.search(r"БИН (\d+)", content) else "N/A"
        date_time = re.search(r"Время: ([\d\.]+ [\d:]+)", content).group(1) if re.search(r"Время: ([\d\.]+ [\d:]+)", content) else "N/A"
        total_sum = re.search(r"ИТОГО:\n([\d\s,]+)", content).group(1).strip() if re.search(r"ИТОГО:\n([\d\s,]+)", content) else "0"
        
        # Барлық тауарларды табу
        items = re.findall(r"\d+\.\n(.+)", content)
        
        receipt_json = {
            "Store": "EUROPHARMA",
            "BIN": bin_num,
            "Date_Time": date_time,
            "Items_Count": len(items),
            "Total": total_sum.replace(" ", "").replace(",", ".")
        }

        print("--- PART 1: RECEIPT DATA ---")
        print(json.dumps(receipt_json, indent=4, ensure_ascii=False))

    except FileNotFoundError:
        print("raw.txt файлы табылмады!")

    # 2. 10 REGEX EXERCISES
    print("\n--- PART 2: REGEX EXERCISES ---")
    
    # 1. 'a' followed by zero or more 'b's
    print(f"1. abbb: {bool(re.fullmatch(r'ab*', 'abbb'))}")
    # 2. 'a' followed by two to three 'b'
    print(f"2. abb: {bool(re.fullmatch(r'ab{2,3}', 'abb'))}")
    # 3. Lowercase letters with underscore
    print(f"3. hello_world: {re.findall(r'[a-z]+_[a-z]+', 'hello_world test_case')}")
    # 4. Upper followed by lower
    print(f"4. UpperLower: {re.findall(r'[A-Z][a-z]+', 'Apple Banana orange')}")
    # 5. Start 'a' end 'b'
    print(f"5. Start 'a' end 'b': {bool(re.fullmatch(r'a.*b', 'axyzb'))}")
    # 6. Replace space, comma, dot with colon
    print(f"6. Colon Replace: {re.sub(r'[ ,.]', ':', 'Hello, World.')}")
    # 7. Snake to Camel
    snake = "python_exercises"
    print(f"7. Camel: {''.join(x.capitalize() for x in snake.split('_'))}")
    # 8. Split at uppercase
    print(f"8. Split Upper: {re.findall(r'[A-Z][^A-Z]*', 'SplitThisWord')}")
    # 9. Insert spaces between capitals
    result_9 = re.sub(r'(\w)([A-Z])', r'\1 \2', 'InsertSpacesHere')
    print("9. Spaces:", result_9)

    # 10. Camel to Snake
    camel = "CamelCaseString"
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel)
    result_10 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    print("10. Snake:", result_10)

if __name__ == "__main__":
    main()