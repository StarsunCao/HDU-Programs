`include "dev.v"
`timescale 1ns/1ps

module dev_tb;


reg [31:0] a,b;
reg clk, rst;
reg start;

wire rdy;
wire [31:0] y;

dev uut(
    .clk_i(clk),
    .rst_i(rst),
    
    .x_bi(a),
    .y_bi(b),
    .start_i(start),

    .y_bo(y),
    .rdy_o(rdy)
);

always #5 clk = ~clk;

initial begin
    
    $dumpfile("time.vcd");
    $dumpvars(0, dev_tb);

    clk   = 0;
    rst   = 1;
    a     = 2;
    b     = 8;
    start = 0;

    #20
    rst   = 0;
    start = 1;
    #20
    start = 0;

    @(posedge rdy);
    #1000
    $finish;
        
end



endmodule
