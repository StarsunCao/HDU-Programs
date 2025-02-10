`include "adder.v"
`include "mult.v"
module dev (
    input clk_i,
    input rst_i,
    
    input [31:0] x_bi,
    input [31:0] y_bi,
    input start_i,
    
    output reg [31:0] y_bo,
    output reg rdy_o
);

reg signed [31:0] a1_op1, a1_op2;
reg signed [31:0] a2_op1, a2_op2;
wire signed [31:0] a1_res, a2_res;

adder a1(
    .a_bi(a1_op1),
    .b_bi(a1_op2),
    .c_bo(a1_res)    
);

adder a2(
    .a_bi(a2_op1),
    .b_bi(a2_op2),
    .c_bo(a2_res)    
);

reg [31:0] m1_op1, m1_op2, y1;
reg m1_start;
wire [15:0] m1_res16;
wire [31:0] m1_res = {16'h0, m1_res16};

mult m1 (
    .clk_i(clk_i),
    .rst_i(rst_i),
    .a_bi(m1_op1[7:0]),
    .b_bi(m1_op2[7:0]),
    .start_i(m1_start),
    .busy_o(m1_busy),
    .y_bo(m1_res16)
);

// FSM control unit code

localparam N = 32;

localparam IDLE               = 0;
localparam CMP_S              = 1;
localparam CALC_MULT_S1_START = 2;
localparam CALC_MULT_S1       = 3;
localparam CALC_MULT_S2_START = 4;
localparam CALC_MULT_S2       = 5;
localparam CALC_B             = 6;
localparam CMP_B              = 7;
localparam CALC_S             = 8;
localparam CALC_MULT_S3_START = 9;
localparam CALC_MULT_S3       = 10;
localparam FINISH             = 11;

reg [3:0] state_r;
reg [31:0] x_r;
reg signed [31:0] s_r;
reg [31:0] y_r;
reg [31:0] b_r;

always@(posedge clk_i)
    if(rst_i) begin
        x_r <= 0;
        m1_op1 <= 0;
        m1_op2 <= 0;
        m1_start <= 0;
        a1_op1 <= 0;
        a1_op2 <= 0;
        a2_op1 <= 0;
        a2_op2 <= 0;
        y_bo   <= 0;
        y_r    <= 0;
        rdy_o  <= 1;
        s_r    <= 0;
        
        state_r <= IDLE;
        
    end else begin
        case(state_r)
            IDLE:
                if(start_i) begin
                    x_r <= x_bi;
                    y_r <= 0;
                    rdy_o <= 0;
                    b_r <= 0;
                    s_r <= 0;
                    
                    // s = N-2
                    a1_op1 <= N;
                    a1_op2 <= -2;
                    
                    state_r <= CMP_S;
                end
            CMP_S:
                begin
                    s_r <= a1_res;
                    if(a1_res > -3) begin
                        y_r = y_r << 1;
                        
                        // 3*y
                        m1_op1 <= 3;
                        m1_op2 <= y_r;
                        m1_start <= 1;
                        
                        // y+1
                        a1_op1 <= y_r;
                        a1_op2 <= 1;
                        
                        state_r <= CALC_MULT_S1_START;
                        
                    end else begin
                        y1 <= y_r;
                        m1_start <= 0;                       
                        state_r <= CALC_MULT_S3_START;
                    end
                end
            CALC_MULT_S3_START:
                if(m1_busy == 0) begin
                    m1_start <= 0;
                    state_r <= CALC_MULT_S3;
                end
            CALC_MULT_S3:
                begin
                    m1_op1 <= y1;
                    m1_op2 <= y_bi;
                    m1_start <= 1;
                    state_r <= FINISH;
                end
            FINISH:
                if(m1_busy == 0) begin
                    y_bo <= m1_res;
                    rdy_o <= 1;
                    state_r <= IDLE;
                end
            CALC_MULT_S1_START: //waiting 1 clk for starting of the mult module
                begin
                    m1_start <= 0;
                    state_r <= CALC_MULT_S1;
                end
            CALC_MULT_S1:
                if(m1_busy == 0) begin
                    // m1_res = 3*y
                    // a1_res = y+1
                    // m1_res * a1_res = 3*y*(y+1)
                    m1_op1 <= m1_res;
                    m1_op2 <= a1_res;
                    m1_start <= 1;
                    
                    state_r <= CALC_MULT_S2_START;
                end
            CALC_MULT_S2_START: //waiting 1 clk for starting of the mult module
                begin
                    m1_start <= 0;
                    state_r <= CALC_MULT_S2;
                end
            CALC_MULT_S2:
                if(m1_busy == 0) begin
                    // 3*y(y+1)+1
                    a1_op1 <= m1_res;
                    a1_op2 <= 1;
                    
                    state_r <= CALC_B;
                end
            CALC_B:
                begin
                    b_r <= a1_res << s_r;
                    state_r <= CMP_B;
                end
            CMP_B:
                if(x_r >= b_r) begin
                    // x-b
                    a1_op1 <= x_r;
                    a1_op2 <= -b_r;
                    
                    // y+1
                    a2_op1 <= y_r;
                    a2_op2 <= 1;
                    
                    state_r <= CALC_S;
                    
                end else begin
                    state_r <= CALC_S;
                end
            CALC_S:
                begin
                    if(x_r >= b_r) begin
                        //x = x-b
                        x_r <= a1_res;
                        
                        //y = y+1
                        y_r <= a2_res;
                    end
                    
                    // s-3
                    a1_op1 <= s_r;
                    a1_op2 <= -3;
                    
                    state_r <= CMP_S;
                end
        endcase
    end

endmodule


















