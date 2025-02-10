`timescale 1ns/1ps

module lab2_tb;

reg [31:0] x;
reg rst, clk, start;
wire [31:0] y_oc, y_mc, y_pipe;
wire rdy_mc, rdy_pipe;

lab2_oc uut_oc(
    .clk(clk),
    .rst(rst),
    .x(x),
    .y(y_oc)
);

lab2_mc uut_mc(
    .clk(clk),
    .rst(rst),
    .start(start),
    .x(x),
    .rdy(rdy_mc),
    .y(y_mc)
);

lab2_pipe uut_pipe(
    .clk(clk),
    .rst(rst),
    .start(start),
    .x(x),
    .rdy(rdy_pipe),
    .y(y_pipe)
);

always #5 clk = ~clk;

always@(negedge clk) begin
    x = ($random % 256) & 8'hFF;
end

initial begin

    $dumpfile("time.vcd");
    $dumpvars(1, lab2_tb);

    clk = 0;
    rst = 1;
    x = 0;
    start = 0;

    #20
    rst = 0;
    start = 1;

    #10
    start = 0;

    #100
    start = 1;

    #10
    start = 0;

    #100
    $finish;

end
endmodule