module counter (
	input clk,
	input reset,
	input x1,
	output reg [31:0] result,
	reg [31:0] x 
);

always@(posedge clk)
	x <= x1;
	if(reset)
		result <= 1;
	else if(x) begin
		result <= result << 1;
		x<=x-1;
	end
endmodule
	
