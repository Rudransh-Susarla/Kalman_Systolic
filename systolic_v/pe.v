module pe(
    input clk,
    input reset,

    input real a_in,
    input real b_in,

    output real a_out,
    output real b_out,

    output real acc
);

real accumulator;

assign a_out = a_in;
assign b_out = b_in;
assign acc   = accumulator;

always @(posedge clk) begin
    if(reset)
        accumulator <= 0.0;
    else
        accumulator <= accumulator + (a_in * b_in);
end

endmodule
