from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from ..service.algService import AlgService

algRouter = APIRouter()
alg_service = AlgService()

class RoundRobinRequest(BaseModel):
    nodes: List[str]
    burst_times: List[int]
    time_slice: int
    arrival_times: Optional[List[int]] = None

class RoundRobinResponse(BaseModel):
    process_sequence: List[tuple]
    waiting_times: List[int]
    turnaround_times: List[int]
    average_waiting_time: float
    average_turnaround_time: float

@algRouter.post("/round_robin", response_model=RoundRobinResponse)
def handle_round_robin(request: RoundRobinRequest):
    if len(request.nodes) != len(request.burst_times):
        raise HTTPException(status_code=400, detail="The number of nodes and burst_times must be equal.")
    
    if request.arrival_times and len(request.nodes) != len(request.arrival_times):
        raise HTTPException(status_code=400, detail="The number of nodes and arrival_times must be equal if arrival_times are provided.")
    
    result = alg_service.round_robin(
        nodes=request.nodes,
        burst_times=request.burst_times,
        time_slice=request.time_slice,
        arrival_times=request.arrival_times
    )
    
    return RoundRobinResponse(**result)
