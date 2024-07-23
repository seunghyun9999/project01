
def calculate_minimum_work_height(harness_length, worker_height):
    # 고정된 신장율 (30%)과 바닥과의 거리 (0.1m)를 사용하여 최소 작업 높이 계산
    harness_stretch_rate = 0.30
    distance_from_floor = 0.1
    minimum_work_height = harness_length + (harness_length * harness_stretch_rate) + (
                worker_height / 2) + distance_from_floor
    return minimum_work_height


def main():

    while True:

        try:
            worker_height = float(input("근로자의 신장 (미터 단위로 입력): "))
            harness_length = float(input("안전대 길이 (미터 단위로 입력): "))

            # 입력 값의 유효성 검사
            if worker_height <= 0 or harness_length <= 0:
                print("근로자의 신장과 안전대 길이는 양수여야 합니다.")
                continue

            # 최소 작업 높이 계산
            min_work_height = calculate_minimum_work_height(harness_length, worker_height)

            # 결과 출력
            print("안전하게 작업을 수행하기 위한 안전고리 체결 높이는 ",round(min_work_height,3)," 미터입니다.\n",round(min_work_height,3),
                  '이상의 높이에 안전고리를 체결해 주세요')

        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해 주세요.")


if __name__ == "__main__":
    main()