import pandas as pd

# Define global variables to store user inputs and results
data = {
    'Choice': [],
    'User_Input': [],
    'Result': []
}

def parse_length(value):
    if value <= 10:
        return value  # meters
    else:
        return value / 100  # convert cm to meters

def get_elongation_rate(rope_type):
    rope_types = {
        "나일론": 0.30,
        "폴리에스터": 0.15,
        "케블라": 0.02,
        "다이니마": 0.02
    }
    return rope_types.get(rope_type, None)

def calculate_minimum_height(safety_belt_length, elongation_rate, worker_height):
    minimum_height = safety_belt_length + (safety_belt_length * elongation_rate) + (worker_height / 2)
    return minimum_height + 0.5

def calculate_max_safety_belt_length(worker_height, required_height, elongation_rate):
    adjusted_height = required_height - 0.5
    max_length = (adjusted_height - (worker_height / 2)) / (1 + elongation_rate)
    return max_length

def find_suitable_ropes(worker_height, safety_belt_length, required_height):
    suitable_ropes = []
    rope_types = {
        "나일론": 0.30,
        "폴리에스터": 0.15,
        "케블라": 0.02,
        "다이니마": 0.02
    }
    for rope_type, elongation_rate in rope_types.items():
        minimum_height = calculate_minimum_height(safety_belt_length, elongation_rate, worker_height)
        if minimum_height <= required_height:
            suitable_ropes.append(rope_type)
    return suitable_ropes

def main():
    global data

    while True:
        print("안전대 관련 계산을 선택하세요:")
        print("1. 안전대 체결 최소 높이 계산")
        print("2. 안전대 로프 종류 적합성 확인")
        print("3. 안전대의 최대 길이 계산")
        choice = input("선택 (1/2/3): ").strip()

        if choice == "1":
            try:
                worker_height = float(input("근로자 신장 : "))
                worker_height = parse_length(worker_height)
                safety_belt_length = float(input("안전대 길이 : "))
                safety_belt_length = parse_length(safety_belt_length)
                rope_type = input("안전대 종류를 입력하세요 (나일론, 폴리에스터, 케블라, 다이니마): ").strip()
                elongation_rate = get_elongation_rate(rope_type)
                if elongation_rate is None:
                    elongation_rate = float(input(f"{rope_type} 로프의 신장율 (%)을 입력하세요: ")) / 100

                minimum_height = calculate_minimum_height(safety_belt_length, elongation_rate, worker_height)
                print(f"안전대 체결 최소 높이: {minimum_height:.2f} m")

                # Store data
                data['Choice'].append("안전대 체결 최소 높이 계산")
                data['User_Input'].append(f"근로자 신장: {worker_height:.2f} m, 안전대 길이: {safety_belt_length:.2f} m, 안전대 종류: {rope_type}")
                data['Result'].append(f"안전대 체결 최소 높이: {minimum_height:.2f} m")

            except ValueError:
                print("유효한 숫자를 입력하세요.")

        elif choice == "2":
            try:
                worker_height = float(input("근로자 신장: "))
                worker_height = parse_length(worker_height)
                safety_belt_length = float(input("안전대 길이 : "))
                safety_belt_length = parse_length(safety_belt_length)
                required_height = float(input("안전대 체결 높이 : "))
                required_height = parse_length(required_height)

                suitable_ropes = find_suitable_ropes(worker_height, safety_belt_length, required_height)
                if suitable_ropes:
                    print("적합한 안전대 로프 종류:")
                    for rope in suitable_ropes:
                        print(f"- {rope}")
                    result_str = ", ".join(suitable_ropes)
                    data['Result'].append(f"적합한 안전대 로프 종류: {result_str}")

                else:
                    print("적합한 안전대 로프 종류가 없습니다.\n안전대 길이를 축소 시키거나, 안전대 체결높이를 상승시키세요")
                    data['Result'].append("적합한 안전대 로프 종류가 없습니다.")

                # Store data
                data['Choice'].append("안전대 로프 종류 적합성 확인")
                data['User_Input'].append(f"근로자 신장: {worker_height:.2f} m, 안전대 길이: {safety_belt_length:.2f} m, 안전대 체결 높이: {required_height:.2f} m")

            except ValueError:
                print("유효한 숫자를 입력하세요.")

        elif choice == "3":
            try:
                worker_height = float(input("근로자 신장 : "))
                worker_height = parse_length(worker_height)
                required_height = float(input("안전대 체결 높이 : "))
                required_height = parse_length(required_height)
                rope_type = input("안전대 종류를 입력하세요 (나일론, 폴리에스터, 케블라, 다이니마): ").strip()
                elongation_rate = get_elongation_rate(rope_type)
                if elongation_rate is None:
                    elongation_rate = float(input(f"{rope_type} 로프의 신장율 (%)을 입력하세요: ")) / 100

                max_safety_belt_length = calculate_max_safety_belt_length(worker_height, required_height, elongation_rate)
                print(f"안전대의 최대 길이: {max_safety_belt_length:.2f} m")

                # Store data
                data['Choice'].append("안전대의 최대 길이 계산")
                data['User_Input'].append(f"근로자 신장: {worker_height:.2f} m, 안전대 체결 높이: {required_height:.2f} m, 안전대 종류: {rope_type}")
                data['Result'].append(f"안전대의 최대 길이: {max_safety_belt_length:.2f} m")

            except ValueError:
                print("유효한 숫자를 입력하세요.")

        else:
            print("유효하지 않은 선택입니다. 1, 2, 3 중에서 선택하세요.")

        # Ask if the user wants to continue or exit
        while True:
            another_calculation = input("더 계산하시겠습니까? (yes/no): ").strip().lower()
            if another_calculation in ["yes", "no"]:
                break
            else:
                print("잘못된 입력입니다. 'yes' 또는 'no'로 다시 입력해주세요.")

        if another_calculation != "yes":
            break

    # Convert data dictionary to DataFrame
    df = pd.DataFrame(data)

    # Write DataFrame to Excel
    excel_file = 'safety_belt_calculations.xlsx'
    df.to_excel(excel_file, index=False)
    print(f"계산 결과가 {excel_file} 파일에 저장되었습니다.")

if __name__ == "__main__":
    main()
