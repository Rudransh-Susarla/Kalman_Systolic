// systolic_array.v — Verilator-compatible 4x4 systolic matrix multiply
//
// Operates directly on 64-bit doubles (Verilog 'real').
// No fixed-point encoding needed — Python writes floats, Verilog reads
// floats, Python reads floats back. No scaling, no precision loss.
//
// FIX: $fwrite uses %.17g (17 significant digits = full float64 precision)
//      so Python float() recovers the exact IEEE-754 value.

module systolic_array;

integer file;
integer outfile;
integer i, j;

reg clk;
reg reset;

integer cycle_count;
integer sim_done;

real A [0:3][0:3];
real B [0:3][0:3];

// Stagger pipeline registers for A column-0 inputs (diagonal wavefront)
real A1_d1;
real A2_d1, A2_d2;
real A3_d1, A3_d2, A3_d3;

always @(posedge clk) begin
    A1_d1 <= A[1][0];
    A2_d1 <= A[2][0];  A2_d2 <= A2_d1;
    A3_d1 <= A[3][0];  A3_d2 <= A3_d1;  A3_d3 <= A3_d2;
end

// Horizontal pass-through wires
real a00, a01, a02;
real a10, a11, a12;
real a20, a21, a22;
real a30, a31, a32;

// Vertical pass-through wires
real b00, b10, b20;
real b01, b11, b21;
real b02, b12, b22;
real b03, b13, b23;

// Accumulator outputs
real C00, C01, C02, C03;
real C10, C11, C12, C13;
real C20, C21, C22, C23;
real C30, C31, C32, C33;

// Row 0 — A fed directly
pe PE00(.clk(clk),.reset(reset),.a_in(A[0][0]),.b_in(B[0][0]),.a_out(a00),.b_out(b00),.acc(C00));
pe PE01(.clk(clk),.reset(reset),.a_in(a00),    .b_in(B[0][1]),.a_out(a01),.b_out(b01),.acc(C01));
pe PE02(.clk(clk),.reset(reset),.a_in(a01),    .b_in(B[0][2]),.a_out(a02),.b_out(b02),.acc(C02));
pe PE03(.clk(clk),.reset(reset),.a_in(a02),    .b_in(B[0][3]),.a_out(),   .b_out(b03),.acc(C03));

// Row 1 — A delayed 1 cycle
pe PE10(.clk(clk),.reset(reset),.a_in(A1_d1),.b_in(b00),.a_out(a10),.b_out(b10),.acc(C10));
pe PE11(.clk(clk),.reset(reset),.a_in(a10),  .b_in(b01),.a_out(a11),.b_out(b11),.acc(C11));
pe PE12(.clk(clk),.reset(reset),.a_in(a11),  .b_in(b02),.a_out(a12),.b_out(b12),.acc(C12));
pe PE13(.clk(clk),.reset(reset),.a_in(a12),  .b_in(b03),.a_out(),   .b_out(b13),.acc(C13));

// Row 2 — A delayed 2 cycles
pe PE20(.clk(clk),.reset(reset),.a_in(A2_d2),.b_in(b10),.a_out(a20),.b_out(b20),.acc(C20));
pe PE21(.clk(clk),.reset(reset),.a_in(a20),  .b_in(b11),.a_out(a21),.b_out(b21),.acc(C21));
pe PE22(.clk(clk),.reset(reset),.a_in(a21),  .b_in(b12),.a_out(a22),.b_out(b22),.acc(C22));
pe PE23(.clk(clk),.reset(reset),.a_in(a22),  .b_in(b13),.a_out(),   .b_out(b23),.acc(C23));

// Row 3 — A delayed 3 cycles; bottom row b_out goes nowhere
pe PE30(.clk(clk),.reset(reset),.a_in(A3_d3),.b_in(b20),.a_out(a30),.b_out(),.acc(C30));
pe PE31(.clk(clk),.reset(reset),.a_in(a30),  .b_in(b21),.a_out(a31),.b_out(),.acc(C31));
pe PE32(.clk(clk),.reset(reset),.a_in(a31),  .b_in(b22),.a_out(a32),.b_out(),.acc(C32));
pe PE33(.clk(clk),.reset(reset),.a_in(a32),  .b_in(b23),.a_out(),   .b_out(),.acc(C33));

initial begin
    clk         = 0;
    reset       = 1;
    cycle_count = 0;
    sim_done    = 0;

    file = $fopen("input.txt", "r");
    if (file == 0) begin
        $display("ERROR: cannot open input.txt");
        $finish;
    end

    for (i = 0; i < 4; i = i + 1)
        for (j = 0; j < 4; j = j + 1)
            $fscanf(file, "%lf", A[i][j]);

    for (i = 0; i < 4; i = i + 1)
        for (j = 0; j < 4; j = j + 1)
            $fscanf(file, "%lf", B[i][j]);

    $fclose(file);
end

always @(posedge clk) begin
    cycle_count <= cycle_count + 1;

    if (cycle_count == 1)
        reset <= 0;

    if (cycle_count == 8 && sim_done == 0) begin
        sim_done <= 1;

        outfile = $fopen("output.txt", "w");
        // %.17g = 17 significant digits — exact round-trip for float64
        $fwrite(outfile, "%.17g %.17g %.17g %.17g\n", C00, C01, C02, C03);
        $fwrite(outfile, "%.17g %.17g %.17g %.17g\n", C10, C11, C12, C13);
        $fwrite(outfile, "%.17g %.17g %.17g %.17g\n", C20, C21, C22, C23);
        $fwrite(outfile, "%.17g %.17g %.17g %.17g\n", C30, C31, C32, C33);
        $fclose(outfile);

        $finish;
    end
end

endmodule
