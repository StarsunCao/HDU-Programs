[ T r a n s i e n t   A n a l y s i s ] 
 { 
       N p a n e s :   3 
       A c t i v e   P a n e :   1 
       { 
             t r a c e s :   1   { 3 4 6 6 8 5 5 5 , 0 , " I ( D _ 0 1 ) " } 
             X :   ( ' m ' , 0 , 0 , 0 . 0 1 , 0 . 1 ) 
             Y [ 0 ] :   ( ' K ' , 1 , - 1 8 0 0 , 3 0 0 , 1 8 0 0 ) 
             Y [ 1 ] :   ( ' m ' , 0 , 1 e + 3 0 8 , 0 . 0 1 , - 1 e + 3 0 8 ) 
             A m p s :   ( ' K ' , 0 , 0 , 1 , - 1 8 0 0 , 3 0 0 , 1 8 0 0 ) 
             L o g :   0   0   0 
             G r i d S t y l e :   1 
       } , 
       { 
             t r a c e s :   2   { 5 8 9 8 3 5 , 0 , " V ( l o a d _ c t r ) " }   { 5 8 9 8 2 8 , 0 , " V ( s o u r c e _ v 1 ) " } 
             X :   ( ' m ' , 0 , 0 , 0 . 0 1 , 0 . 1 ) 
             Y [ 0 ] :   ( '   ' , 0 , - 1 2 0 , 2 0 , 1 2 0 ) 
             Y [ 1 ] :   ( '   ' , 0 , 1 e + 3 0 8 , 2 , - 1 e + 3 0 8 ) 
             V o l t s :   ( '   ' , 0 , 0 , 0 , - 1 2 0 , 2 0 , 1 2 0 ) 
             L o g :   0   0   0 
             G r i d S t y l e :   1 
             A r r o w :   " V "   1   0   ( 0 . 3 7 9 0 7 7 1 1 1 3 8 3 1 0 9 , 8 . 8 6 1 4 6 0 9 5 7 1 7 8 8 4 )   ( 0 . 3 7 8 8 6 1 6 8 9 1 0 6 4 8 7 , 8 . 6 6 8 5 3 6 6 8 7 9 0 6 9 3 ) 
             A r r o w :   " V "   1   0   ( 0 . 3 7 9 0 7 7 1 1 1 3 8 3 1 0 9 , 8 . 8 6 1 4 6 0 9 5 7 1 7 8 8 4 )   ( 0 . 3 7 8 8 6 1 6 8 9 1 0 6 4 8 7 , 8 . 6 6 8 5 3 6 6 8 7 9 0 6 9 3 ) 
             A r r o w :   " V "   1   0   ( 0 . 3 8 0 7 6 0 0 9 7 9 1 9 2 1 7 , 9 . 3 4 0 0 5 0 3 7 7 8 3 3 7 5 )   ( 0 . 3 8 0 5 4 4 6 7 5 6 4 2 5 9 5 , 9 . 1 4 7 1 1 7 1 5 0 1 2 5 3 2 ) 
             T e x t :   " V "   1   ( 0 . 3 7 9 0 7 7 1 1 1 3 8 3 1 0 9 , 8 . 9 0 6 8 0 1 0 0 7 5 5 6 6 8 )   ; 3 7 8 . 8 6 1 6 9 m s , 8 . 6 6 8 5 3 6 7 V 
             T e x t :   " V "   1   ( 0 . 3 8 0 7 6 0 0 9 7 9 1 9 2 1 7 , 9 . 3 8 5 3 9 0 4 2 8 2 1 1 5 9 )   ; 3 8 0 . 5 4 4 6 8 m s , 9 . 1 4 7 1 1 7 2 V 
       } , 
       { 
             t r a c e s :   2   { 5 8 9 8 2 8 , 0 , " V ( s o u r c e _ v 1 ) " }   { 5 8 9 8 3 5 , 0 , " V ( d _ 0 1 _ a ) - V ( l o a d _ c t r ) " } 
             X :   ( ' m ' , 0 , 0 , 0 . 0 1 , 0 . 1 ) 
             Y [ 0 ] :   ( '   ' , 0 , - 1 8 0 , 3 0 , 1 2 0 ) 
             Y [ 1 ] :   ( ' _ ' , 0 , 1 e + 3 0 8 , 0 , - 1 e + 3 0 8 ) 
             V o l t s :   ( '   ' , 0 , 0 , 0 , - 1 8 0 , 3 0 , 1 2 0 ) 
             L o g :   0   0   0 
             G r i d S t y l e :   1 
       } 
 } 
 [Transient Analysis]
{
   Npanes: 3
   Active Pane: 1
   {
      traces: 6 {34668547,0,"I(D1)"} {34668555,0,"I(D_01)"} {34668552,0,"I(D_1)"} {34668555,0,"I(R_in_ctr)"} {34668552,0,"I(R_in_fbr)"} {34668547,0,"I(R_in_hwr)"}
      X: ('m',0,0,0.005,0.2)
      Y[0]: (' ',1,-1,0.2,1)
      Y[1]: ('m',0,1e+308,0.01,-1e+308)
      Amps: (' ',0,0,1,-1,0.2,1)
      Log: 0 0 0
      GridStyle: 1
   },
   {
      traces: 4 {589835,0,"V(load_ctr)"} {589832,0,"V(load_fbr1,load_fbr2)"} {589828,0,"V(source_v1)"} {589827,0,"V(load_hwr)"}
      X: ('m',0,0,0.005,0.2)
      Y[0]: (' ',0,-10,2,10)
      Y[1]: (' ',0,1e+308,2,-1e+308)
      Volts: (' ',0,0,0,-10,2,10)
      Log: 0 0 0
      GridStyle: 1
      Arrow: "V" 1 0 (0.379077111383109,8.86146095717884) (0.378861689106487,8.66853668790693)
      Arrow: "V" 1 0 (0.379077111383109,8.86146095717884) (0.378861689106487,8.66853668790693)
      Arrow: "V" 1 0 (0.380760097919217,9.34005037783375) (0.380544675642595,9.14711715012532)
      Text: "V" 1 (0.379077111383109,8.90680100755668) ;378.86169ms,8.6685367V
      Text: "V" 1 (0.380760097919217,9.38539042821159) ;380.54468ms,9.1471172V
   },
   {
      traces: 4 {589828,0,"V(source_v1)"} {589835,0,"V(d_01_a)-V(load_ctr)"} {589832,0,"V(d_1_a)-V(load_fbr1)"} {589827,0,"V(d1_a)-V(load_hwr)"}
      X: ('m',0,0,0.005,0.2)
      Y[0]: (' ',0,-22,2,12)
      Y[1]: ('_',0,1e+308,0,-1e+308)
      Volts: (' ',0,0,0,-22,2,12)
      Log: 0 0 0
      GridStyle: 1
   }
}
 