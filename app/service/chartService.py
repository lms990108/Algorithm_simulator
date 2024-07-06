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

        gnt.set_ylim(0, 30)
        gnt.set_xlim(0, sum(duration for _, duration in process_sequence))

        gnt.set_xlabel('Time')
        gnt.set_ylabel('Processes')

        process_labels = []
        process_positions = []
        current_time = 0
        process_height = 10
        label_dict = {}

        for i, (process, duration) in enumerate(process_sequence):
            if process not in label_dict:
                label_dict[process] = len(label_dict) * process_height
            gnt.broken_barh([(current_time, duration)], (label_dict[process], process_height - 1), facecolors=('tab:blue'))
            process_labels.append(process)
            process_positions.append(label_dict[process] + process_height / 2)
            current_time += duration

        unique_labels = list(label_dict.keys())
        unique_positions = [label_dict[process] + process_height / 2 for process in unique_labels]

        gnt.set_yticks(unique_positions)
        gnt.set_yticklabels(unique_labels)
        gnt.grid(True)

        plt.savefig(output_path)
