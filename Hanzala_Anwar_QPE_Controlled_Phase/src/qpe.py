"""Reusable circuits and analysis helpers for controlled-phase QPE."""
from __future__ import annotations
import math
from collections import Counter
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import MCPhaseGate


def inverse_qft(qc: QuantumCircuit, qubits: list[int]) -> None:
    """Apply an inverse QFT with final swaps to qubits in little-endian order."""
    n = len(qubits)
    for i in range(n // 2):
        qc.swap(qubits[i], qubits[n - i - 1])
    for j in reversed(range(n)):
        for k in reversed(range(j + 1, n)):
            qc.cp(-math.pi / (2 ** (k - j)), qubits[k], qubits[j])
        qc.h(qubits[j])


def build_qpe_controlled_phase(phi: float, precision: int = 4, measure: bool = True) -> QuantumCircuit:
    """Estimate theta=phi/(2*pi) for U=CP(phi) and eigenstate |11>."""
    if precision < 1:
        raise ValueError("precision must be positive")
    count = QuantumRegister(precision, "count")
    target = QuantumRegister(2, "target")
    classical = ClassicalRegister(precision, "phase")
    qc = QuantumCircuit(count, target, classical if measure else None)

    qc.x(target[0]); qc.x(target[1])  # eigenstate |11>
    qc.h(count)
    for j in range(precision):
        gate = MCPhaseGate(phi * (2 ** j), num_ctrl_qubits=2)
        qc.append(gate, [count[j], target[0], target[1]])
    inverse_qft(qc, list(count))
    if measure:
        qc.measure(count, classical)
    return qc


def decode_counts(counts: dict[str, int], precision: int) -> tuple[float, str, float]:
    """Return mode estimate, modal bit string, and modal probability."""
    bitstring, shots = max(counts.items(), key=lambda item: item[1])
    theta = int(bitstring, 2) / (2 ** precision)
    probability = shots / sum(counts.values())
    return theta, bitstring, probability


def circular_error(theta_est: float, theta_true: float) -> float:
    d = abs(theta_est - theta_true)
    return min(d, 1.0 - d)
