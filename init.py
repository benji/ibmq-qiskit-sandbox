import qiskit
from qiskit import  IBMQ

with open('token.txt', 'r') as file:
    token = file.read().replace('\n', '')

IBMQ.save_account(token)