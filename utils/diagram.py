def print_systolic_diagram():
    """
    Prints a conceptual diagram of the 4×4 systolic array used
    for matrix multiplication in the Kalman filter accelerator.
    """

    print("\n" + "=" * 65)
    print("                4×4 SYSTOLIC ARRAY ARCHITECTURE")
    print("=" * 65)

    print("""
      A matrix rows stream → from LEFT
      B matrix columns stream ↓ from TOP

            B0      B1      B2      B3
             ↓       ↓       ↓       ↓
      A0 →  PE00 →  PE01 →  PE02 →  PE03
             ↓       ↓       ↓       ↓
      A1 →  PE10 →  PE11 →  PE12 →  PE13
             ↓       ↓       ↓       ↓
      A2 →  PE20 →  PE21 →  PE22 →  PE23
             ↓       ↓       ↓       ↓
      A3 →  PE30 →  PE31 →  PE32 →  PE33


      Each Processing Element (PE) performs:

            accumulator += a_in × b_in

      Data movement:
            a_in  → shifts RIGHT
            b_in  → shifts DOWN

      Final output:
            C[i][j] stored in PE[i][j]
    """)

    print("-" * 65)

    print("""
      Timing for 4×4 matrix multiplication

            Total cycles = 2n - 1 + (n - 1)

            For n = 4

            Total cycles = 10 clock cycles

      This is the fundamental idea behind
      modern AI accelerators such as TPUs.
    """)

    print("=" * 65)
