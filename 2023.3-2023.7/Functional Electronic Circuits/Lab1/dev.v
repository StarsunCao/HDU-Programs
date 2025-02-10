module dev(
    input [31:0] x,
    input start,
    input rst,
    input clk,
    output reg rd,
    output reg [31:0] y,
    output reg rdy
);

parameter N= 10;
parameter IDLE = 0;
parameter CALC = 1;


reg state;
reg[2:0] ctr;

always@(posedge clk)
    if(rst) begin
        state <= IDLE;
        ctr <= 0;
        rdy <= 1;
        rd <= 0;
        y <= 1;
    end else begin
        case(state)
            IDLE:
                if(start) begin
                    state <= CALC;
                    rdy <= 0;
                    rd <= 1;
                end
            CALC:
                begin
	  	    ctr <= ctr + 1;
				y<=(y << x) | (y >> (32 - x));

	     if(ctr == (N-1))begin
    	          rd <= 0;
	          state <= IDLE;
	          rdy = 1;
	     end
	     end

            endcase
        end

endmodule
