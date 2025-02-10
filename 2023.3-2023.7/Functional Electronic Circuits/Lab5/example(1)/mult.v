module mult (
    input clk_i,
    input rst_i, // _i means input

    input start_i,

    input [7:0] a_bi, // _bi - input bus. Bus consists several digital lines
    input [7:0] b_bi,

    output reg [15:0] y_bo, // _bo means output bus
    output reg busy_o // _o - means output
);


localparam IDLE = 2'b00;
localparam WORK = 2'b01;
localparam END  = 2'b10;

reg [1:0] state;
reg [7:0] a, b;
reg [2:0] ctr;
reg [15:0] part_res;
wire [7:0] part_sum;
wire [15:0] shifted_part_sum;

assign part_sum = a & {8{b[ctr]}}; // we take b[ctr] bit and scale it to the 8 bit
    //example: if b[ctr] = 0 -> {8{b[ctr]}} = 00000000
    // if b[ctr] = 1 -> {8{b[ctr]}} = 11111111 

assign shifted_part_sum = part_sum << ctr;

always@(posedge clk_i)
    if(rst_i) begin
        // reset logic
        ctr <= 0;
        busy_o <= 0;
        part_res <= 0;
        state <= IDLE;
    end else begin
        case(state)
            IDLE:
                begin
                    if(start_i) begin
                        state <= WORK;
                        a <= a_bi;
                        b <= b_bi;
                        ctr <= 0;
                        part_res <= 0;
                        busy_o <= 1;
                    end
                end
            WORK: 
                begin
                    if(ctr == 3'h7) begin
                        state <= END;
                    end

                    part_res <= part_res + shifted_part_sum;
                    ctr <= ctr + 1;
                end
            END:
                begin
                    y_bo <= part_res;
                    busy_o <= 0;
                    state <= IDLE;
                end
            default: state <= IDLE;
        endcase
    end

endmodule
