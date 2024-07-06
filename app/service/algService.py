from typing import List, Dict, Optional

class AlgService:
    def __init__(self):
        pass  # 초기화 로직이 필요한 경우 여기에 작성

    def round_robin(self, nodes: List[str], burst_times: List[int], time_slice: int, arrival_times: Optional[List[int]] = None) -> Dict:
        """
        라운드 로빈 스케줄링 알고리즘을 구현한 함수입니다.

        매개변수:
        nodes: List[str] - 프로세스의 이름 또는 ID 리스트입니다.
        burst_times: List[int] - 각 프로세스의 실행 시간(버스트 타임) 리스트입니다.
        time_slice: int - 각 프로세스가 한 번에 실행될 수 있는 최대 시간(타임 슬라이스)입니다.
        arrival_times: Optional[List[int]] - 각 프로세스의 도착 시간 리스트입니다. 생략 시 모든 프로세스가 0 시간에 도착한 것으로 간주합니다.

        반환값:
        Dict - 다음을 포함하는 결과 딕셔너리입니다:
            'process_sequence': List[tuple] - 각 프로세스가 실행된 순서와 실행 시간의 튜플 리스트입니다.
            'waiting_times': List[int] - 각 프로세스의 대기 시간 리스트입니다.
            'turnaround_times': List[int] - 각 프로세스의 반환 시간(턴어라운드 타임) 리스트입니다.
            'average_waiting_time': float - 평균 대기 시간입니다.
            'average_turnaround_time': float - 평균 반환 시간입니다.
        """
        if arrival_times is None:
            arrival_times = [0] * len(nodes)
        
        n = len(nodes)
        remaining_burst_times = burst_times[:]
        waiting_time = [0] * n
        turnaround_time = [0] * n
        time = 0
        complete = 0
        process_sequence = []

        while complete != n:
            for i in range(n):
                if arrival_times[i] <= time and remaining_burst_times[i] > 0:
                    if remaining_burst_times[i] > time_slice:
                        time += time_slice
                        remaining_burst_times[i] -= time_slice
                        process_sequence.append((nodes[i], time_slice))
                    else:
                        time += remaining_burst_times[i]
                        waiting_time[i] = time - burst_times[i] - arrival_times[i]
                        turnaround_time[i] = time - arrival_times[i]
                        process_sequence.append((nodes[i], remaining_burst_times[i]))
                        remaining_burst_times[i] = 0
                        complete += 1

        avg_waiting_time = sum(waiting_time) / n
        avg_turnaround_time = sum(turnaround_time) / n

        return {
            'process_sequence': process_sequence,
            'waiting_times': waiting_time,
            'turnaround_times': turnaround_time,
            'average_waiting_time': avg_waiting_time,
            'average_turnaround_time': avg_turnaround_time
        }
