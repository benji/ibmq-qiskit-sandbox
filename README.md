# qiskit-sandbox

Setup: create token.txt containing IBMQ token, run init.ipynb

#### 1_meet_hadamard
```
q_0: |0>┤ H ├──■──┤M├───
        └───┘┌─┴─┐└╥┘┌─┐
q_1: |0>─────┤ X ├─╫─┤M├
             └───┘ ║ └╥┘
 c_0: 0 ═══════════╩══╬═
                      ║ 
 c_1: 0 ══════════════╩═
 ```

After the Hadamard gate, q_0 has 50/50 chances to collapse to 0 or 1.  
In the case of q_0 collapsing to 0, q_1 won't be changed => we get |00>  
In the case of q_0 collapsing to 1, q_1 will be flipped => we get |11>

#### 2_qubit_teleportation

Since we can't read a qubit without collapsing its quantum state, how to copy the quantum information from one qubit to another?

```
q_0: |0>┤ X ├─░─────────────■──┤ H ├─░─┤M├─────────■────
        └───┘ ░ ┌───┐     ┌─┴─┐└───┘ ░ └╥┘┌─┐      │    
q_1: |0>──────░─┤ H ├──■──┤ X ├──────░──╫─┤M├──■───┼────
              ░ └───┘┌─┴─┐└───┘      ░  ║ └╥┘┌─┴─┐ │ ┌─┐
q_2: |0>──────░──────┤ X ├───────────░──╫──╫─┤ X ├─■─┤M├
              ░      └───┘           ░  ║  ║ └───┘   └╥┘
 c_0: 0 ════════════════════════════════╩══╬══════════╬═
                                           ║          ║ 
 c_1: 0 ═══════════════════════════════════╩══════════╬═
                                                      ║ 
 c_2: 0 ══════════════════════════════════════════════╩═
 ```

When q_0 is NOT flipped (=0), then q_2 (measured at c_2) is always 0:
Total count for 00 and 11 are: {'010': 253, '000': 243, '001': 243, '011': 261}
(First bit is c_2)

When q_0 is flipped (=1), then q_2 is always 1:
Total count for 00 and 11 are: {'100': 269, '111': 246, '110': 242, '101': 243}

**The value of q_0 has been reflected to q_2.**


#### Docs

Available Gates:
https://quantum-computing.ibm.com/support/guides/gate-overview?section=5d00d964853ef8003c6d6820