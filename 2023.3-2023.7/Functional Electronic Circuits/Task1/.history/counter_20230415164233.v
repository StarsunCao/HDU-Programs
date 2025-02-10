module counter (
	input clk,
	input reset,
	input x1,
	output reg [31:0] result,
	reg [31:0] a ;
);

always@(posedge clk)
	a <= x1;
	if(reset)
		result <= 1;
	else if(a) begin
		result <= result << 1;
		a<=a-1;
	end
endmodule
	
