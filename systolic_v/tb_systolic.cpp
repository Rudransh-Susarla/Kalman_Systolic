// tb_systolic.cpp — Verilator C++ testbench for systolic_array
//
// The Verilog module drives its own $finish after 8 clock cycles.
// This testbench just needs to toggle clk until that happens.
// A hard cap of 200 cycles prevents an infinite loop if $finish
// is never reached (e.g. file open failure).

#include "Vsystolic_array.h"
#include "verilated.h"

int main(int argc, char** argv)
{
    Verilated::commandArgs(argc, argv);

    Vsystolic_array* top = new Vsystolic_array;

    // Hard cap — the Verilog $finish will normally stop us at cycle 8
    const int MAX_CYCLES = 200;
    int cycle = 0;

    // Initial eval with clk=0 (set in Verilog initial block)
    top->eval();

    while (!Verilated::gotFinish() && cycle < MAX_CYCLES)
    {
        // Rising edge
        top->clk = 1;
        top->eval();

        // Falling edge
        top->clk = 0;
        top->eval();

        cycle++;
    }

    delete top;
    return 0;
}
