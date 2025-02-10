module counter (
	input clk,
	input reset,
	output reg [3:0] result
);

always@(posedge clk)
	if(reset)
		result <= 0;
	else
		result <= result + 1;

endmodule
	
