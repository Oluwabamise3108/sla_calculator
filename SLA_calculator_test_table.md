#   Input               Priority        Hours       Responded      Expected output                 
1. tck-                 high            2           no              BREACHED by 1 hour                              
2. Tck-00123            medium          3           no              ON TRACK  remaining 1 hour                              
3. TCK-ABC              low             10          no              must have digits only after TCK-                            
4. TCK-00123            urgent          0.5         no              must be high, medium or low  
5.  TCK-00123           low             12          no              ON TRACK  remaining 12 hours            
6.  ABC-1               high            1           no              ID must start with TCK-                           
7. TCK-00123            medium          -4          no              No negative hours   
8. TCK-00123            high            4           no              BREACHED by 3 hours          
8. TCK-00123            medium          3.5         no              AT RISk remaining 0.5 hour 
9. TCK-00123            medium          2           no              ON TRACK  remaining 2 hours          
10.                     low             18          no              cannot be empty                 
11. TCK-00123           medium          3.1         no              ON TRACK remaining 1.9 hours
12. TCK-00123           medium          3.2         no              AT RISK remaining 1.8 hours
13. TCK-00123           medium          4           no              AT RISK remaining 0 hour
14. TCK-00123           medium          4.1         no              BREACHED by 0.1 hour
15. TCK-00123           high            0           no              ON TRACK  remaining 1 hour
16. TCK-00123           medium          6           yes             no action needed
17. TCK-00123           HIGH            0.5         Yes             no action needed
18. TCK-00123           low             5           maybe           must be yes or no