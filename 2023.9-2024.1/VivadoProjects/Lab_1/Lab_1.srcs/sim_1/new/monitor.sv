`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2023/10/21 13:13:45
// Design Name: 
// Module Name: monitor
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module 
    monitor(
        input clk, 
        input rst, 
        input [15:0] data_in, 
        input [15:0] data_out
    );
    localparam MATRIX_SIZE = 100;
    reg [7:0] A[MATRIX_SIZE];
    reg [7:0] B[MATRIX_SIZE];
    reg [7:0] C[MATRIX_SIZE];
    reg [7:0] C_expected[MATRIX_SIZE];
    reg [7:0] D[MATRIX_SIZE];
    localparam LOAD_A = 0;
    localparam LOAD_B = 1;
    localparam LOAD_RESULT = 2;
    reg [1:0] state;
    int i;
    int j;
    int k;
    int r;
    int fd;
    wire [7:0] val_in = data_in[7:0];
    wire [7:0] val_out = data_out[7:0];
    wire strb_out = data_out[15];
    wire data_ack = data_out[14];
    reg ack_buf;
    wire ack_rise = !ack_buf & data_ack;
    wire ack_drop = ack_buf & !data_ack;
    reg strb_buf;
    wire strb_rise = !strb_buf & strb_out ;
    reg not_match;
    realtime start_time;
    realtime end_time;
    initial begin
        fd = $fopen("result.txt", "w");
        $fwrite(fd,"Start simulation\n");
        $fflush(fd);
        $timeformat(-6, 2, "us", 10);
        i = 0;
        j = 0;
        state = LOAD_A;
        ack_buf = 0;
        not_match = 0;
    end
    always@(posedge clk)
        if (rst == 0) begin
            ack_buf <= data_ack;
            strb_buf <= strb_out;
        end
    always@(posedge clk)
        if (rst == 0) begin
            case (state)
                LOAD_A:begin
                    if (ack_rise)begin
                        A[i] = val_in;
                        $fwrite(fd,"A[%d] = %d\n", i, A[i]);
                        i += 1;
                    end
                    if (i == MATRIX_SIZE) begin
                        $fflush(fd);
                        state = LOAD_B;
                        i = 0;
                    end
                end
                LOAD_B:begin
                    if (ack_rise)begin
                        B[i] = val_in;
                        $fwrite(fd,"B[%d] = %d\n", i, B[i]);
                        i += 1;
                    end
                    if (i == MATRIX_SIZE) begin
                        $fflush(fd);
                        state = LOAD_RESULT;
                        i = 0;
                        for (j = 0; j < 100; j = j + 1) begin
                            D[j] = A[j] - B[j];
                        end
                        
                        for(j = 0; j < 10; j = j + 1) begin
                            for(k = 0; k < 10; k = k + 1) begin
                                C_expected[j*10+k] = 0;
                                for(r = 0; r < 10; r = r + 1) begin
                                    C_expected[j*10+k] += A[j*10+r] * D[r*10+k];
                                end
                            end
                        end
                    end
                end
                LOAD_RESULT:begin
                    if (ack_drop) begin
                        start_time = $realtime;
                    end
                    if (strb_rise) begin
                        if (i == 0) begin
                            end_time = $realtime;
                        end
                        C[i] = val_out;
                        i += 1;
                    end
                    if (i == MATRIX_SIZE) begin
                        i = 0;
                        for (j = 0;j<MATRIX_SIZE;j+=1)begin
                        if (C[j] != C_expected[j]) begin $fwrite(fd, "%d != %d DOESN'T MATCH\n",C[j], C_expected[j]);
                            not_match = 1;
                        end else begin
                            $fwrite(fd, "%d = %d \n",C[j], C_expected[j]);
                        end
                    end
                    $fwrite(fd, "----------------\n");
                    if (not_match == 1) $fwrite(fd, "TEST FAILED\n");
                    else $fwrite(fd,"TEST PASS\n");
                    $fwrite(fd, "----------------\n");
                    $fwrite(fd, "EXECUTION TIME:%t\n",end_time - start_time);
                    $fclose(fd);
                    $finish;
                end
            end
        endcase
    end
endmodule
