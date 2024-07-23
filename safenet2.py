
    def calculate_fall_distance(height, harness_length, harness_stretch_rate, worker_height):
        # (로프길이 + (로프길이 × 신장률) + 신장길이의 절반) 계산
        fall_distance = harness_length + (harness_length * harness_stretch_rate) + (worker_height / 2)
        return fall_distance


    def main():
        # 입력 받기
        try:
            worker_height = float(input("근로자의 신장 (미터 단위로 입력): "))
            harness_length = float(input("안전대 길이 (미터 단위로 입력): "))
            harness_stretch_rate = float(input("안전대 신장율 (0과 1 사이의 값): "))
            work_height = float(input("작업 높이 (미터 단위로 입력): "))

            # 입력 값의 유효성 검사
            if not (0 <= harness_stretch_rate <= 1):
                print("안전대 신장율은 0과 1 사이의 값이어야 합니다.")
                return

            if worker_height <= 0 or harness_length <= 0 or work_height <= 0:
                print("근로자의 신장, 안전대 길이, 작업 높이는 양수여야 합니다.")
                return

            # 추락 거리 계산
            fall_distance = calculate_fall_distance(worker_height, harness_length, harness_stretch_rate, worker_height)

            # 바닥과의 차이 계산
            distance_from_floor = work_height - fall_distance

            # 결과 출력
            if distance_from_floor < 0:
                print("주의: 추락 시 바닥과의 거리보다 더 낮은 지점에 위치할 수 있습니다!\n"
                      "안전대의 높이를 ",int(distance_from_floor*(-1))+1,'이상 높이 거세요')

            else:
                print(f"추락 시 바닥과의 거리는 {distance_from_floor:.2f} 미터입니다.")

        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해 주세요.")


    if __name__ == "__main__":
        main()
