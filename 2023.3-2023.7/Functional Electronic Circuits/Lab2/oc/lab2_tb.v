`timescale 1ns/1ps

module lab2_tb;

reg [31:0] x;
reg rst, clk;
wire [31:0] y_oc;

lab2_oc uut_oc(
    .clk(clk),
    .rst(rst),
    .x(x),
    .y(y_oc)
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

    #20
    rst = 0;
    
    #100
    $finish;

end
endmodule