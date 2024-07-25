while True:
    def parse_length(value):
        # 입력값의 크기에 따라 m 또는 cm를 자동으로 판별하여 미터 단위로 변환합니다.
        """""
        사용자 편의성 향상을 위해 cm와 m의 자동변환을 적용
        근로자의 신장, 안전대의 길이 모두 단위가 m로서 1의 자리 또는 cm로서 10이상의 수가 나오게 되는데 이를 활용
        """""
        if value <= 10:
            return value  # 미터 단위
        else:
            return value / 100  # cm를 m로 변환

    def get_elongation_rate(rope_type):
        # 안전대 종류에 따른 신장율 반환
        """
        딕셔너리 사용
        """
        rope_types = {
            "나일론": 0.30,
            "폴리에스터": 0.15,
            "케블라": 0.02,
            "다이니마": 0.02
        }
        return rope_types.get(rope_type, None)

    def calculate_minimum_height(safety_belt_length, elongation_rate, worker_height):
        # 최소 높이 계산 (안전대가 체결된 후 이격 거리 0.5미터 추가)
        minimum_height = safety_belt_length + (safety_belt_length * elongation_rate) + (worker_height / 2)
        # 최소 높이 = 안전대 길이+(안전대 길이*신장율)+근로자 신장/2
        return minimum_height + 0.5  # 이격 거리 추가


    def calculate_max_safety_belt_length(worker_height, required_height, elongation_rate):
        # 최대 안전대 길이 계산 (이격 거리 0.5미터 고려)
        adjusted_height = required_height - 0.5
        # 채결 높이 에서 0.5미터 빼기
        max_length = (adjusted_height - (worker_height / 2)) / (1 + elongation_rate)
        # 안전대 최대길이 = (체결 길이 - 신장/2)/신장율
        return max_length

    def find_suitable_ropes(worker_height, safety_belt_length, required_height):
        # 안전대 종류 찾아주는 함수(근로자 신장, 안전대 길이, 작업 높이)
        """
        리스트 사용
        """
        suitable_ropes = []
        rope_types = {
            "나일론": 0.30,
            "폴리에스터": 0.15,
            "케블라": 0.02,
            "다이니마": 0.02
        }
        # 입력값을 계산하고 안전대 신장율을 적용한 안전대 체결 높이가 0.5m보다 높은지 확인해서 높은 안전대 종류를 리스트에 보관한 후
        # 적합하다고 보내주는 함수
        """
        반복문 사용
        """
        for rope_type, elongation_rate in rope_types.items():
            minimum_height = calculate_minimum_height(safety_belt_length, elongation_rate, worker_height)
            # 최소 체결 높이 <= 실제 체결 높이
            # 조건에 맞는 안전대를 리스트에 추가해라
            """
            append 사용
            """
            if minimum_height <= required_height:
                suitable_ropes.append(rope_type)

        return suitable_ropes

    def main():
        print("안전대 관련 계산을 선택하세요:")
        print("1. 안전대 체결 최소 높이 계산")
        print("2. 안전대 로프 종류 적합성 확인")
        print("3. 안전대의 최대 길이 계산")
        """
        strip 양옆에 공백을 없애줌 사용자의 오류를 해결 및 편의성 향상
        """
        choice = input("선택 (1/2/3): ").strip()

        if choice == "1":
            """
            try를 사용해서 사용자가 잘못 적었을시 오류 해결
            """
            # float 수를 부동 소수점으로 변환하는 함수
            try:
                worker_height = float(input("근로자 신장 : "))
                worker_height = parse_length(worker_height)
                safety_belt_length = float(input("안전대 길이 : "))
                safety_belt_length = parse_length(safety_belt_length)
                rope_type = input("안전대 종류를 입력하세요 (나일론, 폴리에스터, 케블라, 다이니마): ").strip()
                # elongation rate 신장율임
                elongation_rate = get_elongation_rate(rope_type)
                if elongation_rate is None:
                    elongation_rate = float(input(f"{rope_type} 로프의 신장율 (%)을 입력하세요: ")) / 100

                minimum_height = calculate_minimum_height(safety_belt_length, elongation_rate, worker_height)
                print(f"안전대 체결 최소 높이: {minimum_height:.2f} m")
            # float 함수를 활용해서 valueError가 나옴
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
                else:
                    print("적합한 안전대 로프 종류가 없습니다."
                          "\n안전대 길이를 축소 시키거나, 안전대 체결높이를 상승시키세요")

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
                """
                안전대의 종류를 입력했을때 미리 입력해두지 않은 안전대라도 
                사용자가 직접 신장율을 적어서 계산을 마저 진행할 수 있도록 진행
                """
                if elongation_rate is None:
                    elongation_rate = float(input(f"{rope_type} 로프의 신장율 (%)을 입력하세요: ")) / 100

                max_safety_belt_length = calculate_max_safety_belt_length(worker_height, required_height, elongation_rate)
                print(f"안전대의 최대 길이: {max_safety_belt_length:.2f} m")

            except ValueError:
                print("유효한 숫자를 입력하세요.")

        else:
            print("유효하지 않은 선택입니다. 1, 2, 3 중에서 선택하세요.")

    if __name__ == "__main__":
        main()
        print('-'*50)