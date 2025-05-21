import heapq
import time
from queue import Queue

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.patients = 0 
        self.max_waiting_time = {
            'emergencia': 0,
            'muito urgente': 600,    
            'urgente': 3600,
            'pouco urgente': 7200,
            'nao urgente': 14400
        }
        self.code_priority = {
            'emergencia': 0,
            'muito urgente': 1,
            'urgente': 2,
            'pouco urgente': 3,
            'nao urgente': 4
        }

    def add_patient(self, code_patient, code_priority):
        
        priority = self.code_priority[code_priority.lower()]
        timestamp = time.time()
        heapq.heappush(self.heap, (priority, timestamp, self.patients, code_patient, code_priority))
        
        self.patients += 1

    def time_priority(self, priority, waiting_time, original_nivel):
        
        time_limit = self.max_waiting_time[original_nivel]
        if priority > 1 and waiting_time > time_limit:
            return 1
        return priority

    def patient_priority(self):
        if not self.heap:
            return None

        reassessing_patients = []
        
        now = time.time()
        
        while self.heap:
            priority, timestamp, order, code, original_nivel = heapq.heappop(self.heap)
            waiting_time = now - timestamp
            new_priority = self.time_priority(priority, waiting_time, original_nivel)
            reassessing_patients.append((new_priority, timestamp, order, code, original_nivel))

        for item in reassessing_patients:
            heapq.heappush(self.heap, item)

        _, _, _, code, _ = heapq.heappop(self.heap)
        return code
    
    def current_queue(self):
        return [{'prioridade': priority, 'código': code} for priority, _, _, code, _ in sorted(self.heap)]   
    
class ScreeningQueue:
    def __init__(self):
        self.queue = Queue()  
        
    def add_patient(self, code_patient):
        self.queue.put(code_patient)  

    def do_screening(self):
        if self.queue.empty():
            return None
        
        pacient = self.queue.get()
        return pacient #paciente em atendimento
    
    def show_queue(self):
        print("Fila atual:", list(self.queue.queue))
