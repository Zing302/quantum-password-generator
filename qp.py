
import string
import random
import qiskit
from qiskit import QuantumCircuit
from qiskit_aer import Aer 

def generate_password(length, include_symbols=True, include_numbers=True):
    allowedchars = string.ascii_letters
    if include_numbers:
        allowedchars += string.digits
    if include_symbols:
        allowedchars += string.punctuation
    numChars=len(allowedchars)
    bitsPerChar=(numChars-1).bit_length() if numChars>1 else 1
    numQubits=bitsPerChar*length
    qc=QuantumCircuit(numQubits, numQubits)

    for q in range(numQubits):
        qc.h(q)
    qc.measure(range(numQubits), range(numQubits))
    
    backend=Aer.get_backend('aer_simulator')
    from qiskit_ibm_runtime import SamplerV2 as Sampler
    sampler=Sampler(mode=backend)
    job=sampler.run([qc], shots=1)
    result=job.result()

    counts=result[0].data.c.get_counts()
    randBits=list(counts.keys())[0]
    
    password=""
    for i in range(0,len(randBits), bitsPerChar):
        charBits=randBits[i:i+bitsPerChar]
        charIndex=int(charBits, 2)
        password+=allowedchars[charIndex % numChars]
    return password
       

    



