`timescale 1ns/1ps

module dev_tb;

reg [31:0] x;
reg start,rst,clk;
wire rd, rdy;
wire [31:0] y;

dev uut(
    .x(x),
    .rd(rd),
    .start(start),
    .rst(rst),
    .clk(clk),
    .y(y),
    .rdy(rdy)
);

always #5 clk = ~clk; // each 5 ns we will get opposite value of clk sigr

always@(negedge clk)
    if(rd)
        x = ($random % 10) & 8'hFF;

initial begin
    $dumpfile("time.vcd");
    $dumpvars(1, dev_tb);
    clk = 0;
    rst = 1;
    start = 0;
    x = 0;
    #20
    rst = 0;
    #20
    start = 1;
    #10
    start = 0;
    #250
    $finish;
end

endmodule