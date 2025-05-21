from queues import PriorityQueue
from queues import ScreeningQueue


fila_atendimento = PriorityQueue()
fila_atendimento.add_patient('paciente001', 'urgente')
fila_atendimento.add_patient('paciente002', 'nao urgente')
fila_atendimento.add_patient('paciente003', 'emergencia')

print(fila_atendimento.patient_priority()) #chama o paciente 3 pois é emergencia 
print(fila_atendimento.current_queue()) #exibe a lista sem paciente 3 pois ele foi atendido

fila_triagem = ScreeningQueue()
fila_triagem.add_patient('Paciente Exemplo1')
fila_triagem.add_patient('Paciente Exemplo2')
fila_triagem.add_patient('Paciente Exemplo3')
fila_triagem.add_patient('Paciente Exemplo4')
fila_triagem.do_screening()#chama o primeiro paciente da fila
fila_triagem.show_queue()
