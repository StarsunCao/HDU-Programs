`timescale 1ns/1ns
module counter_tb;

	reg clk1;
    reg clk2;
	reg reset;
	output reg x;
	wire [31:0] result1;
    wire [31:0] result2;

	counter dut1(
		.clk(clk1),
		.reset(reset),
		.result(result1),
		.x1(x)
	);

    counter dut2(
		.clk(clk2),
		.reset(reset),
		.result(result2),
		.x1(x)
	);

	always #5  clk1 = ~clk1; // inverting of clk1
    always #10 clk2 = ~clk2; // inverting of clk2

	initial begin

		$monitor("%t : %h", $time, result1);
		$dumpfile("time.vcd");
		$dumpvars(1, counter_tb);
		
        // set initial values
		clk1 = 0;
        clk2 = 0;
		reset  = 1;
		x1=10;

		#100

		reset = 0;

		#1000

		$finish;
	end

endmodule
