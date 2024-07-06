import matplotlib.pyplot as plt
import matplotlib
from typing import List

# 백엔드를 'Agg'로 설정
matplotlib.use('Agg')

class ChartService:
    def __init__(self):
        pass

    def create_gantt_chart(self, process_sequence: List[tuple], output_path: str):
        """
        간트 차트를 생성하는 함수입니다.

        매개변수:
        process_sequence: List[tuple] - 각 프로세스가 실행된 순서와 실행 시간의 튜플 리스트입니다.
        output_path: str - 생성된 간트 차트를 저장할 경로입니다.
        """
        fig, gnt = plt.subplots()

        # Y축 크기 조정
        gnt.set_ylim(0, 100)  # 충분히 큰 값으로 설정하여 공백을 추가
        gnt.set_xlim(0, sum(duration for _, duration in process_sequence))

        gnt.set_xlabel('Time')
        gnt.set_ylabel('Processes')

        current_time = 0
        process_height = 4  # 프로세스 블록 높이
        space_between = 6   # 프로세스 블록 사이의 공백
        label_dict = {}
        process_labels = []
        process_positions = []

        for process, duration in process_sequence:
            if process not in label_dict:
                label_dict[process] = len(label_dict) * (process_height + space_between)
            gnt.broken_barh([(current_time, duration)], (label_dict[process], process_height), facecolors=('black'))
            current_time += duration

        unique_labels = list(label_dict.keys())
        unique_positions = [label_dict[process] + process_height / 2 for process in unique_labels]

        gnt.set_yticks(unique_positions)
        gnt.set_yticklabels(unique_labels)
        gnt.grid(True)

        plt.tight_layout()
        plt.savefig(output_path)
